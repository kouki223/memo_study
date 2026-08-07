

# PRを取り込むのが怖くなった理由・今後

kyoheiさん

[理由]
OSSを作るのは、AI以前はDIY的なイメージだった
=> いまは、自分が子供のように作ったOSSが攻撃手段になる可能性

nulabで元々働いていた

OSS

いま、mergeは実質Publishだろうという事
=> CI

最近、レビューしている事は、コードの差分だけではない
=> Botは全部却下

PRをOpenにしているだけで、危険
=> tanstackはPRのキャッシュポイズニング

OSS
=> クリエイターがPRでコミュニケーションしてたり、、、

PRを受けるというのは、運営方法の1つ
=> 透明性を保ちながらコミュニティに貢献したい => kyohei
=> 関わるコミュニティは自由


[以外と知られていないOSSの運営方法]

Labybird(https://gigazine.net/news/20260608-ladybird-change-develop/)
=> PRの受け入れを停止 => 実質、中の人じゃないと直せない => バグレポート等は受け入れる

SQLite
=> testスイートは非公開 => アクセスするためには課金が必要 => public domainを維持
=> 受けたPRは一度、閉じて、中の人が描き直すようになっている

QuickJS
=> quickjs-ngはcommunity developmentにいって、forkした先で成長する

Typora
=> コードは公開していないけど、featureは受け入れる => 透明性がある

postmortem
=> OSSはこの体験を共有する事は重要な役割

pdfme
=> CVE => XSSの指摘 => MITライセンス

発信を通じて開発者へ良い影響を与えられると良いなと思う


# Honoでのサプライチェーン攻撃対策

AIスロープ

問題を起こしてしまう側の話をしましょう

Honoの現状
Tanstack
3つの経路
Honoの対策

依存されている関係
=> 4393

Mastra
MCP SDK
Astro
などなど
↑
多く使われている

共通結果 => マルウェアをnpmパッケージに埋め込まれた

axios
=> 攻撃者が開発者側に攻撃
=> ソーシャルエンジニアリング

Tanstack
=> キャッシュ => マイナーバージョンを向けた

プロべなんす => 出所の正当性

Mastra
=> キャレット指定

過去のコントリビューターの権限の悪用

npというもの使っていた

OIDC
=> 

-no publish 
=> GitHub actionsでビルドする
=> ローカルからのビルドをなくす

GitHub actionsの実行をメンテナの手動許可を必要とする

Hono => 依存がゼロ

プロジェクト側でやれる事を減らす

Stageing publishing

honoのcore自体の機能自体を減らすという事も検討

AWSのコネクタの機能 => 切り出す

# 

npmはパッケージの範囲が広い
脆弱性のあるGitHub actionsは多い

侵害されてもregistryに入らない事を狙う

公開フロー全てを守る事が必要
=> 弱い場所にねらわれる => なので、全体が必要

ローカルのToken管理
=> 必要な時だけ生体認証に応じて取ってくるのみ

ghのローカルに強い権限が存在する

PAT => 普段は昼用ない
ローカル限定
fine-grained PATは用途を絞る

基本的にはread-onlyのトークンで良い

Cheks-APIが対応していない
↑
GitHub

トークンを発行していない
必要な時だけログインして取ってくる

OICDトークン

npmjs.com

permission
=> whirteでもOICD

GitHubEnviroment

特定の

refs/pull/*/merge
↑
特定の環境からしか作成されないPR

provenaseは署名は確認出来る
しかし、その中身は誰かがませている可能性がある
だから、publishした人が誰なのか？を確認したい
npm側の環境する

権限のカスケーディング
=> GitHubとnpmという違う環境の間に壁をちゃんとおく

npmもしくは、GitHubはTokenレスにしたい

公開フローを段階毎に制御する
↑
npm

AIエージェント時代も変わらない
- 最小権限で権限割りを正しくする事が継続して必要

