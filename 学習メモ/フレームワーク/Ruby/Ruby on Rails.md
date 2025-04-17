- 学習ソース
    - Railsの教科書
    - progate
    - Railsドキュメント
    https://qiita.com/Inp/items/cc447237e23bf10d159e

    https://railsgirls.jp/github

    https://railsguides.jp/

    https://railstutorial.jp/

    **[初心者向け]Ruby on Railsについて徹底解説してみた**
    - https://qiita.com/renesisu727/items/a21c7f5d1604700b7111
- Railsの概念
    - Railsとは？
        - Rubyで記載されたwebアプリケーションのフレームワーク
            - フレームワーク
                - 物事を考える上での枠組み
            - Webアプリケーションを作る上での枠組み
                - Railsでアプリケーションの土台を作る
        - 何かを作るもの
            - 枠組みを提供するのが、フレームワーク
        - Railsはプログラミング言語ではない
            - プログラミング言語ではなく、webフレームワーク
                - プログラミング言語
                    - Ruby, Python, C
    - MVCアーキテクチャ
        - M(Model)
            - DBとコントローラーからのデータをどのように繋げるか？
        - C(Controller)
            - クライアントからのリクエストをどのように繋げるか？
        - V(View)→**あまり気にする必要ない**
            - コントローラーからのデータを受け取る
            - コントローラーへデータを渡す
            - アプリ層へリクエストを渡す
    - クラスとインスタンスの関係（上位概念：下位概念）
        - クラス構文と呼ばれるもの
            - クラスという設計図(クラス自体は空)
                - クラス
                    - インスタンス変数
                    - イニシャライズメソッド
                    - インスタンスメソッド
                - インスタンス
                    - クラスとその実体によって表現したい内容をRailsへ渡しクラスの実体を作る
        - 上位概念と下位概念
            - 例：
                - 地球　＝＞　太陽系　＝＞　銀河系　＝＞　宇宙
                    - 宇宙の視点から見た時に銀河系はたくさんある　＝＞　子の関係
                    - 銀河系から見ると宇宙というものは1つ　＝＞　親の関係
            - Railsの場合
                - インスタンス　＝＞　クラス
                    - インスタンスから見るとクラスは1つしかない
                    - クラスから見るとインスタンスはたくさんある
    - Railsの開発志向
        - Railsを使う事で開発が楽になる
            - 最前な開発の方法は1つである
                - 特定の開発において開発手法を1つに絞って、それに沿った支援を全面的に行う
                    - 開発指向に沿わない開発方法は逆にやりずらい
                        - 言語は自由な言語だけど、フレームワークはそうじゃない
    - 大原則
        - 繰り返しを避けよ（Don't Repeat Yourself: DRY）
        - 設定より規約が優先（Convention Over Configuration）
- Ruby on Railsの仕様
    - Ruby on Rails とは？
        - Webフレームワークの一種
            - フレームワークとは？
                - 骨組み　＝＞　様々な機能を提供してくれる骨組み
                    - CLIからDDLを実行する事で最低限必要な各種ファイルが生成される
            - Webフレームワークとは、Webアプリを作るための枠組みの事である
                - Webアプリにおいて共通して使う機能
                    - ユーザーのURLに応じてデータベースを操作する事
                    - HTMLのファイルを作成して送る
                    - ログイン機能
        - 具体例
            - Bootstrap
                - CSSのフレームワーク
                    - Webサイト各々の部品ごとの枠組みを提供する
    - migation
        - データベースに対して行う一連の変更のこと
            - データベースのテーブルやカラム、その他の属性に対して変更、追加、削除などができる
    - Railsコマンド
        - コマンドとは？
            - コンピュータへの指令(命令)
                - コンソール, ターミナルで入力する
                    - コマンド(指令) => コンピュータ
                        - コマンドを実行する上でのインターフェース
        - Railsコマンド一覧（87個）
            - Railsでアプリケーションを作成する
                - rails new アプリケーション名(task-app)
                    - task-appフォルダ(ディレクトリ)
                        - app/ フォルダ
                            - アプリケーションのメインフォルダ
                        - config/ フォルダ
                            - 設定情報
                        - ルーティング
                        - db/ フォルダ
                            - データベースに関するフォルダ
                    - 新しいRailsのアプリケーションを作成
                        - アプリケーションに最低限必要なフォルダやファイルが自動的に生成
                    
                    ### オプション
                    
                    | オプション | 説明 | デフォルト値 |
                    | --- | --- | --- |
                    | –skip-namespace | namespaceの生成をスキップ |  |
                    | –skip-collision-check | コリジョンチェックをスキップ |  |
                    | -r, -ruby=PATH | rubyバイナリのパス |  |
                    | -m, -template=TAMPLATE | テンプレートのパス |  |
                    | -d, –database=DATABASE | データベースの種類 | sqlite3 |
                    | -G, –skip-git | .gitignoreファイルの生成をスキップ |  |
                    | –skip-keeps | .keepファイルの生成をスキップ |  |
                    | -M, –skip-action-mailer | Action Mailerファイルの生成をスキップ |  |
                    | –skip-action-mailbox | Action MailboxのGemをスキップ |  |
                    | –skip-action-text | Action TextのGemをスキップ |  |
                    | -O, –skip-active-recode | Active Recordファイルの生成をスキップ |  |
                    | –skip-active-job | Active Jobをスキップ |  |
                    | –skip-active-storage | Active Storageファイルの生成をスキップ |  |
                    | -C, –skip-action-cable | Action Cableファイルの生成をスキップ |  |
                    | -S, –skip-sprockets | Sprocketsファイルの生成をスキップ |  |
                    | -J, –skip-javascript | JavaScriptファイルの生成をスキップ |  |
                    | –skip-hotwire | Hotwireの統合をスキップ |  |
                    | –skip-jbuilder | jbuilderのGemをスキップ |  |
                    | -T, –skip-test | testファイルの生成をスキップ |  |
                    | –skip-system-test | システムテストファイルの生成をスキップ |  |
                    | –skip-bootsnap | bootsnapのGemをスキップ |  |
                    | –dev | githubリポジトリ上の自分のコードから作成 |  |
                    | –edge | githubリポジトリ上の最新のコードから生成 |  |
                    | –master, –main | RailsのメインブランチのGemfileでアプリケーションをセットアップ |  |
                    | –rc=RC | railsコマンドの追加の構成オプションを含むファイルへのパス |  |
                    | –no-rc | .railsrcファイルからの追加のロードをスキップ |  |
                    | –api | APIのみのアプリケーションを生成 |  |
                    | –minimal | 最小限のRailsアプリケーションを生成 |  |
                    | -j, –javascript=JAVASCRIPT | 組み込むJavaScriptライブラリーを指定 | importmap |
                    | –css=CSS | CSSプロセッサを選択 |  |
                    | ｰB, –skip-bundle | bundle installしない |  |
                    | -f, –force | ファイルが存在する場合に上書き |  |
                    | -p, –pretend | ドライラン |  |
                    | -q, –quiet | 進捗情報を非表示 |  |
                    | -s, –skip | 既に存在するファイルはスキップ |  |
                    | -h, –help | ヘルプ |  |
                    | -v, –version | バージョンを表示 |  |
                    - 例：
                        - My SQLを使うアプリの作成
                            - $ rails new weblog -d mysql
                        - APIのみのアプリケーション（APIモード　Viewを捨てる）
                            - $ rails new weblog --api
                        - 古いバージョンのRailsでアプリケーション
                            - $ rails *6.1.4* new weblog
            - rails generate scaffold
                - アプリケーションの基本的な機能を自動生成するコマンド
                    - コントローラー、モデル、ビューを作成
                        - 一覧(index)
                        - 詳細(show)
                        - 新規作成(new/create)
                        - 編集(edit/update)
                        - 削除(destroy)
                - $ rails generate scaffold 名前 [カラム名:型[:index]..] [オプション]
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –force-plural | 指定されたモデル名を強制的に使用 |  |
                | -o, –orm=NAME | 呼び出されるORMを指定 | active_record |
                | –model-name=MODEL_NAME | 使用するモデル名 |  |
                | –resource-route | リソースルートを生成するか | true |
                | –api | APIを生成するタイミング |  |
                | -c, –scaffold-controller=NAME | 呼び出されるScaffoldコントローラ | scaffold_controller |
                | –migration | migrationファイルを生成するか | true |
                | –timestamps | timestampsファイルを生成するか | true |
                | –parent=PARENT | 生成されたモデルの親クラスを指定 |  |
                | –indexes | belongs_toカラムにインデックスを付与するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | -db, –database=DATABASE | データベースの種類 | sqlite3 |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | –fixture | フィクスチャファイルを生成するか | true |
                | -r, –fixture-replacement=NAME | 呼び出されるフィクスチャを指定 |  |
                | –system-tests=SYSTEM_TESTS | システムテストを指定 | test_unit |
                | –helper | helperファイルを生成するか | true |
                | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                | –jbuilder | jbuilderファイルを生成するか | true |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
                
                ### カラムの型
                
                | データ方 | 説明 |
                | --- | --- |
                | string | 文字列 |
                | text | 長い文字列 |
                | integer | 整数 |
                | float | 浮動小数 |
                | decimal | 精度の高い小数 |
                | datetime | 日時 |
                | timestamp | より細かい日時 |
                | time | 時間 |
                | date | 日付 |
                | binary | バイナリデータ |
                | boolean | Boolean型 |
                
                ### 生成されるファイル
                
                | ファイル | 説明 |
                | --- | --- |
                | db/migrate/YYYYMMDDHHMMSS_create_xxxes.rb | マイグレーションファイル |
                | app/models/xxx.rb | モデルファイル |
                | app/controllers/xxxes_controller.rb | コントローラファイル |
                | app/views/XXXs/index.html.erb | すべてのリストを表示 |
                | app/views/XXXs/edit.html.erb | 編集ファイル |
                | app/views/XXXs/show.html.erb | 詳細ページ |
                | app/views/XXXs/new.html.erb | 新規ページ |
                | app/views/XXXs/_form.html.erb | フォーム用ページ |
                | app/views/xxxes/_xxx.html.erb |  |
                | app/helpers/xxxes_helper.rb | ヘルパー |
                | test/models/xxx_test.rb | モデルテスト |
                | test/fixtures/xxxes.yml | フィクスチャテスト |
                | test/controllers/xxxes_controller_test.rb | コントローラテスト |
                | test/system/xxxes_test.rb | システムテスト |
                | app/views/xxxes/index.json.jbuilder | Jbuilderファイル |
                | app/views/xxxes/show.json.jbuilder | Jbuilderファイル |
                | app/views/xxxes/_xxx.json.jbuilder | Jbuilderファイル |
            - rails generate scaffold_controller
                - モデル以外のアプリケーションのひな型を生成
                    - アプリの基本的な機能に必要なコントローラーとビューを作成
                        - 一覧(index)
                        - 詳細(show)
                        - 新規作成(new/create)
                        - 編集(edit/update)
                        - 削除(destroy)
                    - $ rails generate scaffold_controller 名前 [カラム名:型..] [オプション]
                    
                    ### オプション
                    
                    | オプション | 説明 | デフォルト値 |
                    | --- | --- | --- |
                    | –skip-namespace | namespaceの生成をスキップ |  |
                    | –skip-collision-check | コリジョンチェックをスキップ |  |
                    | –force-plural | 指定されたモデル名を強制的に使用 |  |
                    | –model-name=MODEL_NAME | 使用するモデル名 |  |
                    | –helper | helperファイルを生成するか | true |
                    | -o, –orm=NAME | 呼び出されるORMを指定 | active_record |
                    | –api | APIを生成するタイミング |  |
                    | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                    | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                    | –resource-route | リソースルートを生成するか | true |
                    | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                    | –jbuilder | jbuilderファイルを生成するか | true |
                    | –system-tests=SYSTEM_TESTS | システムテストを指定 | test_unit |
                    | –timestamps | timestampsファイルを生成するか | true |
                    | -f, –force | ファイルが存在する場合に上書き |  |
                    | -p, –pretend | ドライラン |  |
                    | -q, –quiet | 進捗情報を非表示 |  |
                    | -s, –skip | 既に存在するファイルはスキップ |  |
                    | -h, –help | ヘルプ |  |
                    | -v, –version | バージョンを表示 |  |
            - rails generate controller
                - コントローラーとビューの作成
                    - $ rails generate controller 名前 [アクション名..] [オプション]
                        - rails generate controller コントローラー名　アクション名　とコマンドを実行する事でコントローラーが作成できる。
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                | –helper | helperファイルを生成するか | true |
                | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate migration
                - マイグレーションファイルの生成
                    - 必ずupメソッドとdownメソッドを含めなければならない
                    - self.upがmigrationのバージョンを上げるときに実行
                    - self.downがmigrationのバージョンを下げるときに実行
                        - `down`メソッド内で行なう変換
                            - `up`メソッド内で行なう順序の正確な逆順にする
                    - クラス名をすべて小文字にしたものが、ファイル名アンダースコア(_)以降と一致する必要がある
                - $ rails generate migration 名前 [カラム名:型[:index]..] [オプション]
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –timestamps | timestampsファイルを生成するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | -d, –database=DATABASE | データベースの種類 | sqlite3 |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -q, –quiet | 進捗状況を表示しない |  |
                | -p, –pretend | ドライラン |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプを表示 |  |
                
                ### カラムの型
                
                | データ方 | 説明 |
                | --- | --- |
                | string | 文字列 |
                | text | 長い文字列 |
                | integer | 整数 |
                | float | 浮動小数 |
                | decimal | 精度の高い小数 |
                | datetime | 日時 |
                | timestamp | より細かい日時 |
                | time | 時間 |
                | date | 日付 |
                | binary | バイナリデータ |
                | boolean | Boolean型 |
                
                ### 作成されるファイルの基本構成
                
                ```ruby
                class マイグレーション名s < ActiveRecord::Migration
                    def up
                    end
                
                    def down
                    end
                end
                ```
                - カラムを指定して生成
                ```ruby
                $ rails generate migration AddTitleToPage title:string
                ```    
                - rails g maigtion
                    - SQLを実行せずに再現可能な方法でデータベーススキーマを継続的に進化させる事ができる方法
                        - マイグレーションはバージョン管理として捉える事もできる
                            - Active::Recordはどの時点からでも最新の状態に戻す事が可能になる
                    - rails g maigationの内部処理を追っている記事とかは見つけられなかった
                        - ただ、DSLという概念とかをしれた
                - マイグレーション
                    - データの型
                        - 他にどのようなデータの型があるのか？
                            - string : 文字列
                            - text : 長い文字列
                            - integer : 整数
                            - float : 浮動小数
                            - decimal : 精度の高い小数
                            - datetime : 日時
                            - timestamp : タイムスタンプ
                            - time : 時間
                            - date : 日付
                            - binary : バイナリデータ
                            - boolean : Boolean    
            - rails generate model
                - モデルの作成
                    - $ rails generate model 名前 [カラム名:型[:index]..] [オプション]
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –force-plural | 指定されたモデル名を強制的に使用 |  |
                | -o, –orm=NAME | 呼び出されるORMを指定 | active_record |
                | –migration | migrationファイルを生成するか | true |
                | –timestamps | timestampsファイルを生成するか | true |
                | –parent=PARENT | 生成されたモデルの親クラスを指定 |  |
                | –indexes | belongs_toカラムにインデックスを付与するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | –fixture | フィクスチャファイルを生成するか | true |
                | -r, –fixture-replacement=NAME | 呼び出されるフィクスチャを指定 |  |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
                
                ### カラムの型
                
                | 型 | 説明 |
                | --- | --- |
                | string | 文字列 |
                | text | 長い文字列 |
                | integer | 整数 |
                | float | 浮動小数 |
                | decimal | 精度の高い小数 |
                | datetime | 日時 |
                | timestamp | より細かい日時 |
                | time | 時間 |
                | date | 日付 |
                | binary | バイナリデータ |
                | boolean | Boolean型 |
                | primary_key | プライマリキー |
                
                ### indexの種類
                
                | 名前 | 説明 |
                | --- | --- |
                | uniq | ユニーク |
                | index | インデックス |
                - 補足
                    - integer, string, text, binaryでは制限値を{ }で記述
                - 例：
                    - 階層を指定
                    
                    `$ rails generate model admin/account`   
                - rails g model →内部処理
                    - railsコマンド　＝＞　DSLの分類に入る
                        - 特定のタスクを実行する事に特化したコンピューター言語
            - rails generate application_record
                - application_recordファイルを生成
                    - $ rails generate application_record [オプション]
                - オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | -r, -ruby=PATH | rubyバイナリのパス |  |
                | -m, -template=TAMPLATE | テンプレートのパス |  |
                | -d, –database=DATABASE | データベースの種類 | sqlite3 |
                | -G, –skip-git | .gitignoreファイルの生成をスキップ |  |
                | –skip-keeps | .keepファイルの生成をスキップ |  |
                | -M, –skip-action-mailer | Action Mailerファイルの生成をスキップ |  |
                | –skip-action-mailbox | Action MailboxのGemをスキップ |  |
                | –skip-action-text | Action TextのGemをスキップ |  |
                | -O, –skip-active-recode | Active Recordファイルの生成をスキップ |  |
                | –skip-active-job | Active Jobをスキップ |  |
                | –skip-active-storage | Active Storageファイルの生成をスキップ |  |
                | -C, –skip-action-cable | Action Cableファイルの生成をスキップ |  |
                | -S, –skip-sprockets | Sprocketsファイルの生成をスキップ |  |
                | -J, –skip-javascript | JavaScriptファイルの生成をスキップ |  |
                | –skip-hotwire | Hotwireの統合をスキップ |  |
                | –skip-jbuilder | jbuilderのGemをスキップ |  |
                | -T, –skip-test | testファイルの生成をスキップ |  |
                | –skip-system-test | システムテストファイルの生成をスキップ |  |
                | –skip-bootsnap | bootsnapのGemをスキップ |  |
                | –dev | githubリポジトリ上の自分のコードから作成 |  |
                | –edge | githubリポジトリ上の最新のコードから生成 |  |
                | –master, –main | RailsのメインブランチのGemfileでアプリケーションをセットアップ |  |
                | –rc=RC | railsコマンドの追加の構成オプションを含むファイルへのパス |  |
                | –no-rc | .railsrcファイルからの追加のロードをスキップ |  |
                | –api | APIのみのアプリケーションを生成 |  |
                | –minimal | 最小限のRailsアプリケーションを生成 |  |
                | -j, –javascript=JAVASCRIPT | 組み込むJavaScriptライブラリーを指定 | importmap |
                | –css=CSS | CSSプロセッサを選択 |  |
                | ｰB, –skip-bundle | bundle installしない |  |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate helper
                - 新しいヘルパーの作成
                    - RailsのView内で使う
                        - テンプレートのコードを簡潔にする仕組み
                            - ロジック
                                - ヘルパーでまとめて記載してDRYなコードを記載する
                    - $ rails generate helper 名前 [オプション]
                        - $ rails generate helper CreditCard
            - rails generate resource
                - 新しいリソースを生成
                    - RESTfulなリソース指向アプリケーションに適した空のモデルとコントローラを含む新しいリソースを生成
                        - $ rails generate resource 名前 [カラム名[:型][:index]..] [オプション]
                - Railsにおけるリソースとは？
                    
                    https://krs1.hatenablog.com/entry/2016/06/07/180005
                    
                    - リソースとはRESTfulなインターフェイスでCRUDの対象となるデータの事
                        - ルーティングに縛られる事なくヘルパーなどを使う事で表現できる
                    - 単一のリソースを使用する事などができる
                        - 要はDBが対象になる？
                    - resoucesとは
                    - Railsで定義されている7つのアクションのルーティングを自動で作成するメソッド
                        - resoucesを使うことで簡単にルーティングを作成できる。
                            - ルーティングを記載するのを短縮する事ができる
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –force-plural | 与えられたモデル名を強制的に使用 |  |
                | –model-name=MODEL_NAME | 使用するモデル名 |  |
                | -c, –resource-controller=NAME | 使用するリソースコントローラ | controller |
                | -a, –actions=ACTION ACTION | リソースコントローラーのアクション |  |
                | –resource-route | リソースルートを生成するか | true |
                | –migration | migrationファイルを生成するか | true |
                | –timestamps | timestampsファイルを生成するか | true |
                | –parent=PARENT | 生成されたモデルの親クラスを指定 |  |
                | –indexes | belongs_toカラムにインデックスを付与するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | –db, –database=DATABASE | 使用するデータベースを指定 |  |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | –fixture | フィクスチャファイルを生成するか | true |
                | -r, –fixture-replacement=NAME | 呼び出されるフィクスチャを指定 |  |
                | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                | –helper | helperファイルを生成するか | true |
                | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate channel
                - サーバとクライアントに新しいケーブルチャンネルを生成
                    - $ rails generate channel 名前 [メソッド..] [オプション]
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –assets | アセットを生成するか | true |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate integration_test
                - 新しい統合テストを生成
                    - $ rails generate integration_test 名前 [オプション]
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespace の生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –integration-tool=NAME | 呼び出される統合ツール | test_unit |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails sevrer
                - サーバーが立ち上がる
                    - サーバとは？
                        - クライアントに応答するもの
                - ITシステムにおいてのサーバー
                    - コンピュータである
                        - 常に応答するコンピュータ
                        - 立ち上げっぱなしのコンピュータ
                - クライアント(呼び出し元)
            - rails generate system_test
            - rails generate jbuilder
            - rails generate job
            - rails generate mailbox
            - rails generate mailer
            - rails generate benchmark
            - rails generate task
            - rails destroy
            - rails db:create
            - rails db:drop
            - rails db:migrate
            - rails db:encryption:init
            - rails db:environ
            - ment:set
            - rails db:fixtures:load
            - rails dbconsole
            - rails db:version
            - rails db:schema:load (2/4)
            - rails db:schema:dump
            - rails db:schema:cache:clear
            - rails db:schema:cache:dump
            - rails db:seed
            - rails db:seed:replant
            - rails db:prepare
            - rails db:reset
            - rails db:rollback
            - rails db:setup
            - rails db:structure:dump
            - rails db:structure:load
            - rails db:system:change
            - rails assets:clean
            - rails assets:clobber
            - rails assets:environment
            - rails assets:precompile
            - rails plugin new
            - rails console
            - rails runner
            - rails about
            - rails version
            - rails notes
            - rails routes
            - rails action_mailbox:ingress:exim
            - rails action_mailbox:ingress:postfix
            - rails action_mailbox:ingress:qmail
            - rails action_mailbox:install
            - rails action_mailbox:install:migrations
            - rails action_text:install
            - rails action_text:install:migrations
            - rails active_storage:install
            - rails app:template
            - rails app:update
            - rails cache_digests:dependencies
            - rails cache_digests:nested_dependencies
            - rails dev:cacherails importmap:install
            - rails initializer
            - rails log:clear
            - rails middleware
            - rails restart
            - rails secret
            - rails stats
            - rails stimulus:install
            - rails stimulus:install:importmap
            - rails stimulus:install:node
            - rails test
            - rails test:db
            - rails test:all
            - rails time:zones
            - rails tmp:clear
            - rails tmp:create
            - rails turbo:install
            - rails turbo:install:importmap
            - rails turbo:install:node
            - rails turbo:install:redis
            - rails yarn:install
            - rails zeitwerk:check
        - 逆引き（目的から検索する）
            - [新しいRailsのアプリケーションを作成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)  
            - [アプリケーションのひな型を生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            - [モデル以外のアプリケーションのひな型を生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            - [コントローラとビューの生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            - [マイグレーションファイルの生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            - [モデルの生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            - [application_recordファイルを生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
    - Topページを作成する（Railsコマンドの実践）
        - rails generate controller コントローラ名(home) ページ名(top)
            - DBを作成する
                - rails generate model [テーブル名] [カラム名]:データ型
                    - rails g model User name:text
                        - User
    - ルーティング
        - ブラウザとコントローラーを繋ぐもの
            - Pathとアクションの対応表と呼ばれる
                - リクエストの内容に応じて適切なアクションをコントローラーへ知らせる
                    - ブラウザからURLという情報が来る => ルーティング => コントローラ => ビュー
        - Ruby特有のDSLで記述されたルール
            - HTTPリクエストを適切なコントローラーとアクションへ転送する事でリクエストの処理方法を決定する
        - ページのパス
            - /top, /about, /shop
        - アクション
            - 処理
                - 処理A, 処理B, 処理C
        - 対応表
            - /top => 処理A
            - /about => 処理B
            - /shop => 処理C
        - ルーティングが指定するもの
            - 要は、HTTPメソッドとURLパスをペアにしたコード行を指す
        - ルーティングは変更可能
            - localhost:3000以降のURLに対応するようになっている
                - localhost:3000とは？
                    - localhost→ホスト名
                        - ネットワークに接続された機器はホストと呼ばれる
                            - ホストを示すのがIPアドレスやlocalhostとなる
                                - 自分自身のIPアドレスを示すものがループバックアドレスと呼ばれる。
                    - 3000→ポート番号
                        - ポート番号とは、ホスト内のどのポートで受け入れるか？決めるもの
                            - コンピューターがどの通信システムを使用するのか？判別するためのものである。
                                - 16ビットの整数　**0番～65535番まである**
                                    - **WELL KNOWN PORT NUMBERS**
                                        - **0番～1023番**
                                            - 使用目的が定められたポート番号
                                                - **IANAが管理している**
                                    - **REGISTERED PORT NUMBERS(登録ポート番号)**
                                        - **1024番～49151番**
                                    - **DYNAMIC AND/OR PRIVATE PORTS(ダイナミック/プライベートポート番号)**
                                        - **49152番～65535番**
                    - IPレイヤ:TCP/UDPレイヤ(port)
                        - **自分の(PCの)IPの3000番port宛にアクセスしてくれという指示になる**
                            - インターネット・プロトコル・スイート
                        - 自分のIPを指定する方法
                            - MACアドレス
                                - 各端末、LANなどに割り当てられている
        - URLの構成内容
            - プロトコル
                - HTTP => HTTP verb:HTTP動詞
                    - GET
                    - POST
                    - PUT
                    - DELETE
                - HTTPS
            - ホスト
                - local
            - パス
                - index
                - new
                - sreate
            - クエリパラメーター
        - ルーティングにおける基本的な7つの操作
            - index: すべてのレコードを表示します
            - new: 新しいレコード1件を作成するためのフォームをレンダリングします
            - create: newのフォーム送信を処理し、エラーを処理してレコードを1件作成します
            - show: 指定のレコード1件をレンダリングして表示します
            - edit: 指定のレコード1件を更新するためのフォームをレンダリングします
            - update: editのフォーム送信を処理し、エラーを処理してレコードを1件更新します
            - destroy: 指定のレコード1件を削除します
        - 基本的な7つの操作を表現する
            - get "/products", to: "products#index"

            - get "/products/new", to: "products#new"
            - post "/products", to: "products#create"

            - get "/products/:id", to: "products#show"

            - get "/products/:id/edit", to: "products#edit"
            - patch "/products/:id", to: "products#update"
            - put "/products/:id", to: "products#update"

            - delete "/products/:id", to: "products#destroy"
        - リソースルーティング
            - 基本的な7つの操作を毎回手で入力するのは冗長
                - 1行で表現する事ができるショートカットのようなものがある
                    - resources :products
                        - resourcesを使う事で一括で指定する事ができる
    - コントローラー
        - アクション
            - 処理
                - 処理A, 処理B, 処理C
        - アクション　＝＞　メソッド
            - 構文：
                - def top ... end
            - メソッド
                - 普通のメソッド
                    - クラスメソッド
                        - クラスの中で使える
                    - インスタンスメソッド
                        - インスタンスを介して呼び出して使う
    - モデル
        - モデル（モデルクラス）とは？
            - DBとのやり取りをする => テーブル操作
                - テーブル操作
                    - 削除
                    - 追加
                    - 参照
                    - 編集
                        - CRUD(Crete Read Update Delete)
            - Railsの内部
                - ApplicationRecord内のクラスにこれを行うメソッド
        - 命名規則
            - 基本的に単数形で記載する
        - コマンドでの生成方法
            - rails g model User name:text
        - Userモデルが作成される
            - class User < ApplicationRecord ... end
                - アプリケーションレコードを継承したクラス
        - Userモデル
            - usersテーブルを操作する
                - userの作成
                    - user1 = User.new(name: "六倉")
                        - 六倉インスタンスを作成
                - userの編集
                    - 1. ユーザ情報を取得する
                        - user = User.find_by(id: 2)
                    - 2. 1で取得したユーザ情報を編集する
                        - [user.name](http://user.name/) = "六倉"
                        - user.save
                - userの削除
                    - 1. ユーザ情報を取得
                        - user = User.find_by(id: 2)
                    - 2. 1で取得したユーザを、destroyメソッドを使って削除する
                        - user.destroy
                    - 構文：
                        - usersテーブルから、1人のuserを取得する
                        user = User.find_by(id: )
                - userの取得
                    - usersテーブルから、全てのuserを取得する
                        - name変数
                            - name = "六倉"
                            - users = User.all
                    - usersテーブルから、全てのuserを取得する && id順で並び替えたい
                        - users each do |user| puts([user.name](http://user.name/)) end
                            - users = User.all.order(id: :asc)
                                - asc, desc
                                    - 1, 2, 3, 4, 5, or 5, 4, 3, 2, 1
                                - 1, 2, 3, 4, 5 => 昇順 => asc
                                - 5, 4, 3, 2, 1 => 降順 => desc
        - データベースに対するCRUD操作
            - コントローラーからモデルを介してアクセスする
                - コントローラー内で＠変数に対してテーブル情報を代入
                    - View内で変数名.カラム名とする事で特定のデータを参照する事ができる
    - モデルメソッド
        - AplictionRecord(DBへマッピングを行うクラス)を継承したクラスを介して使う事ができるメソッド
            - Ruby特有のメソッドを実行する事でSQLを使わずにRDBの操作をできる
                - Ruby特有のDSLを作成しSQLをメソッドを介して生成している
            - newメソッド
                - オブジェクトの作成
            - saveメソッド
                - オブジェクトの保存
                    - SQLのINSERTクエリを生成する
            - allメソッド
                - DBの全てのオブジェクトを取得
                    - SELECT SQLクエリが生成されて全てのレコードを取得する
            - whereメソッド
                - 条件に合うオブジェクトを取得する
                    - SELECT SQLクエリ WHERE句 特定したい値にマッチするカラムを持つレコードがフィルタリングされる
            - findメソッド
                - IDを指定する形で、1件のレコードを検索する
                    - SELECTクエリが生成されidが1にマッチするidカラムをWHEREで指定する事に加えて返すレコードを1件のみに絞るため、LIMIT 1となる
                        - whereはLIMITの指定がないためレコードをフィルタリンングする機能を持つが、findはLIMITを持つため1つのレコードしか返さない
    - Active Recordとは？
        - RDBをRubyコードにマッピングする機能
            - CRUD操作　＝＞　構造化クエリ言語(SQL)
                - テーブルやレコードの作成、更新、削除など
    - Active Recordモデルの基礎
        - モデルジェネレーターを実行してProductモデルを作成するとapp/models/product.rbにファイルが生成される
            - ApplicationRecordを継承しているのみで他にはコードは記載されていない
                - モデルの定義はどこからくるのか？
                    - 表面上に記載するのではなく、バックグラウンドで処理してくれる
                        - Product.column_names
                            - Railsは動的にクラスの属性を定義する
                                - 開発者が手動で定義する必要がない
        - store(dev)> product = Product.new(name: "T-Shirt")
        - store(dev)> product.save
            - INSERTクエリを生成してレコードをDBへ挿入する
        - store(dev)> product
        - Product.create(name: "Pants")
            - createを使うとインスタンスの生成、DBへの保存を一括で出来る。
        - レコードをクエリで取り出す
            - ActiveRailsモデルを使ってDB内のレコードを検索する事が出来る
                - all => クラスメソッド
                    - Productに対して呼び出す
    - DB（データベース）
        - データの貯蔵庫
            - レコードとカラムで形成されるテーブルが集まったもの
                - データの新規作成、参照、削除、更新という操作が高速にできるようになった仕組み
        - 命名規則
            - テーブル名は複数形で記載する
                - カラムやレコードは基本的に複数存在している
                    - テーブル自体1つのように見えるが、その実態は複数になっている
        - データベースへの情報の保存方法（ユーザ体験から内部での処理の流れ）
            - ユーザがユーザ名やパスワードの登録などを行う
                - Viewファイル
                    - form_tagメソッドを使い、POSTリクエストがコントローラーに送られるようにする、この時にinputタグにはname属性をつける
                - ルーティング
                    - post 対応するルーティング
                - コントローラー
                    - ルーティングに対応するアクションでform_tagメソッドから送られてきたname属性が指定されているデータをparams[name属性]とする事で受け取る
                        - 受け取るデータをUser.new(カラム名: params[name属性], ラム名: params[name属性])とする事でインスタンスを作成する
                        - saveメソッドを使いデータを保存する
                        - redirect_toメソッドを活用して、データが保存に成功した場合に別のページに移動するようにする
    - マイグレーション(migration)
        - データベースに対して行う一連の変更のこと
            - マイグレーションを定義する事で一連の変更をトラッキングできる
    - View
        - 画面 => 表示画面 => ページの見た目
    - コンソール
        - IRB
            - 対話形式のシェル？
                - Rubyの埋め込まれたやつ？
                    - シェルの中にRubyのインタプリンタが埋め込まれている
        - コンソールを立ち上げた時にirbの表示が出てこない
            - 実行環境の違い
                - 細かい部分には目を向けなくても良いかも
                    - バージョン
                        - ライブラリのバージョン等
                - 端末の違い
                    - Mac,winouws
    - multipart
        - 現在、from_tag,from_forメソッドは統合されfrom_withメソッドの使用が推奨されている
            - from_withメソッドに対してfile_fieldを指定した状態で送信等をするとファイル名が文字列として認識されてしまい画像ファイルとして認識されないという事が起きる
                - 対応策：
                    - modelの指定
                        - modelを指定すると自動的にmultipartが適用されて複数の種類のデータを受け取る事が可能になる
                    - multipart ⇒ trueを指定する
                        - modelを指定していない場合などにはデータの種類が文字列ではない事を示すためにmultipartを指定する
    - Fileクラス
        - readメソッド
            - ファイルの内容を読み込むためのメソッド
                - path で指定されたファイルを offset 位置から length バイト分読み込んで返す。
                    - 画像ファイルも中身はバイトになっている
        - writeメソッドを使う
            - データの書き込みを行うメソッド
                - writeで指定したstringを書き込む
                    - 画像ファイルであればreadメソッドを使ってlength分読みこむ
                    - その後、読み込んだstringをwriteメソッドを使って書き込む
        - DBでは書き込まれたpngファイルなどの相対pathを参照できるようにする
            - pngファイルの構成
                - シグネチャ
                - チャンク(IHDR)
                - チャンク......
                - チャンク(IEND)
                    - チャンクの構成
                        
                        
                        | **フィールド名** | **サイズ** | **内容** |
                        | --- | --- | --- |
                        | Length | 4byte | このチャンクの Chank Data の大きさを表す |
                        | Chank Type | 4byte | このチャンクの種類を表すアルファベット4文字 |
                        | Chank Data | 0byte以上 | チャンクの種類に関連したデータ本体 |
                        | CRC | 4byte | データのエラーを検出するための情報 |
            - JPEGファイル
                - SOIマーカー、末尾にEOIマーカーで挟まれた領域で画像を示す
    - pudlicディレクトとは？
        - publicディレクトの責務
            - 静的ファイルを参照したい時にpublicディレクトリを使用する
                - エラーなど
    - ユーザー画像を表示する
        - 画像が表示される仕組み
            - データベースに画像を保存しておく。
                - その画像のファイル名の画像を表示するという流れ
        - publicフォルダ内に画像を表示する
            - 画像を保存するためにusersテーブル（データベース）に画像カラムを追加する
    - assetディレクトリについて
        - assetディレクトリの責務
            - アセットパイプラインを通じた管理と最適化をできる
                - キャッシュ化する事ができる
                    - JavaScriptファイル
                    - スタイルシート
                        - などで効率的に管理をする
    - 知識の整理
        - class
			- 動物クラス
				- 人間, 犬, 猫(インスタンス)
			- メソッド(処理)
				- 食べる
				- 見る
				- 走る
				- 鳴く
			- 変数
				- データに名前をつけた
				- 名前
		- プログラム
			- データと処理
			- 処理
				- メソッド
			- データ
				- 変数
				- クラス
    - データベース
        - データを保存しておく場所
            - テーブル
                - カラム(列)
                    - データの要素(属性)
                        - id, 名前, 年齢
                - レコード(行)
                - id(identification)
                    - レコードを一意に識別するために使う
                    - ユーザーテーブル(id, 名前)
                        - 六倉, 豊田, 堤竹
                        - id => 該当テーブル内のレコードを一意に判別するための仕組み
    - Railsのリクエストに対する処理の流れ(MVCアーキテクチャー)
        - ユーザからリクエスト（HTTPメソッド）がルーティングへ送られる
        - ルーティング内部でリクエストをパスとアクションの指示に形を変換しコントローラーへ渡す
        - コントローラーが対応するアクションとViewを発見しユーザーへ返す
    - リンクの作成
        - リンクをクリックするとなぜ別のファイルに飛べるのか？
            - リンクをクリックすると、指定したURLがリクエストされる。
                - ブラウザからルーティングに渡されてルーティング内でパスとアクションの対応表に応じて処理が実行される
                    - どのコントローラーのアクションと対応するViewを渡すか指示され、ユーザーへViewが返されるため別のファイルが送られる
        - リンクを作成する方法は２つある
            - htmlのaタグのhrefで指定する方法
                ```HTML
                <a href =”test”>test by href<a>
                ```
            - Railsのlink_toメソッドを使う方法
                - <%= link_to(”test by link_to, “test”) %>
                    - 第一引数に`ブラウザに表示する文字`を取り、第二引数に`URL`を取ります。
            - リンクに対応するようにルーティングの変更とコントローラー内であアクションを変更する事が必要
        - .erb（Embedded RuBy：埋め込み型Ruby）ファイル内での<%= %><% %>の違い、使い方
            - <%= %>or<% %>で囲む事でRubyのコードを使う事ができるようになる。
                - <%= %> → ブラウザに表示させる事が必要な場合
                - <%%> → ブラウザに表示させたくない場合
    - データベースについて
        - データベースとは表形式でデータを扱うもの
            - データベースはコントローラーからモデルを作成する事でテーブル操作が可能になる
                - モデルとは？
                    - ApplicationConttrollerを継承したクラスの事
    - Viewファイル内で変数を扱う
        - コントローラーがViewファイルを探してレスポンスする際にコントローラー内で変数を定義する事でViewファイル内で変数を活用する事ができる
            - 変数の前に＠を用いる事で変数はインスタンス変数になる、基本的にコントローラーからViewに変数を渡す場合にはローカル変数ではなくインスタンス変数を用いる
    - データベースのデータをアクションに持ってきて活用する方法
        - モデルの作成
        - rails generate model user カラム名：データの型
            - userがモデル名
            - カラムは必要な数作成する
        - rails db:migrate を実行する事でデータベースが作成される
            - マイグレーションファイルとは？
                - データベースの設計図
        - データベースへの情報の保存方法（console）
            - モデルを活用してデータ保存を行う
                
                ```ruby
                user = User.new(カラム名：”値”,カラム名：”値”）
                user.save
                ```
                
            - newメソッドでデータの準備
            - saveメソッドでデータの保存を行う
    - データベースの確認
        - データベースクライアントの開始
            - テーブルの一覧表示
                - スキーマの表示
        - データベースクライアントの停止
        
        ```ruby
        rails dbconsole
        sqlite>.table
        sqlite>.schema users
        qlite>.quit
        ```
    - 命名規則
        - モデルの命名規則
            - モデルはデータベースに対する操作をするためのクラスでありクラスとモデルは１対１の関係になっているため単数形で作成する。
        - テーブルの命名規則
            - テーブル内の情報は1つになる事は基本的にはない
                - カラムとレコード複数の値になる事が予想される
        - Viewの命名規則
            - Viewフォルダは配下に複数のViewファイルを持つため複数形
                - 各Viewファイルはアクションに対応する名前をつける
        - contorollerは基本的に複数のアクションを持つため複数形で作成する
    - Railsにおける一般的な機能の実装
        - 一覧表示
            - View
                - ＠変数名（複数形）に対して繰り返し処理を行う
            - コントローラー
                - ＠変数名にallメソッドを活用してテーブル情報を代入する
        - レコードの削除
            - View
                - 情報一覧表示をしたコードにlink_toメソッドでdestroyアクションを追加して記載することで削除ボタンを作成する
            - コントローラー
                - 変数に対してViewファイルから送られてきたidと同じidのデータを代入する。def destroy user = User,find_by(id: params[:id])
                - 変数に対してdestroyメソッドを活用してレコードの削除を行う
            - 物理削除
                - 物理的に削除
                    - destroyなどで物理的に削除する事
                        - ファイルを削除→論理削除
                            - ゴミ箱に入っている→物理削除
            - 論理削除
                - 論理的に削除
                    - カラムに削除フラグを設ける
                        - 通常、カラム削除フラグがfalseになっている
                        - 削除する時には削除フラグがtrueになる
                    - データベースからデータを取得する場合に削除フラグがtrueはそもそも表示しないなどという事ができる
                        - データの紛失の対策になる
        - レコードの編集
            - View
                - index
                    - 情報一覧ページでlink_toメソッドを活用してeditアクションへのリンクを作成する
                - edit
                    - form_tagメソッドを活用してコントローラーの指定
                    - input タグには初期値として名前などの情報が表示されるようにするvalue="<%=@変数名.カラム名%>”
            - コントローラー
                - editからupdateアクションを指定
                    - Viewから送られてきたid情報をローカル変数に代入したのちに、新しい値に書き換えて格納、saveメソッドを活用して保存、情報一覧ページへ移動とする
    - バリデーションについて
        - バリデーションとは有効なデータがデータベースに保存されるように事前に制約やルールを設ける事
            - クライアント側でのバリデーションや、コントローラーレベルでのバリデーションなど様々
                - 基本的にはモデルレベルでのバリデーションが適切
            - バリデーションのレイヤー
                - クライアント
                    - ユーザー名側に用意する事もある
                        - 入力中に表示が出るようにしたい
                - バッグエンド
                    - 処理速度を考慮するとバッグエンドで指定する事もある
                - データベース
                    - データの整合性を考えるとここだけでいい
                        - userテーブル
                            - ２文字　英単語のみ
                                - テーブル作成時にカラム単位で指定可能だが処理が遅くなってしまう
                - バリデーションの大前提はデータの不整合を起こさない
                    - ただ、UXを考慮すると入力中に表示が出ると良い
                    - 裏でセキュリティを考慮しないとカラム内にSQLを入れる事ができてしまう
                        - IPアドレスの書き換え
        - バリデーションの設定
            - validates :カラム名,{検証内容}　と記載
                - バリデーションに引っかかった場合にはfalseが返される
                - 引っかからない場合にはtrueとなり処理が実行される
                    - 空でのデータ保存を弾く
                    - 文字数制限を設ける
            - コントローラー
                - バリデーションを設定した場合trueとfalseで処理が分かれるためif文を使って処理が実行できた場合とできなかった場合で処理を分ける
        - 文字数制限のあるバリデーションに引っかかった場合
            - link_toメソッドを使ってページ移動してしまうと直前までの入力内容が保存されずに消えてしまう
            - renderを活用する
                - Viewを直接読み込む事ができるため編集内容が保存されるような形になる
                
                ```ruby
                @content = params[:content]
                if post.save
                    redirect_to("/post/all")
                else
                render("posts/new")
                end
                ```
                
                - View側では初期値として@contentを入れておく
    - Flash
        - ページ上に一度のみ表示されるもの
            - ページの更新や移動で表示が消える
        - 実装には特殊な変数flashを活用する
            - flashは様々な場所で共通して使用されるもののためapplication.html.erbに記載する
            ```ruby
            post.rb
            ↓
            class Post < ApplicationRecord
                    validates :content, {presence: true}
                    validates :content, {length: {maximum: 20}}
            end

            application.html.erb
            ↓
            <%= flash[:notice] %>

            if post.save
                flash[:notice] = "表示させたい内容”
            else
                flash[:notice] = "表示させたい内容”
            end

            ```
    - 変数session
        - ブラウザ上でログインした状態を保つ際に変数sessionを活用する
            - ログインに成功したのちに変数sessionに対してid情報を代入する。
                - ブラウザ上でページ移動などをしてもブラウザ側でログイン情報を保存する。
                    - 変数sessionがid情報をブラウザに返すようになる
                        - ログイン状態が保たれる
                            - session[キー]＝代入する値（ブラウザに表示する内容）
        - 変数sessionの構造
            - ActionController::Metal というクラスにあるsessionメソッド内でインスタンス変数@_requestにdelegateをしている　
                - ActionDispatch::Request::Session クラスのオブジェクトでgetアクションを呼び出す
                    - @_requestインスタンスに key, value が代入される
    - ログイン機能
        - 要件・処理
            - ログイン => {true => ログイン状態 , false => ログアウト状態 or 未サインアップ状態}
                - ユーザがログインページからメールアドレスやパスワードをRailsに送信する
                    - 送信された情報を元に操作しているユーザを特定してログイン状態とする
        - ルーティング
            - localhost:3000/loginのURLでlogin_formアクションが呼び出せるようにする
                - get "login" => "user#login_form"
        - アクション
            - def login_form end
        - View
            - 入力フォーム
                - パスワード入力
                    - パスワード入力フォームは入力すると伏字になるようにしたい
                        - type属性をpasswordに指定する事で入力すると伏字になるようになる
        - 実装時の要件処理
            - ・要件
                - ログインをする際にメールアドレスとパスワードの入力が必要になるようにしたい
            - ・ユーザー体験
                - login_formページでメールアドレスとパスワードを打ち込み。ログインボタンをクリックしてログインする
            - ・処理
                - ログインページを作る
                    - パスワード入力欄を追加で作る。
                - パスワード入力中は入力した内容が伏字になるようにする
                    - パスワードカラムを追加する。
                        - コンソールでrails ganerate maigrate ファイル名でマイグレーションファイルを作成する
                            - ganerateコマンドで作成したマイグレーションファイル内でカラムの追加を記載する
                                - add_columフォルダ名, :カラム名, :データの型を指定する
                                    - rails db:migrateでマイグレーションファイルを実行する
                    - パスワードカラムにバリデーションをかける
                        - パスワード情報は確実に存在して欲しい情報のためバリデーションで本当に存在するのかをチェックする
                            - userコントローラー内でpresence:trueを活用してvaridetionをかける
                                - varidetion :password, {presence:true}
    - before_action
        - 全てのアクションに共通する処理がある場合にはbefore_actionを使う
            - 全てのアクションはapplicationコントローラを経由するため共通する処理はbefore_actionでまとめる事ができる
        - 特定コントローラでの処理において共通して行われる処理がある場合にはDRYの原則に則ってbefore_actionに処理を切り出した上でonly: %i[]を使ってアクションを指定する
    - パーシャルビュー
        - 繰り返した処理などの場合にはパーシャルビューに切り出した上でインスタンス変数はローカル変数へしておくと便利
    - 既存テーブルへのカラムの追加
        - 画像を保存するためのカラムをすでに作成されているテーブルに追加する
            - rails generate model User image_name:string
                - modelとマイグレーションファイルが生成される
                    - 今回はモデルは作成せずにマイグレーションファイルのみ作成したい
        - マイグレーションファイルとは
            - マイグレーション＝移行
                - データベースにおけるマイグレーションの実行とは
                    - データベースの変更をファイルに保存する。保存した内容を実行してスキーマ(データベースの構造を表現する設計図)を変更する事
            - maigrationファイルのみを作成する方法
                - rails g migration ファイル名　で作成する
                    - rails generate maigration User image_name:striog
                        - ファイル名は追加するカラム名を含めるなどわかりやすいものにする
            - マイグレーションファイルの仕組み
                - rails db:migrateはマイグレーションファイル内にあるchangeメソッドに書かれている変更内容を実施する事
                    - 変更内容をマイグレーションファイル内で記載する事でコマンド（rails db:migrate）を実施した際にデータベースに変更が起きる
            - カラムを追加する
                - add_column :テーブル名, :カラム名, :データ型
            - データベースへ変更を加える
                - rails db:migrate
    - ユーザ登録時に初期画像としてdefoltの画像が入るようにする  
        - ユーザ行動
            - Topページのヘッダーにある”新規投稿”のテキストリンクをクリックする
                - 新規登録画面（createアクション）でユーザ名とemailを入力して新規登録ボタンを押す
        - 要件
            - ユーザー登録時の初期画像としてdefoltの画像をカラムへ追加する
                - createアクションで@userをnewメソッドを使い代入する際にimage_nameも引数として一緒に渡す
                    - 初期画像として準備された画像がユーザー詳細ページとユーザー一覧で表示されるようにする
                        - HTMLの<img>タグを使って表示する => src = /user_images/ファイル名
            - Rubyのコード部分は<%= %>で囲む
                - ユーザ一覧では、繰り返し処理で@user.image_nameが表示されるようにする
    - Rubyにおける画像の取り扱いについて
        - 画像とは？
            - 普段、Viewでクライアント（人間側）が見ている画像はコンピューターがデータを元に表示した画像
        - コンピューターにとって画像はデータファイルとして認識されている
            - そのため、画像を表示させたい場合などの際には画像データのファイルを作成しそれを表示する事で画像が表示できるようになる
        - ファイルの生成
            - Rubyに元々あるFileクラスのwriteメソッドを使う
                - File .write(ファイルの場所,ファイルの内容)
        - 送信した画像を保存できるようにする
            - ファイル名をデータベースに保存
                - データベースへの保存はnameやemailの保存をしたようにカラム値の上書きをする
                    - ユーザーのid.jpgになるようにする
                        - "#{@user.id}.jpg"
                            - public フォルダ内に画像を作成
        - 画像を受け取る
            - 画像もinputでname属性を指定しているため変数paramsを活用して受け取る事ができる
                - params[:image]の中には、送信された画像ファイルに関する情報が入っている
    - ここで受け取る画像の情報を元にpublicフォルダ内に画像ファイルを作成する
        - 画像をデータファイルに保存したいが通常のテキストとは違う特殊なファイルになるためその場合にはFile.binwriteメソッドを使う
            - binwriteメソッドに引数として変数imageに対してreadメソッドを使った事で得たとで画像データをファイル内容として保存する事ができる
        - 画像を保存する際は本当に画像データが送信された場合のみに実行するようにする
            - updateアクション内でif文を作成する
                - if  params[;image]とする事でデータが送信されたか確認する
                    - input で name属性をimageと指定している
    - Webアプリケーションにおいてパスワードの管理に関する知識は必須
        - パスワードを安全に管理する
            - Webサービスは不特定多数のクライアントが利用する
                - パスワードが安全に管理できないと流出やPCを覗かれた際に漏れてしまう可能性などがありパスワードが漏れるという事は他人のアカウントにログインできてしまうという事になる
        - 通常のテーブルでのデータ管理方法 => 文字列としてデータの情報
        - 安全性の高いデータ管理方法 => カラム内のデータをハッシュ化して管理する
            - Gem（ジェム）
                - RubyやRailsでよく使う機能をパッケージ化したもの
                    - bcryptというGemを使用する
                        - ハッシュ化するパッケージ
                            - Railsにはインストールしたい Gemを記載するGemfileがある
                                - GemfileにはすでにいくつかのGemがインストールされている
                                    - gem 'gemの名前', 'gemのバージョン'　と記載する事でGemをインストールできる
                                        - バージョンを指定しない場合には最新のものがインストールされる
                    - gem 'bcrypt'
                        - bundle install　をターミナルで実行する事でインストールできる
                            - has_secure_passwordメソッドをモデルで実行する
                                - has_secure_passwordはデータが存在するか？自動で判別してくれる機能もあるためバリデーションが不要になる
                            - 保存されるデータベースはpassword_digest カラムになる
                                - passowordカラムは不要になるため削除
                    - ログイン方法をauthenticateメソッドを使うように変更する
                        - passwordカラムの値と入力内容が一致するか検証する
                            - authenticateメソッドを使う
                                - if @user && @user.authenticate(params[:password])
    - 中間テーブルの概念
        - 投稿機能といいね機能、ユーザーという概念があるWebアプリケーションなどにおいて
            - 特定の投稿に対するいいねという要素とそのいいねを登録したユーザーという概念の2つが重要になる
                - それらを中間でまとめる中間テーブル的な概念が必要になる
                    - ユーザがいいね機能を使用したという事を保存するデータベースが欲しい
                        - １つのいいねに対して(1レコード)
                            - どのユーザーが？
                                - user_id
                            - どの投稿に対していいねしたか？
                                - post_id
                                    - の２つのカラムが必要
                    - データベースを作成する
                        - rails genarate model Like user_id:integer post_id:integer
                            - rails db:maigerate
                                - いいね機能において二つのデータがない事はありえないためバリデーションを作成する
                                    - user_id　 post_id
    - キャッシュ化する
        - cacheメソッドを使うと、HTMLをキャッシュに保存できる
            - 製品に固有のキャッシュキーを生成する
                - $ bin/rails dev:cache
    - フィールドをAction Textでリッチテキストにする
        - リッチテキスト機能やマルチメディア要素の埋め込み機能が求められる
            - RailsのAction Textを使うと機能をすぐに使う事ができる
        - Action TextはActive StorageというRailsの機能の上に構築される
    - 国際化
        - ビューのtranslateヘルパーは訳文を検索　＝＞　ロケール設定に合うテキストを返してくれる
            - デフォルト => config/locales/en.yml
            - Japan => config/locales/ja.yml
                - Railsに使うロケールを指定する
                    - Application Controllerで定義する
                    ```Ruby
                    class ApplicationController < ActionController::Base
                    # （省略）

                        around_action :switch_locale

                        def switch_locale(&action)
                            locale = params[:locale] || I18n.default_locale
                            I18n.with_locale(locale, &action)
                        end
                    end
                    ```
                - http://localhost:3000/products?locale=enをブラウザで開くと、英文が表示されます。
                - http://localhost:3000/products?locale=jaをブラウザで開くと、日本語の訳文が表示されます。
                - ロケールを指定しないhttp://localhost:3000/productsをブラウザで開くと、英語にフォールバックします。
            - config/locales/en.ymlに記述する方法
                ```Ruby
                en:
                hello: "Hello world"
                products:
                    index:
                    title: "Products"
                ```
                - <h1><%= t ".title" %></h1>
                    - .　＝＞　ローケルを相対検索する事を表す指示
                ```Ruby
                ja:
                hello: "こんにちは、世界"
                products:
                    index:
                    title: "製品"
                ```
                - http://localhost:3000/?locale=enで英語ローケルを表示するとProductsが表示される
                - http://localhost:3000/?locale=jaで日本語ローケルが表示されるようになる
    - 通知機能を実装する
        - 特定の在庫が復活した時にeコマースストアでよくみられるもの
    - belongs_toオプション
        - 購読者と製品が１対多の関係性を持つようになる
            - 従属関係になるという事
    - has_many
        - 関連づけしたモデルが関連付けされたモデルのインスタンスを複数持つ事が可能になる
            - 主にbelongs_toの逆側になる事が多い



・要件
ログインしているユーザが表示されている投稿にいいねしている場合にはいいね済み、いいねしていない場合にはいいねしていませんという表示をする
・ユーザー体験
　　いいねした投稿にはいいね済み
　　いいねしていない投稿にはいいねしていませんという投稿がでるようになる
・処理
ログインしているユーザーがその投稿にいいねしたデータが存在する場合にはtrueになるif文を作成する
　if find_by(user_id:@current_user.id , [post_id:@post.id](mailto:post_id:@post.id)



Rails 要約

Ruby on Rails 5
　 Rubyのフレームワーク
　 　Ruby
　 　　プログラミング言語
　　Webアプリ
　　　ブラウザ上で動くアプリケーション
　　　　ブラウザさえあれば動く
　　　　　Android、iOSなどのOS関係なし
　　ネイティブアプリ
　　　Android、iOSで動くアプリ
　　　　特定の環境で動くアプリ
　　　Webアプリを作る上での枠組み
　　　　なぜフレームワークを使うのか？
　　　　　開発に必要な作業を軽減してくれるものであるため
　　　　　　Railsの機能を使う事で作業を軽減してくれる
　　　　　　　システムにおいて共通の部分がある
　　　　　　　　データベースとのやりとり
　　　　　　　　ルーティング
　　作る事ができる機能
　　　ログイン機能
　　　トップページ
　　　新規投稿や編集機能　　など

Railsアプリケーション開発
　　　ターミナルでコマンドを実行する事で開発を始める事ができる
　　　　rails new アプリケーション名　
　　　　　アプリ名と同じフォルダを作成できる
　　　　　　アプリケーション名/
　　　　　　アプリ名と同じフォルダ内にRailsアプリケーションにおいて必要なフォルダやファイルが作成される
　      　app/
　      　 アプリケーションにおけるメインフォルダ
　      　 　コントローラ
　      　 　View
　      　 　モデル
　      　 　　MVCアーキテクチャ
　      　config/
　      　　設定情報に関するフォルダ
　      　　　ルーティング
　      　db/
　      　　データベースに関するフォルダ
　  　rails server 　localhost:3000
　  　 サーバーを立ち上げる
　  　 　サーバーとは？
　  　 　　サーバーは常に待機しているコンピューターでクライアントの要求に常に答えるもの
　  トップページを作る
　  　rails generate controller home top → localhost:3000/home/topというページが作られる
　    rails generateコマンドが実行される事でページを作成するのに必要な３つのファイルが作成される
　　  　　View
　　  　　　ページの見た目
　　  　　　　Rails がクライアントからの要求に応じてViewを返す事でページが表示される
　　  　　　　　Appフォルダ
　　  　　　　　 Viewフォルダ
　　  　　　　　  Home/　フォルダ　→rails generateで新しく作られる　
　　  　　　　　   top.html.erb　ファイル　→rails generateで新しく作られる
　　  　　　　　　　　　htmlファイルの内容を変更する事でページの見た目が変更される
　　  　　controller
　　  　　  Railsはクライアントからの要求を一度コントローラを経由してViewを返している
　　  　　 　 Appフォルダ
　　  　　 　 　controllersフォルダ
　　  　　 　 　　class Home controllers < Application controllers
　　　  　　  　　home_controller.rb　→rails generateで新しく作られる
　　　  　　  　　　.rbファイルの中でTopメソッドが追加される
　　　  　　  　　　　Rails controllersの中でメソッドはアクションと呼ぶ
　　　  　　  　　　コントローラ内のアクションはRailsからブラウザに返すViewを選択する役目がある。
　　　  　　  　　　コントローラと同名のViewフォルダ内からアクション名のついたHTMLファイルを探してブラウザに返す
　　　  　　  　　　　Home_contoroller.rb→ Viewフォルダ→Homeフォルダ→Topアクションに対応するHTMLファイル
　 　 　　routing
　 　 　　　URLのpathとアクションの対応表
　 　 　　　　クライアントの要求とコントローラーを繋ぐ役割
　 　 　　　　　App
　 　 　　　　　 config/フォルダ
　 　 　　　　　  routes.rb
　 　 　　　　　   get "URL" => "コントローラー名(Path)#アクション名"
　 　 　　　　アクションの実態
　 　 　　　　　Application controllerを継承したクラスの中のメソッド
　 　 　　　URLの変更
　 　 　　　　get "URL" => "コントローラー名(Path)#アクション名"
　 　 　　　　　コントローラーとアクション名が変わらずにURLの部分のみ変更する事で表示内容は変更せずにURLのみ変更する事ができる
　 　 　　　　　　get "Home/top" => "Home#top" → get "top" => "Home#top"
　 　 　　　　　　　どちらもViewフォルダ内のHomeフォルダのTopアクションに対応するHTMLファイルを返すようにコントローラーに繋がれる
　 　 　　　　 後ろに/〇〇がないURLを指定した際のコントローラーの指定方法
　 　 　　　　 　get "/" => "home#top”
　 　　rails generate controller home topコマンドを実行した際にページのレイアウトやデザインを決めるCSSファイルも自動生成される
　 　　　app/
　 　　　 asset/
　 　　　  stylesheets/
　 　　　   home.scss
　 　　　stylesheets内で作成されたCSSファイルにコードを書くと全てのViewに自動で適応される
　 　サービス紹介ページを作る（例）
　 　　新たにページを作る際には再度コマンドでコントローラーとファイルの作成はできない
　 　　　コントローラーファイルはもう生成されているため重複してしまう
　 　　同じコントローラー名でページを作成したい場合には自分でルーティング、コントローラ内のアクション、Viewファイルを作成する必要がある
　 　　 ruting,controller
　 　　 　すでにあるruting,controllerファイルに追記する
　 　　 　　ruting
　 　　 　　　get "about" => "home#about"
　 　　 　　controller
　 　　 　　 def about end
　 　　 View
　 　　  VIewファイルは該当するフォルダ上で新規作成を選択する事で新規ファイルが作成され、新規作成されたファイルに名前をつける
　 　画像の保存場所と画像の使用方法
　 　　Publicフォルダに保存する事でViewファイルやCSSファイルで画像名を指定する事ですぐに使用する事ができる
　 　　View → <img src="/画像名" >　CSS → background-image: url("/画像名");
　　　リンクの作成
　　　　テキストリンクはHTMLでの指定方法と同じ
　　　 　aタグで囲みhrefでURLを指定する
　　　 　　<a href=" "> text </a
　　　　 　hrefで指定するURLはルーティングのget ""部分で指定するURLにすることに注意が必要
　　 データベースとは
　　 　データを保存しておく貯蔵庫
　　 　　データベースではテーブルと呼ばれる表で情報を管理している
　　 　　　行　レコード
　　 　　　列　カラム
　　 　データベースの作成方法
　　　 　マイグレーションファイルというデータベースを作成するファイルを作成する
　　　 　 rails generate model テーブル名　カラム名：データの型（text or content）
　　　 　  app/
　　　 　   db /
　　　 　    migrate/
　　　 　     ファイルが自動生成される
　　　 　 マイグレーション
　　　 　 　移行
　　　 　 データーベースにおけるマイグレーション
　　　 　 　データベースに情報を変更・保存する事
　　　 　 　　データベースの変更内容をファイルに保存して、その情報を実行してスキーマを変更する手法の事
　　　 　コマンドでrails db:migrateを実行するとmaigrateファイルの通りにデータベースへ変更される
　　　 　マイグレーションエラー
　　　 　　migrateファイルを作った状態でrails db:migrateを実行せずにページ表示などをするとエラーが表示される
　　　 　model
　　　 　 rails generate model テーブル名
　　　 　 　rails g model コマンドを実行する事で指示したテーブル名のモデルができる
　　　 　 　　モデルとは
　　　 　 　　　Application Recordクラスを継承したクラスの事
　　　 　 　　　　テーブル操作　CRUD
　　　 　 　　　　　作成 Create
　　　 　 　　　　　 インスタンス名＝model名.new インスタンス名.save
　　　 　 　　　　　取得 Read
　　　 　 　　　　　 変数＝model名.find_by(引数)
　　　 　 　　　　　 　find_by
　　　 　 　　　　　 　　１件のみ取得
　　　 　 　　　　　 　全件取得
　　　 　 　　　　　 　　変数＝model名.all
　　　 　 　　　　　削除　Delate
　　　 　 　　　　　 インスタンス＝モデル名.find_by(引数)　インスタンス.destroy
　　　 　 　　　　　編集  Update
　　　 　 　　　　　　インスタンス＝モデル名.find_by(引数)　インスタンス.カラム名＝”上書きしたい内容” インスタンス名.save
　　　 　 　model名とtable名の違い
　　　 　 　　User　users　
　　　 　 　　 model名→単数　テーブル名→複数
　　　 　 　　 　Rails内部でモデル名の単数系からテーブルの複数系へ変更している
　　　 　 　　
　　　 　db作成の流れ
　　　 　　rails generate model テーブル名　カラム名：データの型(数値、文字列　text）　コマンドの実施
　　　 　　rails db:migrateコマンドの実行
　　 投稿一覧ページを作る（例）
　　 　データベースの情報を一つずつ呼び出して表示する事を繰り返す
　　 　　postsコントローラーを作成する
　　 　　　homeコントローラーでも作成可能だが投稿に関する事で分ける
　　 　　　　目的に合わせたコントローラーを作成する
　　 　　　　　rails generate controller posts index
　　 　 データベースでデータとして管理する
　　 　 　HTMLのままではデータベースと接続できない
　　 　 　　変数を定義する
　　 　 　　　＜％　％＞で囲むことでViewの.erb(Embedded Ruby　埋め込み型Ruby)ファイル内でRubyのプログラムを使用する事ができる
　　 　 　　　通常、変数の定義はViewファイルではなく、コントローラーで行う
　　 　 　　　　def アクション名　＠変数名＝内容　end
　　 　 　　　　　通常、アクションで定義した変数はViewファイルでは使用できないが＠を変数名の前につける事で特殊な変数になりViewファイルの中でも使用できるようになる
　　 　 　　定義した変数を出力する
　　 　 　　　＜％＝　％＞で囲むことで変数の出力をする事ができる
　　 　 　　投稿内容を配列にする
　　 　 　　　＜％　posts＝［配列１,配列2,配列3,］　％＞
　　 　 　　　　＜％％＞で配列postsを囲む
　　 　 　　　　　配列は複数行にわたって書くこともできる
　　 　 　　投稿内容が配列になったpostsに対して繰り返し処理を実行する
　　 　 　　　＜％　posts .each do |post| ％＞ <div class = "post-index-item" > <%= post %> <div> <% end %>
　　 　 　　　 .each doは要素の数だけ繰り返して処理するためHTMLを複数かく必要がなくなる
　　　rails console
　　　　コンソールでコマンドを指示する事でモデルにアクセスする事ができ、テーブル操作（CRUD）をする事ができる
　　　　　rails console を実行してからquitをコマンドするまでRubyのコードを実行できる
　　　　　　rails console 1+1 = 2 quit
　　　　　コンソールの起動からquitまで変数を定義した設定が保存される
　　　　　rails console text="kouki" text+"mutsukura" = kouki mutsukura quit
　　データベースへの情報の追加
　　　consoleからモデルを使いnewメソッドを使いインスタンスを作成する
　　　　post = Post.new(content: "Hello world")
　　　　 postテーブルのcontentカラムのHello worldレコードを作成する事ができる
　　　　.save
　　　　 newメソッドを使ってインスタンスを作成した後にsaveメソッドを使う事でテーブルへ保存する事ができる
　　　saveメソッドを使う事ができる理由はpost class が Application record class を継承している事で使う事ができる
　　データベースから情報を引きだす方法
　　　特定の情報のみ引き出す方法
　　　　post= post.first post.content
　　　　postテーブル　一行目のcontentカラムのデータを引き出す
　　　全ての情報を引き出す方法
　　　　rails console posts = Post.all
　　　　 Postテーブルにある情報を全て配列で引きだすことができる
　　　　 　配列の中から情報をインデックス番号で引きだす
　　　　 　　Post.all ［０］
　　　　 　カラムの内容を引きだす
　　　　　　　Post.all ［０］.content
rails consoleでできること
　データの作成
　　newメソッド、saveメソッド　など
　データの取得
　　allメソッド、firstメソッド　など

テーブルの内容をViewに表示する
　　　　コントローラー
　　　　　@posts = Post.all
　　　　　 コントローラー内での変数の定義は変数名の前に＠をつける
　　　　　 Postテーブルから全ての情報を引き出し、配列にする
　　　　　 　@postsは、postテーブル全ての情報が配列になったもの
　　　　View
　　　　　テーブル全ての情報に対して繰り返し処理を実行する
　　　　　　<% @posts .each do |post| %>  <% div class ="post-index-item" %> <%= post.content %> </div> <% end %>
　　　コントローラー内で定義したpostテーブル全ての情報が配列になった@postsを配列一つずつ呼び出しpostへ代入。変数postへdivタグを使いclass名をつける。変数postをカラムcontentに指定し出力する。
　　　共通するHTMLをまとめる方法
　　　　views/layouts/application.html.erbへどのページでも共通するheadタグやbodyタグ、headerなどはまとめて書く
　　　　　<%= yield %>というコードがapplication.html.erbにありTopページのHTMLやAboutページの HTMLなどはyield部分に代入される事でページ毎に共通する部分と変わる部分が出てくる
　　　link_toメソッド
　　　　リンクを作る
　　　　　Rubyのコードであるlink_toメソッドを使い<a>タグを作成する
　　　　　　<%= link_to ("リンク先”, "/リンク先" )％＞　<a href = "/リンク先">表示内容</a>
　　　カラムについて
　　　　データベース作成時に３つのカラムが自動生成される
　　　　　idカラム
　　　　　　データベースに追加された情報に対して順番に番号をつける
　　　　　created_atカラムとupdated_atカラム
　　　　　　データーベースにデータが保存された時刻
　　　　　　データが更新された時刻　が入る
　　　特定のidのデータを取り出して表示する方法
　　　　find_byメソッドを活用する
　　　　　モデル名.find_by(カラム名: 値）
　　　　Post.show
　　　　　ページの表示にはクライアントの要求にルーティングが答えてコントローラーが対応するアクションと、Viewをクライアントに返す事で表示される
　　　　　 rutingのURL（Path）部分に : を用いて記載する事でposts/:id などとする事でposts/〇〇を全て同じアクションに誘導できるようにする
　　　　　　 注意点
　　　　　　 　posts/indexよりも前に記載してしまうとposts/:の対応するものが変わってしまうため後るに書かないように注意
　　　　　showアクション
　　　　　　showアクションではURLのidカラムと表示するidカラムが同一でないといけない
　　　　　　　URLからidカラム値を取得する必要がある
　　　　　　　　変数params
　　　　　　　　 コントローラーのアクション内ではURLのidは変数paramsに入っている
　　　　　　　　  params[:id]とする事でURLの数値を取得する事ができる
　　　　　　投稿詳細ページを作成する（例）
　　　　　　　コントローラ内で投稿内容を変数として定義する
　　　　　　　　@post = Post.find_by(id: params[:id]) →（idカラム  URLのidカラムがハッシュとして代入されたもの）
　　　　　　　＠postをViewで表示する
　　　　　　　　<div class = "post-show-item">   <% = @post.content %>   <div class = "post-time">   <% = @post.created_at %>  </div>  </div>
　　　　　　　　 divタグを使って投稿内容の詳細ページという意味のclass名をつける、URLと同じidカラムのレコードがコントローラー内で変数へ代入されている。同じレコード内のcontentカラムを表示、同じレコード内のcreated_atカラムを表示する
　　　　　　　投稿部分をクリックすると詳細ページへ移動するリンク作成
　　　　　　　　link_toメソッドを使ってリンク作成
　　　　　　　　　<%= link_to(第一引数, 第二引数）　%>
　　　　　　　　　posts .each do |post| (post.content, "/posts/#{[post.id](http://post.id/)}") end
　　　　　　　　　　第一引数　表示内容は投稿内容にするためcontentを指定
　　　　　　　　　　第二引数　リンクは詳細ページへ移動したいため繰り返し処理で変数postへ代入されたデータのURLのid部分を活用
　　　新規投稿機能
　　　　HTMLで使ったinput ,textareaタグなどを活用する
　　　　　type="submit" value="投稿"
　　　　　 input
　　　　　 　多くのtype（型）がある
　　　　　　　　buttom
　　　　　　　　checkbox
　　　　　　　　color などなど
　　　　　　属性
　　　　　　　value
　　　　　　 accept
　　　　　　 alt
　　　　　　 autocapitalize などなど
　　　　createアクション
　　　　　入力フォームから投稿内容を受け取りデータベースへ情報を保存する
　　　　　　/posts/create
　　　 　ルーティング
　　　 　　今までルーティングを記載する際にはget "URL"としてきたがデータベースの変更を行いたい場合には post "URL"　とする
　　　 　　　post "posts/create" = posts#create
　　　  form_tagメソッド
　　　   入力フォームからの情報を送信する先を指定する
　　　   　form_tag(送信先のURL) do　end  HTML内で Rubyのメソッドを使うため＜％％＞で囲む
　　　   　　＜％　form_tag(posts/create) do　％＞  <textarea></textarea>  <input type = "submit" 属性 ="表示内容"> <% end %>
　　　   　　　submitを押した瞬間にposts/createへ入力内容が送信される
　　　 createアクションを実行した後に２点問題がある
　　　 　情報を送信するため送信後に表示するViewがない
　　　 　　Viewを表示するのではなくredirect_toメソッドを使ってページへ転送する
　　　 　　　redirect_to(URL)
　　　 　　　　指定したURLへ転送できる
　　　 　情報を送信するのみで保存ができない
　　　 　　投稿内容をcreateアクションに送信されるようにする
　　　 　　　入力内容に属性をつけて送信できるようにする
　　　 　　　　<textarea name="content" > </textarea>
　　　 　　　　 name がキーになったハッシュが送信される
　　　 　　　　 　変数paramsを活用して受け取る
　　　 　　　　 　　params[ :content ]
　　　 　　　　 　　 paramsはname属性に設定した文字列をキーとしたハッシュになっている
　　　 　　　　 　　 　name="content" 　を指定する事でハッシュになったデータを受け取る事ができる
　　　 　送信された内容を受け取って保存する
　　　 　 rails consoleでやった事を活用する
　　　 　 　postインスタンスを　content:  params[:content ] を用いて、そのpostインスタンスを保存する
　　　 　 　Post.new（content:  params[:content ] ）でcontentカラムに params[:content ] （入力フォームからの入力内容）レコードを保存する
　　　変数paramsの使い方
　　　 ①「:○○」を使ったルーティングのURLから値を取得する
②「name="○○"」が付いたフォームの入力内容を受け取る
　変数paramsはユーザの入力値
　　　投稿一覧の順番を変える
　　　　orderメソッド
　　　　　order(カラム名: 並び替えの順序）のように使う
　　　　　　昇順　:asc　
　　　　　　降順　:desc　新しいものから順に並べる

投稿の編集
　　　投稿の編集に必要な行程
　　　　投稿（データベース）の情報を取得する
　　　　　find_byメソッド
　　　　取得した投稿（データベース）の情報を上書きする
　　　　　カラム値を再定義する
　　　　　　テーブル名.カラム値＝”上書きしたい内容”
　　　　データベースに保存する
　　　　　saveメソッド
　　　updated_at
　　　　投稿やデータベースの情報を編集等変更を加えるとupdated_atのタイムスタンプが更新される
　　投稿の削除
　　　投稿の削除に必要な行程
　　　　投稿（データベース）の情報を取得する
　　　　　find_byメソッド
　　　　取得した情報をdestroyメソッドを使い削除する

投稿編集ページを作る
　　　対応するルーティング、アクション、新しいViewを作成する
　　　 ルーティング
　　　  get "posts/:id/edit = posts#edit
　　　   posts/2/editのようなidに応じた編集画面を作成できるようにする
　　　 アクション
　　　 　postsコントローラー内にeditアクションを作る
　　　 View
　　　 　edit.html.erbを新規で作成する
　　　編集ページへのテキストリンクを作成する
　　　　リンクにはshowアクションで指定する:idを活用する
　　　　　編集したい投稿の情報を取得する（コントローラー）
　　　　　 変数paramsを活用してURLからidを受け取る
　　　　　 　@post = Post,find_by(id: params[:id]
　　　　　取得した情報を上書きできるように編集ページへのリンクを作成する
　　　　　 link_toメソッドにコントローラーで取得したidを活用して編集ページへのリンクを作る
　　　　　 　<%= link_to ("編集" , "posts/#{@post.id}/edit) %>
編集ページに初期値が準備された入力フォームを準備する
　 textareaは初期値を設定する事ができる
　　<textarea>初期値</textarea>
　投稿を呼び出す(コントローラ)
　　@post = Post.find_by(id: params[:id])
　　 @postにfind_byメソッドを活用しid（paramsを使って取得したURL内のID）の投稿を引きだす
　呼び出した投稿の contentカラムを初期値として準備する（View）
<textarea><%= @post.content%></textarea>
　コントローラーで定義した変数@postのcontentカラムを引き出す
updeteアクション
　　　入力フォームから送信される情報をデータベースへ保存する
　　　　ルーティング
　　　　　post posts/:id/updete="posts#updete"
　　　　　 updeteはフォーム（編集して上書きした内容）をを受け取りデータベースの変更をするためpostで始める
　　　投稿一覧ページへ転送する
　　　　コントローラー
　　　　　編集内容を受け取ってデータベースの変更をした後に投稿一覧ページへ転送されるようにする
　　　　　　def updete redairect_to("posts/index") end
　　　　　　 リダイレクトされるためViewは必要ない
　　   投稿するデータ（編集前のデータ）を取得
　　   　@post = find_by(id: params[:id])
　　   フォームから編集されたデータを受け取ってデータベースへ保存する
　　   　変数paramsの機能を使ってtextareaにname属性をつける
　　   　　<textarea name="content">編集内容</textarea>　（View）
　　　　　　投稿データの更新（コントローラー）
　　　　　　　@post.content = params[:content]
　　　　　　　@post.save
　　　投稿を編集した内容をモデルへ送りデータベースへ保存する（View）
　　　　form_tagメソッドを使ってアクション（モデル）へ投稿内容を送信する
　　　　　<% form_tag(posts/#{@post.id}/update) do %> <textarea><%= @post.content%></textarea>  <input type = "submit" 属性 ="保存"> <% end %>
　　　　　 form_tagメソッドを活用し@post = Post.find_by(id: params[:id])と定義した投稿のidカラムを使って送信先を指定し、<textarea>入力欄に初期値として呼び出した投稿のcontentカラムを表示する。入力フォームのTypeなどを指定する。

投稿の削除機能
　destroy アクションには以下の機能をつける。
　　投稿詳細ページの削除リンク
　　　link_toメソッドを使ってルーティングの始まりがpostになっているものとマッチするようにする
　　　　link_to(第一引数、第二引数、第三引数）として
　　　　　第三引数→{method: "post"}を追加する事でルーティングの始まりがpostのものとマッチする
　   投稿の削除
　   　テーブル操作したい情報をデータベースから引きだす
　   　　@post=Post.find_by(id: prams[:id])
　   　destroyメソッドを使い情報を削除する
　   　 @post.destroy
　    投稿一覧画面への転送
　    　redirect_to(URL)
　    　 redirect_to(posts/index)
　　　　ルーティング
　　　　　データベースのテーブル操作を行うため
　　　　　　post ”posts/:id/destroy” ＝ post#destroy　とする
　　　投稿を制限しよう
　　　 不正な投稿があった時にエラーメッセージを表示
　　　 　バリデーション
　　　 　　不正なデータがデータベースに保存されないように、データをチェックをする仕組み
　　　　 　validates
　　　　 　　バリデーションはモデルで設定する
　　　　 　　　validates :検証するカラム ,{検証する内容}
　　　　 　　　　{presence: true}
　　　　 　　　　　「そのカラムの値が存在するかどうか」を検証する
　　　　 　　　　検証する内容はハッシュの形式になっており複数のバリデーションを指定する事ができる
　　　　 　　saveメソッド
　　　　 　　　バリデーションがかかった情報をsaveメソッドが受け付けると
　　　　 　　　　保存成功
　　　　 　　　　　trueを返す
　　　　 　　　　保存失敗
　　　　 　　　　　falseを返す
　　　 　　 空の投稿を防ぐ
　　中身のない投稿が実行されてしまうと空のデータベースが作成されてしま
　  　　　バリデーションを作成し不正なデータはデータとして保存されなくなる
　  　　　　validates :content {presence: true}
　  　　　　 postテーブルのcontentカラムに値が存在するか？しないか？検証するバリデーション
　　　　　　　文字数制限をする
　　　　　　　　文字数が多すぎる投稿が作成されないようにする
　　　　　　　　　lengthを使う事で文字数の検証をする事ができる
　　　　　　　　　　{maximum: 数値}　最大値を設定できる
　　　　　　　　　　　validates :content {maximum: 140}
　　　　　　　バリデーションの結果によって表示内容を変更する
　　　　　　　　def update if @post.save #処理したい内容 redirect_to("/posts/index") eise ＃処理したい内容redirect_to("/posts/#{@post.id}"/edit) end end
　　　直前の編集内容を保存する
　　　　投稿（データベースへの保存）が失敗（バリデーション）した際に変更した編集内容が消えてしまい編集前のデータに戻ってしまう仕様になっている
　　　　　バリデーションによって保存が失敗するとリダイレクトメソッドによってeditアクションに転送している。editアクションは投稿編集前のデータを持っているため編集内容は保存されない
　　　　　　バリデーションによって保存が失敗した際にリダイレクトしeditにもどるのではなく、updeteアクション内の変数@post.contentが表示されれば直前の編集内容を保存する事ができる
　　　　renderメソッド
　　　　　render("フォルダ名/ファイル名")とする事でリダイレクトせずに直接Viewを表示できる
　　　　　　renderメソッドのリダイレクトと違う点は同じアクション内で使った変数をそのまま使う事ができる
　　編集内容の保存に失敗した際にエラーメッセージを表示する
　　　バリデーションの保存に失敗するとRails内でエラーメッセージが生成されている
　　　　@post.errors.full_messages
　　　　　エラーメッセージが配列で入っている
　　編集の保存（投稿）に成功した場合にはサクセスメッセージを表示する
　　　フラッシュ
　　　　特定の処理を行った後に一度のみページに表示されるもの
　　　　　他のページに移動するなどすると表示が消えてしまう
　　　　　　変数flash
　　　　　　　Railsには特殊な変数flashが用意されている
　　　　　　　　変数flash[:notice]にアクションで文字列を代入する事で使う事ができる
　　　　　　　　　変数flashは多くの場所で表示する事になるためメインフォルダのapplication.html.erb(View)で表示する
　　新規投稿の保存に失敗した際にposts/newアクションへrenderする
　　　エラーメッセージの表示
　　　投稿編集の内容保存された@post.contentの表示
　　newアクションでは変数@postが定義されておらず、createアクションを経由せずにnew（View）にアクセスした際にエラーが起きてしまう
　　　　コントローラーのNewアクション内で変数の定義
　　　　　@post=Post.new
　　　　new/html.erb
　　　　 エラーメッセージの表示がされるコードが書いてあるがそもそもエラーの存在がないため配列も用意されず何も表示されない
　　　　 textareaの準備
　　　　　　@post.contenのtextareaを準備するが、同様に保存された投稿内容がないため何も表示されない
　　　新規投稿・投稿の削除に成功した場合にもサクセスメッセージを表示する
　　　　新規投稿成功時
　　　　　@post=Post.new if post.save flash[:notice]=”投稿を作成しました”　redirect_to("/posts/index")　else　　　　　　render("posts/edit")
　　　　　　@postに新しいインスタンスを作成しデータベースへ保存する。post.saveがtrueを返す場合には投稿一覧ページへ転送し同時にサクセスメッセージを表示する。そうでなければ、editアクションでrenderする
　　　　投稿削除成功時
　　　　　if post.destroy flash[:notice]="投稿を削除しました”

Ruby on Rails5 Ⅵ
　[ユーザー機能について]

エラー修正データと処理の流れメモ

ユーザー情報の編集

[要件]2にしたい
処理
　１.ユーザ詳細ページで編集テキストをクリック
　　users/show.html.erb内のaタグ（テキストが編集、リンク先がusers/edit）のテキストリンクが実行されルーティングにusers/editが渡される
　　　ルーティングでusers/edit（users/:id/edit）に対応するアクション(editアクション)がコントローラに渡される。
　　　　userコントローラーでeditアクションが実行される
　　　　　@userにURLの IDを元にfind_byメソッドへ変数pramsを活用してユーザ情報を呼び出して代入。
　　　　　　HTMLファイル(users/edit.html)がViewに渡される
　２.クリックしたのちにユーザ編集ページへ画面が移行する。移行した際に保存されているユーザ名、emailがすでに表示されている状態
　 users/edit.htmlファイルが実行される。
　 　<div class="form-heading">ユーザー情報の編集</div>が実行され文字列が出力。
　 　 <div class="form-body">が実行される
　 　 　<p>タグの”ユーザー名”が出力。
　 　 　<input value="<%= @user.name %>"
　 　 　 valueが@users.nameのinputタグが準備される
　 　 　<p>タグの”メールアドレス”が出力。
　 　 　<input value="<%= @user.email %>"
　 　 　 valueが @user.emailのinputタグが準備される。
　 　 　inputのtypeは"submit" valueが"保存"　にする
期待する動作
　編集テキストからユーザー編集ページへ移動
　ユーザー情報がすでにname,emailに入っている状態にしたい
現在の動作
　ユーザー詳細ページの編集テキストから移動した時にエラー表示がでる
エラー内容
　UsersController#editの文法ミス

SyntaxError in UsersController#edit
/home/progate/tweet_app/app/views/users/edit.html.erb:12: syntax error,
unexpected tIDENTIFIER, expecting ')' buffer.append=( "submit" value="保存" );@output_buffer.saf ^
Usersコントローラーのeditアクションの中で文法ミスが起きている
edit.html.erbの１２行目で文法ミスが起きている

NoMethodError in Users#edit
Showing /home/progate/tweet_app/app/views/users/edit.html.erb where line #8 raised:
undefined method `name' for nil:NilClass
Usersコントローラー内のeditアクションでメソッドが定義されていない
edit.html.erbの８行目
nameのメソッドが見つけられない

NameError in Users#show
Showing /home/progate/tweet_app/app/views/users/show.html.erb where line #7 raised:
undefined local variable or method `user' for #<#Class:0x0000559e9223fa88:0x0000559e90ffdcd0>
Usersコントローラー内のshowアクションで名前に間違えがある
show.html.erbの７行目
userがメソッドもしくわ変数が定義されていない

ユーザー詳細ページ（show）の編集＝users/:id/editへのテキストリンクでユーザ情報編集ページに転送
　編集ページでは初期値としてユーザー情報を表示したい
　　show1ページでは@userで定義しており、@user.nameでユーザーのnameカラムを引きだす

ユーザー機能について

　ユーザーの一覧
　ユーザーの詳細
　ユーザーの新規登録
　ユーザーの情報編集
↑
Ⅵでレッスンする機能

ユーザーのプロフィール画像登録
　ユーザーのログイン機能

データベースにユーザ情報を保存するためのusersテーブルを作成する
　　usesテーブル
　　　カラム
　　　　id name email
　　　　実際にできるテーブル
　　　　　id
　　　　　name
　　　　　email
　　　　　create_at
　　　　　upload_at
　　ターミナル
　　 rails generate model User name:string email:string
　　 rails db:migrate
　　  stringは短い文字列の際に使うカラム値の型
　バリデーション
　　空のユーザー登録・重複したユーザー登録をバリデーションする
　　　バリデーションはmodelに記載する
　　　　validates :email, {uniqueness: true}
　　　　 uniqueness: true→重複がないかチェックするバリデーション
　　　　validates:name,{presence: true}
　　　　　name欄が空白ではないか？
　　　　validates:email,{presence: true,uniqueness: true}
　　　　　email欄は空白ではないか？重複したデータはないか？

ユーザ一覧を作成する
　　View
　　　users/index.html.erb
　　　 全てのユーザーが表示されるようにする
　　　  def index @users .each do |user| [user.name](http://user.name/) end
　　コントローラー
　　　index
　　　 users/index
　　ヘッダーにユーザー一覧のリンクを作成する
　　 <li> <%= link_to("ユーザー一覧”,"/users/index") %><li>
ユーザー詳細ページを作成する
　ルーティング
　  get "users/:id" => "users#show"
　　コントローラー
　　　アクション
　　　　def show @user=User.find_by(id: params[:id])
　　　　　ルーティングからshowアクションに要求があった時にURLからIDを取得して対応するIDのユーザーをデーターベースから引きだす
　　　　　@userにfind_byメソッドを活用して（id：『prams :id』）でURLのIDにあるユーザを取得する
　　View
　　　ユーザー名とemaliを表示
　　　<h2><%= @user.name %></h2>　<p><%= @user.email %></p>
　　　　showアクションで定義した変数@userのnameとemailを表示する

Ruby on Rails リーディング

https://qiita.com/Yaruki00/items/03eb2b6dd96dc44f18b6#5-1-appassets

routes.rbファイル 

- 役割
    - クライアントからの要求（path）に応じてコントローラーへ対応するアクションを渡す
        - 要求される内容に応じてHTTPメソッドを決定
        - パス→コントロラー名＃アクション

=> controllerディレクトリ 

- usersコントローラーファイルリーディング　1月21日
- postsコントローラーファイルリーディング    1月21日
- likesコントローラーファイルリーディング　1月21日
- homeコントローラーファイルリーディング　1月21日
- applicationコントローラーファイルリーディング　1月21日

=> modelディレクトリ 

- application
- like
- user
- post　リーディング　1月21日

=> viewディレクトリ 

- home
    - about
    - top
- layouts
- posts
- users

の順で読んでいく

- バージョン管理
    - チーム開発などにおいてコードの変更内容などをバージョンとして更新する事でチーム全員に変更内容などを共有できる
        - セーブポイントのようなもの
            - Git hubが主流
    - バージョン管理をする流れ
        - .gitconfigファイルの設定
            - —global <attribute> <value>
        - 環境変数の設定
            - —global [user.name](http://user.name) “ユーザー名”
            - —global [user.email](http://user.email) “メールアドレス名”
        - ローカル環境にリポジトリを落とす
            - すでにあるコードのリポジトリを利用する
                - Git hub で forkする
            - コードをHTTPS or SSH　でコードのurlをコピー
        - git clone <url>
        - ローカルのリポジトリに変更を加えてバージョン更新をしたいタイミングでリモートリポジトリに変更内容を更新する
    - Git hubの設定が完了したら
        - バージョン更新
            - リポジトリの変更を行う
            - ローカルで変更内容の保存を行う
            - 全ての変更をステージに上げる
            - 変更内容をリモートリポジトリにコミット
            - 変更内容を同期する

- コントローラー
    - モデルとテーブルの関係性
        - モデルは単数系
        - テーブルは複数形

- **has_secure_password**
    - モデル内で定義する
        - パスワードがハッシュ化されて保存されるようにする

- コミットメッセージについて
    - フォーマット: `<Type>: <Emoji> #<Issue Number> <Title>`
        - 



Railsドキュメント

https://railsdoc.com/rails_base

- 目次(全25題 1題4/100)
    - Railsの基礎知識 2/27 (4/100 :4)
        - 概要
            - Ruby on Railsとは
                - Rubyのフレームワーク
            - 設計哲学
                - 設定より規約（CoC）
                    - 基本的には言語の設定されている規約を使う
                        - 必要がある場合に設定を追加する事も可能
                            - 例：groupというテーブルを作った場合
                                - groupsという名前になる
                - 同じ作業を繰り返さない（DRY）
            - 特徴
                - MVCモデルを採用
                    - M＝model
                    - V=View
                    - C=controller
                - ジェネレーター
                    - Railsのテンプレートを作成するためのツール
                        - コマンドラインから使用する
                - アジャイルな開発
                    - 素早く、機能毎の開発が可能
                - ルーティング
                - テンプレート
                - データベースの管理方法
        - 規約
            - ファイル名の規約
            
            ![image.png](attachment:3311f538-91b5-4c5a-aa08-45d3fc2d9cec:image.png)
            
            - テーブル定義についての規約
                - テーブル名とクラス名
                    - テーブル名は複数形
                    - 単語の区切りはアンダーバー（_）
                    - 対応するクラス名は単語の先頭を大文字、_を取り除いたもの
                - キーのカラム名（RDB 主キーと外部キーの関係性で表現する）
                    - 主キーのカラム名　「id」
                    - 外部キーのカラム名は[テーブル名の単数_id]
                - 日付関連のカラム名
                    - DATE型のカラムには名前を「受動態_on」
                    - TIMESTAMP型のカラムには名前を受動態_at
                    - 更新日時、作成日時は「updated_at」「created_at」
                - 結合テーブル
                    - 関連させたいテーブル名をくっつけた名前
                    - カラム「id」を作らず、関連させる2つのキーのセットを主キーとする
        - Railsの実行環境
            - development
                - 開発中に使用される環境
                    - 実行環境の指定がなければこの環境で起動
                    - ログレベルはdebug
                    - 書き換えた内容がすぐに反映
                    - キャッシュが無効
            - test
                - 自動テストで使用される環境
                    - ログレベルはdebug
                    - キャッシュが有効
            - production
                - 本番稼働で使用する環境
                    - ログレベルがinfo
                    - キャッシュが有効
                    - 書き換えた内容の反映には再起動が必要
        - フォルダ構造
            
            
            | ファイル名 | 説明 |
            | --- | --- |
            | babel.config.js | BabelというJavaScript用の設定ファイル |
            | config.ru | Rack用のファイル |
            | Gemfile | Gemというパッケージマネージャで依存関係を指定できるファイル |
            | Gemfile.lock | Gemfileから実際にインストールされたGemの一覧とバージョン |
            | package.json | npmというJavaScriptのパッケージ管理するツール用の設定ファイル |
            | postcss.config.js | PostCssというCSS関連のプログラム用の設定ファイル |
            | Rakefile | RakeというRubyのビルドツール用のファイル |
            | yam.lock | yamlというパッケージ管理ツール用のファイル |
            | README.md | 作ったアプリケーションの説明を記述するREADMEファイル |
            | .git | Git用のディレクトリ |
            | app/ | アプリケーション用のディレクトリ |
            | app/assets/ | アプリケーション用のリソースを置くディレクトリ |
            | app/assets/config/ | 環境に関するものを管理するファイル用のディレクトリ |
            | app/assets/images/ | 画像用のディレクトリ |
            | app/assets/stylesheets/ | 公開するスタイルシート用のディレクトリ |
            | app/channels/ | Action Cableファイル用のディレクトリ |
            | app/controllers/ | コントローラ用のディレクトリ |
            | app/controllers/application_controller.rb | アプリケーションで共通のコントローラ |
            | app/helpers/ | ヘルパー用のディレクトリ |
            | app/helpers/application_controller.rb | アプリケーションで共通のヘルパー |
            | app/javascript | JavaScript関連のスクリプト用のディレクトリ |
            | app/jobs | Active Job用のディレクトリ |
            | app/mailers/ | Action Mailerファイル用のディレクトリ |
            | app/mailers/application_mailer.rb | Action Mailerのコントローラ |
            | app/models/ | モデル用のディレクトリ |
            | app/views/ | ビュー用のディレクトリ |
            | app/views/layouts/ | ビューのレイアウト用のRHTMLテンプレート用のディレクトリ |
            | app/views/layouts/application.html.erb | アプリケーションで共通のレイアウト |
            | app/views/layouts/mailer.html.erb | Action MailerのHTMLレイアウト |
            | app/views/layouts/mailer.text.erb | Action Mailerのテキストレイアウト |
            | bin/ | アプリケションを管理する様々なスクリプト用のディレクトリ |
            | config/ | アプリケーションの設定ファイル用のディレクトリ |
            | config/environments/ | 環境単位の設定ファイル用のディレクトリ |
            | config/initializers/ | 初期化ファイル用のディレクトリ |
            | config/locales/ | 辞書ファイル用のディレクトリ |
            | db/ | データベース関連のファイル用のディレクトリ |
            | db/seeds.rb | 初期データを生成するファイル |
            | lib/ | 複数のアプリケーション間で共有するライブラリ用のディレクトリ |
            | lib/assets/ | 自分で生成したライブラリ用のディレクトリ |
            | lib/tasks/ | 自分で生成したRakefile用のディレクトリ |
            | log/ | ログファイル用のディレクトリ |
            | node_modules | npmというJavaScriptのパッケージ管理ツールがインストールするディレクトリ |
            | public/ | Web上に公開するファイル用のディレクトリ |
            | storage/ | ファイルのアップロードで保存されるディレクトリ |
            | tmp/ | キャッシュなど、一時的なファイル用のディレクトリ |
            | test/ | アプリケーションのテストに使うファイル用のディレクトリ |
            | temp | 一時ファイル用のディレクトリ |
            | vendor/ | 外部ライブラリ用のディレクトリ |
            | .browserslistrc | bowerというパッケージツール用の設定ファイル |
            | .gitignore | Gitに登録しないファイルを指定 |
            | .ruby-version | Rubyのデフォルトバージョン |
        - アプリケーション作成の流れ
            - 作業ディレクトリの作成
                - mkdir rails
                - cd rails
            - アプリケーション作成
                - rails new demo
            - ディレクトリ移動
                - cd demo
            - ジェネレーター
                - rails generate contoroller Welcome index
            - ルーティング
                - vim config/routes.rb Rails.application.routes.draw do get 'welcome/index' root 'welcome#index' end
            - サーバー起動
                - rails server
    - Rubyの基礎知識 2/27~2/28 (4/100 :8)
        - Rubyとは
            - オブジェクト指向スクリプト言語
                - オブジェクトとオブジェクトの関係性で誰でも手軽に記載できる言語
            - 特徴
                - シンプルな文法
                    - スクリプト言語
                - 普通のオブジェクト指向機能(クラス、メソッドコールなど)
                    - クラスからインスタンスを生成する
                - 特殊なオブジェクト指向機能(Mixin、特異メソッドなど)
                - 演算子オーバーロード
                - 例外処理機能
                - イテレータとクロージャ
                - ガーベージコレクタ
                - ダイナミックローディング(アーキテクチャによる)
                - 多くのUNIX上で動くだけでなく、DOSやWindows、Mac、BeOSなどの上でも動く
        - 変数
            - JavaScriptと異なり、varは不要
            - セミコロン(;)も不要
            - 予約語は、自動的にダブルクォートで囲まれる
                
                ```ruby
                name = "Railsドキュメント"
                ```
                
        - 数値と文字列
            - 数値も文字列もオブジェクトとして扱われる
            - 型は自動的に判定される
                - 定義する必要がない
            - **数値**
                - 足し算やかけ算の結果、Fixnumの値を超えた場合は、自動的にBignumに変換
                - 整数値と小数値を計算した場合は、自動的にFloatに変換
                - 数値を表すオブジェクトのクラスは3つ
                
                | クラス | 説明 |
                | --- | --- |
                | Fixnum | 変数に整数を代入 |
                | Bignum | 非常に大きな整数を代入 |
                | Float | 小数点付きの数字を代入 |
            - 文字列
                - 文字列をシングルクォート(‘)やダブルクォート(“)で囲むと、オブジェクトができる
                - 「+」で連結
                - ダブルクォート内の、「＃｛｝」は、式として評価された値が展開
                - ダブルクォート内の特殊文字
                
                | エスケープシーケンス | 説明 |
                | --- | --- |
                | \a | ベル |
                | \b | バックスペース |
                | \e | エスケープ |
                | \f | 改行ページ |
                | \n | 改行 |
                | \r | 復帰 |
                | \t | 水平タブ |
                | \v | 垂直タブ |
                | \” | ダブルクォート(“) |
                | \’ | シングルクォート(‘) |
                | \ | ￥マーク |
            - 数値と文字列の変換
                - 数字から文字列
                    - .to_s
                - 文字列から数字
                    - .to_i
        - 配列について
            - 連番がつけられた変数の集合体
                - sampleメソッド
                    - ランダムにn個の要素を取り出す
                        - 配列.sample(個数)
                    
                    ```ruby
                    [1, 2, 3, 4, 5, 6, 7].sample(2)
                    # [3, 1]
                    ```
                    
                - keep_ifメソッド
                    - 条件を満たさない要素を配列から削除する
                        - 配列.keep_if {|arr| 条件式 }
                    
                    ```ruby
                    ["ipad", "iPhone", "ipod", "iTunes", "Android"].keep_if {|i| i =~ /^i/ }
                    # ["ipad", "iPhone", "ipod", "iTunes"]
                    ```
                    
                - repeated_combinationメソッド
                    - 配列から、任意の○個の重複の組み合わせを列挙
                        - 配列.repeated_combination(個数) {|arr| block }
                - repeated_permutationメソッド
                    - 配列から、任意の○個からなる重複順列を列挙
                        - 配列.repeated_permutation(個数) {|arr| block }
                - rotateメソッド
                    - 配列から、要素を回転させるようにして要素をずらした配列
                        - 配列.rotate(個数)
        - ハッシュについて
            - キーを使って複数のオブジェクトへの参照を行うオブジェクト
        - 条件分岐 ~2/27
            - 条件に応じて実行する処理を分ける
                - 比較演算子
                
                | 演算子 | 説明 |
                | --- | --- |
                | == | 等しい |
                | === | 等しい |
                | != | 等しくない |
                | > | より大きい |
                | >= | 等しいか、より大きい |
                | < | より小さい |
                | <= | 等しいか、より小さい |
                | <=> | 小さいときはｰ1、等しいときは0、大きいときは１ |
                | =~ | 世紀表現のパターンマッチ(一致) |
                | !~ | 世紀表現のパターンマッチ(一致しない) |
                - 論理演算子
                
                | 演算子 | 説明 |
                | --- | --- |
                | && | かつ |
                | and | かつ |
                | | | | または |
                | or | または |
                | ! | ではない |
                | not | ではない |
            - if文
                
                ```ruby
                if 条件式1 (then)
                elsif 条件式2 (then)
                else
                end
                ```
                
            - unless
                - 条件式が真ではなく偽の場合に式を実行する
                
                ```ruby
                unless 条件式1 (then)
                else
                end
                ```
                
            - 三項演算子
                - 条件1 ? 正しいとき : 正しくないとき
            - case
                - 対象となる値と複数の候補の中から一致するものを探し、処理を実行する
                    - if文は条件式を複数用意するのに比べて値に対して候補を用意する形
                
                ```ruby
                case
                when 条件式1 (then)
                when 条件式2 (then)
                else 条件に一致するものがない場合に実行する
                end
                
                case 変数
                when 式1 (then)
                when 式2 (then)
                else
                end
                ```
                
            - while
                - 条件式が真を返す場合にはdoからendまで繰り返して実行する
                
                ```ruby
                whike 条件式 do
                end
                
                while 条件式 do
                  実行する処理1
                  実行する処理2
                end
                
                num = 0
                while num < 2 do
                  puts("num = " + num.to_s)
                end
                puts("End")
                ```
                
        - ブロックとイテレータ　2/28~
            - イテレーター
                - 繰り返し処理に使うメソッド
                    
                    ```ruby
                    数字.time do |i|
                    end
                    ```
                    
            - each
                - 配列やハッシュの要素数だけ繰り返す
                    
                    ```ruby
                    配列の場合
                    
                    配列.each do |i|
                    end
                    
                    ハッシュの場合
                    
                    ハッシュ.each do |key, value|
                    end
                    ```
                    
        - オブジェクトについて
            - オブジェクトとは
                - クラスという設計図を元に作成されたインスタンス
                    - 本質
                        - データと処理
                            - Ruby：
                                - インスタンスメソッド
                                - インスタンス変数
                                    - インスタンス→実体
                - オブジェクトの生成
                    
                    ```ruby
                    クラス.new
                    ```
                    
            
            ### メソッドの呼び出し制限
            
            | レベル | 説明 |
            | --- | --- |
            | public | メソッドはどこからでも呼び出せる |
            | protected | 同じクラスやサブクラス内のメソッドの中だけ呼び出せる |
            | private | 同じクラスやサブクラス内のメソッドの中だけ呼び出せる |
        - シンボルについて
            - プログラムのどこからでも同一のオブジェクトを名前で表せるようにしたもの
                
                ```ruby
                :シンボル名←オブジェクトの名前
                ```
                
            
            ### シンボルと文字列の使い分け
            
            Railsでのシンボルと文字列の個人的な使い分け
            
            - コントローラやアクションの指定は文字列
            - 上記以外で識別子的に使う場合はシンボル
            - それ以外は文字列
        - 正規表現
            - 文字列のパターンを記述するためのもの
                - 文字列が指定したパターンを含んでいるか？
                    - 含んでいる場合にはどこの場所なのかがわかる
                        
                        ```ruby
                        /pat/
                        %r{pat}
                        ```
                        
            
            ### オプション
            
            | オプション | 説明 |
            | --- | --- |
            | i | 大文字小文字の区別しない |
            | o | 一度だけ式展開 |
            | x | ＃をコメントと見なす |
            | m | 複数行モード |
        - Rubyの便利なメソッド
            - **配列**
                - 配列をランダムに取り出す
                    - randというメソッドは擬似乱数をランダムに生成するもの
                
                ```ruby
                [:aaa, :bbb, :ccc].rand
                ```
                
                - 配列を分割
                    - 文字列や配列などを分割する事ができる
                        - デフォルト：
                            - 空白文字(” “(半角スペース)、”\n”(改行コード)、”\t”(タブ)など)で分割
                        - 引数：
                            - 分割数
                            - 区切り文字の指定
                            - 正規表現にマッチする部分で分割
                            - 1文字ずつ分割
                                - “”(ブランク)を使用
                                
                                ```ruby
                                [1, 2, 3, 4, 5].split(3)
                                ```
                                
                - 配列をグループ化
                
                ```ruby
                %w(1 2 3 4 5).in_groups_of(4){ |g| p g }
                ```
                
                - 特定のキーからハッシュを作る
                
                ```ruby
                User.find(:all).index_by(&:login)
                ```
                
            - **ハッシュ**
                - ハッシュの差を取得
                
                ```ruby
                {one: 1, two: 2, three: 3 }.diff(one: 0, two: 2, four: 4)
                ```
                
                - ハッシュから特定の値を取り除く
                
                ```ruby
                hash.except(:controller, :action)
                ```
                
                - ハッシュから特定の値だけど取り出す
                
                ```ruby
                hash.slice(:title, :body)
                ```
                
                - 元のハッシュの内容を優先してマージ
                
                ```ruby
                hash.reverse_merge(template: "entries/list")
                ```
                
    - railsコマンド(4:100 :12)
        - コマンド一覧(87個　23⇒1)
            - rails new
                - 新しいRailsのアプリケーションを作成
                    - アプリケーションに最低限必要なフォルダやファイルが自動的に生成
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | -r, -ruby=PATH | rubyバイナリのパス |  |
                | -m, -template=TAMPLATE | テンプレートのパス |  |
                | -d, –database=DATABASE | データベースの種類 | sqlite3 |
                | -G, –skip-git | .gitignoreファイルの生成をスキップ |  |
                | –skip-keeps | .keepファイルの生成をスキップ |  |
                | -M, –skip-action-mailer | Action Mailerファイルの生成をスキップ |  |
                | –skip-action-mailbox | Action MailboxのGemをスキップ |  |
                | –skip-action-text | Action TextのGemをスキップ |  |
                | -O, –skip-active-recode | Active Recordファイルの生成をスキップ |  |
                | –skip-active-job | Active Jobをスキップ |  |
                | –skip-active-storage | Active Storageファイルの生成をスキップ |  |
                | -C, –skip-action-cable | Action Cableファイルの生成をスキップ |  |
                | -S, –skip-sprockets | Sprocketsファイルの生成をスキップ |  |
                | -J, –skip-javascript | JavaScriptファイルの生成をスキップ |  |
                | –skip-hotwire | Hotwireの統合をスキップ |  |
                | –skip-jbuilder | jbuilderのGemをスキップ |  |
                | -T, –skip-test | testファイルの生成をスキップ |  |
                | –skip-system-test | システムテストファイルの生成をスキップ |  |
                | –skip-bootsnap | bootsnapのGemをスキップ |  |
                | –dev | githubリポジトリ上の自分のコードから作成 |  |
                | –edge | githubリポジトリ上の最新のコードから生成 |  |
                | –master, –main | RailsのメインブランチのGemfileでアプリケーションをセットアップ |  |
                | –rc=RC | railsコマンドの追加の構成オプションを含むファイルへのパス |  |
                | –no-rc | .railsrcファイルからの追加のロードをスキップ |  |
                | –api | APIのみのアプリケーションを生成 |  |
                | –minimal | 最小限のRailsアプリケーションを生成 |  |
                | -j, –javascript=JAVASCRIPT | 組み込むJavaScriptライブラリーを指定 | importmap |
                | –css=CSS | CSSプロセッサを選択 |  |
                | ｰB, –skip-bundle | bundle installしない |  |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
                - 例：
                    - My SQLを使うアプリの作成
                        - $ rails new weblog -d mysql
                    - APIのみのアプリケーション（APIモード　Viewを捨てる）
                        - $ rails new weblog --api
                    - 古いバージョンのRailsでアプリケーション
                        - $ rails *6.1.4* new weblog
            - rails generate scaffold
                - アプリケーションの基本的な機能を自動生成するコマンド
                    - コントローラー、モデル、ビューを作成
                        - 一覧(index)
                        - 詳細(show)
                        - 新規作成(new/create)
                        - 編集(edit/update)
                        - 削除(destroy)
                - $ rails generate scaffold 名前 [カラム名:型[:index]..] [オプション]
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –force-plural | 指定されたモデル名を強制的に使用 |  |
                | -o, –orm=NAME | 呼び出されるORMを指定 | active_record |
                | –model-name=MODEL_NAME | 使用するモデル名 |  |
                | –resource-route | リソースルートを生成するか | true |
                | –api | APIを生成するタイミング |  |
                | -c, –scaffold-controller=NAME | 呼び出されるScaffoldコントローラ | scaffold_controller |
                | –migration | migrationファイルを生成するか | true |
                | –timestamps | timestampsファイルを生成するか | true |
                | –parent=PARENT | 生成されたモデルの親クラスを指定 |  |
                | –indexes | belongs_toカラムにインデックスを付与するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | -db, –database=DATABASE | データベースの種類 | sqlite3 |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | –fixture | フィクスチャファイルを生成するか | true |
                | -r, –fixture-replacement=NAME | 呼び出されるフィクスチャを指定 |  |
                | –system-tests=SYSTEM_TESTS | システムテストを指定 | test_unit |
                | –helper | helperファイルを生成するか | true |
                | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                | –jbuilder | jbuilderファイルを生成するか | true |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
                
                ### カラムの型
                
                | データ方 | 説明 |
                | --- | --- |
                | string | 文字列 |
                | text | 長い文字列 |
                | integer | 整数 |
                | float | 浮動小数 |
                | decimal | 精度の高い小数 |
                | datetime | 日時 |
                | timestamp | より細かい日時 |
                | time | 時間 |
                | date | 日付 |
                | binary | バイナリデータ |
                | boolean | Boolean型 |
                
                ### 生成されるファイル
                
                | ファイル | 説明 |
                | --- | --- |
                | db/migrate/YYYYMMDDHHMMSS_create_xxxes.rb | マイグレーションファイル |
                | app/models/xxx.rb | モデルファイル |
                | app/controllers/xxxes_controller.rb | コントローラファイル |
                | app/views/XXXs/index.html.erb | すべてのリストを表示 |
                | app/views/XXXs/edit.html.erb | 編集ファイル |
                | app/views/XXXs/show.html.erb | 詳細ページ |
                | app/views/XXXs/new.html.erb | 新規ページ |
                | app/views/XXXs/_form.html.erb | フォーム用ページ |
                | app/views/xxxes/_xxx.html.erb |  |
                | app/helpers/xxxes_helper.rb | ヘルパー |
                | test/models/xxx_test.rb | モデルテスト |
                | test/fixtures/xxxes.yml | フィクスチャテスト |
                | test/controllers/xxxes_controller_test.rb | コントローラテスト |
                | test/system/xxxes_test.rb | システムテスト |
                | app/views/xxxes/index.json.jbuilder | Jbuilderファイル |
                | app/views/xxxes/show.json.jbuilder | Jbuilderファイル |
                | app/views/xxxes/_xxx.json.jbuilder | Jbuilderファイル |
            - rails generate scaffold_controller
                - モデル以外のアプリケーションのひな型を生成
                    - アプリの基本的な機能に必要なコントローラーとビューを作成
                        - 一覧(index)
                        - 詳細(show)
                        - 新規作成(new/create)
                        - 編集(edit/update)
                        - 削除(destroy)
                    - $ rails generate scaffold_controller 名前 [カラム名:型..] [オプション]
                    
                    ### オプション
                    
                    | オプション | 説明 | デフォルト値 |
                    | --- | --- | --- |
                    | –skip-namespace | namespaceの生成をスキップ |  |
                    | –skip-collision-check | コリジョンチェックをスキップ |  |
                    | –force-plural | 指定されたモデル名を強制的に使用 |  |
                    | –model-name=MODEL_NAME | 使用するモデル名 |  |
                    | –helper | helperファイルを生成するか | true |
                    | -o, –orm=NAME | 呼び出されるORMを指定 | active_record |
                    | –api | APIを生成するタイミング |  |
                    | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                    | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                    | –resource-route | リソースルートを生成するか | true |
                    | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                    | –jbuilder | jbuilderファイルを生成するか | true |
                    | –system-tests=SYSTEM_TESTS | システムテストを指定 | test_unit |
                    | –timestamps | timestampsファイルを生成するか | true |
                    | -f, –force | ファイルが存在する場合に上書き |  |
                    | -p, –pretend | ドライラン |  |
                    | -q, –quiet | 進捗情報を非表示 |  |
                    | -s, –skip | 既に存在するファイルはスキップ |  |
                    | -h, –help | ヘルプ |  |
                    | -v, –version | バージョンを表示 |  |
            - rails generate controller
                - コントローラーとビューの作成
                    - $ rails generate controller 名前 [アクション名..] [オプション]
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                | –helper | helperファイルを生成するか | true |
                | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate migration
                - マイグレーションファイルの生成
                    - 必ずupメソッドとdownメソッドを含めなければならない
                    - self.upがmigrationのバージョンを上げるときに実行
                    - self.downがmigrationのバージョンを下げるときに実行
                        - `down`メソッド内で行なう変換
                            - `up`メソッド内で行なう順序の正確な逆順にする
                    - クラス名をすべて小文字にしたものが、ファイル名アンダースコア(_)以降と一致する必要がある
                - $ rails generate migration 名前 [カラム名:型[:index]..] [オプション]
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –timestamps | timestampsファイルを生成するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | -d, –database=DATABASE | データベースの種類 | sqlite3 |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -q, –quiet | 進捗状況を表示しない |  |
                | -p, –pretend | ドライラン |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプを表示 |  |
                
                ### カラムの型
                
                | データ方 | 説明 |
                | --- | --- |
                | string | 文字列 |
                | text | 長い文字列 |
                | integer | 整数 |
                | float | 浮動小数 |
                | decimal | 精度の高い小数 |
                | datetime | 日時 |
                | timestamp | より細かい日時 |
                | time | 時間 |
                | date | 日付 |
                | binary | バイナリデータ |
                | boolean | Boolean型 |
                
                ### 作成されるファイルの基本構成
                
                ```ruby
                class マイグレーション名s < ActiveRecord::Migration
                  def up
                  end
                
                  def down
                  end
                end
                ```
                
                - カラムを指定して生成
                
                ```ruby
                $ rails generate migration AddTitleToPage title:string
                ```
                
            - rails generate model
                - モデルの作成
                    - $ rails generate model 名前 [カラム名:型[:index]..] [オプション]
                
                ### オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –force-plural | 指定されたモデル名を強制的に使用 |  |
                | -o, –orm=NAME | 呼び出されるORMを指定 | active_record |
                | –migration | migrationファイルを生成するか | true |
                | –timestamps | timestampsファイルを生成するか | true |
                | –parent=PARENT | 生成されたモデルの親クラスを指定 |  |
                | –indexes | belongs_toカラムにインデックスを付与するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | –fixture | フィクスチャファイルを生成するか | true |
                | -r, –fixture-replacement=NAME | 呼び出されるフィクスチャを指定 |  |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
                
                ### カラムの型
                
                | 型 | 説明 |
                | --- | --- |
                | string | 文字列 |
                | text | 長い文字列 |
                | integer | 整数 |
                | float | 浮動小数 |
                | decimal | 精度の高い小数 |
                | datetime | 日時 |
                | timestamp | より細かい日時 |
                | time | 時間 |
                | date | 日付 |
                | binary | バイナリデータ |
                | boolean | Boolean型 |
                | primary_key | プライマリキー |
                
                ### indexの種類
                
                | 名前 | 説明 |
                | --- | --- |
                | uniq | ユニーク |
                | index | インデックス |
                - 補足
                    - integer, string, text, binaryでは制限値を{ }で記述
                - 例：
                    - 階層を指定
                    
                    `$ rails generate model admin/account`
                    
            - rails generate application_record
                - application_recordファイルを生成
                    - $ rails generate application_record [オプション]
                - オプション
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | -r, -ruby=PATH | rubyバイナリのパス |  |
                | -m, -template=TAMPLATE | テンプレートのパス |  |
                | -d, –database=DATABASE | データベースの種類 | sqlite3 |
                | -G, –skip-git | .gitignoreファイルの生成をスキップ |  |
                | –skip-keeps | .keepファイルの生成をスキップ |  |
                | -M, –skip-action-mailer | Action Mailerファイルの生成をスキップ |  |
                | –skip-action-mailbox | Action MailboxのGemをスキップ |  |
                | –skip-action-text | Action TextのGemをスキップ |  |
                | -O, –skip-active-recode | Active Recordファイルの生成をスキップ |  |
                | –skip-active-job | Active Jobをスキップ |  |
                | –skip-active-storage | Active Storageファイルの生成をスキップ |  |
                | -C, –skip-action-cable | Action Cableファイルの生成をスキップ |  |
                | -S, –skip-sprockets | Sprocketsファイルの生成をスキップ |  |
                | -J, –skip-javascript | JavaScriptファイルの生成をスキップ |  |
                | –skip-hotwire | Hotwireの統合をスキップ |  |
                | –skip-jbuilder | jbuilderのGemをスキップ |  |
                | -T, –skip-test | testファイルの生成をスキップ |  |
                | –skip-system-test | システムテストファイルの生成をスキップ |  |
                | –skip-bootsnap | bootsnapのGemをスキップ |  |
                | –dev | githubリポジトリ上の自分のコードから作成 |  |
                | –edge | githubリポジトリ上の最新のコードから生成 |  |
                | –master, –main | RailsのメインブランチのGemfileでアプリケーションをセットアップ |  |
                | –rc=RC | railsコマンドの追加の構成オプションを含むファイルへのパス |  |
                | –no-rc | .railsrcファイルからの追加のロードをスキップ |  |
                | –api | APIのみのアプリケーションを生成 |  |
                | –minimal | 最小限のRailsアプリケーションを生成 |  |
                | -j, –javascript=JAVASCRIPT | 組み込むJavaScriptライブラリーを指定 | importmap |
                | –css=CSS | CSSプロセッサを選択 |  |
                | ｰB, –skip-bundle | bundle installしない |  |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate helper
                - 新しいヘルパーの作成
                    - RailsのView内で使う
                        - テンプレートのコードを簡潔にする仕組み
                            - ロジック
                                - ヘルパーでまとめて記載してDRYなコードを記載する
                    - $ rails generate helper 名前 [オプション]
                        - $ rails generate helper CreditCard
            - rails generate resource
                - 新しいリソースを生成
                    - RESTfulなリソース指向アプリケーションに適した空のモデルとコントローラを含む新しいリソースを生成
                        - $ rails generate resource 名前 [カラム名[:型][:index]..] [オプション]
                - Railsにおけるリソースとは？
                    
                    https://krs1.hatenablog.com/entry/2016/06/07/180005
                    
                    - リソースとはRESTfulなインターフェイスでCRUDの対象となるデータの事
                        - ルーティングに縛られる事なくヘルパーなどを使う事で表現できる
                    - 単一のリソースを使用する事などができる
                        - 要はDBが対象になる？
                    - resoucesとは
                    - Railsで定義されている7つのアクションのルーティングを自動で作成するメソッド
                        - resoucesを使うことで簡単にルーティングを作成できる。
                            - ルーティングを記載するのを短縮する事ができる
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –force-plural | 与えられたモデル名を強制的に使用 |  |
                | –model-name=MODEL_NAME | 使用するモデル名 |  |
                | -c, –resource-controller=NAME | 使用するリソースコントローラ | controller |
                | -a, –actions=ACTION ACTION | リソースコントローラーのアクション |  |
                | –resource-route | リソースルートを生成するか | true |
                | –migration | migrationファイルを生成するか | true |
                | –timestamps | timestampsファイルを生成するか | true |
                | –parent=PARENT | 生成されたモデルの親クラスを指定 |  |
                | –indexes | belongs_toカラムにインデックスを付与するか | true |
                | –primary-key-type=PRIMARY_KEY_TYPE | 主キーのタイプ |  |
                | –db, –database=DATABASE | 使用するデータベースを指定 |  |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | –fixture | フィクスチャファイルを生成するか | true |
                | -r, –fixture-replacement=NAME | 呼び出されるフィクスチャを指定 |  |
                | –skip-routes | config/routes.rbへのルート追加をスキップ |  |
                | –helper | helperファイルを生成するか | true |
                | -e, –template-engine=NAME | 呼び出されるテンプレートエンジンを指定 | erb |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate channel
                - サーバとクライアントに新しいケーブルチャンネルを生成
                    - $ rails generate channel 名前 [メソッド..] [オプション]
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespaceの生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –assets | アセットを生成するか | true |
                | -t, –test-framework=NAME | 呼び出されるテストフレームワークを指定 | test_unit |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate integration_test
                - 新しい統合テストを生成
                    - $ rails generate integration_test 名前 [オプション]
                
                | オプション | 説明 | デフォルト値 |
                | --- | --- | --- |
                | –skip-namespace | namespace の生成をスキップ |  |
                | –skip-collision-check | コリジョンチェックをスキップ |  |
                | –integration-tool=NAME | 呼び出される統合ツール | test_unit |
                | -f, –force | ファイルが存在する場合に上書き |  |
                | -p, –pretend | ドライラン |  |
                | -q, –quiet | 進捗情報を非表示 |  |
                | -s, –skip | 既に存在するファイルはスキップ |  |
                | -h, –help | ヘルプ |  |
                | -v, –version | バージョンを表示 |  |
            - rails generate system_test
            - rails generate jbuilder
            - rails generate job
            - rails generate mailbox
            - rails generate mailer
            - rails generate benchmark
            - rails generate task
            - rails destroy
            - rails db:create
            - rails db:drop
            - rails db:migrate
            - rails db:encryption:init
            - rails db:environ
            - ment:set
            - rails db:fixtures:load
            - rails dbconsole
            - rails db:version
            - rails db:schema:load (2/4)
            - rails db:schema:dump
            - rails db:schema:cache:clear
            - rails db:schema:cache:dump
            - rails db:seed
            - rails db:seed:replant
            - rails db:prepare
            - rails db:reset
            - rails db:rollback
            - rails db:setup
            - rails db:structure:dump
            - rails db:structure:load
            - rails db:system:change
            - rails assets:clean
            - rails assets:clobber
            - rails assets:environment
            - rails assets:precompile
            - rails plugin new
            - rails server
            - rails console
            - rails runner
            - rails about
            - rails version
            - rails notes
            - rails routes
            - rails action_mailbox:ingress:exim
            - rails action_mailbox:ingress:postfix
            - rails action_mailbox:ingress:qmail
            - rails action_mailbox:install
            - rails action_mailbox:install:migrations
            - rails action_text:install
            - rails action_text:install:migrations
            - rails active_storage:install
            - rails app:template
            - rails app:update
            - rails cache_digests:dependencies
            - rails cache_digests:nested_dependencies
            - rails dev:cacherails importmap:install
            - rails initializer
            - rails log:clear
            - rails middleware
            - rails restart
            - rails secret
            - rails stats
            - rails stimulus:install
            - rails stimulus:install:importmap
            - rails stimulus:install:node
            - rails test
            - rails test:db
            - rails test:all
            - rails time:zones
            - rails tmp:clear
            - rails tmp:create
            - rails turbo:install
            - rails turbo:install:importmap
            - rails turbo:install:node
            - rails turbo:install:redis
            - rails yarn:install
            - rails zeitwerk:check
        - 逆引き
            
            [新しいRailsのアプリケーションを作成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            
            [アプリケーションのひな型を生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            
            [モデル以外のアプリケーションのひな型を生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            
            [コントローラとビューの生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            
            [マイグレーションファイルの生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            [モデルの生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            [application_recordファイルを生成](https://www.notion.so/Rails-1a7972e6c96080c28637d9da59072bca?pvs=21)
            新しいヘルパーを生成
            新しいリソースを生成
            新しいケーブルチャンネルを生成
            新しい統合テストを生成
            新しいシステムテストを生成
            jbuilderファイルを生成
            アクティブなジョブファイルを作成
            新しいメールボックスクラスを生成
            新しいメーラーとそのビューを生成
            ベンチマークを生成
            新しいRakeタスクを生成
            自動生成したファイルの削除
            データベースを作成
            データベースを削除
            マイグレーションの実行
            暗号化を構成するための鍵セットを生成
            データベースの環境値を設定
            フィクスチャを現在の環境のデータベースにロード
            コンソールを起動
            マイグレーションのバージョンを確認
            スキーマファイルでデータベースを作成
            現在のデータベースからスキーマファイルを生成
            schema_cache.ymlファイルをクリア
            schema_cache.ymlファイルを作成
            データベースに初期データを投入
            現在の環境の各データベースのテーブルを切り捨てseedをロード
            データベースのリペア
            データベースのリセット
            データベースのロールバック
            データベースのセットアップ
            データベース構造をダンプ
            structure.sqlファイルからデータベースを再構築
            使用するデータベースを変更
            古いコンパイル済みのアセットを削除
            コンパイル済みのアセットを削除
            アセットのコンパイル環境の読み込み
            指定されたすべてのアセットをコンパイル
            プラグインをインストール
            ローカルでサーバを起動
            コンソールを起動
            Rails環境で動かすバッチ処理
            Railsアプリケーションの色々な情報を出力
            Railsのバージョン
            コードからコメントの部分を抽出
            定義されている全ルーティングを出力
            Eximからの受信メールをアクションメールボックスにリレー
            Postfixからの受信メールをアクションメールボックスにリレー
            Qmailからの受信メールをアクションメールボックスにリレー
            アクションメールボックスとその依存関係をインストール
            アクションメールボックスからアプリケーションへのマイグレーションのコピー
            マイグレーション、スタイルシート、JavaScriptの各ファイルをコピー
            マイグレーションをアクションテキストからアプリケーションにコピー
            アクティブストレージのセットアップ
            テンプレートを適用
            対話形式でアップデート
            直接のテンプレートの依存関係を調査
            ネストしたテンプレートの依存関係を調査
            development環境のキャッシュのオンオフ
            アプリケーションにImportmapを設定
            イニシャライザをパスとともに起動順に表示
            logディレクトリ以下にあるすべてのlogファイルを0バイトに切り詰める
            Rackのミドルウェアスタックを出力
            アプリケーションを再起動
            暗号化された安全な秘密鍵を生成
            アプリケーションの統計情報
            Stimulusをアプリケーションにインストール
            importmap-railsが動作しているアプリケーションにStimulusをインストール
            アプリケーションが動いているノードにStimulusをインストール
            テストの実行
            テストの実行とデータベースのリセット
            システムテストを含むすべてのテストの実行
            全てのタイムゾーンの一覧表示
            tmpディレクトリをクリア
            キャッシュやソケットなどをtmpディレクトリに作成
            Turboをアプリケーションにインストール
            アセットパイプラインでTurboをアプリケーションにインストール
            webpackerでTurboをアプリケーションにインストール
            Redisのスイッチを入れ開発で使用
            Yarnで指定されたすべてのJavaScriptの依存関係をインストール
            Zeitwerkの互換性についてプロジェクト構造をチェック
            

- 学習メモ
    - 第 1 章 はじめに
        - Rubyは開発者を幸せにする言語-matz
            - 普段使っているWebアプリケーションにはプログラミングが大きく関わっている
        - 1.1 本書の目的
            - ミニブログアプリの作成
        - 1.2 本書の対象読者
            - プログラミング初学者
            - Railsドキュメントを自分で読める人は対象外
        - 1.3 書式例
            - ruby および rails コードの書式例
            - 差分がある場合の書式例
            - ターミナルコマンドの書式例
            - ターミナルの実行結果の書式例
        - 1.4 サンプルコード
        - 1.5 開発環境
            
            Mac に開発環境をつくる
            
            Windows に開発環境をつくる
            
            Ruby と Rails をインストールする
            
    - 第 2 章 一番小さな Rails アプリづくり
        
        2.1 一番小さな Rails アプリをつくる
        
        rails g コマンドでページを作る
        
        ```
        mkdir my_web_app
        cd my_web_app
        rails new helloworld
        cd helloworld
        rails s
        ```
        
        コラム: タイムゾーンの設定 
        
        ```
        config/application.rb
        
        Time.current.in_time_zone('Asia/Tokyo')
        ```
        
        - configファイルで定義すると全体に定義され、複数回にわたって記載する必要ない
        
        2.2 Web アプリはどのように動作しているか
        
        - データと処理の流れ
            - クライアント側からURLでリクエストを送る
            - リクエストから送られてした内容に基づいて
            - 適切なViewをサーバーが返す
            - Viewファイル（HTML）をブラウザが解釈して表示する
        - コラム: Web サーバ
            - Railsの場合はpumaというWebサーバーを使用している
        
        2.6 Rails が生成するファイル
        
        - rails new コマンド
            - rails new アプリケーション名とする事でアプリの雛形を作成する事ができる
        
        rails g コマンド 
        
        2.7 Rails アプリの処理の流れ
        
        - Routes
            
            http://localhost:3000/rails/info/routes
            
            記載したパスとアクションの対応表が一覧として見る事ができる
            
            ![image.png](attachment:5914eaec-9425-462e-8f67-40fbaa0f973f:image.png)
            
        - コントローラ
            - class BooksController < ApplicationControllerから最後の行のendまで
                - その中でアクションの定義を行う
                    - def ~~~ end　が一つのアクションの定義になる
        - ビュー
            - Webサーバーから返ってきたViewをブラウザが解釈して表示する
    - 第 3 章 CRUD の基礎と index アクション
        
        3.1 CRUD 基礎
        
        - CRUD
            - C：新規作成(Create)
            - R：表示(Read)
            - U：更新(Update)
            - D：削除(Delate)
        - アプリの作成
            - 基本的な機能を持った状態でアプリの雛形が生成されるコマンド
                - scaffold コマンド
                    - rails g scaffold
                        - 基本的なアプリの機能CRUDを一度に生成してくれる機能
                    - 作成されるページ
                        - 4つの表示内容がある画面
                            - 一覧：index
                            - 新規入力：new
                            - 編集機能：edit
                            - 詳細：show
                        - 3つの表示画面の無い画面
                            - 新規作成：create
                            - 更新：update
                            - 削除：destroy
        
        3.2 index アクション
        
        1. Routes
            - http://loacal:300/rails/info/routesにアクセスする事で設定されているルーティンングの一覧を見る事ができるようになっている
            - indexアクションは/books(アプリ名)になっている
            - ルーティングでURLのパスとアクションに応じて処理を分ける
        2. コントローラ
            - indexアクションの定義
                
                ```ruby
                def index
                	@books = Book.all
                end
                ```
                
                - 命名規則
                    - コントローラー名
                        - 複数形で命名する
                            - コントローラー内に基本的には複数のアクションが入る事が予想されるため
                    - モデル名
                        - 単数型での命名
                            - BookモデルはApplicationRecordを継承してクラスで中身が複数あるわけではないため
                    - テーブル名
                        - 複数形で命名する
                            - テーブル内のデータは0個の可能性もあるが、基本的には複数になる事が多いため複数形で基本、命名する
        3. ビュー
            - コントローラーの処理が終わったらViewに処理が移る
                - ViewはHTMLで記載する
                    - Rubyのコードを記載できるフォーマット（.erb）の場合には
                        - Rubyのコードを埋め込む
                            - <% %>
                                - HTMLの画面には表示されない
                        - Rubyのコードを表示する
                            - <%= %>
                                - HTMLの画面に表示される
            - renderメソッド
                - 他のファイルを埋め込むメソッド
                    - <%= render モデルオブジェクト %>
                - 埋め込むファイル
                    - パーシャルビュー
    - 第 4 章 new, create アクション
        
        4.1 概略
        
        - CRUDの中のC（Create）の部分、新規作成機能になる
            
            ステップ 1: new アクション（新規作成画面）
            
            - newアクションが実行されると新規入力画面を表示する
                - 登録する情報を入力してcreateアクションを呼び出す
            
            ステップ 2: create アクション（画面なし）
            
            - newアクションの画面で入力された情報を登録するアクション
                - 対応するビューはない
        
        4.2 new アクション 
        
        Routes
        
        - パス
            - books/new
        - HTTP
            - GET
        
        コントローラ
        
        - def new @book = [Book.new](http://Book.new) end
            - newメソッドを使ってインスタンスを作成する
                - Bookモデルオブジェクト
                    - Bookクラスをもとに作成される
        
        ビュー 
        
        - パーシャルビューを使ってフォーム部分のコードを別のファイルに記載する
        
        ```ruby
        <h1>New book</h1>
        <%= render "form", book: @book %>
        <br>
        <div>
        	<%= link_to "Back to books", books_path %>
        </div>
        
        ↓
        <%= render 埋め込むパーシャルビュー, パーシャル内で使う変数名: 渡すオブジェクト>
        <%= render "form", book: @book>
        ```
        
        - パーシャルビューに変数を渡す
            - <%= render "form", book: @book %>
                - book: @bookとする事で変数@bookを渡す事ができる
        - 埋め込んでいるパーシャルビュー
        
        ```ruby
        app/views/books/_form.html.erb
        
        <%= form_with(model: book) do |form| %>
        
        ＜＜以下、エラーのためのコード＞＞
        <% if book.errors.any? %>
        <div style="color: red">
        <h2><%= pluralize(book.errors.count, "error") %> prohibited this book from being saved:</h2>
        <ul>
        <% book.errors.each do |error| %>
        <li><%= error.full_message %></li>
        <% end %>
        </ul>
        </div>
        <% end %>
        ＜＜ここまで＞＞
        
        <div>
        	<%= form.label :title, style: "display: block" %>
        	<%= form.text_field :title %>
        </div>
        <div>
        	<%= form.label :memo, style: "display: block" %>
        	<%= form.text_area :memo %>
        </div>
        <div>
        	<%= from.submit %>
        </div>
        <% end %>
        ```
        
        - 各部品
            - title入力欄
                - <div>タグで囲んだエリアがグルーピングされている
                - <%= %>でRubyコードのformメソッドを使っている
                    - form.label
                        - ラベル名の表示
                    - form.text_field
                        - bookに関するtextを記載する
                    - form.text_area
                        - text._fieldより広く改行などもできる入力欄ができる
        
        リクエストを観察する
        
        - Chromのデベロッパーツールでリクエストを観察する
            - createボタンを押すとどのようなリクエストが発生するのか？
        - リクエスト内容
            - HTTPメソッド
                - POST
            - URL
                
                /books
                
        
        ![image.png](attachment:364d5602-b680-4e34-b531-08ef17b1195a:image.png)
        
        - PayLoadタブにはbool[title],book[memo]の情報を見つける事ができる
        
        ![image.png](attachment:3bf3f80d-808e-468a-ad4a-8b561460f07c:image.png)
        
        4.3 Create アクション
        
        ### 新たなリクエスト
        
        - books newメソッドでcreateボタンをクリックするとcreateアクションが実行されるようになる
        
        Routes
        
        - HTTPメソッド
            - POST
        - URL
            - /books
        
        ### コントローラ
        
        - books#create
            - @book = Book.new(book_params)
                - @bookにBookモデルのnewメソッドを使って引数にはbook_paramsメソッドを取ってインスタンスを作成
        
        ```ruby
        @book = Book.new(book_params)
        ```
        
        ### パラメータ
        
        - ブラウザから飛んでくるリクエストの中に含まれている情報
            - 先ほどのnewアクションであればtitle名やmemoの内容が含まれる
        - ブラウザで作成したリクエストの内容とparamsの内部に入っている値は同じであった
        
        ![image.png](attachment:cec71d70-0d1f-4208-9fd3-187f297df7e7:image.png)
        
        ### Strong Parameters
        
        - require、permitメソッド
            - どちらも意図しないデータが入ってこないようにするためのメソッド
                - require引数に対象のモデルを定義
                - permitは受け取るプロパティを指定
                    - これらをストロングパラメーターと呼ぶ
        - 目的
            - セキュリティ面
                - 攻撃者がプログラマの意図しない形の情報だけではないデータをリクエストに送る可能性がある
        
        ### まとめ
        
        - 新規入力画面　＝＞　newアクション
            - newアクションへはGETで辿り着ける
        - 新規登録　＝＞　createアクション
            - createアクションへはPOSTでいく
        - ユーザからのリクエスト
            - ユーザーがformなどで入力した内容はリクエスト内容としてparamsとしてバックエンドへ送られてくる
        
        4.5 さらに学びたい場合は
        
        - Railsガイド読む
            
            https://railsguides.jp/action_controller_overview.html 
            
    - 第 5 章 モデル
        - データの長期保存とモデルについての説明
        
        5.1 データの永続化
        
        - コードの中で変数に代入したデータは変数の有効範囲(スコープ)が終わると消える
            - ＠などがついていない変数はローカル変数と呼ばれている
                - コントローラーであればメソッドの中だけで有効な変数ということになる
            - @がついている変数は1つのリクエストが終わるまでが変数の有効範囲という事ができる
        - 1つのリクエストだけでなくどのリクエストでも情報を取得できる理由
            - 新規入力画面（newアクション）で情報を登録する事で複数回のリクエストでも同様の情報を取得する事ができる
                - インスタンス変数のみでは表現する事ができないデータの流れである
                    
                    ＝＞　モデルが重要な役割を持っている
                    
        
        5.2 モデルの基本的な使い方　その 1 　保存 
        
        ```ruby
        if @book.save
        ```
        
        - モデルを使うとデータを保存する事ができる
            - Book.newでBookオブジェクトを作る事ができる
                - タイトルとメモの情報を渡す事ができる
                - 情報を渡す事でインスタンスとして情報を保持する事ができる
        - モデルの命名
            - 英語の単数形、大文字で始める
            - モデル名の小文字で始まるものは全て変数
        - save,save!,create,create!メソッド
            - ！は情報の保存ができなかった場合に例外を投げるメソッドになる
            - ！がないメソッドはfalseを返す
        - saveメソッドとcreateメソッドの違い
            - saveメソッドはすでにインスタンスが存在する場合にデータを保存する方法
            - createメソッドは新しいインスタンスを作成して保存するメソッドになる
        
        5.3 モデルの基本的な使い方　その 2 　読み込み
        
        ```ruby
        books = Book.all.to_a
        ```
        
        - 保存されているBookモデルのデータを全て取得できる
            - Array（配列）にBookオブジェクトが入る
            - 変数booksに対して複数のBookオブジェクトを代入している
        - to_aメソッド
            - 値をオブジェクトへ変換するメソッド
        
        5.4 モデルの基本的な使い方　その 3 　検索
        
        - whereメソッド
            - カラムのデータを指定するとその条件に合致するオブジェクトが返ってくる
        - first
            - データに合致するオブジェクトの最初の1つを取得する
        - 変数book
            - 取得するオブジェクトは1つなので単数形
        
        5.5 実習 : rails console でモデルを使う
        
        - rails console
            - RailsにはRubyが埋め込まれたirbを使ってRailsのコードを実行する事ができる
            - rails cコマンドをターミナルで実行する事でRailsのコードを一行ずつ実行する事ができる
        
        5.6 モデルの仕組み
        
        コンソールでデータを保存する方法
        
        - コンソールの立ち上げ
            
            rails c
            
        - # モデルオブジェクト作成
            
            book = Book.new(title: "some title", memo: "somememo") 
            
        - # 保存
            
            book.save! 
            
        - # 上で保存したデータの表示
            
            Book.last
            
        
        ### Bookモデルにはコードが記述されていない
        
        問: save や all といったメソッドが使えるのはなぜか？
        
        - ApplicationRecordクラスを継承している事で様々なメソッドを使用する事ができる
        
        問: title や memo といった要素があることをどこで知るのでしょうか？
        
        - DBから情報を取得している事でbook.titleやbook.memoなどというメソッドで要素を取得している
        
        ### データベース（DB）とは？
        
        - データを保存したり、読み出す、検索する事に特化したプログラムである
            - 通常、SQLという言語で操作する事ができる
                - モデルはDBを便利に扱う事ができる
        
        5.7 DB はいつ作られたのか？
        
        - scaffold コマンドを実行した時にマイグレーションファイルが生成されている
            - その後、db:migrateを実行する事でmaigrationファイルの設計図通りにdbが生成される
        
        5.8 マイグレーション（migration）ファイル
        
        - booksテーブルを生成する
            - t.string :title
            - t.text :memo
        
        ```ruby
        class CreateBooks < ActiveRecord::Migration[7.0]
        	def change
        		create_table :books do |t|
        			t.string :title
        			t.text :memo
        			t.timestamps
        		end
        	end
        end
        ```
        
        5.9 保存したあとの処理
        
        - respond_to do |format|
            - リクエストされたレスポンスの形式によって分岐させる文
                - ブラウザでnew画面で入力した情報をformat.htmlが選ばれる
                - スマホなどからのリクエストの場合にはjson形式が選択される
        - @book.save
            - 成功　＝＞　true
            - 失敗　＝＞　false
                - trueの場合には処理を実行
                - falseの場合には処理を実行せずにelseに処理が飛び、endまでが処理が実行される
        - true
            - redirect_to @book, notice: ’Book was successfully created.’
                - showアクションへのリクエストが発生する
        - false
            - render :new
                - 再度、リクエストする
    
        
        5.12 既存の DB テーブルにカラムを増やすには？
        
        - 一番最初にDBを生成したmigrationファイルに変更を加えたとしてもDBにカラムを追加する事はできない
        - 新たなmigtationファイルを生成する必要あり
            - rails g migration AddAuthorToBooks author:string
                - rails genarateにmigrationを追加すると
                    - migrationファイルのみを生成する事ができる
            - 再度、db:migrateを実行する事で内容を反映する事ができる
            
            ```ruby
            class AddAuthorToBooks < ActiveRecord::Migration[7.0]
            	def change
            		add_column :books, :author, :string
            	end
            end
            ```
            
        
        5.13 新しいモデルと migration を一緒に作るには？
        
        - rails g にモデル名を指定すると
            - モデル
            - migrationファイルがどちらも生成される
        
        ```ruby
        rails g model book title:string memo:text
        ```
        
        5.14 rails g コマンドまとめ
        
        5.15 scaffold でつくった既存テーブルへカラムを追加するには？
        
    - 第 6 章 Gem ライブラリ
        - Gemライブラリとは？
            - ライブラリ
                - 便利なプログラムが公開されたものをライブラリと呼ぶ
            - その中でも[rubygems.org](http://rubygems.org/)に公開されているライブラリをGemライブラリと呼ぶ
                - Gemライブラリの集合体がRailsになる
                    - Gemを使うと便利にWebアプリケーションを開発する事ができる
        - Gemの使い方
            - インストール
                
                gem install Gem名
                
        - Bundler
            - Gemをインストールする際にGemの数だけコマンドを実行していると時間がかかってしまう。
                - Gemの管理をする Bundlerを活用してGemをインストールする
        - Bundlerを使ってGemライブラリを管理する方法
            - Gemfile
                - 必要なGemを記載する
            - bundle install
                - Gemfile内に記載されたGemがインストールされる
                    - Gemfileに記載されているGemをインストールしてGemfile.lockに記載
                - GemfileとGemlock.fileは注文書と納品書の関係になっている
        - Gemのバージョン
            - Gemはインストール時に基本的に最新バージョンがインストールされる
                - バージョンを最新バージョンにあげたい場合には
                    - gem updateを行う
                    - Gem名を指定しなければ全てのGemに適用される
            - Gemfileに記載された古いバージョンを使いたい
                - Gemファイルのバージョンが書き換わるわけではないのでGemファイルの中にはupdateした場合にも古いバージョンが残るようになっている
                    - bundle execを使う事で古いバージョンのGemを使う事ができる
            - バージョンを指定する
                - Gemfileの中にはバージョンが最初から指定されている場合がある
                    - 〇〇以上のバージョンを使用する
                        
                        gem 'Gem名','>= バージョン数'
                        
                    - 〇〇かつ〇〇より大きなバージョンは受け入れない
                        
                        gem 'Gem名’,'~> バージョン数'
                        
    - 第 7 章 画像アップロード機能の追加
        
        7.1 画像情報を格納するための DB カラムを追加
        
        - migration コマンドを使ってmigrationファイルを作成する
            - migrataファイルの内容を確認
                - rails db:migrateを実行してDBへ変更を反映させる
        
        7.2 carrierwave gem を追加
        
        - 画像アップデート機能を持つライブラリ
            - Gemファイルへgem "carrierwave”を記述
                - bundle installをする事でGemを追加
        - carrewave gemが提供するコマンド
            - rails g uploader Picture コマンド を実行する
                - uploaders/picture_uploader.rbファイルが生成される
        
        7.3 モデルの変更
        
        - Bookモデル内にmount_uploader :picture, pictureUploaderを記載する
            - mount_uploader
                - ラックベースのアプリケーションをマウントする
            - uploaderのマウント時にpictureをPictureUploaderに渡す
        
        7.4 コントローラの変更 
        
        - Bookコントローラーでリクエストから受け取るストロングリクエストパラメーターの引数にpictureを追加する
        
        7.5 ビューの修正
        
        - formのパーシャルビューにpicture用のfieldを準備する
            - fieldはtextではなくfileにする
        
        7.6 動作確認
        
        - ViewにPictureをファイル形式でアップロードするfieldが追加された
        - 画像をアップロードする事が可能になり、show画面、index画面で画像も表示されるようになった。
        
        7.7 まとめ 
        
        - carrierwaveを使うと画像のアップロード機能を追加する事ができる
        - GemfileにGem名を追加してBundleインストールする方法
        - カラムの追加方法
            - rails g migration Addカラム名Toテーブル名　カラム名:データの型
    - 第 8 章 あとがき
        
        8.1 さらに学びたい方への資料
        
        Git と GitHub でソースコードを管理する
        
        - GitHunでグローバルにリポジトリを公開する事ができる
        - 他の人が作ったリポジトリもローカルに引くことができる
        
        つくったアプリを公開する
        
        - 作成したアプリを公開する
            - Paasというサービスを使用すると簡単に公開する事ができる
                - アプリケーションのソースコードを転送するだけで良い
                    - Railsで人気なサービス
                        - Heroku
            - AWS
                - サーバーをレンタルする必要があるなどPaasと比較すると面倒になる
        
        Ruby を学ぶ資料
        
        - そもそもRailsはRubyで記載されているためRubyに関する知識をもっと深める
        
        8.2 Ruby コミュニティ
        
        - 1番重要な事は自分が作りたいサービスを作成するという事が重要
            - Rubyのコミュニティがある
                - Rubyの事で詰まったりした時に行ってみるのもあり

Rails
　Rubyのフレームワーク
　　MVCアーキテクチャ
　　　M model　データベースとRailsを繋ぐ役割
　　　View　見た目
　　 Contoloer　Railsとクライアントを繋ぐ
　　 　ルーティングから受け取った対応表を元にアクションを実行する
　　 　 アクション
　　 　　 Viewを返す
　　 　  modelでテーブル操作をする
　　最近の流れ
　　　RailsをMVCとして扱わずにMCのみを活用しViewは他の言語を使用する

- ***Railsドキュメント(/52章)***

- Ruby on Rails インストールガイド
    - Rubyプログラミング言語とRuby on Railsのインストール方法について解説します。
- Dev Container での開発ガイド
    - VS CodeとDev Containerを使ってRailsアプリケーションの開発を行う方法について解説します。
- モデル
    - Active Record の基礎
        - Active Recordの基礎となるモデル、データベースへの永続的な保存、Active Recordパターンとライブラリについて解説します。

Active Record マイグレーション
Active Recordのマイグレーション（migration）を使って、データベースを構造化された方法で整然と変更する方法について解説します。

Active Record バリデーション
Active Recordのバリデーション機能について解説します。

Active Record コールバック
Active Recordのコールバックについて解説します。

Active Record の関連付け
Active Recordが提供するすべての関連付け機能（アソシエーション）について解説します。

Active Record クエリインターフェイス
Active Recordが提供するすべてのデータベースクエリインターフェイスについて解説します。

Active Model の基礎
Active Recordを使わずにモデルクラスを扱う方法について解説します。

ビュー
Action View の概要
Action Viewの概要を紹介し、共通のビューヘルパーについてもある程度解説します。

レイアウトとレンダリング
Action ControllerとAction Viewが提供する基本的なレイアウト機能について解説します。画面出力（レンダリング）やリダイレクト、content_forブロックとパーシャル（部分テンプレート）の利用方法についても解説します。

Action View ヘルパー
Action Viewで提供されるヘルパーの概要について解説します。

Action View フォームヘルパー
ビルトインのフォームヘルパーについて解説します。

コントローラ
Action Controller の概要
本ガイドでは、コントローラの動作と、アプリケーションのリクエストサイクルでコントローラがどのように使われるかについて説明します。セッション、フィルタ、cookie、データストリーミング、リクエストによって発生する例外、その他多くの話題を取り扱っています。

Action Controller の高度なトピック
本ガイドでは、クロスサイトリクエストフォージェリの防止、HTTP認証、データストリーミング、例外の処理、ログのフィルタリングなど、Railsアプリケーションのコントローラーに関連する多くの高度なトピックを扱います。

Rails のルーティング
Railsのルーティング機能について解説します。Railsアプリケーションで行われているルーティングのしくみについて理解したい場合は、ここからお読みください。

他の構成要素
Active Support コア拡張機能
Active Supportで定義されているRubyのコア拡張機能に関するドキュメントです。

Action Mailer の基礎
Action Mailerを使ってメールを送受信する方法について解説します。

Action Mailbox の基礎
Action Mailboxを使ってメールを受信する方法について解説します。

Action Text の概要
Action Textを使ったリッチテキスト形式のデータの取り扱い方法について解説します。

Active Job の基礎
バックグラウンドで動作するジョブの作成・キュー送信・実行方法に必要なすべてを解説します。

Active Storage の概要
Active Recordモデルにファイルを添付する方法について解説します。

Action Cable の概要
リアルタイム機能を実現するAction Cableの動作と、WebSocketsの利用法について解説します。

Webpacker の概要
Railsがラップするwebpackビルドシステム「Webpacker」について解説します。

高度なトピック
Rails 国際化（I18n）API
Railsアプリケーションを国際化する方法について解説します。これによりアプリケーションを異なる言語に翻訳することができ、さらに単数形/複数形ルールを変更したり、その国に適した日付フォーマットを設定したりできます。

Rails テスティングガイド
Railsでさまざまなテストを実行するための総合的な解説を行います。「テスティングとは何か」から結合テストまですべてのトピックを扱います。

Rails アプリケーションのデバッグ
Railsアプリケーションのデバッグ方法について解説します。さまざまなデバッグ方法や、作成したコードの舞台裏でどのような動作が行われているかについても解説します。

Rails アプリケーションの設定項目
Railsアプリケーションの基本的な設定方法（Config：コンフィグ）について解説します。

コマンドラインツール
Railsが提供する各種コマンドラインツールについて解説します。

アセットパイプライン
アセットパイプラインガイドでは、重要なアセット管理タスクを処理するフレームワークであるPropshaftの使い方について解説します。

Rails で JavaScript を利用する
importmapやjsbundling-railsを用いてRaisアプリケーションにJavaScriptを組み込む方法を解説します。RailsでTurboを使う基本的な方法についても解説します。

Rails の初期化プロセス
Work in progress
Rails内部の初期化プロセスについて解説します。

Rails の自動読み込みと再読み込み
Rails内部の自動読み込みや再読み込みの動作について解説します。

Classic から Zeitwerk への移行
RailsアプリケーションをClassicモードからZeitwerkモードに移行する手順を解説します。

Active Support Instrumentation で計測
Work in progress
RailsなどのRubyコード内のイベント測定に使う、Active Support内のInstrumentation APIについて解説します。

Rails アプリケーションのテンプレート
Work in progress
テンプレートを使って生成/カスタマイズを行う方法や、テンプレートAPIを使って再利用可能なテンプレートを開発する方法について解説します。

Rails による API 専用アプリケーション
JSON APIアプリケーションをRailsで効果的に作成する方法を解説します。

デプロイ用パフォーマンスチューニング
Ruby on Railsアプリケーションをproduction環境にデプロイする際のパフォーマンスとコンカレンシーの設定について解説します。

Rails のキャッシュ機構
キャッシュを活用してRailsを高速化する方法について解説します。

Rails セキュリティガイド
Webアプリケーション全般におけるセキュリティ問題と、Railsでこれらの問題を回避する方法について解説します。

Rails アプリケーションのエラー通知
Railsアプリケーションで発生するエラーを管理する方法について解説します。

Active Recordの高度な話題
Active Record と PostgreSQL
Work in progress
PostgreSQLに特化したActive Recordの利用法について解説します。

Active Record と暗号化
Work in progress
Active Recordを用いてデータベースの情報を暗号化する方法について解説します。

Active Record の複数データベース対応
Active Recordで複数のデータベースを利用する方法について説明します。

Active Record の複合主キー
データベースのテーブルに複合主キーを導入する方法について解説します。

Rails を拡張する
Rails プラグイン作成入門
Work in progress
プラグインを作成してRailsの機能を拡張する方法について解説します。

Rails と Rack
RailsとRackがどのように統合されているか、および他のRackコンポーネントとのインターフェイスについて解説します。

Rails ジェネレータとテンプレート入門
新しいジェネレータを拡張に追加したり、ビルトインのRailsジェネレータの要素に別の要素を提供したりする方法（scaffoldジェネレータに別のテストスタブを提供するなど）について解説します。

Rails エンジン入門
Work in progress
マウント可能なエンジンの作成方法について解説します。

Rails のスレッドとコード実行
Work in progress
Railsアプリケーションの並行性について考慮すべきことや利用可能なツールについて解説します。

Ruby on Rails に貢献する
Ruby on Rails に貢献する方法
Railsは「どこかで誰かがうまくやってくれているフレームワーク」ではありません。現在も継続しているRailsフレームワーク開発に貢献するさまざまな方法について解説します。

Rails コア開発環境の構築方法


・要件
　　いいね取り消しボタンを作成する
・ユーザー体験
　　いいね取り消しボタンをクリックするといいねを取り消せる
・処理
　　destloyアクションを作成する
　　　アクション
　　　 変数に削除したいLikeインスタンスを呼び出して代入する
　　　 変数にdestroyメソッドを実行する
　　　 投稿詳細ページへリダイレクトするようにする
　　　ルーティング
　　　　likes/@post_id/destloy
　　いいね取り消しボタンを作成する　View
　　link_toメソッドを活用
　　　第一引数　いいね取り消し　第二引数　destroyアクションへのリンク　第三引数　postで始まるルーティングへアクセスするためのメソッド

・要件
Font Awesomeを活用していいねボタンをハートマークにする
・ユーザー体験
　　なし
・処理
　　Font Awesomeの読み込み
　　 Font Awesomeは<head>タグ内で行わないといけない
　　 　共通のHTML内でlinkを使って使用可能な状態にする
　　HTML要素をlink_toメソッドで表示する
　　　link_toメソッドの第一引数で表示したい内容を記載するが、HTMLのURL（要素）を入れても文字列として認識されてしまうためHTML要素をlink_toで使用する場合には異なった方法を用いる必要がある
　　　　<%= link_to(URL) do %>と<% end %>の間にHTML要素を書く
　　　　　<%= link_to(URL) do %>　「fa fa-heart 　<% end %>
　　　　いいねのリンクがハートになる
　　いいねしている状態といいねしていない状態で色を変える事でわかるようにする

・要件
いいねの数を表示する
・ユーザー体験
　　なし
・処理
　　いいねの数を取得して表示されるようにする

・要件
ユーザ詳細ページでいいねした投稿一覧が表示されるようにする
・ユーザー体験
　なし
・処理
　コントローラーで変数を定義する
　　必要な変数
　　　ユーザ詳細ページで表示するユーザの情報（インスタンス情報）
　　　　@user = User.find_by(id: params[:id])
　　　表示するユーザのいいねした全ての投稿
　　　　@likes = Like.where(user_id: @user.id)
　　　それらの変数を元にいいねした投稿一覧をViewで表示
　　　　いいねした投稿一覧の変数に対して繰り返し処理を実行
　　　　　実行内容は変数postに対してlikeした投稿の内容を代入する
　　　　　　<% post = Post.find_by(id: like.post_id) %>

Ruby on Rails5 学習レッスン IX

・要件
投稿とユーザーを紐付ける
　postsテーブルにユーザIDのカラムを追加する
　postsテーブルのユーザDカラムにバリデーションをかけて投稿が行われた時にカラム値が追加されるようにする
投稿したユーザのIDを保存する
　ポストを作成した際にcontent内容だけではなく、user.idも追加で保存する
・ユーザー体験
なし
・処理
　　ターミナルでrails generate model　ファイル名とする事でマイグレーションファイルを作成する
　　　マイグレーションファイル内でカラムの追加を行う
　　　　rails db:maigrateでデータベースに変更を加える
　　投稿を作成する際に投稿作成したユーザのIDを登録する
　　 user_id: @current_user.id

・要件
　　投稿にユーザ情報を表示させる
　　　ユーザが登録したプロフィール画像
　　　ユーザ名
　　　　リンクにする
・ユーザー体験
投稿詳細ページにユーザ名やプロフィール画像などが表示される
・処理
　　showアクション内で@userを定義する
　　　定義する@userは投稿したユーザにしたいため@post.user_idにする
　　Viewで画像とユーザ名を表示させる
　　　画像
　　　　imgタグ
　　　ユーザー名
　　　　link_toメソッド
　　　　　link_to("@user.name","/users/#{@user.id}")

・要件
投稿に紐づくユーザー情報のインスタンスメソッドを作成する
　投稿にユーザー情報を紐づける作業は多く行うためインスタンスメソッドにして簡単に使えるようにする
　　インスタンスメソッド
　　　Rails はモデル内で定義したインスタンスメソッドをインスタンスに対して活用する事で使える
・ユーザー体験
　　なし
・処理
　　userアクション
　　　postモデル（定義するモデル）に投稿（コンテンツ）と紐づいているインスタンスを戻り値として返すメソッド
　　　　コントローラー
　　　　　User.find_by(id: self.user_id)
　　　　　　selfはインスタンス自身が適応される
　　　　　　　投稿しているユーザのIDをfind_byメソッドを活用してユーザ情報を取得する
　　　　　　　 戻り値を返したいためreturnを使う
　　　return = User.find_by(id: self.user_id)

・要件
投稿一覧でもユーザ情報が表示されるようにしたい
・ユーザー体験
　　なし
・処理
　　index.htmlでユーザ一覧（index）内の繰り返し処理でcontentのみではなくユーザ名、プロフィール画像が表示されるようにしたい
　　　画像
　　　　imgタグ
　　　　　srcにpostモデルで定義しているuserアクションで呼び出したインスタンスのimage_nameカラムの値を入れる事でプロフィール画像を表示させる事ができる
　　　　　　<img src="<%= "/user_images/#{post.user.image_name}" %>">
　　　　ユーザ名
　　　　　ユーザ名部分はテキストリンクにしたいためlink_toメソッドを活用する
　　　　　　第一引数にはpostモデルのuserアクションで呼び出したインスタンスのnameカラムを、第二引数にはpostモデルのuserアクションで呼び出したインスタンスのidカラム値を活用する
　　　　　　　<%= link_to([post.user.name](http://post.user.name/),"/users/#{[post.user.id](http://post.user.id/)}") %>

・要件
　　ユーザ詳細ページにそのユーザの投稿一覧を表示する
　　　ユーザ詳細ページでwhereメソッドを活用してユーザ一覧を表示する
・ユーザー体験
　　なし
・処理
　　ユーザ詳細ページ（show.html  user/id）でwhereメソッドを活用して投稿一覧を作成する
　　　モデルでユーザに紐づく投稿を全て呼び出してくれるメソッドを作成する
　　　　def posts return Post.where(user_id self,id)
　　　Viewではインスタンスを作成しメソッドを呼び出す

whereメソッド
　指定した条件に合致するものを配列にするメソッド
　　find_byメソッドはが一致するものを１つ呼び出すメソッドになっている
　　指定する条件に合致する値が複数ある場合にはwhereを活用する

・要件
投稿内容編集を投稿者自身のユーザでのみ編集・削除できるようにする
　index前でif文を作成してログインしているユーザと@post（投稿したユーザー）情報が正しい場合のみ編集・削除のリンクが出てくるようにする
・ユーザー体験
　　自身の投稿した投稿詳細ページのみで編集・削除ボタンが表示される
・処理
　　index前で編集・削除のリンクをログインしているユーザと投稿を作成したユーザが同じ場合のみに表示するようにする
　　　@post.user_id  ==  @current_user.id

・要件
投稿内容の編集をURLで直接指定しても投稿一覧ページへ転送されるようにしてフラッシュメッセージを出す
・ユーザー体験
　　なし
・処理
　　クライアントが直接URLを指定しても表示されないようにensure_correct_userを定義する