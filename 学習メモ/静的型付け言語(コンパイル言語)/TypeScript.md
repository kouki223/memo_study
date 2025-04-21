- 学習ソース
    https://mosya.dev/react/dashboard
    https://recursionist.io/learn/languages/typescript/function/callback
    - サバイバルTypeScript
        - 実務において最低限使う内容のみをまとめたドキュメント
            - TypeScriptを網羅的にまとめたドキュメントとは違う
                - 実務においてこれだけ知っていれば死なない（サバイバル）ようにするドキュメント
- Type Scriptの概要
    - TypeScriptとは？
        - プログラミング言語
            - 静的型付け言語
                - JavaScriptに型という概念が追加された言語
                    - JSの上位互換的な立ち位置
    - TypeScriptの歴史
        - JavaScriptでも大規模開発をする事ができるように開発されたプログラミング言語
            - 解決策としてはJSが進化する事で解決するのではないか？
                - しかし、そうならなかった
        - 1990年　＝＞　JS誕生以前
            - 簡単なフォームのバリデーションもサーバーサイドで行う必要があった
                - Netscape Navigatorというブラウザを開発するNetscape社がクライアントサイドで動くプログラムの重要性に気づきJavaScriptを実装した
            - JavaScriptはHTMLの補助的なものと考えられていた
                - アニメーションを実装したり
                - フォームのバリデーションに使う程度
                    - JavaScriptが大規模開発に使われると思っていない
                        - 当時のJSはあくまで補助的な立ち位置だった
        - 2000年初頭
            - ブラウザアプリの実現する技術としてJavaアプレットやAdobe Flashがあった
                - 大規模開発のニーズが強まる
                    - 当時は「リッチインターネットアプリケーション」と呼ばれた対話型のウェブアプリケーションにJavaアプレットやFlashが担っていた
                        - 中にはJSを使うプログラマもいた
        - 失われた10年
            - この頃から大規模開発に耐えうるJSが望まれた
                - ECMAScriptがJSの言語仕様を策定するようになった
                    - ES4で議論された機能
                        - モジュール
                        - Javaのようなクラス
                        - 静的型付け
                        - Nullable型
                        - ユニオン型
                        - ジェネリクス
                            - TSに備わっている機能に似ている
                                - ES4はJSと後方互換性を持たず、Microsoftと対立した
                                    - 2008年に破棄される事になる
        - 2000年代中盤
            - JSは足踏み状態
                - 本格的なアプリを開発する言語ではないというJSのイメージは支配的
                    - 2005年にGoogle Mapが登場する
                - 当時のマップサイトは移動のたびにリロードされるので画面遷都の問題があった
                    - そこにGoogle Mapのような画面遷都の必要ないものは画期的だった
        - 2000年代後半
            - ブラウザさえあれば他のものをインストールする必要がないアプリは魅力的
                - JSによる大規模開発のニーズが日に日に増す
        - 進化なきJS、一世風靡のAltJS
            - JSへの期待が高まる中でも進化しないJS
                - JSにコンパイルする事ができる言語を作ればいいのでは？
                    - CoffeScript
                        - Rubyのような完結な文法でコーディングする事ができる言語
                            - AltJSと呼ばれるようになる 
                                - JSは現代のアセンブラと呼ばれる事もある
        - ECMAScript2015始動
            - JSも改善のために動き出す
                - 過去のJSと互換性があるHarmonyという言語仕様が検討されるようになった
        - 2010年代
            - 新たな言語仕様に向けて議論される中、2012年にTSが発表される
                - JSのスーパーセット
                - モジュール
                - 型
                    - の3つを強調して打ち出す
                        - CoffeScriptがドラスティックな言語であったのにも関わらずスーパーセットにとどめた
                            - スーパーセットにする事でJSの資産が無駄にならない
            - モジュール性の強み
                - コードを適切な粒度に切り分ける
                    - 実際の詳細をカプれるかできる
                        - 後にJSも実装する
            - 型が最大の特徴
                - コーディング中にコードジャンプできる事、コード補完ができる恩恵が生産性を高めた
            - JSも日々更新される
                - ECMAScriptは毎年アップデートされるようになった
                    - 徐々に大規模な開発に耐える事ができるよになってきている
    - 型の概念が追加されたJavaScript
        - プログラム全般
            - 安全である事
            - コードの改善、修正がしやすい事
                - が求められる
        - 大規模開発、複雑なアプリケーションなどにおいて特に求められる要素である
            - TypeScriptを言語として使う事が選択されている
                - オブジェクト指向プログラミング
                - 関数型プログラミング
                    - 堅牢ながら柔軟なプログラミングが可能
                        - オープンソースだがMicrosoftのサポートを受ける事ができる
        - 型のチェック
            - データの型をチェックする事で間違いを教えてくれる
                - 事前に間違いを防ぐ事が出来る
        - TSはJSの文法を拡張したもの
            - 素のJSもTSとして扱う事ができる
                - TSCはこれを解析できる
            - TS側から見た時にJSはTSの一部と見ることができる
                - TSを理解するにはJSの理解が欠かせない
    - 静的型付け
      - 型の決定するタイミング
        - 処理の実行時に型が決まる言語　＝＞　動的型付け言語
        - コンパイル時に型が決まる言語　＝＞　静的型付け言語
      - 型注釈はコスト、投資と考えるか
        - 変数毎に型注釈を記載する必要がある
          - コストと考える事ができる
            - コンパイラを育てるための投資と考える事もできる
    - プログラミング指向
      - TypeScriptはオブジェクト指向、関数型プログラミングのどちらもサポート
    - TSのエコシステム
      - TSを学習する時にTSそのものを学習する事は不可欠である
        - 実務においてはTSを学習する事に加えてTSを取り囲む
      - 言語　＝＞　ECMAScript
      - ライブラリ
        - UIライブラリ
      - フレームワーク
        - Next.js
        - Nuxt
        - Gatsby
      - 型定義ファイル
        - DefinitelyTypedが公開
      - 実行環境
        - Node
      - 開発ツール
        - パッケージマネージャー
          - 中央集権型のパッケージ管理ツール
            - 全てのライブラリはnpmjs.comにホスティングされている
        - モジュールバンドラー
          - 複数のJSファイルを結合するツール
            - 素のままでは適切な順番で読み込む順を指定する必要があるが、ツールを使う事で解決する事ができる
        - タスクランナー
          - ビルドを自動化してくれるツール
        - トランスパイラー
          - コンパイラーの一種
            - 高水準言語から高水準言語への変換を行う
        - コードフォーマッター
          - コードのインデントなどを自動で揃えてくれるツール
        - リンター
          - コーディング規約に違反していないか？判断する
        - Gitフック
          - Gitフックは、Gitにコミットするタイミングや、プッシュするタイミングに、何らかのプログラムを実行する機能
            - Gitコミット時にTypeScriptのコンパイルで型チェックをする
            - リンターのチェックを起動する
            - コードフォーマッターでコード整形をかけるなど
              - Gitフックを手軽に利用できるようにするツールとして、huskyやlint-stagedがある。
    - TypeScriptの開発背景
        - 1995年 JavaScript開発される
            - JavaScriptは当初、大規模開発を想定されていなかった
                - 開発されてから10年間で大規模開発のニーズが顕在化する
        - JavaScriptは大規模開発のニーズに応える事ができなかった
            - JavaScriptが停滞している間に2012年TypeScriptが開発された
                - JavaScriptも2015年にはECMAScriptを発表した
                    - 特徴
                        - JavaScriptのスーパーセット
                        - モジュール性
                        - 型
        - TypeScriptはスケーラブルなJavaScriptの上位互換言語
          - 大規模開発にも適している
    - 静的型付け言語と動的型付け言語の差
        - 静的型付け言語
            - コンパイル時に型が決まる言語
                - 静的型付け言語(TypeScript)が実行されるまでの流れ
                    - エディターでコードを記述
                    　↓ *　エディターの補完機能によるチェック
                    - コンパイラー(TSCコンパイラー)によってコンパイルされて実行される
                    　↓ *　ASTによる型のチェックが入る
                    - トランスパイラーによってJavaScriptにトランスパイルされる
            - トランスパイル　＝＞　同言語レベルへの変換
                - 最終的にJavaScriptに変換されてブラウザ、アプリで表示される
                    - TypeScriptは直接、ブラウザやアプリでは表示できない
                        - TypeScriptのコードをトランスパイルしてJavaScriptへ変換される
                            - Reactで使うJSXもTypeScriptでサポートされている
            - コンパイル
                - 特定のコンピューター言語で記載されたプログラムを特定のコンピューター言語に変換する事
                    - 型のチェックを行う
                - 型注釈
                    - 型注釈は、自分専属のコードレビュアであるコンパイラを育てるための投資
        - 動的型付け言語
            - 実行時に型が決まる言語
    - 型のシステム
      - 公称型　＝＞　Java、PHP
        - 継承関係に着目するシステム
          - 同じようなプロパティ、データ構造を持っていたとした場合でも継承関係がなければ互換性がないシステム
      - 構造的部分型システム　＝＞　TS
        - オブジェクトの形状に基づいて型を判別する
          - データ構造が同じであれば互換性がある
            - データ構造　=> オブジェクトが持つプロパティが互換しているのか？
    - エディターとの相性
        - データの型情報を事前に渡す事でエディターの補完機能を使う事が出来る
            - 開発効率も向上する
    - TypeScriptからみたJavaScript
        - TypeScriptからみたJavaScriptはTypeScriptの一部になる
            - JavaScriptのコードをTypeScriptは100％コンパイル（静的検査）する事ができる
                - 根本的にJavaScriptの理解が重要になってくる
    - TypeScriptは何者なのか？
        - TypeScriptにランタイムは存在しない
            - TypeScriptは最終的にJavaScriptに変換される
                - TypeScript専用のランタイムは存在しない
        - TypeScriptが実行できる事
            - ソースコードを解析し、問題点をチェックする
            - ソースコードを別の言語に変換する
        - TypeScriptがやらない事
            - 最適化する
        - TypeScriptとJavaScriptを比較した時に実行後の速度に変化が起きる事はない
            - TypeScriptは型チェックを実行したのちには計算結果などに変換する訳ではない
                - JavaScriptになってからは処理に差がない
    - サバイバルTypeScript
      - これからプログラムを始める
      - 始めたばかり
        - 最低限これだけ知っていればという内容の知識を詰め込んだドキュメント
    - TypeScriptにおけるメモリ管理
      - JavaScriptと同様のメモリ管理を行う
        - JavaScriptの画ベレージコレクションを用いて自動的にメモリを解放する
    - TypeScriptを使う理由
      - Webアプリケーションにおけるフロントエンド開発において最低限の知識として必要になる言語はHTMLやCSSを除くとJavaScriptになる
        - JSを使う事でかなり自由にフロントエンドを実装する事ができる
          - ではなぜTSが必要になるのか
      - TSが開発された背景
        - JSが賄う事ができなくなった大規模開発を克服するために生まれたのがTSである
          - 型による静的チェック
            - プログラムを実行する前に欠陥に気づく事ができる
              - バグは発見が遅れるほど修正コストがつく
              - エディターの保管機能を活かす事ができる
                - コーディング効率の改善
            - 品質保証の銀の弾丸ではない
              - チェック対象
                - 客観的に判断できるような欠陥
          - モジュール性
          - 緩やかな学習コスト
            - JSのスーパーセット
              - TSを使用するためにはJSを学習する事が必須になっているが、逆にJSの知識があれば段階的に導入する事ができる
      - TSは古いバージョンのブラウザ仕様にも対応できる
        - コンパイルする言語のバージョン指定をする事も可能
      - TSはESNextにも対応している
        - JSの次の言語仕様にもなっている
    - TSは最もポピュラーなAltJSである
      - 満足度が高い
      - エコシステムが充実している
      - 使用用途が多いため採用などの面でも有利
    - ランタイムエンジン
        - V8エンジン　＝＞　Googleが開発　＝＞　高速な実行環境
        - SpiderMonkey
        - JavaScriptCore
        - Chakra
        - Nashorn
    - ECMAScript
        - 仕様
            - どの実行環境でも共有の環境
                - JavaScriptはこのECMAScriptnによって仕様が決まっている
                    - JS・TSが準拠する仕様
        - JSとECMAScriptの関係
            - 仕様を定義する
                - 仕様　＝＞　決まりごと
                    - ブラウザがJSを読み込んだ時にどのように解釈するのか？
                        - 処理がどのように動くのか？という事を定義する
            - 歴史
                - JSを標準化するべくECMAScriptが策定された
                    - JSはNetscape社が開発した言語
                        - Netscape社はJSを標準化するために国際規格策定団体Ecmaインターナショナルに依頼する
                            - その結果
                                - Ecmaによって標準化されたJavaScriptはECMAScriptと呼ばれる事になっている
            - JSが従うべき仕様
                - ECMAScriptがJSがどのように振る舞うかを定義している
                    - JSの実装　＝＞　ECMAScriptの実装と呼ばれる事もある
            - 命名由来
                - 競争関係だったNetscape社とMicrosoft社
                    - ECMAScriptが合意できる妥協案だった説
                        - Netscape社 => JavaScript
                        - Microsoft社 => JScript
                - JavaScriptという言葉が商標だった事
                    - JavaScriptは当時Sunが所有する商標だった
                        - 現在はorakle社が保有
        - JavaScriptの仕様は毎年更新される
            - ECMAScriptは毎年更新される
                - JavaScriptには新しい構文や機能が増え続ける
                    - ECMAScriptは後方互換性に優れる
                        - 学びは無駄にならない
        - 仕様改訂のステップ
            - ステージ	条件
                - 0 **Strawperson**	なし
                - 1 **Proposal**	チャンピオン(委員会の改定推進パートナー)が決まっている
                    - 課題と解決策を説明したリポジトリが公開されている
                        - デモがあるとよい
                - 2 **Draft**	ECMAScriptの仕様記述言語で主要な部分の仕様が書かれていること
                - 3 **Candidate**	完全な仕様書があること。レビュアとECMAScript編集者の署名があること
                - 4 **Finished**	2つ以上のJSエンジンに実装が存在していること。
                    - ECMAScriptへプルリクエストが送信されている
                        - ECMAScript編集者に承認されていること
        - ECMAScriptとブラウザの関係
            - ECMAScripが決めるクライアントサイドのJSは部分的
                - ECMSScriptは主に
                    - 言語の文法、構文の解釈方法、コアのAPIなど言語の中核部分を決める
                        - 関数宣言の書き方はこういう文法になる
                        - 変数が宣言されたとき、JavaScriptエンジンはこういう動作になる
                        - StringやArrayオブジェクトにはこういうメソッドがある
            - JSにおけるブラウザ仕様を決める団体 => 標準化団体WHATWG
                - HTML Living Standard
                    - windowオブジェクト
                    - HTMLDivElement
                    - ローカルストレージなどのAPI
            - ブラウザ内部は様々な部品で分ける事ができる
                - レンダリングエンジン
                    - JSエンジンを組み込んだブラウザの表示機能を担うモジュール
                        - JSのみならずHTMLやCSSも解釈して総合的に画面表示をする
                            - Blink
                                - V8エンジンをJSエンジンに採用
                            - Gecko
                            - WebKit
                - JavaScriptエンジン
                    - ECMAScriptを実装したモジュール
                        - V8
                        - SpiderMonkey
                        - JavaScriptCore
                - レンダリングエンジンは変更される事や環境に応じて変わる
                    - iosのエンジンはWebKitと独占的に利用を許されている
                        - 同じサービスでも環境に応じて変化する
                - エンジニアはエンジンについて理解する事が重要
                    - 普段、コードを書くエンジニアはエンジンについて理解する事が重要である
                        - エンジンについて理解する事　＝＞　実行環境ついて理解する事
                            - テストなど、バグに関して基本的にはECMAScriptに準拠するエンジンでも少しの違いなどが出てくる可能性がある
                ![alt text](https://typescriptbook.jp/img/overview/ecmascript/browser-rendering-engine-javascript-engine-ecmascript-relations.svg)
        - JSにおける仕様決定の棲み分け
            - モジュール
                - ECMAScript
                    - importやexportの構文や、モジュール内部の仕様
                - HTML Living Standard
                    - import "指定子"
    - Ecmaインターナショナル
        - 情報通信技術のさまざまな国際規格を策定している
            - 各規約には番号が振られている
                - ECMAScriptの規格番号 => ECMA-262
            - 様々な専門委員会
                - 委員会の名称　＝＞　TC39
    - TSの射程
      - FE
        - 最も人気な分野
          - JSのエコシステムに乗っかっているため大きな力を発揮する
      - BE
        - バックエンドのアプリケーションもTSで作成可能
          - Node.jsで使う事が出きる
      - FEとBEでTSを扱うメリット
        - プロジェクト全体で1つの言語を使って開発をできる面
          - モジュール内で共有可能
            - 原義が違うとロジックを共有する事ができない
          - プロジェクト全体でノウハウが共有できる
      - 学習のパフォマンスが最大化する
        - 言語を覚える事はかなり時間がかかる
          - 座学で知識ベースで学習
          - 実務でベストプラクティスを選択できるようになる
            - もの2つには大きな差があり、時間がかかる
      - デスクトップアプリ
        - TSはデスクトップアプリの作成も可能CLIアプリも可能
      - サーバーレス(FaaS)
        - サーバーの構築、保守なしにサーバーサイドのプログラムを実行できる
          - クラウドベンダーがJavaScriptなどのマネージド実行環境を提供　＝＞　AWSなど
        - インフラ構成管理(Iac)
          - インフラが物理的なものから仮想的なものへ変化する
      - ブラウザ拡張
        - ブラウザの拡張機能をJSで書く事ができる
          - TSで書いたコードもJSに変換される
      - 機械学習
        - JavaScriptでも機械学習などのツールが多数作られてきている
          - TypeScriptプログラマーも手が届きやすくなっている
            - TensorFlow.jsはGoogleが開発した機械学習ライブラリ
            - Brain.jsはニューラルネットワークのライブラリ
      - 組み込み形
        - Static TypeScript(STS)　＝＞　TSのサブセット言語
          - リソースの少ない組み込みデバイスを対象とする言語
      - WebAssembly
        - ブラウザで動くアセンブリー言語
          - WASMはJavaScriptよりも高速な処理が必要とされるところで用いられる
- TypeScriptの仕様
    - 型の指定
        - 型の種類と基本構文：
            - **number**（ナンバー）
                - 数字を扱う型
                    
                    ```tsx
                    const age: number = 20;
                    const score: number = 100;
                    ```
                    
            - **string**（ストリング）
                - 文字列を扱う型
                    - 変数に代入する文字列をダブルクウォーテーションorシングルクウォーテーションで囲む
                    
                    ```tsx
                    const name: string = "mosyabo";
                    ```
                    
            - **boolean**（ブーリアン）
                - true or false のどちらかの値を持つ型
                    - 条件式の評価を行う場合に使われる
                    
                    ```tsx
                    const isOpen: boolean = true;
                    
                    if (isOpen) {
                      console.log("ドアが開いています！");
                    } else {
                      console.log("ドアは閉まっています。");
                    }
                    ```
                    
            - **any**（エニー）
                - 何でもありの型
                    - 便利な型であるばTypeScriptの型チェックが適用されないため極力使わないようにする事が必要
                    
                    ```tsx
                    const message: any = "こんにちは";
                    message = 10;
                    message = true;
                    
                    ```
                    
            - **型のエイリアス**
                - typeというキーワードで既存の型に新しい名前をつける
                    
                    ```tsx
                    type Message = string;
                    
                    // Message型を使って変数を宣言
                    const greeting: Message = "Hello, TypeScript";
                    ```
                    
            - ユニオン
                - またはという意味を持つ型
                    - 複数の型のうちから一つの値を持つこと
                    
                    ```tsx
                    const 変数名: 型1 | 型2 |;
                    ```
                    
                    - 実際の例：
                    
                    ```tsx
                    //この関数ではinputはstring型、number型どちらも取りうる
                    function display(input: string | number) {
                     console.log(input);
                    }
                    //このinputにtrueなどを引数に渡すとエラーになってしまう
                    ```
                    
                - ユニオン型が必要になる場面
                    - 取得するデータが複数の型を持ちうる時
                        - サーバーからユーザ情報を取得する場合
                            - ユーザ情報を取得したい場合
                                - ユーザ側
                                - 管理者側
                                    - 名前
                                    - ID
                    
                    ```tsx
                    type User = {
                      id: number;
                      role: "user";
                      name: string;
                    };
                    
                    type Admin = {
                      id: number;
                      role: "admin";
                      name: string;
                    };
                    
                    // UserOrAdmin 型の変数が User 型または Admin 型のどちらかの値を取ることができる
                    type UserOrAdmin = User | Admin;
                    
                    function getAdmins(user: UserOrAdmin[]) {
                      return user.filter((user) => user.role === "admin");
                    }
                    
                    ```
                    
            - インターセクション(交差型)
                - 複数の型を組み合わせて新しい型を作成する
                    - ＆は型の交差（組み合わせる）を示す
                - インターセクションを使う事でDRYの原則で型の定義を行える
                    - DRY ＝＞　Don't Repeat Yourself
                        - 同じコードを繰り返し記載しない
                            - 再利用可能なコードを記載する
                    
                    ```tsx
                    type 新しい型 = 型1 & 型2;
                    ```
                    
                    - 基本構文
                    
                    ```tsx
                    type User = {
                      id: number;
                      role: "user";
                      name: string;
                    };
                    
                    type AdditionalField = {
                      tel: string;
                      address: string;
                    };
                    
                    type UserWithAdditionalField = User & AdditionalField;
                    ```
                    
            - unknown型
                - anyと同様にどのような型でも許容される型
                    - 型チェックを行わないと演算やメソッドを活用する事ができない
                        - エラー例：
                        
                        ```tsx
                        let a: unknown;
                        
                        a = 3;
                        
                        const b = a + 4; // aはunknown型なので演算に利用できない
                        ```
                        
                - typeof
                    - unknownはtypeofを使い型の指定をする事で演算やメソッドを活用する事ができる
                        - any型は型チェックを行わずに使う事が可能である
                            - unknown型はany型よりも安全な型
                        
                        ```tsx
                        let a: unknown;
                        
                        a = 3;
                        
                        if (typeof a === "number") {
                          const b = a + 4; // この中ではaはnumber型になる
                        }
                        ```
                        
        - タイプガード
            - ある変数の型が決まりきらない場合にとりあえず型をunknownに指定する
                - 指定したunknownの型を条件分岐に応じて決定する方法
                    - typeof 演算子
                        - if文と組み合わせて使う
                            - if文の条件式としてtypeof valueとする
                        - プログラムの実行時に値に応じて型が決まり処理が実行される
                        
                        ```tsx
                        let value: unknown = "こんにちは";
                        
                        if (typeof value === "string") {
                          console.log(value.length); // String型のプロパティにアクセスできる
                        } else if (typeof value === "number") {
                          console.log(value.toFixed(2)); // Number型のメソッドにアクセスできる
                        } else {
                          console.log("文字列でも数値でもありません");
                        }
                        ```
                        
                    - instanceof 演算子
                        - 特定のオブジェクトがクラスのインスタンスであるか判断する演算子
                    - カスタム型ガード関数
                        - typeof演算子を使って渡された引数に応じた処理を行う
                            - typescriptにおいてはisも使う
                                - isは関数がtrueを返す場合にはisで指定された型であるという事
                            
                            ```tsx
                            //isString関数は引数としてvalueを受け取る
                            //引数の型はunknownであり、isString関数がtrueの場合には
                            //valueの型はstringである事を示す
                            function isString(value: unknown): value is string {
                            	//typeof演算子でunknownの型をstringに指定する
                              return typeof value === "string";
                            }
                            
                            function isNumber(value: unknown): value is number {
                              return typeof value === "number";
                            }
                            
                            function printValue(value: unknown) {
                              if (isString(value)) {
                                console.log(`文字列: ${value}`); // value は string 型として扱われる
                              } else if (isNumber(value)) {
                                console.log(`数値: ${value}`); // value は number 型として扱われる
                              } else {
                                console.log("文字列でも数値でもない");
                              }
                            }
                            
                            ```
                            
        - 配列型
            - あらかじめ複数の値を持つことができる型
                - 要素に指定された型の後ろに[]とする事で配列の型を指定できる
                    - 実際の配列は[]で囲む
                    
                    ```tsx
                    // 数値の配列
                    const numbers: number[] = [1, 2, 3, 4, 5];
                    
                    // 文字列の配列
                    const fruits: string[] = ["apple", "banana", "cherry"];
                    
                    const numbers: number[] = [1, 2, 3,];
                    
                    a.push(4); 
                    a.push("5"); // 👈 コンパイルエラー
                    ```
                    
            - 配列にユニオン型を適用する事ができる
                
                ```tsx
                const 変数名: (型1 | 型2 )[];
                
                const mix (number | string)[] = [1, "two", 3, "four"];
                ```
                
            - タプル型
                - 配列の各々の型を指定する事ができる
                    - 要素の型の[]内に,で区切って型を記載する
                    
                    ```tsx
                    const 変数名: [型1, 型2, ...];
                    
                    const user: [string, number] = ["mosyabo", 20];
                    
                    適切な順番、型で操作しないとエラーになる
                    user.push("mosya"); // 👈 コンパイルエラー
                    user.push(30); // 👈 コンパイルエラー
                    ```
                    
                - useStateはタプル型を活用したものである
                    
                    ```tsx
                    const [count, setCount] = useState(0);
                    
                    このコードでuseState(0)を記載すると
                    初期値として0を持つ変数countと変数countを更新するための関数seCountが取得できる
                    [count, setCount]で[変数, その変数を変更するための関数]となる
                    ``` 
    - 型推論
      - 型注釈がついていない変数でもコンテキストに基づいて型を推測する
        - 型を明示しなくても安全性がます
    - 関数に型を定義する
        - 関数に型を適用する
            - 関数の受け取る引数
            - 戻り値
                - この2つに型を定義する
        
        ```tsx
        function 関数名(引数1: 型1, 引数2: 型2, ...): 戻り値の型 {
          // 関数の処理
          return 戻り値;
        }
        ```
        
        - アロー関数（functionが省略されて記載される関数コンポーネント）の型定義
            - Add型というエイリアスを作成する
            - 作成したAdd型をアロー関数のaddコンポーネントへ適用する
        
        ```tsx
        type 型名: (変数名: 引数1の型, 変数名: 引数2の型, ...) => 戻り値の型;
        ```        
    - オブジェクトや配列などの複雑な型を示す方法
        - オブジェクトにtypeを使って型を示す方法
            - オブジェクトの各プロパティに対してデータの型を示す事が出来る
                - まずは型のエイリアスを作成してオブジェクトの型を指定する
                - その後、適切な値を入れてオブジェクトを定義する
                
                ```tsx
                type オブジェクト名 = {
                  プロパティ名1: 型1;
                  プロパティ名2: 型2;
                  // これを繰り返して、必要なプロパティを定義できます
                };
                
                具体例：
                 type User = {
                  name: string;
                  age: number;
                };
                
                型のエイリアスに応じて値を代入する
                const user: User = {
                  name: "mosyabo",
                  age: 20,
                };
                ```
                
            - オプショナル
                - オブジェクトのプロパティに値がない場合にエラーを起こさないようにする
                
                ```tsx
                type Human = {
                  name: string;
                  age: number;
                  birthday?: Date;
                };
                
                const human: Human = {
                  name: "daigo",
                  age: 30,
                  // birthdayがなくてもOK
                };
                ```
                
            - ＆演算子を使ってType同士を合体させる
                - 型と型同士を＆を使って組み合わせて使う事もできる
                
                ```tsx
                type TextMessage = {
                  text: string;
                };
                
                type ImageMessage = {
                  imageUrl: string;
                  alt: string;
                };
                
                type Message = TextMessage & ImageMessage;
                
                このMessageという型はtxetに加えて、imageUrl,altも持っている
                ```
                
            - Mapped Types
                - オブジェクトのkey側の取りうるプロパティが無数にある場合や変則的な場合に利用する
                
                ```tsx
                type Obj = {
                  [key: string]: any;
                };
                ```
                
                - この時のKeyは全てstring型であるオブジェクト型を定義している
                
                ```tsx
                type Human = {
                  name: string;
                  age: number;
                  birthday: Date;
                };
                
                type MaybeHuman = {
                  [key in keyof Human]?: Human[key];
                };
                ```
                
                - []内で別の型のキーを展開する事も可能
            - ORの表現
                - | を使って表現する
                
                ```tsx
                type Judge = "OK" | "NG";
                ```
                
        - interface
            - どのプロパティがどのようなデータの型を持つのか定義する事が出来る
                - プログラム内でプロパティを追加して記載する事ができる
                
                ```tsx
                interface User {
                  name: string;
                };
                
                interface User {
                  age: number;
                };
                
                // TypeScriptがこれらを自動で1つにまとめる
                const member: User = {
                  name: "mosyabo",
                  age: 20
                };
                ****
                ```
                
            - オプショナルの機能
                - Type同様の機能がある
            - Extendsを利用したinterface同士の組み合わせ
                - Typeでの＆演算子を使った合体
            - 上書き
                - のちに書いたinterfaceの型が追加される
            - クラスのinterfaceとして使用する方法
                
                ```tsx
                interface ICar {
                  speed: number;
                  x: number;
                  run(): void;
                }
                
                class Car implements ICar {
                  speed: number;
                  x: number;
                  constructor(speed: number) {
                    this.speed = speed;
                    this.x = 0;
                  }
                  run() {
                    this.x += this.speed;
                  }
                }
                ```
                
        - Typeとinterfaceの違い
            - どちらもオブジェクトの型を指定する役割を持つ
                - Type特有の機能
                    - オプショナル
                    - ＆演算子を使ったTypem同士の合体
                    - MappedTypes
                    - ORの表現（　｜　を使う）
                - Interface特有の機能
                    - そもそもinterfaceはClassとオブジェクトのための機能である
                        - オプショナル
                        - extendsを使ったinterface同士の組み合わせ
                        - 上書き
                        - クラスのinterfaceとして利用する方法
            - Typeにある機能でinterfaceになり機能、その逆も然り
                - チームの方針、コントリビュートしているプロジェクトに応じて使い分け
                    - 普段は type を使い、class の implements の時にだけ interface を使う
    - オブジェクトの任意プロパティ
        - 存在する場合と存在しない場合のどちらにも対応できるようにする
            - 通常、プロパティを定義した場合にはそのプロパティが存在しないとエラーが発生
                - しかし、プロパティが存在しない場合という事は状況に応じてある
                    - プロパティが存在しない場合もエラーが発生しないようにする
        - プロパティの後に？をつける
            
            ```tsx
            interface User {
              name: string;
              age: number;
              hobby?: string; // 👈 オプショナルプロパティ
            };
            
            function getHuman(member: User) {
              // 関数の中身
            }
            
            ```
            
        - オプショナルチェイニング
            
            ```tsx
            type Member = {
              name: string;
              age: number;
              hobby?: {
                getAll: () => string;
              };
            };
            
            console.log(member.hobby?.getAll());
            
            ```
            
        - Null合体演算子
            - デフォルトの値を定義する事ができる
            
            ```tsx
            type Member = {
              name: string;
              age: number;
              hobby?: {
                getAll: () => string;
              };
            };
            const member: Member = {
              name: "mosyabo",
              age: 20,
              // hobby: { getAll: () => "プログラミング" },
            };
            const myHobby = member.hobby?.getAll() ?? "趣味はありません";
            ```            
    - classとinterface
        - オブジェクトの雛形
            - クラスからインスタンスを作成する
              - interfaceを使う事でコードの再利用、継承、大規模プロジェクトを管理する際に役に立つ
            
            ```tsx
            class Greeter {
              greeting: string;
              name: string;
            
              constructor(message: string, name: string) {
                this.greeting = message;
                this.name = name;
              }
            
              greet() {
                return this.greeting + this.name;
              }
            }
            
            let greeter = new Greeter("Hello, ", "Taro");
            console.log(greeter.greet()) // => Hello, Taro 
            ```            
    - constructor
        - インスタンスの生成時に実行されるメソッド
            - Rubyでのattr_accessorのようなもの
            
            ```tsx
            class User {
                name: string;
                //インスタンス化するとこのcounstructor()が実行されてthis.nameにTaroが入る。
                constructor(name: string){
                    this.name = name;
                }
            }
            
            var taro = new User("Taro");
            console.log(taro.name); //Taroが出力される。
            
            ```            
    - readOnly
        - 一度設定された値を変更できないようにする（読み取り専用）にするもの
            - プロパティ名の前にreadOnlyを記載する事で読み取り専用になる
        - データを安全に扱う事が出来る
            - **間違いを防止する** :
                - バグの原因となる意図しないデータの変更を防ぐことができます。
            - **コードの意図が明確になる** :
                - このデータは変更されることがないという開発者の意図を伝えることができるので、他の人もコードを理解しやすくなる。
            
            ```tsx
            interface オブジェクト名 {
              readonly プロパティ名: プロパティの型;
            };
            ```
            
            - 読み取り専用にプロパティをする
            
            ```tsx
            class Animal {
              readonly kind: string;
            
              constructor(kind: string) {
                this.kind = kind;
              }
            
              changeKind() {
                this.kind = "cat"; // エラー: 'kind' は読み取り専用プロパティです。
              }
            }
            ```
            
        - 配列にreadOnlyを使う
            - 配列の型の前にreadOnlyを記載する事で適用される
            
            ```tsx
            const numbers: readonly number[] = [1, 2, 3];
            
            number[0] = 5;←エラーになる（読み取り専用）
            ```
            
        - タプル型に使う
            
            ```tsx
            const pair: readonly [number, string] = [1, "apple"];
            pair[0] = 2; // エラー
            ```            
    - ジェネリクス
        - 型の変数
            - <T>を使う事で様々な種類の型を同じ関数で使う事ができる
                - ＜＞の中に入るものは型パラメーターと呼ばれる
                    - Typeの頭文字でTが取られる事が多い
          - 汎用的で再利用可能なコードを書ける
        - 使い方
            - 関数名の後に<T>を記載する
                - ＜T＞は様々な型に対応する事ができる
                - (引数: T)と指定する事でTとした型の値を受け取る
                - ：Tは返り値の値の型はTである事を示す
            
            ```tsx
            function 関数名<T>(引数: T): T {
              // 関数の中身
            };
            ```
            
        - 実際の使用例
            - 文字列でも数値でも関数が使うことができる
            
            ```tsx
            function findElement<T>(items: T[], target: T): T | undefined {
              return items.find((item) => item === target);
            };
            // 数値の配列から要素を探す
            const numbers = [1, 2, 3, 4, 5];
            const targetNumber = findElement(numbers, 3);
            console.log(targetNumber); // targetNumberの型はnumber | undefined
            
            // 文字列の配列から要素を探す
            const strings = ["apple", "banana", "cherry"];
            const targetString = findElement(strings, "banana");
            console.log(targetString); // targetStringの型はstring | undefined
            ```            
    - callback関数に関して
        - コールバック関数とは
            - 関数の引数にその関数自身によって呼び出される関数が入ったもの
                - 関数の実行の後で実行される関数
        - シンプルなコード例：
            
            ```tsx
            function add(a: number, b: number, callback: (result: number) => void): void {
                const result = a + b;
                callback(result);
            }
            
            add(1, 2, (result) => {
                console.log(result); // 3
            });
            ```
            
            - この関数がとる引数は3つある
                - 2つの数値（a, b）
                - コールバック関数（callback）
                    - 計算結果を呼び出し元に返す
        - コールバック関数を使う事でUIの更新などもする事ができる
            
            ```tsx
            function processData(data: string[], callback: (result: string) => void): void {
                let result = "";
                for (const item of data) {
                    result += item.toUpperCase() + " ";
                }
                result = result.trimEnd();
                callback(result);
            }
            
            processData(["hello", "world"], (result) => {
                console.log(result); // "HELLO WORLD"
            });
            ```
            
            - 関数processDataは、文字列の配列（data）とコールバック関数（callback）を引数として受け取る
                - コールバック関数は (result: string) => void型
                - string型の引数を1つだけ取る、何も返さない
            - processData関数は、データ配列を繰り返し処理する。
                - 各文字列を大文字に連結して1つの結果文字列を生成
                - そして、コールバック関数を使用して、呼び出し元のコードに結果の文字列を返します。
            - この例では、processData関数のコールバックとして無名関数を渡しています。この無名関数は、1つの引数（result）を受け取り、コンソールにログを出力します。
        - setTimeoutを使った例：
            
            ```tsx
            function delayedGreeting(name: string, callback: (greeting: string) => void): void {
                setTimeout(() => {
                    const greeting = `Hello, ${name}!`;
                    callback(greeting);
                }, 1000);
            }
            
            delayedGreeting("John", (greeting) => {a
                console.log(greeting); // "Hello, John!"
            });
            ```
            
            - 関数delayedGreetingの受け取る引数
                - 文字列の引数（name）
                - コールバック関数（callback）
                    - コールバック関数は、(greeting: string) => void型
                        - string型の引数を一つ取り、何も返さない
            - 関数delayedGreetingは、setTimeoutを使って1秒後にコールバックを実行し、挨拶文を作成してコールバック関数の引数として渡しています。
                - 関数delayedGreetingへのコールバックとして、無名関数を渡しています。この無名関数は一つの引数（greeting）を受け取り、コンソールにログを出力する
            - この関数はsetTimeoutが終了した後にコールバックを使用してメッセージを出力する。これはデータの読み込みやアニメーション、ユーザーとのインタラクションなど、遅延が発生する可能性のある実世界のシナリオを扱う場合によくあるパターンです。
        - 少し複雑な例：
            
            ```tsx
            function getUserData(userId: number, callback: (user: { name: string; age: number }) => void): void {
                const users = [{ id: 1, name: "John", age: 30 }, { id: 2, name: "Jessica", age: 25 }];
                const user = users.find((u) => u.id === userId);
                callback(user);
            }
            
            let user;
            getUserData(1, (data) => {
                user = data;
            });
            
            console.log(user); // { id: 1, name: "John", age: 30 }
            ```
            
            - getUserData関数が受け取る引数
                - ユーザーID（userId）
                - コールバック関数（callback）
                    - コールバック関数は、(user: { name: string; age: number }) => void型
                        - { name: string; age: number }型の引数を1つだけ取る。
                            - 何も返さない
            - getUserData関数は、引数userIdと同じIDを持つユーザーをusers配列から見つけ、コールバック関数を使用してユーザーデータを呼び出し元のコードに返します。
            - また、コールバックを使ってUIを更新することもできる。
                - ユーザー情報を取得するリクエストを行う
                    - アプリに名前や年齢を表示したい場合
                        - データが返ってきた後にコールバックでUI変更を実行すること可能
        - UI更新のコールバック関数
            
            ```tsx
            getUserData(1, (data) => {
                const nameLabel = document.getElementById("name");
                const ageLabel = document.getElementById("age");
                nameLabel.innerText = data.name;
                ageLabel.innerText = data.age;
            });
            ```
    - 非同期処理
      - JavaScript同様にイベント駆動型の非同期プログラミング
        - Promiseやasync/awaitを使って非同期処理を実装する
    - シングルスレッドモデル
      - シンプルで分かりやすいコードを実現する
        - イベントループ
        - 非同期処理
          - これらでタスク処理をコントロールする
    - 演習
        - 引数に型を指定する
            - 要件
                - yearToDate関数の引数に適切な型を示す
            - ユーザー体験
                - なし
            - 処理
                - yearToDate関数**は365日を一年として年数から日数を計算する関数**
                    - 引数として受け取るものは年数（数字）
                    - 呼び出し元に返す値は日数（数字）
        - 1番背が高い人を探す関数`getHighestPersON` 関数を作成する
            - 要件
                - `Person`型を定義する
            - ユーザー体験
                - 無し
            - 処理
                - Typeを使ってデータの型を示す
                - 配列の要素を一つずつ検証して1番数値が高いものを探す
                
                ```tsx
                export function getHighestPerson(people: Person[]) {
                  // ここに処理
                  let maxPerson: Person = people[0];
                  for (let i = 0; i < people.length; i++) {
                    if (maxPerson.height < people[i].height) {
                      maxPerson = people[i];
                    }
                  }
                  return maxPerson;
                }
                ```
                
                - 変数maxPersonを定義する
                    - データの型はPersonとする
                - peple[0]
                    - 受け取った配列になっている引数の0（最初の要素）を取得する
                - for分を使う
                    - 変数iを0と定義する
                    - 変数iから引数として受け取ったpepleの引数の要素の数まで
                        - if (maxPerson.height < people[i].height) {maxPerson = people[i];}}を実行する
                            - if文
                                - maxPerson.height < people[i].height
                                - maxPersonのheightプロパティとpeopleに対して変数iで定義したインデックス番号の要素のheigtを比較する
                                    - 条件に一致するのであれば変数maxPersonにpeople[i]を代入する
                            - 最終的にmaxPersonに代入される要素は1番背が高い要素になる
                - maxPerson**を戻す**
        - ユーザープロフィールを更新するWebアプリ開発（年齢の更新）
            - 要件
                - ユーザ情報を登録、更新する
                    - 年齢の入力をする際に
                        - 数値としての年齢
                        - 文字列としての年齢
                    - ２通りの登録方法ができてしまうという不整合がおきる
                        - 年齢を登録する関数normalizeAgeInputは引数valueを持つ
                            - valueの型はunknownとする
                            - valueが文字列であれば文字列を返す
                            - valueが数値であれば文字列に変換して返す
                            - それ以外はエラーとする
            - ユーザー体験
                - 文字列、数値どちらでも年齢の登録が可能になる
            - 処理
                - 用意されているコード
                
                ```tsx
                export function normalizeAgeInput() {}
                
                normalizeAgeInput(23); // -> "23"
                normalizeAgeInput("30"); // -> "30"
                ```
                
                - export function normalizeAgeInput()
                    - 引数
                        - value : unknown
                - {}
                    - if (typeof value === “string”){ return normalizeAgeInput(value); }; else (typeof === “number”){ String(value);  return normalizeAgeInput(value);}
                - 回答したコード
                
                ```tsx
                export function normalizeAgeInput( value : unknown) {
                  if (typeof value === "string") {
                   return normalizeAgeInput(value); }
                  else (typeof value === "number") {
                    return String(value); }
                }
                
                normalizeAgeInput(23); // -> "23"
                normalizeAgeInput("30"); // -> "30"
                
                //回答のコード
                //関数normalizeAgeInputの型も指定する
                //ageはstringとして全て登録するため型はstringで指定する
                export function normalizeAgeInput(value : unknown):string {
                  if (typeof value === "string") {
                   return value; }
                  else if (typeof value === "number") {
                    return String(value); }
                  throw new Error("年齢の形式が不正です。");
                }
                
                normalizeAgeInput(23); // -> "23"
                normalizeAgeInput("30"); // -> "30"
                ```
                
        - タイプガードを使う
            - 要件
                - チャットアプリを作成する
                    - メッセージがテキスト型か画像型か判断する関数を定義する
                    - メッセージの種類に応じて処理を変える
                        - テキストの場合
                        
                        ```tsx
                        <div class="text-message">
                          <p>テキストメッセージ</p>
                        </div>
                        ```
                        
                        - 画像の場合
                        
                        ```tsx
                        <div class="image-message">
                          <img src="https://example.com/image.png" />
                        </div>
                        
                        ```
                        
            - ユーザー体験
                - なし
            - 処理
                - 型の判別をする
                    - 対象となる型はMessage
                        - 内容：
                            
                            ```
                            type TextMessage = {
                              type: "text";
                              text: string;
                            };
                            
                            type ImageMessage = {
                              type: "image";
                              url: string;
                            };
                            ```
                            
                        - textタイプとimageタイプの２通りがある
                            - 2つのタイプを判別するis関数を作成する
                                - 引数としてmessageを受け取る
                                - messageの型はMessageになる
                            - タイプガードを実装する
                            
                            ```tsx
                            // タイプガードを実装してください
                            export function isTextMessage(message: Message): message is text {
                              // この関数の中身を実装してください
                              return typeof message === "text";
                            }
                            
                            // タイプガードを実装してください
                            export function isImageMessage(message: Message): message is image {
                              // この関数の中身を実装してください
                              return typeof message === "image";
                            }
                            ```
                            
                - メッセージの種類の応じて処理を変える
                    - typeof演算子を使ってif文とtypeof演算子で型に応じて処理を修正する
                    
                    ```tsx
                    export function showMessage(message: Message) {
                      // この関数の中身を実装してください
                      if (isTextMessage(message))
                    	  return {
                    	  <div class="text-message">
                    		  <p>テキストメッセージ</p>
                    		</div>
                    		};
                    	else if (isImageMessage(message))
                    		return {
                    		<div class="image-message">
                    		  <img src="https://example.com/image.png" />
                    		</div>
                    		};
                    }
                    
                    console.log(showMessage({ type: "text", text: "hello" }));
                    console.log(
                      showMessage({ type: "image", url: "https://example.com/image.png" })
                    );
                    ```
                    
        - 配列の要素（数値）を全て足して返すsum関数を作成する
            - 要件
                - 与えられた配列（文字列と数値が混ざっている）
                    - const array = [1, "2", 3, "4", 5];
                - 配列の要素（数値）を全て足して返すsum関数を作成する
            - ユーザー体験
                - なし
            - 処理
                - 配列内の要素が文字列と数値が混ざっている
                    - 要素を全て数値にして新しい配列itemsを作成する
                        - **.map(Number)**
                    - 新しく作成した配列itemsを引数に渡す
                        
                        ```
                        export function sum(items) {
                          // ここに実装してください
                          
                        }
                        ```
                        
                    - その数値を全て足して返す
                        
                        ```
                        
                        let sum: number = 0;
                        
                        for (let i = 0; i < numbers.length; i++) {
                          sum += numbers[i];
                        }
                        ```
                        
            - 自分で回答したコード
            
            ```tsx
            const array: [number, string, number, string, number] = [1, "2", 3, "4", 5];
            
            const items = array.map(Number);
            
            export function sum(items) {
              // ここに実装してください
              let sum: number = 0;
              for (let i = 0; i < items.length; i++){
                sum += items[i];
              }
            }
            
            console.log(sum(array));
            ```
            
            - 答えのコード
            
            ```tsx
            const array = [1, "2", 3, "4", 5];
            
            //配列の数値と文字列を全て合計するsum関数を定義する
            //引数として受け取った配列をitemsと定義する
            //itemsの型はstringもしくわnumberどちらも取りうる
            //sum関数の戻り値は数値とする
            export function sum(items: (string | number)[]): number {
            	変数resultを初期値が0として定義する
              let result = 0;
              //for文で変数iを0として定義する
              //変数iが配列の要素の数より小さい場合
              //iに1を加えて処理を実行する
              for (let i = 0; i < items.length; i++) {
            	  //itemをitems[i]としてコピーする
                const item = items[i];
                //if文でtypeof演算子を使いitemが文字列の場合には処理を行いそれ以外がelseの処理を行う
                if (typeof item === "string") {
            	    //変数resultに対してitems[i]がコピーされたitemを引数にとってparseIntを使い
            	    //文字列を推測される(数学的記数法の底)に基づいて数値に変換されてresultに追加される
                  result += parseInt(item);
                } else {
                  result += item;
                }
              }
              return result;
            }
            
            console.log(sum(array));
            
            //文字列を数値に変換してくれる
            //string単体で入れた場合には推測に応じた数学的記数法の底の数値に変換される
            parseInt(string)
            //文字列と指定した数学的記数法の底の数値に変換される
            parseInt(string, radix)
            ```
            
        - 任意プロパティを使ってゲームのキャラクター情報を管理するシステムを作る
            - 要件
                - キャラクター情報を管理する
                    - 用意されている配列
                    
                    ```tsx
                    const characters: Character[] = [
                      {
                        name: "アルド",
                        race: "人間",
                        job: "戦士",
                        level: 1,
                      },
                      {
                        name: "ミヤビ",
                        race: "エルフ",
                        job: "魔法使い",
                        level: 10,
                      },
                      {
                        name: "クラウディア",
                        race: "人間",
                        level: 5,
                      },
                      {
                        name: "ユウ",
                        race: "人間",
                        job: "僧侶",
                        level: 3,
                      },
                    ];
                    ```
                    
            - ユーザー体験
                - なし
            - 処理
                - キャラクター情報を管理する
                    - キャラクターの型、情報を管理する関数の型を定義する
                        - 型の定義
                            - Character型
                                - プロパティ
                                    - 名前・文字列：任意
                                    - 種族・文字列：任意
                                    - 職業・文字列：任意（職業は持っていないキャラクターもいる）
                                    - レベル
                                    
                                    ```tsx
                                    type Character = any;
                                    
                                    プロパティ
                                    name
                                    race
                                    job
                                    level
                                    ```
                                    
                            - Query型
                                - プロパティ
                                    - 名前・文字列：任意
                                    - 種族・文字列：任意
                                    - 職業・文字列：任意
                                    - レベル・数値：任意
                    - 情報を管理する関数を作成する
                        - findCharacter関数
                            - 引数として配列charactersと呼び出し元から受けとる型がQueryである値の変数queryを受け取る
                            - 戻り値の型はCharacter型とする
                        - if文を使って返す値を変更する
                    - 答え
                        
                        ```tsx
                        {
                        //filter関数を使い、配列charactersに対して引数をcharacterと取った時にif文を使って条件分岐を行う
                        return characters.filter((character) => {
                        	//変数queryのnameプロパティと変数characterのnameプロパティが
                        	//変数queryのnameプロパティと一致しない場合にはfalseを返す
                          if (query.name && character.name !== query.name) {
                            return false;
                          }
                          //変数queryのraceプロパティと変数characterのraceプロパティが
                        	//変数queryのraceプロパティと一致しない場合にはfalseを返す
                          if (query.race && character.race !== query.race) {
                            return false;
                          }
                          //変数queryのjobプロパティと変数characterのjobプロパティが
                        	//変数queryのjobプロパティと一致しない場合にはfalseを返す
                          if (query.job && character.job !== query.job) {
                            return false;
                          }
                          //変数queryのlevelプロパティと変数characterのlevelプロパティが
                        	//変数queryのlevelプロパティと一致しない場合にはfalseを返す
                          if (query.level && character.level !== query.level) {
                            return false;
                          }
                          //変数queryと変数characterの値が等しい場合にはtrueを返す
                          return true;
                        });
                        ```
                        
        - 人の名前を扱うPersonクラスを定義する（readOnly）
            - 要件
                - Personクラスを定義する
                    1. Personクラスを定義する
                    2. コンストラクタでPersonクラスのプロパティを引数として受け取る
                    3. 変更不可（読み取り専用に変更する）
                    4. メソッドを作成してフルネームを返す
            - ユーザー体験
                - なし
            - 処理
                - 
- React＋TypeScriptの概要
    - React
        - UIコンポーネントを作成するJavaScriptのフレームワーク
    - TypeScript
        - JavaScriptに型の概念を追加した静的型付け言語
    - Reatに型の概念を使っているものがReact＋TypeScript
- React+TypeScriptの仕様
    - コンポーネントに型を追加する
        - コンポーネントの型を定義する事で
            - どんな情報を受け取るか明確になる
            - どんな情報を返すのか明確になる
        - Propsに型の定義をする
            
            ```tsx
            type Props = {
              name: string;
            };
            ```
            
        - 定義したPropsを受け取るコンポーネントで型の定義をする
            
            ```tsx
            import React from "react";
            type Props = {
              name: string;
            };
            function Hello(props: Props) {
              return <div>Hello, {props.name}</div>;
            };
            ```
            
    - React.ReactNode
        - React要素の型
            - Reactでレンダリングできるあらゆるものを表現できる
        - コンポーネントを入れ子構造にする
            - テキスト
            - 画像
                - など、複数の型が必要になる場合に使われる
                    - 様々なReactの要素を扱う事が必要な場合に必要になる
        - 使用例：
            
            ```tsx
            import React from "react";
            import type { ReactNode } from "react";
            
            // Propsの型定義で、childrenプロパティがReact.ReactNode型であることを宣言
            type Props = {
              children: ReactNode;
            };
            
            // Boxコンポーネントは、どんなReact要素も子要素として受け取れる
            function Box({ children }: Props) {
              return (
                <div className="box">
                  <div className="box-content">{children}</div>
                </div>
              );
            };
            
            // Appコンポーネントでは、Boxの中にテキストを入れている
            function App() {
              return <Box>ここに内容</Box>;
            };
            ```
            
            現状のコードではPropsとしてここに内容という要素しか受け取っていないが{children}として他の要素を受け取る事も可能
            
    - イベントハンドラーに型の指定をする
        - Reactのイベントに型を指定する事でハンドラーから受け取る値を明確にする
            - クリックイベント
                - handleClick関数に型をつける
                    - React.MouseEvent型を使う
                        - MouseEventのインポート
                            - マウスに関連するイベント（クリック、マウスオーバー）
                        
                        ```tsx
                        import React from "react";
                        import type { MouseEvent } from "react";
                        ```
                        
                    - HTMLButtonElement
                        - クリックイベントが発生したHTML要素を渡す
                    - event.targetとevent.currentTargetの違い
                        - event.targetはイベントバブリングの影響を受ける可能性がある
                            - 子要素から親要素へ順に伝わっていく事
                                - buttun内のsapan要素の場合
                                    - buttonを指定したいのにspanが指定されてしまうなどの可能性がある
                        - event.currentTargetはイベントハンドラーが発生した要素を取得する
                            - イベントが発生したHTML要素を取得したい場合にはevent.currentTargetを使うのが安全
            - 入力された要素に型を指定する
                - ChangeEvent型を使う
                    - ChangeEventのインポート
                    
                    ```tsx
                    import React from "react";
                    import type { ChangeEvent } from "react";
                    ```
                    
                - 入力フィールドを指定するためにHTMLInputElementをchangeイベントに渡す
                    
                    ```tsx
                    import React from "react";
                    import type { ChangeEvent } from "react";
                    
                    function App() {
                      // ChangeEvent<HTMLInputElement>型を使って、イベントオブジェクトの型を正確に指定
                      const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
                        console.log(event.target.value); //ここでevent.target.valueの型がstringであることが保証される
                      };
                    
                      return <input onChange={handleChange} />;
                    };
                    ```
                    
                    - event.target.value
                        - event.targetはイベントが発生したHTML要素の事を示す
                        - イベントが発生したvalueプロパティを指定している
                            - input要素のvalueプロパティは標準でstringのため型の指定はなし
    - useStateの型を定義する
        - useStateで扱う変数の値の型をジェネリクス＜T＞を使って定義する
            - useStateには型の定義が必要な場合と不要な場合の２通りがある
                - useStateは初期値を元に変数の型を推論する能力がある
                    - 必要な場合：
                        - 空の配列やnullが初期値となっている場合
                            
                            ```tsx
                            import { useState } from "react";
                            const [users, setUsers] = useState([]);
                            // 👆 初期値が空の配列のため推論が効かない
                            ```
                            
                    - 不要（必要ない）場合：
                        - 単純なuseStateで初期値が設定されている場合
                            
                            ```tsx
                            import { useState } from "react";
                            const [count, setCount] = useState(0);
                            ```
                            
                            ```tsx
                            import { useState } from "react";
                            const [users, setUsers] = useState([
                              { name: "John", age: 20 },
                              { name: "Mike", age: 30 },
                            ]);
                            ```
                            
                - 型の指定方法
                    
                    ```tsx
                    import { useState } from "react";
                    const [users, setUsers] = useState<{
                    	 name: string; age: number 
                     }[]>([]);
                    ```
                    
    - useReducerと型定義
        - useReducer複数の状態管理を1つにしてまとめる事ができるHook
            - 状態（`State`）とアクション（`Action`）の型を定義する事が一般的
        - カウンターアプリの例：
            - 状態の型の定義
                
                ```tsx
                type State = {
                  count: number; //カウンターの値
                };
                ```
                
            - アクションの型定義（Action）
                - actionは通常、型プロパティを持つ
                    - 複数のアクションを管理するためにユニオン型にする事が多い
                
                ```tsx
                type Action =
                  | { type: "INCREMENT" } // カウントを1増やす
                  | { type: "DECREMENT" } // カウントを1減らす
                ```
                
            - レデューサー関数の定義（Reducer）
                - レデューサーから受け取った情報を元に現在の状態とアクションの差分で新しい状態を返す。
                - Reducer関数のactionとtypeに定義した型を適用させる
                
                ```tsx
                type State = {
                  count: number; //カウンターの値
                };
                
                type Action =
                  | { type: "INCREMENT" } // カウントを1増やす
                  | { type: "DECREMENT" } // カウントを1減らす
                
                function counterReducer(state: State, action: Action): State {
                  switch (action.type) {
                    case "INCREMENT":
                      return { count: state.count + 1 };
                    case "DECREMENT":
                      return { count: state.count - 1 };
                    default:
                      throw new Error("未知のアクションタイプ");
                  }
                };
                ```
                
            - useReducerフックの定義
                - action.typeの型を定義しているため"INCREMENT"と"DECREMENT"以外の値はエラーが発生するようになる
                
                ```tsx
                import { useReducer } from "react";
                
                type State = {
                  count: number; //カウンターの値
                };
                
                type Action =
                  | { type: "INCREMENT" } // カウントを1増やす
                  | { type: "DECREMENT" } // カウントを1減らす
                
                function counterReducer(state: State, action: Action): State {
                  switch (action.type) {
                    case "INCREMENT":
                      return { count: state.count + 1 };
                    case "DECREMENT":
                      return { count: state.count - 1 };
                    default:
                      throw new Error("未知のアクションタイプ");
                  }
                };
                
                const initialState: State = { count: 0 };
                
                const [state, dispatch] = useReducer(counterReducer, initialState);
                
                ```
                
    - 演習
        - useRef
            - 要件
                
                **1.** `useSliderRef`という名前のカスタムフックを作成しましょう！
                
                このフックは、スライダーの動きをコントロールするために、DOM要素への直接参照を作成し、管理する役割を持ちます。
                
                **2.** useRef フックを使って、DOM要素を参照してください。
                
                **3.** useRefに適切な型を指定してください。
                
            - ユーザー体験
                - スライダーで画像がスムーズに移動する
            - 処理
                - `useSliderRef`関数を定義する
                    - useRef
                        
                        ```tsx
                        function useSliderRef() {
                          // useRefを使ってこの関数を実装してください
                          const sliderRef = useRef<HTMLInputElement>();
                          return sliderRef;
                        }
                        ```
                        
                    - buttonと紐付ける
                        - 関数コンポーネントなので関数を返すためにreturnが必要
                - bottonタグにrefをつける
                - useRefに型をHTMLInputElementとして定義する
                    
                    ```tsx
                    onClick={() => {
                              const container = sliderRef.current;
                              if (container) {
                                container.scrollLeft -= scrollAmount;
                              }
                    ```
                    
        - useReducer
            - 要件
                - クイズアプリの状態管理部分を作成する
                    - 4 択のクイズを 1 問ずつ表示する
                    - 回答すると、正解か不正解かを表示する
                    - 「次に進む」ボタンを押すと、次のクイズを表示する
                    - すべてのクイズに回答したら、結果を表示する
                        - 上記の条件を満たすようなReducer関数を作成する
            - ユーザー体験
                - 4択のクイズが回答できる
                - 次に進むボタンをクリックする事で次のクイズを表示できる
            - 処理
                - Reducer関数を作成する
- 概念
    - 型という概念
        - 変数の宣言時に宣言する変数が持っているデータの種類を示す方法
            - 型の種類：
                - **number**（ナンバー）
                    - 数字を扱う型
                        
                        ```tsx
                        const age: number = 20;
                        const score: number = 100;
                        ```
                        
                - **string**（ストリング）
                    - 文字列を扱う型
                        - 変数に代入する文字列をダブルクウォーテーションorシングルクウォーテーションで囲む
                        
                        ```tsx
                        const name: string = "mosyabo";
                        ```
                        
                - **boolean**（ブーリアン）
                    - true or false のどちらかの値を持つ型
                        - 条件式の評価を行う場合に使われる
                        
                        ```tsx
                        const isOpen: boolean = true;
                        
                        if (isOpen) {
                          console.log("ドアが開いています！");
                        } else {
                          console.log("ドアは閉まっています。");
                        }
                        ```
                        
                - **any**（エニー）
                    - 何でもありの型
                        - 便利な型であるばTypeScriptの型チェックが適用されないため極力使わないようにする事が必要
                        
                        ```tsx
                        const message: any = "こんにちは";
                        message = 10;
                        message = true;
                        
                        ```
                        
                - **型のエイリアス**
                    - typeというキーワードで既存の型に新しい名前をつける
    - プログラミングにおいてプログラムの重要な概念
        - 安全である事
        - 修正・改善などコードの保守がしやすい事


- 読んで学ぶTypeScript
  - 値・型・変数
  変数宣言: letとconst
  変数宣言の型注釈
  varはもう使わない
  変数宣言の型推論
  型推論と動的型付けの違い
  プリミティブ型
  boolean型
  number型
  string型
  null型
  undefined型
  undefinedとnullの違い
  symbol型
  bigint型
  型強制
  ボックス化
  リテラル型
  any型
  オブジェクト
  構造的型付け
  配列
  タプル
  列挙型
  ユニオン型
  判別可能なユニオン型
  インターセクション型
  型エイリアス
  型アサーション「as」
  constアサーション「as const」
  satisfies演算子 「satisfies operator」
  明確な割り当てアサーション
  typeof演算子
  等価であるということ
  truthyな値、falsyな値
  型のメンタルモデル
  - 文
  変数のスコープ
  if-else文
  三項演算子
  for-of文 - 拡張for文
  switch文
  switchのフォールスルー問題
  switchと変数スコープ
  例外処理
  never型
  制御フロー分析と型ガードによる型の絞り込み
  unknown型
  anyとunknownの違い
  - 関数
    関数宣言
    関数式
    アロー関数
    関数の型の宣言
    関数宣言と巻き上げ
    従来の関数とアロー関数の違い
    関数は値
    関数はオブジェクト
    戻り値がない関数とvoid型
    関数の引数
    値渡しと参照渡し
    オプション引数
    デフォルト引数
    残余引数/可変長引数
    this引数
    分割代入引数
    キーワード引数とOptions Objectパターン
    型ガード関数
    アサーション関数
    即時実行関数式(IIFE)
    コールバック関数
    オーバーロード関数
  - 非同期処理
    Promise<T>
    async
    await
  - オブジェクト指向
    クラス
    インターフェース
    JavaScriptとTypeScriptのオブジェクト指向機能の比較
  - JSX
  - 組み込みAPI
    Map<K, V>
    Set<T>
    Date
    RegExp
    Error
  - 🚧モジュール
  - import、export、require
  - シングルプロセス・シングルスレッドとコールバック
  - 型の再利用
    typeof型演算子
    keyof型演算子
    ユーティリティ型
    Mapped Types
    インデックスアクセス型
    Conditional Types
    infer
    ユニオン分配
  - ジェネリクス
    ジェネリクスが使われている標準ライブラリ
    型変数
    型引数の制約
    デフォルト型引数
    変性
  - tsconfig
    tsconfig.jsonを設定する
    オプションの一覧
    strict
    noImplicitAny
    strictNullChecks
    strictFunctionTypes
    strictBindCallApply
    strictPropertyInitialization
    noImplicitThis
    useUnknownInCatchVariables
    alwaysStrict
    noUnusedLocals
    noUnusedParameters
    exactOptionalPropertyTypes
    noImplicitReturns
    noFallthroughCasesInSwitch
    noUncheckedIndexedAccess
    noImplicitOverride
    noPropertyAccessFromIndexSignature
    isolatedModules
  - 型定義ファイル
    Advanced Topics
  - NPMパッケージ開発者のためのtsconfig
  デュアルパッケージ開発者のためのtsconfig
  ジェネレーター
  セッターとゲッター
  プロジェクト参照
- Tips
  オブジェクトを浅くコピーする
  オブジェクトをマージ (結合) する
  オブジェクトのサブセットを得る
  オブジェクトで受け、オブジェクトを返す
  コンパニオンオブジェクトパターン
  オブジェクトから型を生成する
  オブジェクトからキーの型を生成する
  オブジェクトからプロパティの型を生成する
  配列から型を生成する
  配列から全要素の型を生成する
- 索引:記号とキーワード
  - 記号
    ! 論理否定演算子 (logical not operator) js
    ! 非Nullアサーション (non-null assertion operator) ts
    ! 明確な割り当てアサーション演算子 (definite assignment assertion operator) ts
    !! Double Bang js
    != 不等価演算子 (inequality operator) js
    !== 厳密不等価演算子 (strict inequality operator) js
    " 文字列リテラル (string literal) js
    # プライベートプロパティ (private property) js
    $ ドル変数 (dollar variable) js
    $ 文字列中の変数展開 (placeholder) js
    % 剰余演算子 (reminder operator) js
    %= 剰余代入 (reminder assignment) js
    & ビット論理積 (bitwise and) js
    & インターセクション型 (intersection type) ts
    &= ビット論理積代入 (bitwise and assignment) js
    && 論理積 (logical and) js
    &&= 論理積代入 (logical and assignment) js
    ' 文字列リテラル (string literal) js
    () 即時実行関数の一部 (IIFE: immediately invoked function expression) js
    * 乗算演算子 (multiplication operator) js
    * ジェネレーター関数の宣言 (generator) js
    * yield*式 (yield) js
    *= 乗算代入 (multiplication assignment) js
    ** べき乗演算子 (exponentiation) js
    **= べき乗代入 (exponentiation assignment) js
    + 単項正値演算子 js
    + 加算演算子 (addition operator) js
    + 文字列結合演算子 (concatenation operator) js
    + 修飾子の付加 ts
    += 加算代入 (addition assignment) js
    ++ インクリメント (increment) js
    , 関数引数の区切り js
    , 配列要素の区切り js
    , オブジェクトプロパティの区切り js
    , タプル型の要素の区切り ts
    , カンマ演算子 (comma operator) js
    - 単項負値演算子 js
    - 減算演算子 (subtraction operator) js
    - 修飾子の削除 ts
    -= 減算代入 (subtraction assignment) js
    -- デクリメント (decrement) js
    . プロパティへのアクセス (dot operator) js
    ... スプレッド構文 (spread syntax) js
    ... 残余構文 (rest syntax) js
    / 除算演算子 (division operator) js
    / 正規表現リテラル (regular expression literal) js
    /= 除算代入 (division assignment) js
    // 一行コメント (one line comment) js
    /* 複数行コメント (multiline comment) js
    /** JSDoc
    : オブジェクトの一部 js
    : 三項演算子の一部 (conditional operator) js
    : 型アノテーション (type annotation) ts
    < 小なり演算子 (less than operator) js
    < ジェネリクス (generic) ts
    < JSX ts
    < 型アサーション (type assertion) ts
    <= 小なりイコール演算子 (less than or equal) js
    << ビット左シフト演算子 (left shift operator) js
    <<= 左シフト代入 (left shift assignment) js
    = 代入演算子 (assignment) js
    == 等価演算子 (equality) js
    === 厳密等価演算子 (strict equality) js
    => アロー関数の一部 (arrow function) js
    > 大なり演算子 (greater than) js
    >= 大なりイコール演算子 (greater than or equal) js
    >> ビット右シフト演算子 (right shift) js
    >>= 右シフト代入 (right shift assignment) js
    >>> 符号なし右シフト演算子 (unsigned right shift) js
    >>>= 符号なし右シフト代入 (unsigned right shift assignment) js
    ? 三項演算子の一部 (conditional operator) js
    ? オプション修飾子 (optional property) ts
    ?. オプショナルチェーン (optional chaining) js
    ?? Null合体 (nullish coalescing operator) js
    ??= Null合体代入 (logical nullish assignment) js
    @ デコレーター (decorator) ts
    [ 配列リテラル (array literal notation) js
    [ アクセッサー (bracket notation) js
    [ 配列の分割代入 (destructuring assignment) js
    [ インデックス型 (index signature) ts
    [] 配列型 (array type) ts
    文字列エスケープシーケンス (escaping character) js
    ^ ビット排他的論理和 (bitwise xor) js
    ^= ビット排他的論理和代入 (bitwise xor assignment) js
    _ 数値の区切り文字 js
    _ アンダースコア変数 js
    ` テンプレートリテラル (template literal) js
    { ブロック文 (block) js
    { オブジェクトの分割代入 (destructuring assignment) js
    | ビット論理和 (bitwise or) js
    | ユニオン型 (union type) ts
    |= ビット論理和代入 (bitwise or assignment) js
    || 論理和 (logical or) js
    ||= 論理和代入 (logical or assignment) js
    ~ ビット否定演算子 (bitwise not) js
    ~~ Double Tilde js
    キーワード
    as 型アサーション (type assertion) ts
    as const constアサーション (const assertion) ts
    const const js
    get ゲッター (get) js
    in in演算子 (in operator) js
    in for-in構文 js
    in Mapped Types ts
    is 型アサーション関数の一部 (user-defined type guard) ts
    keyof keyof型演算子 (keyof) ts
    n bigintリテラル (bigint literal) js
    typeof typeof演算子 (typeof) js
    typeof typeof型演算子 (typeof) ts
    set セッター (set) js
    void void演算子 (void) js
    void void型 (void) ts
- TypeScriptの学習リソース
  - 最終的にはドキュメントを読む必要があるという部分
    - ただ、英語で記載されているなどの障壁があるため難しい部分がある可能性がある
      - 読み方などのハンドブックを作成
- TypeScript Playgroundの使い方
  - ブラウザでTSの実行環境が用意されている
    - TSをインストールせずにブラウザで使用が可能になる
- 🚧TypeScript超入門 〜10分でわかるTypeScriptの概要〜
  - 今後、開設予定
            