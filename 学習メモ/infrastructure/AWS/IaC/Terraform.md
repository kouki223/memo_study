# Terraform（AWS IaC）

## 概要

**Terraform** は IaC（Infrastructure as Code）ツールで、サーバや各社のパブリッククラウドのインフラ環境をコードで自動構築できる。

- 公式チュートリアル: [Build Infrastructure - AWS](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)
- 参考記事: [Terraformを使ったAWS環境構築を試してみる](https://qiita.com/Mouflon_127000/items/767b964c833ed0428eb6)

### 主なコマンド

| コマンド | 説明 |
|---|---|
| `terraform init` | 作業ディレクトリの初期化（プロバイダのダウンロード等） |
| `terraform fmt` | コードのフォーマット |
| `terraform validate` | 構文チェック |
| `terraform plan` | 実行プランの確認（変更内容のプレビュー） |
| `terraform apply` | リソースの作成・更新 |
| `terraform destroy` | リソースの削除 |

`terraform init` 実行後、作業ディレクトリ配下に `.terraform/` と `.terraform.lock.hcl` が生成される。

---

## 実行環境

### 構成

| 項目 | 内容 |
|---|---|
| 接続元端末 | Windows 11 / TeraTerm 5.0 |
| Terraform実行サーバ | EC2（Amazon Linux 2023, t2.micro） |
| AMI | `ami-0dfa284c9d7b2adad` |
| AWS CLI | 2.14.5 |
| 配置 | Terraformで構築する環境とは別VPCのパブリックサブネット上（事前作成済み） |

### Terraform インストール（Amazon Linux）

```bash
# yum-utilsの導入
sudo yum install -y yum-utils

# リポジトリ追加
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo

# Terraformインストール
sudo yum -y install terraform

# 確認
terraform -version
# => Terraform v1.6.6 on linux_amd64
```

AWS CLI も必要。権限周りの躓きを防ぐため、実行ユーザーには `PowerUserAccess` を付与。

---

## チュートリアル1: EC2インスタンスの作成

### ディレクトリ準備

```bash
mkdir learn-terraform-aws-instance
cd learn-terraform-aws-instance
touch main.tf
```

### main.tf（初版）

公式ドキュメントの内容をベースに、リージョンを東京（`ap-northeast-1`）、AMIを東京リージョンの AL3 に変更。

> 公式チュートリアルの AMI ID は `us-west-2` 専用。別リージョンを使う場合は AMI ID を変更する必要がある。

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0dfa284c9d7b2adad"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
```

### 作業フロー

```bash
terraform init      # 初期化
terraform fmt       # フォーマット
terraform validate  # 構文チェック => Success! The configuration is valid.
terraform apply     # 実行（yes で承認）
```

### エラー: デフォルトVPCが存在しない

**1回目の `terraform apply` で失敗:**

```
Error: creating EC2 Instance: VPCIdNotSpecified: No default VPC for this user.
       GroupName is only supported for EC2-Classic and default VPC.
```

**原因:** 公式チュートリアルは `us-west-2` にデフォルトVPCが存在することが前提。EC2リソースだけ書けばデフォルトVPCに自動配置される想定だが、東京リージョンにはデフォルトVPCがない。

**対処:** 既存VPCにデプロイする場合は、SG ID とサブネット ID を指定する。

### main.tf（修正版）

```hcl
resource "aws_instance" "app_server" {
  ami                    = "ami-0dfa284c9d7b2adad"
  instance_type          = "t2.micro"
  vpc_security_group_ids = ["<SG ID>"]
  subnet_id              = "<subnet ID>"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
```

**2回目の `terraform apply` で成功:**

```
aws_instance.app_server: Creation complete after 32s [id=i-xxxxxxxxxxxxxxxx]
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

### リソース削除

```bash
terraform destroy
# => Destroy complete! Resources: 1 destroyed.
```

---

## チュートリアル2: VPCを含めた環境構築

既存VPC上へのデプロイではなく、VPCも含めて新規構築する。

### ディレクトリ構成

```
TF-WORK/
├── main.tf
├── network.tf
└── ec2.tf
```

### 構成図

- VPC（`192.168.0.0/16`）
  - パブリックサブネット（`192.168.0.0/24`, 1a）→ IGW経由でインターネット接続
  - プライベートサブネット（`192.168.1.0/24`, 1a）
- EC2（パブリックサブネット上）
- SGは作成せず、VPCデフォルトのものをアタッチ

### main.tf

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "ap-northeast-1"
}
```

### network.tf

```hcl
# VPC
resource "aws_vpc" "tf-vpc-01" {
  cidr_block           = "192.168.0.0/16"
  instance_tenancy     = "default"
  enable_dns_hostnames = true

  tags = {
    Name = "TF-VPC-01"
    Env  = "TF-WORK"
  }
}

# Subnet（パブリック）
resource "aws_subnet" "tf-vpc-01-pub-01-a" {
  vpc_id                  = aws_vpc.tf-vpc-01.id
  cidr_block              = "192.168.0.0/24"
  availability_zone       = "ap-northeast-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "TF-VPC-01-Pub-01-a"
    Env  = "TF-WORK"
  }
}

# Subnet（プライベート）
resource "aws_subnet" "tf-vpc-01-pri-01-a" {
  vpc_id            = aws_vpc.tf-vpc-01.id
  cidr_block        = "192.168.1.0/24"
  availability_zone = "ap-northeast-1a"

  tags = {
    Name = "TF-VPC-01-Pri-01-a"
    Env  = "TF-WORK"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "tf-vpc-01-igw-01" {
  vpc_id = aws_vpc.tf-vpc-01.id

  tags = {
    Name = "TF-VPC-01-IGW-01"
    Env  = "TF-WORK"
  }
}

# Route Table（パブリック）
resource "aws_route_table" "tf-vpc-01-rtb-pub-01" {
  vpc_id = aws_vpc.tf-vpc-01.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.tf-vpc-01-igw-01.id
  }

  tags = {
    Name = "TF-VPC-01-RTB-Pub-01"
    Env  = "TF-WORK"
  }
}

# Route Table（プライベート）
resource "aws_route_table" "tf-vpc-01-rtb-pri-01" {
  vpc_id = aws_vpc.tf-vpc-01.id

  tags = {
    Name = "TF-VPC-01-RTB-Pri-01"
    Env  = "TF-WORK"
  }
}

# Route Table Association
resource "aws_route_table_association" "tf-vpc-01-rtb-at-pub" {
  subnet_id      = aws_subnet.tf-vpc-01-pub-01-a.id
  route_table_id = aws_route_table.tf-vpc-01-rtb-pub-01.id
}

resource "aws_route_table_association" "tf-vpc-01-rtb-at-pri" {
  subnet_id      = aws_subnet.tf-vpc-01-pri-01-a.id
  route_table_id = aws_route_table.tf-vpc-01-rtb-pri-01.id
}
```

### ec2.tf

```hcl
resource "aws_instance" "tf-ec2-01" {
  ami           = "ami-0dfa284c9d7b2adad"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.tf-vpc-01-pub-01-a.id
  key_name      = "TF-AWS-KEY"

  tags = {
    Name = "TF-EC2-01"
    Env  = "TF-WORK"
  }
}
```

### 実行結果

```bash
terraform validate
# => Success! The configuration is valid.

terraform plan
# => Plan: 9 to add, 0 to change, 0 to destroy.

terraform apply
# => Apply complete! Resources: 9 added, 0 changed, 0 destroyed.
```

作成されるリソース（9件）:

| リソース | 名前 |
|---|---|
| VPC | TF-VPC-01 |
| Subnet | TF-VPC-01-Pub-01-a / TF-VPC-01-Pri-01-a |
| IGW | TF-VPC-01-IGW-01 |
| Route Table | TF-VPC-01-RTB-Pub-01 / TF-VPC-01-RTB-Pri-01 |
| Route Table Association | 2件 |
| EC2 | TF-EC2-01 |

---

## 学んだこと・メモ

- 実行環境の構築は簡単。Terraformファイルの記述やパラメータ指定は CloudFormation より感覚的に書ける印象。
- リソースの依存関係が自動分析される（例: `subnet_id = aws_subnet.tf-vpc-01-pub-01-a.id` で参照）。
- デフォルトVPCがないリージョンでは、VPC・サブネット・SGの明示的な指定が必要。
- ファイル分割（`main.tf` / `network.tf` / `ec2.tf`）で管理しやすくなる。
- 未着手: 変数（`variable`）、出力（`output`）、モジュール等の公式チュートリアル続き。
