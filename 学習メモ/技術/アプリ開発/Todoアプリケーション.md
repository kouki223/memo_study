- 進捗管理
    
    Rails+React（SPA）TODOアプリチュートリアル【0から学ぶ】
    
    https://zenn.dev/prune/books/0d7d6e3c5f0496
    
    - 全15 issue(”1”~”7”→20％　”8”→”16” 各10％)
        1. RailsとReactを0から学んでTODOアプリを作ってみよう！
        2. 完成物を見てみる
        3. 【Rails】Ruby・Railsと関連パッケージのインストール
        4. 【React】Reactの関連パッケージのインストール
        5. 【Rails】新規プロジェクトを作成
        6. 【React】create-react-appで新規プロジェクトを作成
        7. 【React】Reactの基礎とJSX（20/100） ~2/27 
        8. 【React】コンポーネントを学んでTaskコンポーネントを作成(10 20/100) 2/28~
        9. 【React】ChakraUIを使ってTaskコンポーネントのデザインを整える(10 30/100) ~3/1
        10. 【React】React Hooksについて学んで、実際に使ってみる(10 40/100)　3/2~
        11. 【Rails】RailsAPIの基礎(10 50/100)　3/3~
            1. [Railsの通信の流れを解説（MVCモデル）](https://zenn.dev/prune/books/0d7d6e3c5f0496/viewer/d8bed7#rails%E3%81%AE%E9%80%9A%E4%BF%A1%E3%81%AE%E6%B5%81%E3%82%8C%E3%82%92%E8%A7%A3%E8%AA%AC%EF%BC%88mvc%E3%83%A2%E3%83%87%E3%83%AB%EF%BC%89)
                1. [ルーティング（route.rb）](https://zenn.dev/prune/books/0d7d6e3c5f0496/viewer/d8bed7#%E3%83%AB%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%88route.rb%EF%BC%89)
                2. [コントローラー（controller）](https://zenn.dev/prune/books/0d7d6e3c5f0496/viewer/d8bed7#%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%EF%BC%88controller%EF%BC%89)
                3. [モデル（Model）](https://zenn.dev/prune/books/0d7d6e3c5f0496/viewer/d8bed7#%E3%83%A2%E3%83%87%E3%83%AB%EF%BC%88model%EF%BC%89)
            2. [最後に](https://zenn.dev/prune/books/0d7d6e3c5f0496/viewer/d8bed7#%E6%9C%80%E5%BE%8C%E3%81%AB)
        12. 【Rails+React】タスク一覧機能(10 60/100)　3/4~
        13. 【Rails+React】タスク作成機能(10 70/100)　3/5~
        14. 【Rails+React】タスク削除機能(10 80/100)　3/6~
        15. 【Rails+React】タスク完了機能(10 90/100)　3/7~
        16. さいごに(10 100/100)
- 筆者
    - フルスタックエンジニア
        - フロントエンドからバックエンドまで幅広く活躍するエンジニア
            - 万能エンジニアなどとも呼ばれる
- Webアプリケーション開発形式
    - MPA
        - マルチページアプリケーション
            - リクエスト毎にHTMLを受け取る
                - ユーザーのリクエストに応じてサーバー側でHTMLが生成されてページ全体が更新される
    - SPA
        - シングルページアプリケーション
            - 最初のページ読み取り時にコンテンツの情報も受け取る
                - ユーザーのリクエストに応じてコンテンツ情報が更新される
                    - ページ全体の更新ではなくコンテンツ単位で更新される
                        - MPAよりも表示速度などで優位
- Rails APIモード
    - RailsのMVCアーキテクチャという思想を捨てる
        - フロントエンドのフレームワーク(Reactなど)との疎結合な連携を目的にしてJSON APIとして振る舞うバックエンド領域特化として開発するモード
            - JSON
                - JavaScriptのわかりやすいように連想思考型でデータを返す形式
- この本での学習の進め方
    - 最初のうちは理解が難しい
        - 理解できなくても先に進む事をオススメ
            - 先に進む事で全体像を把握でき
                - 全体像が把握できると次々と理解できるようになる
- Rails APIモードのローカルを作成
    - Railsはデータを返す（基本的にはJSON形式）ことに専念してフロント側は他のアプリケーションに任せる
- React
    - Facebookが提供しているCLI ツール
        - コマンドライン（文字入力）でコンピューターソフトウェアやオペレーティングシステムと対話するためのツール
            - create-react-appを使って雛形を作成する
                - npx create-react-app todo-web
    - npm
        - インストールする事なくコマンドが実行できる
    - 任意の場所で実行する
        - rails 作成時点での最新のバージョン new todo_api --api
            - --apiと実行する事でAPIモードで作成される
    - bundleをインストール
        
        ```ruby
        # 作成したRailsプロジェクトに移動
        $ cd todo_api
        
        $ bundle install
        # 略
        Using spring 3.0.0
        Using sqlite3 1.4.2
        Bundle complete! 8 Gemfile dependencies, 52 gems now installed.
        Use `bundle info [gemname]` to see where a bundled gem is installed.
        ```
        
        ### **bundlerとgemって何？**
        
        - gem：**ライブラリ**のこと
        - bundler：**gemfileとgemfile.lockを使って、gemを管理をするライブラリです。**
    - ポート番号を変更する
        - config/puma.rbファイル内の記載内容を変更する
            - port ENV.fetch("PORT") { 3000 }
                - 3000の部分を変更する
    - データベースの作成
        - rails db:create
    - CORS（Cross-Origin Resource Sharing）を設定
        - React等の別のオリジンからRailsAPIにアクセス（GET, POST, PUT, DELETEなど）することがデフォルトだと制限されているため制限を解除する
    - Gemファイル
        - gem 'rack-cors’のコメントアウトを解除する
    - バンドルインストールを行う
        - bundle install
    - Reactで使用する予定のポートからの通信を許可するプログラムを記載する
        - http://localhost:3000
        
        ```ruby
        Rails.application.config.middleware.insert_before 0, Rack::Cors do
          allow do
            origins 'http://localhost:3000'
        
            resource '*',
                headers: :any,
                methods: [:get, :post, :put, :patch, :delete, :options, :head],
                credentials: true
          end
        end
        ```
        
- JSX
    - React内部のプログラムの記載は基本JSXで記載する
        - HTMLのような書き方の中にJavaScriptも書くことができる構文
- 開発録 ~2/27
    - まずはJSXを知る
        - デフォルトの記載から変更する
            - アロー関数へ記載変更する
            - 必要のない記述を削除
            - h1タグで「これはテストです」という文章を表示
        
        ```jsx
        import logo from './logo.svg';
        import './App.css';
        
        function App() {
          return (
            <div className="App">
              <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                  Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                  className="App-link"
                  href="https://reactjs.org"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn React
                </a>
              </header>
            </div>
          );
        }
        
        export default App;
        
        ↓
        
        const App = () => {
          return (
            <h1>これはテストです</h1>
          );
        }
        
        export default App;
        ```
        
    - ディレクトリの移動方法
        - サーバーを立ち上げてhttp://localhost:3000/で実行内容を確認できるようにする
            - ディレクトリはプログラム直下の配下にいる時にサーバーを立ち上げる必要あり
        - cd ~ → ホームディレクトリに移動
        - cd ディレクトリを登っていく
        - pwdでどこのディレクトリの配下にいるのか？確認できる
        - npm start　でサーバーを立ちあげることができる
    - コンポーネント ~2/27
        - コンポーネントとは？
            - UIの部品
                - コンポーネントを組み合わせる事でページを作っていく
        - コンポーネントにおける情報の受け渡し
            - コンポーネントにおいて情報の受け渡しはpropsで受け渡される
        - コンポーネントの管理
            - コンポーネントはsrcディレクトリ内にcomponentディレクトリを作成する
            - １コンポーネントにおいて１ファイルを作成する方法が多い
        - Taskコンポーネントを作成する
            - 完成系
            
            ![image.png](attachment:908f1715-452c-4a8d-a686-5424dfa9a8e0:image.png)
            
        - クラスコンポーネントから関数コンポーネントへ
            - 元来Reactはクラスコンポーネントで記載される事が多かった
                - 関数コンポーネントでもクラスコンポーネントの機能であるHooksが使えるようになったため関数コンポーネントに移行してきている
        - importとexport
            - import
                - 他のファイルでexportされている定数やコンポーネントなどを取り込む
            - export
                - 他のファイルでもコンポーネントや定数が使えるようにする事
                    - default export
                    - named export
            
            ```jsx
            const Member = (props) => {
              return (
                <p>名前：{props.name}</p>
                <p>年齢：{props.age}</p>
              )
            }
            
            const App = () => {
              return (
                //　ここでMemberコンポーネントを使いたい！
              )
            }
            
            // Memberコンポーネントをexport（今回はnamed export）
            export const Member = (props) => {
              return (
                <p>名前：{props.name}</p>
                <p>年齢：{props.age}</p>
              )
            }
            
            import { Member } from './Member'
            
            const App = () => {
              return (
                <Member name="田中" age="25" />
              )
            }
            ```
            
        - Taskコンポーネントを作成する
            
            ![image.png](attachment:0753ea32-b265-4799-90ce-77d5de7eec54:image.png)
            
            - VsScode
                - コンポーネントディレクトリをsrcフォルダ内で作成する
                    - mkdir src/component
                - その後、Taskコンポーネントの管理をするJSXを作成する
                    - touch src/component/Task.jsx
            - Task.jsx
                - 関数コンポーネントの作成
                    - <li>{[props.name](http://props.name/)}</li>を返す
                - 他のファイルでも使えるようにexport default Task
                
                ```jsx
                const Task = (props) => {
                  return (
                    <li>{props.name}</li>
                  )
                }
                
                export default Task
                ```
                
                - Raect Fragment
                    - JSXは一つの親要素で囲まないといけないというルールがある
                        - <div>タグで囲む方法もある
                            - 少しでもノードを減らすという目的からFragmentが使われる
                
                ```jsx
                import Task from './component/Task';
                
                const App = () => {
                  return (
                    <>
                      <h1>タスク一覧</h1>
                      <Task name="買い物" />
                      <Task name="ランニング" />
                      <Task name="プログラミングの勉強" />
                    </>
                  );
                }
                
                export default App;
                ```
                
        - UIの工夫（ChakraUI）
            - ChakraUIというCSSのフレームワークを導入する
                - ChakraUIのパッケージをインストール
                    - 本で指示されたコマンド
                        
                        ```jsx
                        $ yarn add @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^
                        ```
                        
                    - 実際に実行したコード
                        
                        ```jsx
                        npm i @chakra-ui/react @emotion/react
                        ```
                        
            - プロバイダーの設置
                - インポート
                    - import { ChakraProvider } from "@chakra-ui/react";
                - Appコンポーネントをラップする
                    - <ChakraProvider><ChakraProvider/>
                
        - UIのコンポーネントへの適応
            - TaskコンポーネントにChakraUIを当てる
                
                ```jsx
                import { Checkbox, Box, Text } from "@chakra-ui/react";
                
                const Task = (props) => {
                  return (
                    <Box mb="16px">
                      <Checkbox colorScheme="blue" size="lg">
                        <Text>{props.name}</Text>
                      </Checkbox>
                    </Box>
                  );
                };
                
                export default Task;
                ```
                
                - **Boxはdivタグのようなもの**
                    - 属性として`mb`というものを受け取る。
                        - `margin-buttom`
                            - このように書くことでCSSをわざわざ書かなくてもスタイリングをあてることができます。
        - Appコンポーネントの作成
            - Centerタグ
                - Boxタグ
                    - Textタグ　fontsizeを指定
                        - タスク一覧という文字列
                - CheckboxGroupタグ
                    - Taskコンポーネントの表示
                        - nameプロパティの表示
                            - 買い物
                            - ランニング
                            - プログラミングの勉強
                    
                    ```jsx
                    <Box mt="64px">
                      <Center>
                        <Box>
                          <Box mb="24px">
                            <Text fontSize="24px" fontWeight="bold">
                              タスク一覧
                            </Text>
                          </Box>
                          <CheckboxGroup>
                            <Task name="買い物" />
                            <Task name="ランニング" />
                            <Task name="プログラミングの勉強" />
                          </CheckboxGroup>
                        </Box>
                      </Center>
                    </Box>
                    ```
                    
            - Task.jsx
                - chakra-uiからCheckbox, Box, Textをインポート
                - タスクコンポーネント
                    - return
                        - <Box>タグ　mb=`margin-buttom`
                            - Checkboxタグ
                                - Textタグ
                                    - props.name
                
                ```jsx
                import { Checkbox, Box, Text } from "@chakra-ui/react";
                
                const Task = (props) => {
                  return (
                    <Box mb="16px">
                      <Checkbox colorScheme="blue" size="lg">
                        <Text>{props.name}</Text>
                      </Checkbox>
                    </Box>
                  );
                };
                
                export default Task;
                ```
                
    - ChakuraーUI
    - Hooks
        - React Hooks
            - React Hooksとは、以前はクラスコンポーネントで使えたもの
                - 関数コンポーネントでも使用できるようになったものがHooksである
            - useState
                - 関数コンポーネントでコンポーネントの状態を管理するHooks
                    - 状態という概念
                        - コンポーネントが内部で保持するもの
                            - 値
                            - 文字列
                            - bool値
                            - 配列
                - useStateには重要な設定が大きく2つある
                    - 状態変数
                    - トリガーとなるset関数
                        - const [name, setName] = useState('田中')
                            - name=状態変数
                            - setName=状態関数に変更がかかるトリガーとなる関数
            - useEffect（副作用）
                - 特定の処理をタイミングを指定して実行する事ができる
                    - タイミング：
                        - コンポーネントの初期化時
                        - レンダリング時
                        - アンマウント時など
                    - 処理内容：
                        - SPI通信
                        - 変数の代入
            - useStateとuseEffectを使ってタスク作成機能を作成する
                - useStateの値を使ってTaskを表示させる
                - useEffectを使ってTaskの初期値を設定する
                - タスクが完了か、未か？の値を持たせる
                    - propsから受け取ったisDoneをisCheckedという属性に入れる
                        - タスクの完了情報をコンポーネントに渡す
                    - チェックボックスの情報を受け取る
                        - isDone
                            - true or false
                    
                    ```tsx
                    import { Checkbox, Box, Text } from "@chakra-ui/react";
                    
                    const Task = (props) => {
                      return (
                        <Box mb="16px">
                          <Checkbox
                            isChecked={props.isDone}
                            colorScheme="blue"
                            size="lg"
                            onChange={() => {
                              props.toggleIsDone(props.index);
                            }}
                          >
                            <Text>{props.name}</Text>
                          </Checkbox>
                        </Box>
                      );
                    };
                    
                    export default Task;
                    ```
                    
                - Taskの初期値を追加、一覧表示する
                    
                    ```jsx
                    import React, { useState, useEffect } from "react";
                    import Task from "./component/Task";
                    import { Center, Box, CheckboxGroup, Text } from "@chakra-ui/react";
                    
                    //Appコンポーネント
                    const App = () => {
                    　タスクの初期値を配列として管理する
                    　この配列はタスク名を表すnameプロパティ、そのタスクの完了未完了のisDonde
                    　の2つのオブジェクトを持つ
                      const initialTasks = [
                        {
                          name: "買い物",
                          isDone: true,
                        },
                        {
                          name: "ランニング",
                          isDone: false,
                        },
                        {
                          name: "プログラミングの勉強",
                          isDone: false,
                        },
                      ];
                    
                    	useStateを定義する
                    	扱う変数はtasksとしてトリガーとなる変数はsetTasksとする
                      const [tasks, setTasks] = useState([]);
                    
                    　useEffectを定義する
                      useEffect(() => {
                      　set関数を定義する
                      　引数に配列initialTasksを受け取る
                        setTasks(initialTasks);
                        依存配列は空のため、ページのレンダリング時に一度だけ行われる
                      }, []);
                    
                    　toggleIsDone関数を定義する
                    	引数にはindexを受け取る
                      const toggleIsDone = (index) => {
                    	  変数tasksCopyとしてuseStateの変数を展開して代入する
                        const tasksCopy = [...tasks];
                        変数isDoneを定義する
                        変数tasksCopy
                        const isDone = tasksCopy[index].isDone;
                        tasksCopy[index].isDone = !isDone;
                        setTasks(tasksCopy);
                      };
                    
                      return (
                        <Box mt="64px">
                          <Center>
                            <Box>
                              <Box mb="24px">
                                <Text fontSize="24px" fontWeight="bold">
                                  タスク一覧
                                </Text>
                              </Box>
                              <CheckboxGroup>
                                {tasks.map((task, index) => {
                                  return (
                                    <Task
                                      key={index}
                                      index={index}
                                      name={task.name}
                                      isDone={task.isDone}
                                      toggleIsDone={toggleIsDone}
                                    />
                                  );
                                })}
                              </CheckboxGroup>
                            </Box>
                          </Center>
                        </Box>
                      );
                    };
                    
                    export default App;
                    ```
                    
    - **Railsの通信の流れを解説（MVCモデル）**
        - データの流れ
            - クライアントからURLを介してHTTPメソッドでリクエストが送られてくる
                - 3wayハンドシェイクによって通信を確立して実行する
            - ルーティングがリクエストを受け取る
            - パスとアクションの対応表に従ってコントローラーにアクションを渡す
            - コントローラーで必要な処理が実行され、モデルを介してDBからデータを取得
            - 必要なViewやデータがクライアントに渡される
    - ルーティング
        - **URLとコントローラーとアクション（処理）を結びつける役割**
            - get "members" => "members#index”
        - `config/routes.rb`には**基本的に**下記の情報を記述する必要があります。
            - HTTPメソッド：上記の例では`get`の部分
            - URL（Path）：上記の例では`members`の部分
            - コントローラーとアクション：上記の例では`members#index`の部分
    - コントローラー
        - 特定のURLにアクセスした時に行う処理の内容を管理する場所
            - 具体的な処理を書く場所
        - ファイル名とコントローラー名
        
        　　ファイル名：
        
        　　app/controllers/members_controller
        
        ```ruby
        class MembersController < ApplicationController
          # ここに処理を書いていく
        end
        ```
        
        - ファイル名はスネークケースで記載
        - コントローラー名はキャメルケースで記載
        
        ```ruby
         def index
            members = Member.all
            render json: members
          end
        ```
        
        - membersコントローラーのindexアクションでMemberモデルを全てjson形式で返す
            - 処理の流れ：
                - クライアントからhttp://localhost:3010/membersが送られる
                    - config/routes.rbでmembers（コントローラー）#index（アクション名）で処理されるように設定
            - **`app/controllers/members_controller`のindexアクションで処理がされる**
    - モデル
        - コントローラーからデータの作成・更新・削除の指示を受けてデータベースとやりとりする場所
            - モデルの機能を使って、データベースを操作するロジックを書いたり、モデル同士の関連などを記述します。
    - この本では簡単な説明になるためドキュメントを良いタイミングで読む
        
        https://railsguides.jp/active_record_basics.html
        
        https://railsguides.jp/action_controller_overview.html
        
        https://railsguides.jp/routing.html
        
    - タスク一覧機能を作成する
        - 【Rails】Taskモデルの作成とMigration
            - db/migrate/20210930120855_create_tasks.rb
                - マイグレーションファイル
                    - このファイルにTaskモデルに追加するカラムを書き込む
                    
                    ```ruby
                    class CreateTasks < ActiveRecord::Migration[6.1]
                     def change
                       create_table :tasks do |t|
                         t.string :name
                         t.boolean :is_done
                         t.timestamps
                       end
                     end
                    end
                    ```
                    
                    - name：タスク名
                    - is_done：タスクが完了したかどうか
            - app/models/task.rb
                - モデル情報を管理するファイル
                    - ビジネスロジックやモデル同士のアソシエーションを記載する
            - test/models/task_test.rb
                - テスト関連のファイルです。今回は使用しない
            - test/fixtures/tasks.yml
                - テスト関連のファイルです。今回は使用しない
        - 【Rails】Tasks関連のルーティングを記述
            - ルーティングに設定を記載する事でリクエストの内容に応じた対応をできる
                - getメソッドでhttp://localhost:3010/tasksにアクセス
                    - taskコントローラーのindexアクションが呼び出されるようにする
                - ルーティングファイルに下記を記載
                    - get "tasks" => "tasks#index”
                        - getメソッド
                        - taskコントローラーのindexアクションを渡すルーティング
                - rails routes
                    - ルーティングの設定を確認する事ができる
                - rails routes | grep 条件にする文字列
                    - 条件を絞って確認する事ができる
        - 【Rails】Tasksコントローラーの作成
            - railsコマンドを実行する事でコントローラーが自動で作成される
                - rails g controller tasks
                    - app/controllers/tasks_controller.rb
                        - コントローラーファイル
                            - 具体的な処理を書く
                    - test/controllers/tasks_controller_test.rb
                        - テスト関連のファイル
                            - 今回は使用しない
        - Tasksコントローラーにindexアクションを追加
            - indexアクションを作成する
                - taskの情報を返す処理を記載する
                    - getメソッドでhttp://localhost:3010/tasksをリクエストした際に実行される
                - Tasksコントローラーファイル内でindexアクションを定義
                    
                    ```ruby
                    class TasksController < ApplicationController
                    + def index
                    +   tasks = Task.all
                    +   render json: tasks
                    + end
                    end
                    ```
                    
                    - Task.all
                        - Taskモデルを使って
                        - ApplicationControllerを継承したTasksControllerのallメソッドを呼ぶ
                            - Taskモデルに紐づくテーブル（Tasksテーブル）のデータを取得
                    - render json: tasks
                        - 取得したデータをjson形式で返している
            - rails consoleを使ってTaskデータを作成する
                - Rails consoleは内部的にIRBを使用している
                    - Webサイトにアクセスする事なくサーバーのデータなどを変更できる
        - 【React】Tasksデータを取得する
            - コンソールでコードを実行する
                - Task.create
                - Task.all
            - Axiosを使ってHTTP通信
                - Railsを使った通信は可能になっている
                - Reactを通じてデータの取得を行う
                    - HTTPでAPI通信を行うためのツール
        - Axiosを使ってHTTPでAPI通信を行う
            - AxiosはHTTPでAPI通信を行えるもの
                - React配下のプロジェクトでAxiosをダウンロードする
                特に、今回はRailsのプロジェクトもあるので気をつける
                    - yarn Axios
                - axiosをインポートする
                - その後、fetch関数を定義する
            - 同期的に非同期処理を行う
                - 同期的に処理を実行している処理の中でawaitを使う事で処理を止める事ができ、awaitの処理が終わり次第、次の処理に移行する事などができる
                - useEffectを組み合わせる事でコンポーネントのレンダリング時に同期的に非同期処理を実行する事ができる
            
            ```jsx
            const fetch = async () => {
            async内で
              const res = await axios.get("http://localhost:3010/tasks");
              setTasks(res.data);
            };
            
            useEffect(() => {
              fetch();
            }, []);
            ```
            
            - ServerSide
                - require()
                    - JSのモジュール化
                        - common JS
                            - これをclientSideでも使えるようにしたもの
                                - <script data-main="js/main.js" src="bower_components/requirejs/require.js"></script>
                    - require()は、jsをモジュール化する仕組み
                        - 再利用しやすい
                        - 単体テストがしやすい
                    - Reactと相性がいい
                        - 多数のコンポーネントを作成していくReactと相性がいい
                - webpack
                    - Require.jsをもっとリッチにしたもの
                        - altJSのコンパイル
                        - CSSやHTMLファイル取り込み
                        - （bower経由などの）jsファイル取り込み
                - 機能の違い：
                    - Require.jsは、ブラウザ側で、個々のファイル（モジュール）を非同期に読み込むスタイル。
                    - webpackは、サーバー側で依存関係を全て見て、一つのjsファイルを生成しておくスタイル。
                        - （もちろん、sourceMappingされるので実行時デバッグも問題ない。）
    - タスク作成機能を作成する
        - ルーティング
            - HTTPメソッド
                - post
            - コントローラーとアクションの対応表
                - "tasks" => "tasks#create”
                    - タスクコントローラーのcreteアクション
        
        ```ruby
        class TasksController < ApplicationController
          //indexアクション
          //タスク一覧機能
          def index
            tasks = Task.all
            render json: tasks
          end
        
        	//createアクション
          def create
        	  //Taskモデルを介してApplication recordeを継承したApplicationControllerを
        	  　継承したTasksControllerのcreateメソッドを使って引数をtask_paramsとして
        	  　データを受け取りTasksテーブルにデータを生成している
            Task.create(task_params)
            //ヘッダ部分のみデータを返している
            head :created
          end
          
          private
        
        　//task_paramsアクション(createアクションのcreateメソッドへ渡す値)
          def task_params
        	  //paramsはクライアント(フロント：プレゼンテーション層から受け取ったデータが格納されているもの)
        	  //permit=ストロングパラメーターと呼ばれる
        	  //許可されたデータのみを受け取る事を受け付ける仕組みの事
        	  //nameカラムとis_doneカラムだけを許可している
            params.permit(:name, :is_done)
          end
        end
        ```
        
        - コントローラー
            - creatアクションを定義する
        - View（React）
        
        ```tsx
        import React, { useState, useEffect } from "react";
        import Task from "./component/Task";
        import {
          Flex,
          Center,
          Box,
          CheckboxGroup,
          Text,
          Input,
          Button,
        } from "@chakra-ui/react";
        import axios from "axios";
        
        const App = () => {
        	//useState状態を管理するHook
          const [tasks, setTasks] = useState([]);
          //変数nameをsetName関数で管理
          const [name, setName] = useState("");
        
        　//fetch関数を定義する
        	//asyncとawaitを使う事で非同期処理を実行する
          const fetch = async () => {
        	  //APIから受け取ったデータをresに代入する
            const res = await axios.get("http://localhost:3010/tasks");
            //set関数を定義する
            //APIから受け取った値resのdataプロパティを引数に取って変数nameに代入
            setTasks(res.data);
          };
        
        	//Taskを作成する関数
        	//asyncとawaitで非同期的に処理を行う
          const createTask = async () => {
        	  //axiosを使ってHTTPメソッドをpostとしてTasksテーブルに新しいデータを追加する
            await axios.post("http://localhost:3010/tasks", {
        	    //追加するデータはnameカラムにnameを、is_doneにはfalseを追加する
              name: name,
              is_done: false,
            });
            setName("");
            fetch();
          };
        
          useEffect(() => {
            fetch();
          }, []);
        
          const toggleIsDone = (index) => {
            const tasksCopy = [...tasks];
            const isDone = tasks[index].is_done;
            tasksCopy[index].isDone = !isDone;
            setTasks(tasksCopy);
          };
        
          return (
            <Box mt="64px">
              <Center>
                <Box>
                  <Box mb="24px">
                    <Text fontSize="24px" fontWeight="bold">
                      タスク一覧
                    </Text>
                  </Box>
                  <Flex mb="24px">
                    <Input
                      placeholder="タスク名を入力"
                      value={name}
                      onChange={(e) => setName(e.target.value)}
                    />
                    <Box ml="16px">
        	            //ボタンをクリックしたらcreateTaskが発火するようにする
                      <Button colorScheme="teal" onClick={createTask}>
                        タスクを作成
                      </Button>
                    </Box>
                  </Flex>
                  <CheckboxGroup>
                    {tasks.map((task, index) => {
                      return (
                        <Task
                          key={index}
                          index={index}
                          name={task.name}
                          isDone={task.is_done}
                          toggleIsDone={toggleIsDone}
                        />
                      );
                    })}
                  </CheckboxGroup>
                </Box>
              </Center>
            </Box>
          );
        };
        
        export default App;
        ```
        
    - タスク削除機能を実装する
        - ルーティング
            - delete "tasks/:id" => "tasks#destroy”
            - HTTPメソッド
                - delete
            - パスとアクションの対応表
                - "tasks/:id" => "tasks#destroy”
                    - tasksコントローラーのdestroyアクションを呼び出す
                        - 例：
                            - idが123というTaskの削除
                            - deleteメソッド　`http://localhost:3010/tasks/123`　で削除
        - コントローラー
            - tasksコントローラーのdestroyアクションを定義する
                - destroyアクション
                    - 削除したいタスクを変数taskとする
                        - アプリケーションレコードのfindメソッドを使ってURLのパラーメータからid情報を受け取り代入する
                    - taskの情報が代入された変数に対してtaskモデルを介してdestroyアクションをTasksテーブルに実行する
                    - head :ok
                        - 応答ステータス
                            - :okは成功を返す
                            - コードは200
                
                ```ruby
                def destroy
                   task = Task.find(params[:id])
                   task.destroy
                   head :ok
                 end
                ```
                
        - View（React）
            - Taskコンポーネントに削除機能を実装
                - propsから引数として情報を受け取る
                    - <CloseIcon onClick={() => props.destroyTask(props.id)} />
                        - chakra-uiからインポートしたIcon
                            - propsから受け取ったdestroyTask関数を実行する
                        - また、削除するTaskも特定する必要があるためpropsからIDを受け取る
                            - (props.id)
                
                ```tsx
                import { Checkbox, Flex, Text } from "@chakra-ui/react";
                import { CloseIcon } from "@chakra-ui/icons";
                
                const Task = (props) => {
                  return (
                    <Flex mb="16px" justifyContent="space-between" alignItems="center">
                      <Checkbox
                        isChecked={props.isDone}
                        colorScheme="blue"
                        size="lg"
                        onChange={() => {
                          props.toggleIsDone(props.index);
                        }}
                      >
                        <Text>{props.name}</Text>
                      </Checkbox>
                      <CloseIcon onClick={() => props.destroyTask(props.id)} />
                    </Flex>
                  );
                };
                
                export default Task;
                ```
                
            - Appコンポーネントに紐づける＋dstroy関数を定義する
                - dstroy関数の定義
                    - 引数にidを受け取る
                        - asyncとawitで非同期処理を実行しaxios.deleteの処理が終了したら
                    - `http://localhost:3010/tasks/${id}`
                        - ``シングルクウォーテーションで囲む事で引数に受け取ったidを展開
                    - fetch();を行い
                        - const fetch = async () => {
                        const res = await axios.get("http://localhost:3010/tasks");
                        setTasks(res.data);
                        };
                        - タスクの再取得を行う
                        - set関数を使う事でuseStateを発火させてコンポーネントの再レンダリングをおこす
                - Appコンポーネントの子要素であるTaskコンポーネントにdestroyTaskを紐づけ
                    - destroyTask={destroyTask}
                
                ```tsx
                const destroyTask = async (id) => {
                  await axios.delete(`http://localhost:3010/tasks/${id}`);
                  fetch();
                };
                
                destroyTask={destroyTask}
                ```
                
    - タスク完了機能を実装する
        - タスク完了＝タスクの状態を新しくする
            - UIで更新された状態をupdateして代入する事で状態を保つ
        - ルーティング
            - HTTPメソッド
                - PUT
                    - サーバーにデータを送るため
            - パスとアクションの対応表
                - "tasks/:id" => "tasks#update”
                    - tasksコントローラーのupdateアクション
                        - tasks/1 などのURLが適用される
        - コントローラー
            - updateアクションを定義する
                - Taskモデルのfind関数を使ってレコードを取得する
                    - 特殊な変数paramsを使ってURLからidを受け取る
                - 取得したレコード(変数task)に対してupdataメソッドを実行する
                    - 引数には下で定義しているtask_paramsを取る
                - そこからnameは変わらず、is_doneが更新された値を受け取る
            
            ```ruby
            def update
               task = Task.find(params[:id])
               task.update(task_params)
               head :ok
             end
            ```
            
        - View（React）
            - toggleIsDone関数を定義する
                - asyncとawaitで非同期処理を実行する
                    - 引数にはidとindexを渡す
                - 変数isDoneを定義する
                    - 配列tasksに引数から受け取ったindexを使って該当するtaskのis_doneプロパティを代入する
                - awaitとしてaxiosでHTTP通信を非同期的に行う
                    - is_done: !isDone
                        - is_doneプロパティにisDoneを!反転させたものを代入する
                - fetch関数を実行して状態を最新状態に保つ
                    - 非同期処理で変数resにaxiosでHTTP通信をHTTPメソッドがgetで行う
                    - set関数を発火し引数に変数resのdataプロパティを渡す事で最新状態に更新する
                    
                    ```tsx
                    const fetch = async () => {
                        const res = await axios.get("http://localhost:3010/tasks");
                        setTasks(res.data);
                      };
                    ```
                    
            
            ```tsx
            const toggleIsDone = async (id, index) => {
                const isDone = tasks[index].is_done;
                await axios.put(`http://localhost:3010/tasks/${id}`, {
                  is_done: !isDone,
                });
                fetch();
              };
            ```
            
- エラー集
    
    [Taskコンポーネントが表示されない](https://www.notion.so/Task-1a8972e6c96080ab8a43d409166d7d48?pvs=21)
    
    [useEffectを使う時に起きうるエラー](https://www.notion.so/useEffect-1ab972e6c96080918ffaff964ccda7f9?pvs=21)
    
    [エラー解決](https://www.notion.so/1ad972e6c9608066881ee40df7ed3c38?pvs=21)
    
- 追加で実装する機能
    - システムにおいて機能を作成する時などには概念整理が重要になる
        - 例：Todoアプリ
            - すでにある機能
                - チェックボックス
                    - 未 or 完了
                - タスクの作成
                - タスクの削除
            - Todoアプリの概念を整理する
                - チェックボックスと削除の違い
                    - チェックボックスでの完了と削除の違い
                        - 削除のみで良くないのか？
                        - 完了があるのはなんで？
                        - 間違えて削除する事ないか？
                            - ゴミ箱機能必要？
                                - 一度、消したものを復元できる
                        - 現在実行中のタスクと次やるタスクなどなど
                - 作成と削除がある場合には削除→作成で新しくする事ができる
                タスク名の編集という機能はいるのか？
                    - ステータスの更新と編集機能は何が違うか？
                    - タスク名の編集だけでいいのか？
                - https://note.com/naro143/n/n31d2b7f97a16
    - タスク内容の編集機能を実装する
        - 要件→ユースケースを決める
            - すでに作成したタスクを編集してタスク名を変更できるようにする
                
                ユースケース（概念整理）：
                
                - ユーザー体験　UI・UX
                    - 編集ボタンを押してテキストがinputに変わる
                        - ボタンが保存に変わる
            - すでに作成したタスクを編集する事ができる
                - 抽象的すぎる
                    - 既存のタスクサービスを触ってどのようなUI・UXにしたいか考える
            - 編集ボタンで編集ページに飛ぶ
                - ページ遷都の手間がかかる
                    - だったら削除してから新規作成でいい
            - 編集ボタンを押すとModuleが出てくる
                - これも同様にページの遷都の手間が出てくる
        - 開発において
            - ただ、作るだけであれば受託開発に行った方がいい
            - 自社サービス開発に行くのであれば思考回路があった方がいい
            - サービスの修正、作成には概念整理が重要
            - 機能が多いことがいいわけではない
                - 認知量がちょうど良くないといけない
        - 処理
            - バックエンド
                - ルーティング
                    - put "tasks/edit/:id" => "tasks#edit”
                        - 対象となるリソース（nameプロパティ）
                        - PUTメソッド
                            - 対象リソースの現在の表現全体を、リクエストのリソースで置き換える
                            - また、冪等性のあるリクエストのため複数回のリクエスト（ボタンの連打）があっても毎回同じものが入るようにする
                - コントローラー
                    - editアクション
                        - ローカル変数のTask
                            - findメソッドを使って編集したいTaskテーブルのレコードを取得する
                                - 特殊な変数paramsを使ってidを引数にとる
                                    - findメソッドで取得したレコードを変数Taskに代入する
                        - task.update(task_params)
                            - taskモデルのアップデートメソッドを使う
                                - 引数にtask_paramsを渡す
                                    - privateメソッドの中に定義したtask_params
                                    
                                    ```
                                    def task_params
                                       params.permit(:name, :is_done)
                                    end
                                    ```
                                    
                        - ステータスコード
                            - head ok で 200を返す
            - フロントエンド（React）
                - View（React）
                    - フロントでの状態
                        - 編集前
                        - 編集中
                            - 編集後にfalshメッセージはない
                    - ユーザー行動
                        - 編集ボタンを押してタスク名の編集をして保存ボタンを押す
                    - 処理
                        - 編集ボタンがクリックされるとクリックイベントが発生する
                            - タスクコンポーネントのタスク名を表示している部分がinputタグに変わる。初期値として編集前のタスク名が入る
                                - タスク名の部分は
                                    - 編集前なのか、編集中なのかで変わる
                                        - 編集中＝true
                                            - inputタグ
                                        - 編集前＝false
                                            - textタグ
                                - 状態の定義、管理
                                    - useStateで管理する
                                        - 編集しているか？
                                            - isEdite,setEdite
                                                - const [isEdite,setEdite] =useState(false)
                    - 表示条件
                        - 三項演算子を使って条件に応じたコンポーネントを表示
                            - 編集前
                                - !isEditeがtrueの場合
                                    - 編集ボタンが表示される
                            - 編集中
                                - !isEditeがfalseの場合
                                    - 編集中には保存ボタンとキャンセルボタンを表示する
                        - それぞれのボタンに状態を紐づける
                            - 条件に応じて表示を切り変える→思考が飛んだ
                                - 編集ボタン
                                - 保存ボタン
                                - キャンセルボタン
                                    - イベントハンドラー
                                        - クリックしたら〜をコンソールに表示
                        - 状態を定義する
                            - 変数を定義して
                            - useStateで状態を管理する
                                - 持たせる値はtrue or false
                            - 変数isEdit　管理する関数 setEdit
                                - useState　初期値はfalse(編集前にする)
                                    - useStateは状態変数と状態を管理する関数
                                        - 状態を管理する変数は状態変数にsetをつける
                        - イベントハンドラーの中身を関数に切り出す
                        - onClick時に状態が変化する
                            - イベントハンドラー内で状態の更新を行う
                            
                            ```tsx
                            {!isEdite ? <text>{props.name}</text>
                             :
                             <>
                              <input value={name} onChange={(e) => console.log(e.target.value)}/>
                              <button onClick={(console.log(キャンセルをクリックした))}>キャンセル</button>
                             </>
                             }
                            
                            ```
                            
                        - ボタン表示
                            - 編集ボタン
                            - 保存ボタン
                            - キャンセルボタン
                        - クリックイベント
                            - 編集中or編集前のどちらかに切り替える
                                - 編集ボタン
                                    - 編集中の状態に変える
                                        - 編集ボタンは保存ボタンに変わる
                                            - false　＝＞　true
                                    - 編集前　＝＞　編集中
                                        - isEditを反転させると前の状態が違う場合には状態が変化しない
                                            - true　＝＞　false
                                - 保存ボタン
                                    - 編集前の状態に変える
                                        - 編集中　＝＞　編集前
                                            - true　＝＞　false
                                    - APIを叩いて値を更新する
                                        - ユーザーが編集したタスク名が更新される
                                            - useStateで新しい変数editNameを定義する
                                                - onChange関数で更新されたinputの中のユーザーの入力値
                                            - editNameを変える事ができるようにする
                                - キャンセルボタン
                                    - 編集前の状態に戻す
                                        - 編集中　＝＞　編集前
                                            - true　＝＞　false
                        - 保存ボタンを押した時にAPIを叩けくようにする
                            - 保存ボタンを押した際にクリックイベントが発生する
                                - クリックイベントの内容
                                    - 状態の遷都
                                        - 編集中　＝＞　編集前
                                            - true　＝＞　false
                                    - axiosを使って非同期的にHTTP通信を行なってリソースを更新する
                                        - HTTPメソッド
                                            - put
                                        - 渡す値（第２引数）
                                            - nameカラムに新しい変数のeditNameを入れる
                                    - 新しく代入された値を反映したコンポーネントを表示する
                                        - 再レンダリングが起きるようにする
                                    - popsとして渡されているApp.jsxのfetch関数を使う
                                    - APIのリクエストにidを渡す必要があるためonClick関数にidを引数として渡す
                            - タスク名の編集機能の実装完了
                                - 問題発生
                                    - キャンセルボタンを押した際にタスク名が反映されない
                                        - 前の編集内容が保存されてしまう
                                            - onChangeで常に更新している
                                        - キャンセルボタン
                                            - クリックイベントが発生して状態の遷都
                                        - 変数の管理
                                            - タスク名の値をset関数で更新する
                                                - setEditName([props.name](http://props.name/))
        - 切り出した流れ
            - ボタンを表示する
                - イベントハンドラーにクリックしたら~と表示がでるようにする
                - イベントハンドラーの処理内容をそれぞれ関数に切り出す
            - 状態を定義する
                - ボタンに状態を定義する
            - 状態に応じて表示を切り替える
                - ボタンのクリックイベントに応じて状態を変更する
            - ユーザーの入力内容に応じて状態が更新されるようにonChange関数を定義する
        - 開発の処理の順番がわからなかった理由
            - いきなり4個目を目指していた
                - だから、ボタンが表示できなかったり
                - 条件の定義できなかったり
                    - もっと、言語化、要件定義する
                    - 状態の把握と状態の遷移を把握する