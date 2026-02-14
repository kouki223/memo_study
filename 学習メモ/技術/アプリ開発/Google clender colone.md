https://zenn.dev/prune/books/32a2fd62831c7f/viewer/2969b9
- 進捗管理
    1. 【Rails×React】本格的なGoogleカレンダークローンアプリをSPAで開発してみよう！
    2. 【Rails】Ruby・Rails関連パッケージのインストール
    3. 【React】React関連パッケージのインストール
    4. 【Rails】APIモードで環境構築
    5. 【React】Reactの新規プロジェクトを作成
    6. 【Rails】RailsAPIの基礎
    7. 【React】Reactの基礎とJSX
    8. 【Rails】devise_token_authを使ったログイン・ユーザー登録機能の開発 
    9. 【React】Chakra UIのインストール
    10. 【React】ログイン・ユーザー登録機能の開発
    11. 【Rails】カレンダー予定を管理するAPIを実装
    12. 【Rails】カレンダー予定「一覧」APIを実装
    13. 【Rails】カレンダー予定「作成」APIを実装
    14. 【Rails】カレンダー予定「更新」APIを実装
    15. 【React】カレンダー機能を実装
    16. さいごに
- グーグルカレンダークローンアプリ
    - 概念・ユースケース
        - ユーザー（利用者）の概念
            - ユーザー登録機能
            - ログイン機能
                - バックエンドの機能には認証・認可周りなどユーザーの管理ができる事が求められる
        - カレンダー機能
            - 日付
            - 予定を可視化して表示する
                - FE
                    - 状態管理をする事ができるもの
                        - ユーザー行動に応じてUIを更新していく
                - Backend
                    - FrontからのリクエストをAPIという形で受け取りサーバーとのやりとりをする
        - 予定
            - 予定の作成
                - FrontからBackendへリクエストを送る
                    - Backendはサーバーの操作を行う
            - 予定内容の編集
                - FrontからBackendへupdateのためにAPIリクエストを送る
        - 特定のユーザーに紐づいたカレンダー機能、それに合わせて予定管理ができるアプリ
            - ログイン画面からログイン後
            - ログイン後の画面
                - カレンダー
                - 予定の管理
                    - 予定の作成
                    - 予定の変数
                        - 予定部分を触ったら編集できるように
- システム構成（技術スタック）
    - front
        - React
            - ネットワークアプリケーション
                - **Node.js**
            - パッケージ管理
                - npm
                - yarn
            - バージョン管理
                - **Homebrew**
    - Backend
        - Ruby on Rails —APIモード
            - 認証・認可周り
                - **devise_token_auth**
        - Webサーバー
            - puma
        - DB
            - ローカル環境　＝＞　sqlite3
            - 本番環境　＝＞　mysql2
                - Rails
                - devise
- ユーザー登録、ログイン機能の実装
    - 認証機能
        - front
            - HTTP通信（APIを叩く）
                - axis
                    - ログイン機能
                        - const options = {ignoreHeaders: true,};
                            - ヘッダーに関してはケバブケースのままで良いので適用を無視するオプションを追加
                        - const client = axios.create({baseURL: process.env.REACT_APP_API_DOMEIN,}),options);
                            - Rubyではスネークケースで記載されているものもケバブケースで記載するようにする
                        - client
                            - API(Rails)を叩く
                                - baseURLに環境変数の設定
                                    - https://zenn.dev/kachuno/articles/4b2e6d8e1a944f
                                    - 練習環境で使いたいベースエンドポイントと本番環境でのベースエンドポイントを環境変数によって設定する事ができる
                                        - 開発環境ではlocal:host
                                        - 本番環境では[http://xxxx](http://xxxx/)というような形にする
                                            - 環境毎に分けた.envファイルを作成する
                                - baseURLを設定する事で相対パスでルーティングを指定する事ができる
                                
                                ```ruby
                                .envの空ファイルを生成する
                                $ touch .env
                                
                                Rails APIのドメインを設定する
                                $ REACT_APP_API_DOMEIN=http://localhost:3010
                                ```
                                
                    - axiosで定義したclientを使ってログイン周りのコードを記述する
                        
                        ```jsx
                        import Cookies from "js-cookie";
                        import client from "./client";
                        
                        export const signUp = (params) => {
                          return client.post("auth", params);
                        };
                        export const signIn = (params) => {
                          return client.post("auth/sign_in", params);
                        };
                        export const getUser = () => {
                          if (
                            !Cookies.get("_access_token") ||
                            !Cookies.get("_client") ||
                            !Cookies.get("_uid")
                          )
                            return;
                          return client.get("/auth/sessions", {
                            headers: {
                              "access-token": Cookies.get("_access_token"),
                              client: Cookies.get("_client"),
                              uid: Cookies.get("_uid"),
                            },
                          });
                        };
                        ```
                        
                        - ユーザ登録とログインのAPIを叩く
                            - client.httpメソッド（path, params）
                                - ユーザ登録の場合
                                    - HTTPメソッド
                                        - post
                                    - path
                                        - auth
                                    - APIに渡す情報(params)
                                        - メールアドレス
                                        - パスワード
                                - client.post("auth", params)
                            - ログインの場合
                                - HTTPメソッド
                                    - post
                                - path
                                    - auth/sign_up
                                - APIに渡す情報(params)
                                    - メールアドレス
                                    - パスワード
                                - client.post("auth/sign_in", params);
                        - ログイン中のユーザを取得するAPIを叩く
                            
                            export const getUser = () => {
                              if (
                                !Cookies.get("_access_token") ||
                                !Cookies.get("_client") ||
                                !Cookies.get("_uid")
                              )
                                return;
                            
                            - Cookies情報がが正しくない場合(ログインしていない場合)にはreturn
                            
                            return client.get("/auth/sessions", {
                                headers: {
                                  "access-token": Cookies.get("_access_token"),
                                  client: Cookies.get("_client"),
                                  uid: Cookies.get("_uid"),
                                },
                              });
                            };
                            
                            - ログインしている場合にはユーザー情報を返す
                                - 第２引数にはheader情報にCookie情報を渡す
                - js-cookie
                    - cookieを操作するためのもの
            - ルーティング用のライブラリ
                - react-router-dom
                    
                    **URLとコンポーネントを紐付ける事ができるライブラリ**
                    
                    - `BrowserRouter`をimport
                        - Appコンポーネントをラップする
                    - ルーティングを設定する
                        - BrowserRouterでルーティングを設定する方法
                    
                    **設定したいルーティング**
                    
                    - `/`：トップ画面
                        - Top画面はパスの指定なく遷都する
                    - `/calendar`：カレンダー画面
                    - `signUp`：ユーザー登録
                    
                    **TOP画面にリンクを設置する**
                    
                    - react-router-domからLinkコンポーネントをインポートする
                        - <Link to="/signUp">登録画面</Link>
                            - Appコンポーネントの中にLinkコンポーネントを入れる
                    
                    **index.jsでルーティングの設定を記載する**
                    
                    - RoutesでRouteをラップする
                        - RouteにはPathとPathに対応するコンポーネントを指定する
                    
                    ```jsx
                    Top画面の場合
                    ↓
                    <Route index element={<App />} />
                    
                    SignUp画面の場合
                    ↓
                    <Routes>
                    	<Route path="signUp" element={<SignUp />} />
                    </Routes>
                    ```
                    
            - UI
                - スタイリングはChakra UIを使う
                    - ChakraUIは要素に対して直接的にスタイルを指定する事ができる
                        - <Image w="400px" src="calendar.png" />
                    - ChakraUIからインポートしたコンポーネント
                        - Box
                            - Chakra UI で最も抽象的なスタイル設定コンポーネント
                            - ショートハンド
                                - backgroundColor の代わりに bg
                                - margin の代わりに m
                        - Flex
                            - フレックスレイアウトのためのコンポーネント
                                - 方向を変更する
                                    - direction
                                    - flexDirection プロパティを使用する
                                    
                                    ![image.png](attachment:42adae0e-88cd-4c30-b8bf-eb7e61eee1d3:image.png)
                                    
                                - 子要素のスタイル
                                    - align
                                    - alignItems プロパティを使用する
                                        - 交差軸に沿って配置します。
                                    
                                    ![image.png](attachment:8de1d61a-aac8-4245-9670-56c3edfbe981:image.png)
                                    
                                    - justify
                                    - justifyContent プロパティを使用する
                                        - 主軸に沿って揃えます。
                                    
                                    ![スクリーンショット 2025-03-12 18.34.31.png](attachment:7c33be05-59a0-44c7-8dcc-e1036d32a236:スクリーンショット_2025-03-12_18.34.31.png)
                                    
                                - orderプロパティ
                                    - 子要素の順番を帰る
                                - Auto Margin
                                    - Flex要素にmarjinを適用する
                                
                                ![image.png](attachment:6bf5b2e7-2851-4c18-aefc-89f7836f11f5:image.png)
                                
                                - Wrap
                                    - 子要素が親要素からオーバーフローしたときに、 wrap または flexWrap プロパティを使用して子要素をラップする
                                    
                                    ![image.png](attachment:9b3f980b-7077-4205-b8c6-db46f369ace9:image.png)
                                    
                        - Image
                            - Heightプロパティ
                                - 高さの調整
                            - Circularプロパティ
                                - 画像を円形にして表示
                            - Aspect Ratioプロパティ
                                - アスペクト比を調節する
                            - Fitプロパティ
                                - コンポーネントフィットするように調節
                            - HTML Width and Height
                                - HTMLの高さと幅を調節する
                        - Text
                        - Input
                            - Variantsプロパティ
                                - inputタグの見た目を変化させる
                            - sizeプロパティ
                            - Helper Text
                                
                                ```jsx
                                import { Field, Input } from "@chakra-ui/react"
                                
                                const Demo = () => {
                                  return (
                                    <Field.Root required>
                                      <Field.Label>
                                        Email <Field.RequiredIndicator />
                                      </Field.Label>
                                      <Input placeholder="Enter your email" />
                                      <Field.HelperText>We'll never share your email.</Field.HelperText>
                                    </Field.Root>
                                  )
                                ```
                                
                                ![image.png](attachment:26492573-b644-4dfc-a8d0-cad2de42204e:image.png)
                                
                        - Button
                        - Link as CLink
                    
                    ```jsx
                    import { Link } from "react-router-dom";
                    import {
                      Box,
                      Flex,
                      Image,
                      Text,
                      Input,
                      Button,
                      Link as CLink,
                    } from "@chakra-ui/react";
                    
                    const App = () => {
                      return (
                        <Flex h={"100vh"}>
                          {/* 画像 */}
                          <Flex
                            w="50%"
                            justifyContent="center"
                            alignItems="center"
                            flexDirection="column"
                          >
                            <Image w="400px" src="calendar.png" />
                            <Text fontSize="32px" color="blue.500" fontWeight="bold">
                              Googleカレンダークローンアプリ
                            </Text>
                          </Flex>
                          {/* フォーム */}
                          <Flex
                            w="50%"
                            justifyContent="center"
                            alignItems="center"
                            flexDirection="column"
                          >
                            <Box w="400px">
                              <Text fontSize="24px" color="gray.700" fontWeight="bold" mb="24px">
                                ログインページ
                              </Text>
                              //Input要素でメールアドレス、パスワードの要求をする
                              <Input placeholder="メールアドレス" mb="16px" />
                              <Input placeholder="パスワード" mb="16px" />
                              <Button w="400px" colorScheme="blue" mb="8px">
                                ログインする
                              </Button>
                              <Box textAlign="right">
                                <CLink color="blue.500">
                                  <Link to="/signUp">ユーザー登録はこちら</Link>
                                </CLink>
                              </Box>
                            </Box>
                          </Flex>
                        </Flex>
                      );
                    };
                    
                    export default App;
                    ```
                    
                    - Input要素でメールアドレスとパスワードを入力するfieldを用意する
                - App.jsにclietとaxiosで定義したログイン機能を紐つける
                    
                    ```jsx
                    import { Link } from "react-router-dom";
                    import { useState } from "react";
                    import {
                      Box,
                      Flex,
                      Image,
                      Text,
                      Input,
                      Button,
                      Link as CLink,
                    } from "@chakra-ui/react";
                    import { signIn } from "./lib/api/auth.js";
                    
                    const App = () => {
                      const [email, setEmail] = useState("");
                      const [password, setPassword] = useState("");
                      const navigate = useNavigate();
                    
                      const login = async () => {
                        try {
                          const res = await signIn({ email, password });
                          Cookies.set("_access_token", res.headers["access-token"]);
                          Cookies.set("_client", res.headers["client"]);
                          Cookies.set("_uid", res.headers["uid"]);
                          navigate("calendar");
                        } catch (e) {
                          console.log(e);
                        }
                      };
                    
                      return (
                        <Flex h={"100vh"}>
                          {/* 画像 */}
                          <Flex
                            w="50%"
                            justifyContent="center"
                            alignItems="center"
                            flexDirection="column"
                          >
                            <Image w="400px" src="calendar.png" />
                            <Text fontSize="32px" color="blue.500" fontWeight="bold">
                              Googleカレンダークローンアプリ
                            </Text>
                          </Flex>
                          {/* フォーム */}
                          <Flex
                            w="50%"
                            justifyContent="center"
                            alignItems="center"
                            flexDirection="column"
                          >
                            <Box w="400px">
                              <Text fontSize="24px" color="gray.700" fontWeight="bold" mb="24px">
                                ログインページ
                              </Text>
                              <Input
                                placeholder="メールアドレス"
                                mb="16px"
                                value={email}
                                onChange={(event) => setEmail(event.target.value)}
                              />
                              <Input
                                placeholder="パスワード"
                                mb="16px"
                                value={password}
                                onChange={(event) => setPassword(event.target.value)}
                              />
                              <Button w="400px" colorScheme="blue" mb="8px" onClick={login}>
                                ログインする
                              </Button>
                              <Box textAlign="right">
                                <CLink color="blue.500">
                                  <Link to="/signUp">ユーザー登録はこちら</Link>
                                </CLink>
                              </Box>
                            </Box>
                          </Flex>
                        </Flex>
                      );
                    };
                    
                    export default App;
                    ```
                    
                    - 追記部分
                        - useStateを定義する
                            
                            const [email, setEmail] = useState("");
                            const [password, setPassword] = useState("");
                            
                            - emailとpasswordをstate変数として定義する
                        
                        ```jsx
                        const login = async () => {
                        	try {
                        	  const res = await signIn({ email, password });
                        	  Cookies.set("_access_token", res.headers["access-token"]);
                        	  Cookies.set("_client", res.headers["client"]);
                        	  Cookies.set("_uid", res.headers["uid"]);
                        	  navigate("calendar");
                        	} catch (e) {
                        	  console.log(e);
                        	}
                        };
                        ```
                        
                        - login関数を定義する
                            - 非同期処理でsignIn関数を発火させてemail,passwordを渡す
                            - 帰ってきたtokenにAPIから取得した情報を渡す
                            - navigate関数でcalendarへ移行する
                            - https://api.reactrouter.com/v7/functions/react_router.useNavigate.html
                        - Input要素
                            - onChange関数を使ってそれぞれの値をuseStateで更新する
                                - Button要素にはlogin関数を紐つける
                - カレンダー画面（ログイン後の画面）src/routes/Calendar.jsx
                    
                    ```jsx
                    import { Link } from "react-router-dom";
                    
                    const Calendar = () => {
                      return (
                        <div>
                          <p>カレンダーページ</p>
                          <Link to="/">ホーム画面に戻る</Link>
                        </div>
                      );
                    };
                    
                    export default Calendar;
                    ```
                    
                - App画面（初期画面）でログイン済みの場合にはカレンダー画面に遷都させる
                    - useEffetを使って実装する
                        - 非同期処理でgetUserを発火させる
                    - if文
                        - res.data.isLogin
                            - getUserでユーザー情報が取得できた場合にはnavigate関数を使ってcalender画面に遷都する
                        - eventをchtchする
                    - クリーンアップ関数のf()を記載する
                        - **「第1引数の関数の戻り値にはクリーンアップ関数を設定する必要がある非同期関数をそのまま書くとエラーが起きてしまう」**
                        - https://zenn.dev/syu/articles/b97fb155137d1f
                            - 第一引数に非同期処理を記載してしまうとエラーが起きてしまう
                                - Promise型となってしまうため
                            - エラーにならない方法
                                - 関数内で実行する方法
                                - 定数を定義して実行する方法
                                    - どちらもクリーンアップ関数を記載する事でエラーにならずに記載する事ができる
                    
                    ```jsx
                    useEffect(() => {
                      const f = async () => {
                        try {
                          const res = await getUser();
                    if (res.data.isLogin) {
                            navigate("calendar");
                          }
                        } catch (e) {
                          console.log(e);
                        }
                      };
                      f();
                    }, [navigate]);
                    ```
                    
                - SIgnUpコンポーネント
                    - App.jsと似た構造になる
                        - ユーザ登録の機能(register)ではSIgnInではなくsignInを使用している
                    
                    ```jsx
                    import { Link, useNavigate } from "react-router-dom";
                    import { useState } from "react";
                    import {
                      Box,
                      Flex,
                      Image,
                      Text,
                      Input,
                      Button,
                      Link as CLink,
                    } from "@chakra-ui/react";
                    import { signUp } from "../lib/api/auth.js";
                    import Cookies from "js-cookie";
                    
                    const SignUp = () => {
                      const [email, setEmail] = useState("");
                      const [password, setPassword] = useState("");
                      const navigate = useNavigate();
                    
                      const register = async () => {
                        try {
                          const res = await signUp({ email, password });
                          Cookies.set("_access_token", res.headers["access-token"]);
                          Cookies.set("_client", res.headers["client"]);
                          Cookies.set("_uid", res.headers["uid"]);
                          navigate("/calendar");
                        } catch (e) {
                          console.log(e);
                        }
                      };
                    
                      return (
                        <Flex h={"100vh"}>
                          {/* 画像 */}
                          <Flex
                            w="50%"
                            justifyContent="center"
                            alignItems="center"
                            flexDirection="column"
                          >
                            <Image w="400px" src="calendar.png" />
                            <Text fontSize="32px" color="blue.500" fontWeight="bold">
                              Googleカレンダークローンアプリ
                            </Text>
                          </Flex>
                          {/* フォーム */}
                          <Flex
                            w="50%"
                            justifyContent="center"
                            alignItems="center"
                            flexDirection="column"
                          >
                            <Box w="400px">
                              <Text fontSize="24px" color="gray.700" fontWeight="bold" mb="24px">
                                ユーザー登録ページ
                              </Text>
                              <Input
                                placeholder="メールアドレス"
                                mb="16px"
                                value={email}
                                onChange={(event) => setEmail(event.target.value)}
                              />
                              <Input
                                placeholder="パスワード"
                                mb="16px"
                                value={password}
                                onChange={(event) => setPassword(event.target.value)}
                              />
                              <Button w="400px" colorScheme="blue" mb="8px" onClick={register}>
                                登録する
                              </Button>
                              <Box textAlign="right">
                                <CLink color="blue.500">
                                  <Link to="/">ログインはこちら</Link>
                                </CLink>
                              </Box>
                            </Box>
                          </Flex>
                        </Flex>
                      );
                    };
                    
                    export default SignUp;
                    ```
                    
        - BE(Rails)
            - deviseの初期設定(認証)
                - Gemfilm
                    
                    gem 'devise'
                    gem 'devise_token_auth'
                    
                    - Gemファイルに記載する事で必要なライブラリをインストールする
                - ターミナル
                    
                    $ bundle install
                    
                    - ライブラリ等のインストール
                    
                    $ rails g devise:install
                    
                    - devaise初期設定に必要なディレクトリやファイルが生成される
                    
                    $ rails g devise_token_auth:install User auth
                    
                    - devise_token_auth初期設定に必要なディレクトリやファイルが生成される
                    - Userモデルの生成
                    
                    $ rails db:migrate
                    
                    - データベースの生成
                - config/initializers/devise_token_auth.rb
                    
                    config.headers_names = {
                    :'authorization' => 'Authorization',
                    :'access-token' => 'access-token',
                    :'client' => 'client',
                    :'expiry' => 'expiry',
                    :'uid' => 'uid',
                    :'token-type' => 'token-type'
                    }
                    
                    ↑
                    
                    コメントアウトされている
                    
                    コメントアウトを外す事で適用する
                    
                    - 認証用のヘッダーの名前を定義している
                    
                    config.change_headers_on_each_request = false
                    
                    - falseにする事でアクセス毎にトークンの更新が起きないようにする
                        - 今回はローカルのみの開発なのでfalseにしておく
                    - trueの場合にはアクセス毎にトークンのチェックが必要になるため認証が働く
                - config/initializers/cors.rb
                    
                    Rails.application.config.middleware.insert_before 0, Rack::Cors do
                    allow do
                    origins '[http://localhost:3000](http://localhost:3000/)'
                    
                    resource '*',
                    headers: :any,
                    expose: ["access-token", "expiry", "token-type", "uid", "client"],
                    methods: [:get, :post, :put, :patch, :delete, :options, :head],
                    credentials: true
                    end
                    end
                    
                    - 設定したヘッダー情報をレスポンスに含める
                - ターミナル
                    
                    $ rails g controller auth/registrations
                    $ rails g controller auth/sessions
                    
                    - コントローラーの生成
                        - registrationsコントローラー
                        - sessionsコントローラー
                - app/controllers/auth/registrations_controller.rb
                    
                    class Auth::RegistrationsController < DeviseTokenAuth::RegistrationsController
                    
                    private
                    
                    def sign_up_params
                    
                    params.permit(:email, :password, :password_confirmation, :name)
                    
                    end
                    
                    end
                    
                    - ユーザ作成用のコントローラー設定
                        - DeviseTokenAuth::RegistrationsControllerを継承している
                            - devise側で設定されているDeviseTokenAuthを継承してsign_up_paramsの処理を変更する事ができるようになる
                - app/controllers/auth/sessions_controller.rb
                    
                    class Auth::SessionsController < ApplicationController
                    
                    def index
                    
                    if current_user
                    
                    render json: { is_login: true, data: current_user }
                    
                    else
                    
                    render json: { is_login: false, message: "ユーザーは存在しません" }
                    
                    end
                    
                    end
                    
                    end
                    
                    - ログインの状態を管理するコントローラー
                        - current_userはdeviseが提供しているメソッド
                            - ログインしているユーザーがいる場合にはユーザー情報を返して、ログインしない場合にはユーザーは存在しませんと返す
                - app/controllers/application_controller.rb
                    
                    class ApplicationController < ActionController::Base
                    
                    include DeviseTokenAuth::Concerns::SetUserByToken
                    
                    skip_before_action :verify_authenticity_token
                    
                    end
                    
                    - ユーザーがログインしているかどうかを確認するメソッドであるuser_signed_in?を使うためにinclude
                    - token検証をスキップする
                - config/application.rb
                    
                    config.session_store :cookie_store, key: '_session'
                    config.middleware.use ActionDispatch::Cookies
                    config.middleware.use config.session_store, config.session_options
                    
                    - cookieの設定
                - config/routes.rb
                    
                    Rails.application.routes.draw do
                    
                    mount_devise_token_auth_for 'User', at: 'auth', controllers: {
                    
                    registrations: 'auth/registrations'
                    
                    }
                    
                    namespace :auth do
                    
                    resources :sessions, only: %i[index]
                    
                    end
                    
                    end
                    
                    - mount_devise_token_auth_forによって認証に必要なルーティングをマウントしている
                    - ログイン中のユーザを返すエンドポイントとしてauth/sessionsを定義する
    
- カレンダー予定を管理するAPI
    - 要件定義
        - ユーザー情報に紐づいた予定
            - 予定の要素
                - title：予定の内容
                - description: 予定の詳細
                - start_date：予定開始日付
                - end_date：予定終了日付
    - 必要な機能を実装する
        - BE
            - railsコマンドを使って作成
                - rails g model CalendarEvent
            - 追加するモデル
                - CalendarEventモデル
            - DB
                - テーブル
                    - CalendarEventsテーブル
                        - migrate fileを作って生成する
                    - create_calendar_events.rb
                        - カラム構成
                            - stringタスク名＝＞title
                            - stringタスク内容＝＞description
                            - stringタスク開始＝＞start_date
                            - stringタスク終了＝＞end_date
                            - 外部キー制約
                                - references型
                                - indexは自動で付与される
                                - :user, foreign_key: true
                                    - reference型で外部キー制約をつける場合には対象にするテーブルの単数型,foreign_key: trueにする
                                        - 自動で外部キーとなるカラムが生成される
                                            - user_id
                    
                    ```ruby
                    class CreateCalendarEvents < ActiveRecord::Migration[7.0]
                      def change
                        create_table :calendar_events do |t|
                          t.string     :title
                          t.string     :description
                          t.string     :start_date
                          t.string     :end_date
                          //外部キー制約
                          t.references :user, foreign_key: true
                          t.timestamps
                        end
                      end
                    end
                    ```
                    
                    ![image.png](attachment:679cefb9-53a2-4801-a568-418e1254ba07:image.png)
                    
                    - rails db:migrate
                - モデル
                    - CalendarEventモデル
                        - calendar_event.rb
                            - モデル情報を管理するファイル
                                - ビジネスロジック
                                - モデル同士のアソシエーション
                                    - 等を記載する
                        - belongs_to :userを記載
                            - Userと紐付ける
                                - 宣言を行ったモデルが指定したモデルに従属する
                                    - calendar_eventがuserに従属する形になる
                                        
                                        ↑
                                        
                                        モデル名は単数にする
                                        
                    - Userモデル
                        - has_one :calendar_events
                            - has_one
                                - 相手側のモデルが参照元(自分のモデルへの参照を持っている事を示す)
                                    
                                    ↑
                                    
                                    has_oneやhas_manyを記載する時には複数系で記載する事に注意する
                                    
                    - 関連づけを指定する事でコードの記述をシンプルにする事ができる
            - ルーティング
                - アクセスされたリクエスト（エンドポイント）とコントローラーを設定する
                    - リクエストとコントローラーを結びつける
                - エンドポイント
                    - 予定一覧：getメソッド
                        - http://localhost:3010/calendar_events
                    - 予定作成：postメソッド
                        - http://localhost:3010/calendar_events
                    - 予定更新：putメソッド
                        - [http://localhost:3010/calendar_events/[id]](http://localhost:3010/calendar_events/%5Bid%5D)
                - config/routes.rb
                    - get '/calendar_events', to: 'calendar_events#index’
                    - post '/calendar_events', to: 'calendar_events#create’
                    - put '/calendar_events/:id', to: 'calendar_events#update’
                        
                        ↑
                        
                        Rails 8.0では
                        
                        エンドポイント, to: ‘コントローラー#アクション’になる
                        
            - コントローラー
                - railsコマンドを使ってファイル生成する
                    - rails g controller calendar_events
                        - calendar_events_controller.rb
                            - コントローラーファイルが生成される
                - 予定一覧のAPI　＝＞　indexアクション
                    - before_action
                        - deviceの提供しているメソッド
                            - 認証機能の実装
                    - indexアクションを定義する
                        - current_user.idはdeviseに提供されているメソッド
                            - ログインしているユーザー情報を返す
                            - user_idに対してログインしているユーザーのidを代入する
                            
                            https://github.com/heartcombo/devise#controller-filters-and-helpers
                            
                            ↑
                            
                            ヘルパー
                            ユーザー認証が付いているコントローラーになる
                            
                        - CalendarEvent.where(user_id: user_id)
                            - CalendarEventモデルを介してCalendarEventsテーブルのuser_idカラムとログインしているユーザーのidが一致するレコードを取得する
                        - calendar_events =
                            - 取得したレコードを配列の形にしてcalendar_eventsに代入する
                        - render json: calendar_events
                            - json形式にして返す
                    
                    ```ruby
                    before_action :authenticate_user!  
                      
                    def index
                      user_id = current_user.id
                      calendar_events = CalendarEvent.where(user_id: user_id)
                      render json: calendar_events
                    end
                    ```
                    
                - 予定作成のAPI　＝＞　createアクション
                    - calendar_events_controller
                    
                    ```ruby
                    def create
                        calendar_event = CalendarEvent.new(calendar_event_params)
                        calendar_event.user_id = current_user.id
                        calendar_event.save!
                        render json: calendar_event
                      end
                      
                      private
                      
                      def calendar_event_params
                        params.require(:calendar_event).permit(:title, :description, :start_date, :end_date)
                      end  
                    ```
                    
                    - createアクション
                        - calendar_event = CalendarEvent.new(calendar_event_params)
                            - 変数calendar_event に代入する
                            - CalendarEvent.new(calendar_event_params)
                                - CalendarEventモデルのnewメソッドを使ってインスタンス生成
                                - 引数には(calendar_event_params)を受け取る
                            - calendar_event.user_id = current_user.id
                                - calendar_event.user_id(外部キー) ⇒ 作成する予定にcurrent_user.id ⇒ ログイン中のユーザーのidを格納する
                            - calendar_event.save!
                                - saveメソッドを使ってDBへ保存する
                            - render json: calendar_event
                                - json形式に変換して返す
                    - privateメソッド
                        - privateメソッドは外部から呼び出す時には外部から呼び出す必要がある
                        - しかし、privateのメソッドはレシーバーをつけて呼び出してしますとエラーが起きてしまう。
                    - calendar_event_params
                        - params
                            - リクエストパラメーター
                        - require(:calendar_event)
                            - オブジェクトの指定
                                - calendar_eventを指定する
                                https://qiita.com/gogotakataka1234/items/47ad430fed87a2335f6d
                        - permit(:title, :description, :start_date, :end_date)
                            - ストロングパラメーター
                                - :title, :description, :start_date, :end_date
                                    - 引数に渡すデータ
                - 予定更新のAPI　＝＞　updateアクション
                    - calendar_events_controller
                    
                    ```ruby
                     def update
                        calendar_event = CalendarEvent.find(params[:id])
                        calendar_event = calendar_event.update!(calendar_event_params)
                        render json: calendar_event
                      end
                    ```
                    
                    - updateアクション
                        - calendar_event = CalendarEvent.find(params[:id])
                            - 変数calendar_eventに対してfind関数を使ってリクエストから送られてきたidと合致するレコードを代入する
                        - calendar_event = calendar_event.update!(calendar_event_params)
                            - 変数calendar_eventに対してupdate!メソッドを使ってリクエストから受け取ったデータを引数に受け取りデータを更新する
                                - titleプロパティの値が変わっている場合には他の場所は変わらずにtitleプロパティに変化が起きる
        - FE
            - カレンダー機能を実装する
                - 予定一覧、予定作成、予定更新、予定削除のAPIを叩くコードを記載する
                    - APIを叩いた時の認証情報
                    
                    ```jsx
                    if (
                    !Cookies.get("_access_token") ||
                    !Cookies.get("_client") ||
                    !Cookies.get("_uid")
                    
                    headers: {
                          "access-token": Cookies.get("_access_token"),
                          client: Cookies.get("_client"),
                          uid: Cookies.get("_uid"),
                    ```
                    
                - Fullcalendarライブラリを使ってUIを実装する
                    - インストールする
                        - yarn add @fullcalendar/react @fullcalendar/core @fullcalendar/daygrid
                            - @fullcalendar/react
                                - FullCalendarのReact向けライブラリ
                            - @fullcalendar/core
                                - コアライブラリ
                            - @fullcalendar/daygrid
                                - プラグイン
                - 作成する機能
                    - イベント作成モーダル
                        - touch src/components/CreateEventModal.jsx
                            - 記載する内容：
                                
                                ```jsx
                                export const CreateEventModal = ({ isOpen, onClose, createEvent }) => {}
                                ```
                                
                            - 受け取る引数
                                - isOpen
                                    - モーダルが開いている
                                - onClose
                                    - モーダルを閉じる関数
                                - createEvent
                                    - カレンダーイベントを作成する関数
                            - 必要な値を管理するuseState
                                
                                ```jsx
                                const [title, setTitle] = useState("");
                                予定の内容
                                const [description, setDescription] = useState("");
                                予定の説明
                                const [startDate, setStartDate] = useState("");
                                開始日
                                const [endDate, setEndDate] = useState("");
                                終了日
                                ```
                                
                            - 入力値を空にする関数
                                - clearEvent
                            - ChakraUIのモーダルコンポーネントを活用する
                                - Modal
                                    - モーダルコンポーネントをラップするコンポーネント
                                - ModalOverlay
                                    - モーダルダイアログの背後にある薄暗いオーバーレイ
                                - ModalContent
                                    - モーダルダイアログのコンテンツのコンテナ
                                - ModalHeader
                                    - モーダルダイアログのラベルとなるヘッダー
                                - ModalFooter
                                    - モーダルアクションを格納するフッター
                                - ModalBody
                                    - モーダルのメインコンテンツを格納するラッパー
                                - ModalCloseButton
                                    - モーダルを閉じるボタン
                            - Modalの中でInput要素を用意して情報を受け取る
                                - ModalBody
                                    - title情報を引数に渡して更新を行う
                                
                                ```jsx
                                <Input
                                    placeholder="タイトル"
                                    value={title}
                                    onChange={(event) => setTitle(event.target.value)}
                                    mb="16px"
                                  />
                                ```
                                
                                - その後にBotton要素に関数を紐づける
                                    - 最初にcreateEventを発火させる
                                    - clearEventを実行し関数を空にする
                                    - onCloseとしてモーダルを閉じる
                                
                                ```jsx
                                <Button
                                    colorScheme="blue"
                                    onClick={() => {
                                      createEvent({ title, description, startDate, endDate });
                                      clearEvent();
                                      onClose();
                                    }}
                                  >
                                    イベントを追加
                                  </Button>
                                ```
                                
                    - イベント更新モーダル
                        - 更新するモーダル用のファイルを作成する
                        
                        ```jsx
                        $ touch src/components/UpdateEventModal.jsx
                        ```
                        
                        - 更新用のモーダルには初期値として既存の値を準備する
                            - 引数として受け取る
                                - updateTitle,
                                - updateEventId,
                                - updateDescription,
                                - updateStartDate,
                                - updateEndDate,
                            - 値を更新するための引数
                                - setTitle,
                                - setDescription,
                                - setStartDate,
                                - setEndDate,
                        
                        ```jsx
                        export const UpdateEventModal = ({
                          isOpen,
                          onClose,
                          updateEvent,
                          updateTitle,
                          updateEventId,
                          updateDescription,
                          updateStartDate,
                          updateEndDate,
                          setTitle,
                          setDescription,
                          setStartDate,
                          setEndDate,
                        }) => {}
                        ```
                        
                        - モーダル内に関数の依存関係を定義する
                        
                        ```jsx
                         <Input
                            placeholder="タイトル"
                            value={updateTitle}
                            onChange={(event) => setTitle(event.target.value)}
                            mb="16px"
                          />
                        ```
                        
            - カレンダー画面（UI）
                
                ```jsx
                import { useState, useEffect } from "react";
                import FullCalendar from "@fullcalendar/react";
                import dayGridPlugin from "@fullcalendar/daygrid";
                ↑
                Fullcalenderのインポートとプラグインのインポート
                
                import { Box, Flex, Button, Image, useDisclosure } from "@chakra-ui/react";
                
                import { CreateEventModal } from "../components/CreateEventModal";
                import { UpdateEventModal } from "../components/UpdateEventModal";
                ↑
                作成した予定作成のモーダルと更新用のモーダルをimportする
                
                import {
                  getCalendarEvents,
                  createCalendarEvent,
                  updateCalendarEvent,
                } from "../lib/api/calendarEvent";
                import { getUser } from "../lib/api/auth.js";
                import { useNavigate } from "react-router-dom";
                
                const Calendar = () => {
                  const {
                    isOpen: isCreateModalOpen,
                    onOpen: onCreateModalOpen,
                    onClose: onCreateModalClose,
                  } = useDisclosure();
                  const {
                    isOpen: isUpdateModalOpen,
                    onOpen: onUpdateModalOpen,
                    onClose: onUpdateModalClose,
                  } = useDisclosure();
                  ↑
                  ChakraUIが提供するカスタムHooksのuseDisclosure
                  モーダルの状態管理をする事ができる
                  
                  const [events, setEvents] = useState();
                  ↑
                  Eventを配列で管理するuseState
                  
                  const [updateTitle, setTitle] = useState("");
                  const [updateDescription, setDescription] = useState("");
                  const [updateStartDate, setStartDate] = useState("");
                  const [updateEndDate, setEndDate] = useState("");
                  const [eventId, setEventId] = useState("");
                	↑
                	更新用のモーダルで使うモーダルの初期値を管理するuseState
                
                  const navigate = useNavigate();
                	↑
                	navigate関数を定義する
                
                  const clearEvents = async () => {
                    try {
                      const res = await getCalendarEvents();
                      const calendarEvents = res.data.map((calendarEvent) => {
                        return {
                          eventId: calendarEvent.id,
                          title: calendarEvent.title,
                          description: calendarEvent.description,
                          start: calendarEvent.startDate,
                          ↑
                          既存で設定していたstartDateではFullcalenderが動作しないためstartに変更
                          end: calendarEvent.endDate,
                          ↑
                          既存で設定していたendDateではFullcalenderが動作しないためendに変更する
                        };
                      });
                      setEvents(calendarEvents);
                    } catch (e) {
                      console.log(e);
                    }
                  };
                  ↑
                  カレンダーイベントの配列情報を取得する（変数resへ代入）
                  イミュータブルな言語のため変数resに対してマップ関数を実行した値を
                  calendarEventsへ代入してuseStateをset関数を発火させてstate更新を行う
                  catch関数でエラーハンドリングを行う
                  
                  useEffect(() => {
                    const f = async () => {
                      try {
                        const getUserRes = await getUser();
                        if (!getUserRes.data.isLogin) {
                          navigate("/");
                        }
                        await clearEvents();
                      } catch (e) {
                        console.log(e);
                      }
                    };
                    f();
                  }, [navigate]);
                  ↑
                  すでに処理済みのカレンダーイベントを取得する関数
                  getUser=>ログインしているユーザーを取得するAPIを叩く関数
                  ログインしていない場合（!getUserRes.data.isLoginがtrueの場合）
                  navigate関数を発火させて初期画面（ログイン画面）に遷都する関数
                  ログイン済みだった場合（!getUserRes.data.isLoginがfalseの場合)
                  clearEvents()を実行してイベント内容を取得する
                  
                  実行されるタイミング
                  ・useEffect
                	  ・コンポーネントが初期化されたタイミング
                
                  const createEvent = async (event) => {
                    await createCalendarEvent({
                      title: event.title,
                      description: event.description,
                      startDate: event.startDate,
                      endDate: event.endDate,
                    });
                    await clearEvents();
                  };
                  ↑
                  イベント作成モーダルで実行される関数
                  イベントを作成する際に引数として対応する値を渡す
                  その後、カレンダーイベントをクリアにする関数
                  
                  const updateEvent = async (event) => {
                    await updateCalendarEvent({
                      calendarEventId: event.updateEventId,
                      title: event.updateTitle,
                      description: event.updateDescription,
                      startDate: event.updateStartDate,
                      endDate: event.updateEndDate,
                    });
                    await clearEvents();
                  };
                  ↑
                  イベント更新モーダルで実行される関数
                  必要な値を渡した後にカレンダーイベントをクリアにする関数
                  
                  //この関数は任意のイベントをクリックした時に実行される関数
                  //引数infoはFullcalenderから渡される
                  const eventClick = (info) => {
                    const zeroPad = (n) => {
                      return n < 10 ? "0" + n : n;
                    };
                    ↑
                    月日の値が0~9の場合(n < 10)には0を付け足す("0" + n)文字列と変数の連結
                    そうでない場合にはnをそのまま返す
                    const startDatetime = info.event.start;
                    ↑
                    引数としてFullcalenderから受け取ったinfoのevent.startを変数へ代入
                    const endDatetime = info.event.end ? info.event.end : startDatetime;
                    ↑
                    event.endプロパティはstartと同日の場合にはnullになるというdefalutの設定があるので
                    三項演算子を使ってinfo.event.endがtrueの場合にはinfo.event.endを代入
                    null(false)の場合にはstartDatetimeを代入する
                
                    const startDate = `${startDatetime.getFullYear().toString()}-${zeroPad(
                      startDatetime.getMonth() + 1
                    )}-${zeroPad(startDatetime.getDate())}`;
                
                    const endDate = `${endDatetime.getFullYear().toString()}-${zeroPad(
                      endDatetime.getMonth() + 1
                    )}-${zeroPad(endDatetime.getDate())}`;
                    ↑
                	  data型のデータをstring型に変換するコード
                
                    setTitle(info.event.title);
                    setDescription(info.event.extendedProps.description);
                    setStartDate(startDate);
                    setEndDate(endDate);
                    setEventId(info.event.extendedProps.eventId);
                    onUpdateModalOpen();
                    ↑
                    クリックしたイベント情報を格納する
                    info.eventはFullcalenderから受け取ったデフォルト以外の場合には
                    info.event.extendedProps.valueの形でアクセスする必要がある
                    それらの処理を行った後に更新用のモーダルを開いている
                  };
                
                  return (
                    <>
                      <CreateEventModal
                        isOpen={isCreateModalOpen}
                        onClose={onCreateModalClose}
                        createEvent={createEvent}
                      />
                      ↑
                      useDisclosureから受け取るモーダルを管理するための{isCreateModalOpen}、
                      {onCreateModalClose}を渡す、イベントを作成するためのcreateEventも渡す
                      <UpdateEventModal
                        isOpen={isUpdateModalOpen}
                        onClose={onUpdateModalClose}
                        updateEvent={updateEvent}
                        updateTitle={updateTitle}
                        updateDescription={updateDescription}
                        updateStartDate={updateStartDate}
                        updateEndDate={updateEndDate}
                        updateEventId={eventId}
                        setTitle={setTitle}
                        setDescription={setDescription}
                        setStartDate={setStartDate}
                        setEndDate={setEndDate}
                      />
                      ↑
                      useDisclosureから受け取るモーダル管理用の{isCreateModalOpen}、
                      {onCreateModalClose}を渡す。
                	    更新するためのupdate関連の関数を渡す
                      <Flex justifyContent="center" mt="16px">
                        <Flex
                          w="200px"
                          justifyContent="center"
                          alignItems="center"
                          flexDirection="column"
                        >
                          <Button w="80%" colorScheme="blue" onClick={onCreateModalOpen}>
                            予定を追加
                          </Button>
                          ↑
                          クリックイベントが発生すると予定作成用のモーダルが開くようにする
                          <Image src="calendar-view.png" />
                        </Flex>
                        <Box w="1200px">
                          <FullCalendar
                            plugins={[dayGridPlugin]}
                            locale="ja"
                            events={events}
                            headerToolbar={{
                              left: "today",
                              center: "title",
                              right: "prev,next",
                            }}
                            eventClick={eventClick}
                            editable={true}
                            selectable={true}
                            height="95vh"
                          />
                          ↑
                          カレンダーUIの実質的な部分
                          FullcalenderからImportしたFullCalendarコンポーネントを使う
                          渡す引数
                	          plugins
                	          locale
                	          events
                		          すでにFullcalenderで表示できように加工したイベントの配列を渡す
                		          useStateで管理する事で新規作成や更新などの状態に変化が起きた時に
                		          useStateでコンポーネントの再レンダリングが起きるようにしている
                	          headerToolbar
                	          eventClick
                        </Box>
                      </Flex>
                    </>
                  );
                };
                
                export default Calendar;
                ```
                
                - public配下に**calendar-view.pngを入れておく**
                    - <a href="https://storyset.com/education">Education illustrations by Storyset</a>
                        
                        ![English teacher-rafiki.png](attachment:839fb1a3-d990-4374-bc39-34159ac62b7c:English_teacher-rafiki.png)