**Docker**

- 多種多様な課題をITの力を使って解決する事ができる世の中になった現在において、ハードとしてのサーバーが重要視されるようになった
    - 仮想化技術がハードとしてのサーバーを活用する上で活用されるようになる
        - 仮想化におけるコンテナ技術が扱いやすくなったプラットフォームがDockerとなる
            - 特定の開発環境をマシンが変わっても同じ環境を共有する事ができるようにしたものをコンテナ技術と呼ぶ

- 従来の仮想化とDockerで扱うコンテナ技術の違い
    - 仮想化技術においてDockerを使う有意な点は何か？
        - 起動までの時間
            - 従来の仮想化
                - 物理マシン=>ホストOS(ホストのカーネル)=>ハイパーバイザー(リソースの割り当て機能)=>ゲストOS=>アプリケーション
                    - 物理サーバーの上にホストOSがあり、それに加えてゲスト側でもOSが必要になる
                        - ゲストOSのダウンロードがあるためリソースの不足や起動までの時間を要するなどという点が存在する
            - Dockerによるコンテナ技術を活用した仮想化
                - 物理マシン=>ホストOS(ホストのカーネル)=>Dockerエンジン=>アプリケーション
                    - ホストOSのカーネルを共有して使用するためゲストOSのダウンロードなどが必要なくなる
                        - 従来と比較して起動数秒程度で可能になった
                        - CPUやメモリの節約
                    - Docker エンジン(Docker engine)
                        - Docker CLI
                            - Dockerをコマンドベースで操作
                        - REST API
                            - クライアント(Docker CLI)から受けつけたリクエストに応じてAPIとしてサーバーとの通信を介在する
                        - Docker デーモン
                            - サーバー
                    - Docker エンジン
                        - 管理対象
                            - コンテナ
                            - イメージ
                            - ネットワーク
                            - データボリューム
- Dockerにおいて実現する事ができる事
    - 1台のサーバーで複数のアプリケーション実行環境を用意する事が可能になる
    - Dokerコンテナ単位でのデータの移行などが簡単に可能
    - 他エンジニアとの開発環境の共有が簡単に実行する事ができる

- Dockerについて理解する
    - Dockerコンテナ
        - 仮想環境の事
            - コンテナ1つ1つが独立しており、互いに干渉する事がない状態になる
    - Dockerイメージ
        - Dokerコンテナの動作環境についてまとめたテンプレートファイル
            - 静的なDockerイメージを専用コマンドで実行する事でDockerコンテナが作成されアプリケーション実行環境が用意される
    - Docker file
        - Dokerイメージを作成するための設計図にあたるテキスト
            - Dockerコンテナの設計内容がコマンド形式でまとまっている
                - 専用コマンドのbuildを実行する事でDokerイメージが作成されてrunする事でDockerコンテナが作成される
    - Dockerレジストリ
        - Dockerイメージを保存や共有する事のできる場所
            - Dockerイメージの保存
            - Dockerイメージの共有
            - 他のユーザーが作成したDockerイメージの取得
        - 例：Docker Hub
            - 様々なアプリケーションにおける実行環境が公開されている
                -　簡単に実行環境を用意する事が可能になる

- Docker操作関連コマンド
    - Dockerコンテナ操作専用コマンド
        - 共通ルール => doker container + コマンド名 + （コンテナ名など）
            - コンテナの起動 => start
                - docker container start （コンテナ名）
            - コンテナの停止（より安全な方法） => stop
                - docker container stop （コンテナ名）
            - コンテナの停止（強制的に停止する方法） => kill
                - docker container kill （コンテナ名）
            - コンテナの削除 => rm
                - docker container rm （コンテナ名）
            - コンテナの再起動 => restart
                - docker container restart （コンテナ名）
            - コンテナの一覧を表示 => ls
                - docker container ls -a
            - Dockerイメージからコンテナを生成 => run
                - docker container run （イメージ名）

    - Dockerイメージの管理やレジストリ(Docker Hub)の利用方法
        - 共通ルール：doker image + コマンド名 + (イメージ名)
            - Dockerイメージ（最新版）を「Docker Hub」からダウンロード => pull
                - docker image pull （イメージ名）
            - Dockerイメージの一覧を表示 => ls
                - docker image ls
            - Dockerイメージの削除 => rm
                - docker image rm （イメージ名）
            - Dockerイメージを「Docker Hub」へアップロード => push
                - docker image push （イメージ名）

    - Doker fileからDokerイメージの作成
        - コマンド：docker image build [オプション] Dockerfileのパス
            - Dockerfileはテキストファイルのためviエディタで作成する事が可能になる
                - vi Dockerfail

    - Dockerfileの書式

        ```text
        FROM centos
        RUN yum -y install httpd
        EXPOSE 80
        CMD [ここにコマンドを記述する]
        ```
        - Dockerイメージの指定 => FROM
            - FROM centosなど
        - 実行内容の指定 => RUN
            - RUN yum -y install httpd
        - docker run 時に実行するコマンドの指定 => CMD
            - CMD [コマンドの記述]
        - 公開するポートの指定 => EXPOSE
            - EXPOSR 80 など

    - Dockerのバージョン表示 => version
        - docker version
    - Dokerイメージの検索 => search
        - docker search (イメージ名)

[コンテナについて]

[コンテナについて]:./コンテナ.md