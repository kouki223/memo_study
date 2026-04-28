# FRP（Fast Reverse Proxy）

[FRP（Fast Reverse Proxy）入門: ngrok代替のセルフホスト型リバースプロキシ](https://blog.tumf.dev/posts/diary/2021/1/2021-1-12/)

- ngrok(エングロック)というトンネリング/リバースプロキシツール
    - ローカルのポートで開発しているものをhttps化してインターネットへ公開する事を可能にする事ができる
        - 手軽に開発機のポートをネットに晒す事ができるのがngrokである

- FRPは？
    - NATやファイアーウォールの内側にあるローカルサーバをインターネットに公開するための高速リバースプロキシ
        - ngrokのようなサービスを自分で構築する事が出来るという事 => 自分のポートを公開する事が出来る

- frpsとfrpcのインストール方法
    - FRPは以下の2つのコンポーネントで構成
        - frps（サーバー側）: 外部公開用のリバースプロキシサーバ
        - frpc（クライアント側）: ローカルサーバとfrpsを繋ぐクライアント

- 内部仕様
    - 内部的にはGoでかかれている
        - なので、コンパイルされたGitHub Releasesからバイナリを取得する事が簡単
            - brew install frpc でもインストール出来る(クライアント側のみしかインストールされない点に注意)

- 設定
```m
### frps.toml

bindPort = 7000
auth.token = "your-secure-token"
```

```
### frpc.toml

serverAddr = "frps.example.com"
serverPort = 7000
auth.token = "your-secure-token"
```

- 7000番ポートでfrcpからfrpsに接続する事が出来る場所に立てる必要がある
    - frps,frpsどちらにも設定ファイルが必要になる

- 実際の使い方

```
サーバー側

# TOML形式（v0.52.0以降）
$ frps -c frps.toml

# INI形式（v0.51.x以前）
$ frps -c frps.ini

クライアント側
# TOML形式（v0.52.0以降）
$ frpc -c frpc.toml

# INI形式（v0.51.x以前）
$ frpc -c frpc.ini

期待する出力
↓
2021/01/11 16:18:51 [I] [service.go:288] [06845eb1e7aa771a] login to server success, get run id [06845eb1e7aa771a], server udp port [0]
```

ngrokとFRPの主な違いは？

| 項目 | ngrok | FRP |
|------|-------|-----|
| ホスティング | SaaS（ngrok社管理） | セルフホスト（自分で管理） |
| コスト | 月額課金 | サーバ代のみ（無料） |
| カスタマイズ | 制限あり | 自由 |
| ドメイン | ngrok提供 | 独自ドメイン使用可 |
