- 進捗管理(全21題　1題　5/100)　〜3/26
    - 入門編 (30/100)
        1. ~~React入門1~~
        2. ~~React入門2~~
        3. ~~コンポーネントに動きをつける~~
        4. ~~コンポーネントのスタイリング~~
        5. ~~Hooksについて~~
        6. ~~リストの更新(全4レッスン)~~
        7. ~~リストの更新(全4レッスン)~~
    - 中級編 (1題 5% 60/100)  ~21
        1. ~~TypeScript(全10レッスン)~~ (35/100)
        2. ~~React＋TypeScript(全5レッスン)~~ (40/100)
        3. ReactでAPIに接続する(全6レッスン)  (45/100)3/3~4
        4. アニメーション入門(全3レッスン) (50/100)3/5
        5. フォームを作成する(全5レッスン) (55/100)3/6~7
        6. パフォーマンスを意識したフックの活用方法(全3レッスン) (60/100)3/8~9
        7. Router入門(全4レッスン) (65/100)3/10~11
        8. 知って差をつけるTyep Script(全7レッスン) (70/100)3/12~14
        9. コンポーネント間で共通する状態を管理する(全4レッスン) (75/100)3/15~16
        10. リントで綺麗なコードを書く(全5レッスン) (80/100)3/17~18
        11. Next.ベータ版(全8レッスン) (85/100)3/19~21
        12. 知って差をつけるNext.ベータ版(1レッスン) (90/100)3/21
    - 実践編 (10/100)   3/21~26(6日間)
        1. Reactでコンポーネントを作成する
        2. 簡単なメモアプリを作成しよう
- 学習ソース
    https://mosya.dev/react/dashboard
    https://ja.react.dev/learn
- Reactの概要
    - Reactとは？
        - JavaScriptのフレームワーク
            - JSXを使ってUIコンポーネントを作成するためのライブラリーである
                - Web 上の部品（UIコンポーネント）を作るためのもの
                    - コンポーネント
                        - ボタン
                        - フッター
                - UIを構築するためのJavaScirptライブラリ
                    - コンポーネント指向
                        - UIをコンポーネントに分けてプログラミングすること
                            - コンポーネントに分ける
                                - 再利用可能になる
                                    - 変更箇所が少ない
                                        - 保守。運用が楽になる
                                    - 可読性
                                    - 凝縮性が高くなる
        - Reactを使う理由
            - JavaScriptのみでもページは作成可能だが、ページが大きくなったり構造が複雑になると管理や表現、更新する事が難しくなる
                - Raectでコンポーネントに分ける事で共通化できる
                    - 利点：
                        - 繰り返して使ったり
                        - 他のページで使ったりする事ができる
                        - 変更が簡単になる
            - 生のJavaScriptのみでは難しい事もReactを使うことで実現できる
    - 開発者
        - Reactは、Facebook（現 Meta Platforms） によって開発された
    - Webページの基本構造
        - Webページの表示内容は基本、HTMLで書かれている
            - HTMLに対してCSSがスタイルを当てる事で見た目が整う
        - Reactではhtmlを表示するために関数を作成する（関数コンポーネント）
            - HTMLを表示する関数を作成する
    - JSX
        - JavaScriptの拡張機能である
            - Reactでコンポーネントの入れ子構造などを記載する際に視覚的に優れている言語である
                - HTMLと似た構文になっているがHTMLではなくJavaScriptの拡張機能
                    - Reactでは基本的にこのJSXで記載する
        - JSXを使う時の注意点
            1. JSX のタグは必ず閉じる
                - imgタグやinputタグのような通常の記載方法では終了タグが必要ないタグであっても必ず最後を/で閉じる
            2. JSX のタグは必ず一つの親要素で挟む
                - JSX のタグは、HTML のように複数の要素を並べて書くことができない
                    - １つの要素は１つの親要素で囲む必要がある
                        - その上でさらに<div>などを使って囲む
        
        ```jsx
        import React from "react";
        import {creatRoot} from "react-dom/client";
        
        import {app} from "./app"
        
        const root = creatRoot(document.getElementById("root"))
        →Domidがrootであるものを受け取る
        
        //JSXでも良いがコンポーネントを記載する
        root.render(<app />)
        
        ```   
    - Reactの特徴
        - JSXを返す関数コンポーネントをいくつも積み上げていって一つのアプリケーションを作っていくのがReactの特徴
        
        ```jsx
        const List = ({ items, className }) => (
          <nav className={className} style={{ marginTop: "10px" }}>
            <ul className="list">
              {items.map((item) => (
                <li key={item.id} className="item">
                  {item.label}
                </li>
              ))}
            </ul>
          </nav>
        );
        
        const Main = () => {
          const items = [
            { label: "react", id: "react" },
            { label: "vue", id: "vue" },
          ];
          return (
            <div className="main">
              <List className="nav" items={items} />
            </div>
          );
        };
        
        ```
        
        - 関数の最初は大文字で始める
            - listではなくListとする
    - Reactを使って開発する理由
        - JavaScriptとHTMLのみで開発する場合
            - 要素の追加、削除
            - フィルタリング
                - 複雑になってしまう
        - コンポーネントという概念のもと、コンポーネント単位で作業する事によって楽に作業する事が可能になる
            - 要素の削除や追加はPropsという機能を使うことでリレー式で値を渡せる
        - Hooksを使う事でページのレンダリングや値の更新を管理する
    - Reactを使う優位性
        - React以外にもUIを構築するためのライブラリは世の中にある
            - https://ja.vuejs.org/
            - https://svelte.dev/
        - 他のライブラリと比較してReactの利点
            - TypeScriptとの親和性
                - 現在の開発環境においてJavaScriptは使用されない事が多くなっている
                - TypeScriptを使用する事が主流になっている
                    - コンパイルが必要な言語
                        - JavaScriptにコンパイルされる
                    - TypeScriptが使用される要因
                        - 型の概念が追加されている
                            - プログラムの可読性
                            - 保守・点検的な面
                        - コンパイラーの機能が数年前の機能と比較にならない
                            - 大規模開発において型の概念が重要になる
                            - 型の概念がある方が大規模開発の場合には優位
                            - コンパイル後のパフォーマンスが動的言語より優位になる
            - 配布されているライブラリ数
                - Reactは世界で1番使用されているUIライブラリのため公開されているライブラリ数も多くなっている
                - ライブラリがある事でUIを1から作る必要がなくなる
    - オブジェクト指向
        - プログラムにおいて現実世界のものや概念をオブジェクトとして表現して、それらを組み合わせてシステムを構築するもの。
    - ライフサイクル
        - コンポーネントの表示から消えるまでの一連の処理
- Reactの仕様
    - JSX
        - React内でHTMLのようなマークアップをJavaScriptがかけるようになったJavaScrioptの拡張機能である
            - 根本的にはJavaScriptであるがHTMLのような階層構造で記載できるもの
                - ローカル開発におすすめなツールは全てJSXに対応する
        - JSX内でJavaScriptを使用する方法
            - JSXでは{}を使う事でJavaScriptの変数や式を直接埋め込む事ができる
                - JSX ＝＞ JavaScriptのスーパーセット
                    - JavaScriptであると明示的に示す事が必要になる
            - 戻り値として扱う値はJAXが理解できる値にする事が重要
        - 属性にJavaScriptの変数を埋め込む
            - 属性に変数を埋め込む
                - JSX内のタグに属性を指定する際、JavaScriptの変数を使う事もできる
                
                ```jsx
                function App() {
                  const url = "https://www.google.com";
                  return <a href={url}>Google</a>
                };
                ```
                
                - urlをhttps://www.google.comと定義する
                - aタグのherfに対して定数urlを{}で囲み展開する
            - JSXは直接オブジェクトやクラスを表示しようとするとエラーになってしまう
                
                ```jsx
                function App() {
                 const obj = {name: "Mosyabo"};
                 return <h1>{obj}</h1>
                }
                ```
                
                - オブジェクトを直接HTMLに変換する事ができない
                    - オブジェクトを表示する場合にはプロパティを指定するなどして具体的に値を絞る必要性がある
                    
                    ```jsx
                    function App() {
                      const obj = { name: "Mosyabo" };
                      return <h1>{obj.name}</h1>; 
                    }
                    // 画面には "Mosyabo" と表示される
                    ```
                    
        - JSXではコンポーネント指向でプログラムを構築する
            - 例：function App()という関数コンポーネント（関数を返すコンポーネント）
                - JavaScriptで
                    - 定数の定義
                        - const name= "mosyabo";
                    - 変数展開
                        - return <h1>Hello, {name}!</h1>
                            - をしている
                        - タグで囲まれた範囲内で変数を展開したい場合には{}で囲む
                            - 変数に定義された値が代入されるようになる
            
            ```jsx
            function App() {
             const name= "mosyabo";
             return <h1>Hello, {name}!</h1>
            }
            // 画面には "Hello, Mosyabo!" と表示される
            ```
            
        - 戻り値として扱える値
            - export app "./app"
             ↑
            - appコンポーネントの内部にはJSXが記載されている
                - JSXの内部には{}を記載する事でJavaScriptが記載できる
            - Reactにおいて呼び出す関数は例外があるが基本２種類ある
                - 値を返す関数
                    - 数値
                    - 文字列
                    - 配列
                    - JavaScript
                    - JSXでも呼べる
                    - {}
                - 関数の呼び出し方
                    - 関数名()
                - JSXを返す関数もある
                - JSX内でのみ呼べる
                    - <>で囲む事で呼べる
            - オブジェクトの定義
                - const オブジェクト名{プロパティ:値}
            - import
                - 他のファイルに書かれたコードやデータを自分のファイルで使えるようにする
                - JavaScript→JavaScriptは無理だがバイナリーファイルのみ受け取れる
            - export
                - 他のファイルでコード、データが使用できるようにする事
            - デフォルト	or 名前付き
                - 名前付き
                    - 決められた名前でimport,exportする事
                    - ファイルにおいて何回でも行える
                    - export exportしたい対象(なんでも良い
                        - 関数
                        - 型
                    - import { app } from "./app"
                    - 名前付きエクスポートする際には{}をつける
            - デフォルト
                - 名前をつけずにimport.exportする事
                - 1ファイルにつき1回のみ
                    - ファイルのpathのみでimportする
                        - 複数あるとわからなくなる
                        		 export defalut exportしたい対象(なんでも良い　関数、型)
                        		 import なんでもいい　from "ファイルのパス";
                        		 デフォルトインポートの場合には{}を使わない
                        		 その他の場合には使わない
                        		 分割代入という考え方がある
            
            ```jsx
            function add() {
            	return 1 + 1;
            }
            
            function app() {
             const hello ="hello";
             const url ="google.com";
             const obj ={name:"mutsukra"}
             console.log(obj);
             return <div>
            	 <div className="name">
            	 { hello }
            	 <nav />
            	 </div>
            	 <div>
            	 world
            	 <div/>
            	 { add() }
            	 <a href={ url }>url<a/>
            	 { obj.name }
             <div/>
            };
            
            function nav() {
             return <li>
            		 list
            	 </li>
             };
            ```
            
        - JSX内で数字を表示したい場合
            - {}で囲んだ中で数字を記載する
                - 関数展開ではないが{}を使う必要がある
        - JSX内で関数を実行する方法
            - JSX内で関数を実行する
                - JavaScriotの関数を呼び出す事が可能
                    - 関数の戻り値は数値、文字列、JSX要素になる事が必要
                
                ```jsx
                function getYear() {
                  return new Date().getFullYear();
                }
                
                function App() {
                  return <p>今は西暦{getYear()}年です。</p>
                }
                ```
                
            - getYear()関数は現在の年を数値で返します
                - JSXの中で表示する事ができる
                    - これは、関数の戻り値が「数値」のためJSXで表示する事が可能になっている
        - 属性にbooleanを表現したい場合
            - [**React booleanとは**](https://www.google.com/search?q=React+boolean%E3%81%A8%E3%81%AF&sca_esv=2f601072485c5a0d&rlz=1C5CHFA_enJP1142JP1143&sxsrf=AHTn8zoft_rAKiiUWjzFHCQS8akDHky_Ig%3A1737974176162&ei=oGGXZ4q7CaDe2roPkfzriQc&ved=0ahUKEwiKi5ir2pWLAxUgr1YBHRH-OnEQ4dUDCBA&uact=5&oq=React+boolean%E3%81%A8%E3%81%AF&gs_lp=Egxnd3Mtd2l6LXNlcnAiE1JlYWN0IGJvb2xlYW7jgajjga8yCBAAGIAEGKIEMggQABiABBiiBDIFEAAY7wUyCBAAGKIEGIkFMgUQABjvBUjcFVCVD1jGE3ABeAGQAQCYAZ4BoAG0BKoBAzAuNLgBA8gBAPgBAZgCA6ACvQLCAgoQABiwAxjWBBhHwgIFECEYoAGYAwCIBgGQBgqSBwMxLjKgB5kK&sclient=gws-wiz-serp)
                - 値がtrueの場合には属性の宣言だけで良く、属性＝trueが省略できる
    - トランスパイル
        - JSXは直接ブラウザーが理解する事ができない
            - JavaScriptに変換する事が必要
                - BabelなどのトランスパイラーでJavaScriptに変換される
        - どのようにトランスパイルで変換されるのか？
            - JSXでボタンの部品を書いた場合
            
            ```jsx
            <button className="btn">
              クリックしてね！
            </button>;
            ```
            
            - トランスパイラーで<botton>…</botton>をReact.createElementという関数を使ってJavaScriptに変換する
            
            ```jsx
            React.createElement(
              "button",
              { className: "btn" },
              "クリックしてね！"
            );
            ```
            
        - トランスパイラーが裏側でコードを変換している事でコードが実行できているか？確認しながら進める事ができる
        - コンパイル
            - TypeScriptも同様になっている
            - tsc(TypeScriptコンパイラー)が型のチェックやコンパイルをする
    - コンポーネント
        - React では、画面に表示する部品のことを「コンポーネント」と呼ぶ
            - ボタン
            - テキストボックス
            - ヘッダー
            - フッター
        - コンポーネントは独自のロジックと外見を持つUIの部品
            - マークアップを返すJS関数
        - なぜコンポーネントを作るのか？
            - 一度使ったコンポーネントは使い回す事ができる
            - コンポーネントにして部品毎でWebページを作成する事で設計がしやすい
                - チーム開発において
                    - コンポーネント毎に担当を分ける事ができる
                    - コンポーネント毎に名前をつける事ができる
                    - 変数の共有は少し煩雑になってしまう
                        - user contextというフックスが出てくる
        - 関数コンポートネント**（Function Component）**
            - 呼び出し元に対して表示内容をreturnで返すコンポーネント
                - 関数コンポーネント内はJSXで記載されているためレンダリングされてJavaScriptに変換される
                    
                    ```jsx
                    import react from "react" 
                    function app () {
                    	return <div　className="hello">hello</div>
                    };
                    ```
                    
                    - function App() { return <div>Hello</div>;}
        - コンポーネントにクラスを追加する
            - htmlではclassをつけてスタイルを当てる事で見た目を整える
            - Reactではclass名をつける時にはc**lassNameを使う**
                - className = "クラス名”
                    - class名をつける事でCSSを使ってスタイルを適用させる事が可能になる
                        - JavaScriptにおいてclassはすでに予約語になっているためclassNameを使う
                            - このclassNameがpropsと呼ばれたり、プロパティと呼ばれるもの
        - カスタムコンポーネントの使い方
            - 自身でカスタムしたコンポーネントを使う方法
                - 親コンポーネントで装飾する方法
                    - jsx要素(Bottomタグ)などに対して親コンポーネント内で処理を定義し子コンポーネントを作成する方法の場合にはボタンの処理内容を実行しても実行した内容が保存されずに画面に反映されない
                - Propsを受け渡す方法
                    - 親コンポーネント内で関数コンポーネントを作成しPropsを受け渡す方法
                        - 状態が保持され表示画面が更新される
        - コンポーネントを親コンポーネントの入れ子にする(children)
            - コンポーネントを使い回す事や、コードをスッキリ整理する事ができる
                - chiidren Propsという特別なPropsがある
                
                ```jsx
                親コンポーネント内
                <animal>
                	<dog name="nama">
                		<p> ”名前はdogです” </p>
                	<dog/>
                	<cat />
                </animal>
                
                -children-
                 <dog>
                		<p> ”名前はdogです” </p>
                <dog/>
                ↑
                dogからdogで囲まれた範囲をchildrenとする
                ハンバーガーで考える所のバンズとバンズで挟まれた部分になる
                
                dogコンポーネント内
                
                export function dog({ name, children }) {
                	return (
                	<div>
                		<h1>{name}</h1>
                		{children}
                		↑
                	  親コンポーネント内で記載された
                		<p> ”名前はdogです” </p>が入る
                	</div> 
                ```
                
                ```jsx
                App.jsx
                
                import {
                  Card,
                  CardImage,
                } from "./Card.jsx";
                
                export function App() {
                  return (
                    <div>
                      <Card title="タイトル1">
                        <p>ここに本文が入ります。</p>
                        <CardImage
                          src="https://static.mosya.dev/react-props-children/sample-img.png"
                          alt="サンプル画像"
                        />
                      </Card>
                      <Card title="タイトル2">
                        <p>ここに本文が入ります。</p>
                        <CardImage
                          src="https://static.mosya.dev/react-props-children/sample-img.png"
                          alt="サンプル画像"
                        />
                      </Card>
                    </div>
                  );
                }
                
                Card.jsx
                
                export function Card({
                  title,
                  children,
                }) {
                  return (
                    <div className="card">
                      <h1 className="card-title">
                        {title}
                      </h1>
                      <div className="card-text">
                        {children}
                      </div>
                    </div>
                  );
                }
                
                export function CardImage({
                  src,
                  alt,
                }) {
                  return (
                    <img
                      src={src}
                      alt={alt}
                      loading="lazy"
                      className="card-image"
                    />
                  );
                }
                
                App.jsx内で要素の内容を記載してCard.jsx内で{props}として情報を渡す
                Card.jsxで作成したコンポーネントをApp.jsX内では2回使用しているがコンポーネントの型に沿って2回記載する事で
                PropsとしてAppコンポーネントからCardコンポーネント（子コンポーネント）に情報が渡されて表示される
                コンポーネント指向でプログラムをする事の利点がある部分がこのコンポーネントを何回でも使える
                かつPropsで情報を渡せるという部分である
                ```         
    - コンポーネントのネスト
        ```JavaScript
        function MyButton() {
            return (
                <button>I'm a button</button>
            );
        }

        コンポーネントを宣言してネストする
        ↓
        export default function MyApp() {
            return (
                <div>
                <h1>Welcome to my app</h1>
                <MyButton />
                </div>
            );
        }
        ```
        - Reactにおけるコンポーネントは全て大文字で始める必要がある
            - HTMLは小文字であり、区別する
    - レンダリング
        - 表示画面にコンポーネントを直接表示する事はできない
            - React
                - コンポーネント指向
            - HTML
                - 階層構造
        - DOMでレンダリングを行った上で画面に表示する事が必要になる
            - **DOMでツリー構造に変換する**
                - DOMに変換されると、各要素はDOMノードと呼ばれる
                    - **DOMノードの取得、変更などを行う場合にはdocument.querySelectorを使う**
                        - DOMノードの取得
                            - IDを使って取得する方法
                                - document.querySelector("#ID名");
                                    - とする事で取得する
                                        - (”#ID名”)
                            - クラス名を使って取得する方法
                                - document.querySelector(".title");
                                    - とする
                                        - (”.クラス名”)
                            - HTMLを取得する場合に文字列として取得したい場合
                                - innerHTML（インナーHTML）を使う
                                
                                ```jsx
                                const animalElement = document.querySelector("#animal");
                                console.log(animalElement.innerHTML);
                                
                                ```
                                
                            - HTMLタグを除いてテキストのみを取得する方法
                                - textContentプロパティを使う
                                
                                ```jsx
                                const description = document.querySelector(".description");
                                console.log(description.textContent);
                                ```
                                
        - 実際に表示された画面を構成するファイルは何か？
            - App.jsの記載内容が表示されている
                - jsxは直接画面を構成する事はできないためレンダリングされて表示される
                    - index.html内のid属性がrootのdivタグにレンダリングされたAppコンポーネントが表示されている
    - import,export,default export
        - Webページには多くのコードや機能が組み合わさっている
            - 全てのものを一つのページで管理するのは大変
                - 区切りをつけてファイル毎にコードを管理するようにする
        - ファイル同士を繋げる役割をするのがインポートとエクスポートである
            - 必要な部分のコードのみを取り出す仕組み
        - インポート
            - 他のファイルにに書かれたコードやデータなどを自分のファイル内で使用できるようにする事
        - エクスポート
            - 他のファイルでも使用できるようにコードやデータをを公開する事
                - エクスポートとインポートどちらも行う事で他のファイルのもの使用できるようになる
            - 同じプロジェクト内にあるファイルを取り込む
                - 例：chara.jsというファイル内のcharacterという変数をインポート、エクスポートしたい場合
                - エクスポート（chara.js）
                
                ```jsx
                export const character = "mosyabo";
                ```
                
                - インポート
                
                ```jsx
                import { character } from "./chara.js";
                ```
                
                - ./は現在のディレクト内のという意味
        - **named export と named import**
            - {}でデータの名前を囲むのは特定のデータをexport,importしたいからである
                - 決められた名前で**データーを公開・取り込む方法の事を”named export と named import”と呼ぶ**
            - コンポーネントもimportする事ができる
                
                ```jsx
                import { Button } from "./button.jsx";
                ```
                
                - コンポーネントが含まれるファイルの拡張子は`.jsx`にすることが多い
        - export default（エクスポート デフォルト）
            - export default（エクスポート デフォルト）は、名前をつけずに関数を外部に公開する機能
                - 一つのファイルで `export default` は1回しか使えない
            
            ```jsx
            export default function greet() {
              console.log("Hello!");
            }
            
            export default const name ="kouki";
            ```
            
            - import
                - export defaultで公開された要素をインポートするときは、{}を使わずに自分の好きな名前でインポートできる
            
            ```jsx
            import greeting from "./functions.js";
            
            greeting(); // これで "Hello!" と表示される
            ```
            
            [公開されているライブラリーをimportする](https://www.notion.so/import-18a972e6c9608100b49fd810ad0b5da2?pvs=21)            
    - Props
        - 「**Props**」（プロップス）とは、「プロパティ」の略でコンポーネントに渡すデータのこと
            - コンポーネント間で情報を送ったりする方法
        - コンポーネントに情報を渡す際に属性として指定する事で必要な値を送る事ができる
        
        ```jsx
        <Card
         title="タイトル名"
          text="ここに本文が入ります"
        />;
        ```
        
        ```jsx
        function book(props) => {
          return <div>{props.name}<div/>
        };
         
          function JavaScriptの関数
          propsを渡すPropsにはname属性が指定されている
          nameプロパティを使ってBooknameを書き換える
        ```
        
        - 自分で作った属性（titleやtext）を使ってデータを渡している
            - 属性のようなものをPropsと呼ぶ
                - Propsを使って外からデータを渡したりする事で動き、見た目をカスタマイズする
        - コンポーネントでPropsを受け取る方法
            - Propsをオブジェクトとして受け取る方法
            
            ```jsx
            function Card(props) {
              return (
                <div className="card">
                  <h1 className="card-title">{props.title}</h1>
                  <p className="card-text">{props.text}</p>
                </div>
              );
            }
            ```
            
            ```jsx
            function Card(props){...}
            ```
            
            - Propsをオブジェクトとして扱いドット記法をする事でデータにアクセスする事ができる
                - props.titleやprops.textのような形になる
                    
                    ↑
                    
                - この書き方はどんなPropsも一度オブジェクトに入れてコンポーネント内で使っている形
            - 分割代入で受け取る方法
                - JavaScriptの分割代入を使って必要なデータを取り出す方法
                
                ```jsx
                function Card({ title, text }) {
                  return (
                    <div className="card">
                      <h1 className="card-title">{title}</h1>
                      <p className="card-text">{text}></p>
                    </div>
                  );
                }
                
                function Card({ title, text }) 
                ↑
                この書き方でtitleとtext2つのPropsを受け取っている
                ```
                
            - 分割代入の方法、オブジェクトに一度入れて記載する方法どちらでも大丈夫
                - 分割代入を使うと、props.titleと書く代わりに、titleと直接的に書ける
        - デフォルトの値を設定する
            - Propsにデフォルトの値を設定する事も可能
                
                ```jsx
                export function Card({ title = "タイトルなし", text })
                ```
                
            - titleというPropsに対して何も値が渡されなかった場合に渡される値になる
      - 親コンポーネントへのリフトアップ
        - 状態を管理する際に複数のコンポーネントがそれぞれ自分の状態を管理する方法ではなく、親コンポーネントがまとめて状態を管理する方法がある
          - 親コンポーネントへのリフトアップと呼ぶ
            - 今回の３目並べでの状態管理
              - const [squares, setSquares] = useState(Array(9).fill(null));
                - コンポーネントはvalueとしてpropsで情報を渡す
                  - 表示するコンポーネントでは値を定義する
                    - 'X' 、'O'、または空の場合は null 
        - Square コンポーネントが呼び出す関数から始める
          - その関数を onSquareClick関数と定義する
            - クリックに応じて関数が発火するようにする事ができる
        - ハンドル関数とオン関数で紐づける
          - ハンドル関数ないでは配列に対してインデックス番号を使ってさらにsliceメソッドなどを活用して新しい配列のコピーを作成して書き換える
            - ミューテーと
            - イミュータブル
        - 状態が変更されると再レンダーが起こる
          - しかし、差異がないコンポーネントに関してはレンダーをスキップしたい場面がある
            - その場合にはレンダリングをスキップする事ができる
              - イミュータブルの利点がある部分
    - Hooks
        [Hooksの内部プログラム](https://www.notion.so/Hooks-1a6972e6c96080bcb853f118d8dfadc6?pvs=21)
        - Hooksとは？
            - 関数コンポーネントでReactの機能を使えるようにしたもの
                - 関数コンポーネントは表示内容を呼び出し元に返すコンポーネント
                    - returnする時などにHooksを使う
                        - 無駄なレンダリングを防ぐ機能や、計算式や値、関数のメモ化を行うなど
            - 元々、Reactではクラスコンポーネントが主流になっていた。
                - 現在、関数コンポーネントに移行された
                    - Reactの機能をクラスを使用せずにコンポーネントでも使用できるようにしたのがHooks
            - 関数コンポーネント内でReactの機能が使えるようになったもの
                - 元々、Reactはクラスコンポーネントで使われていた
        - Rreactにおいて変わっていく要素を監視・管理するものをhooksという
            - useStateというHooksの例
                - const [todos,setTodos] = useState(0)
                    - setTodosによってtodosが更新された際にページをページを再レンダリングする
                        - 引数を渡すこともできる
                            - 初期値として渡された引数が用意される
                - todos
                    - オブジェクトとして扱う
                        - id
                        - name
                        - completed
            
            ```ruby
            <>
             <TodoList todos={todos} />
            </>
            propsと呼ばれるもの
            
            const TodoList = (props) => {
             return <div>{props.todos}</div>
             };
             {}はJavaScriptが記載できる
             
             const TodoList = ({todos}) => {
             return <div>{todos}</div>
             };
            ```
        - Hooks
            - 状態管理
            - ライフサイクル処理 ⇒ 初表示・更新・破棄されるまでの流れ
                - 元々、クラスコンポーネントの時代にあった機能を関数コンポーネントでも使えるようにしたもの           
            ![alt text](/Public/React_Hooks_Lifecycle.png.png)
            - useState
                - コンポーネントの状態を管理する
                    - クリックに応じて値が増えるコンポーネント
                        - 値の状態をuseStateで管理する
                            - 状態が変わるとコンポーネントを再レンダリングする
            - useEffect ⇒ 関数の実行タイミングをReactのレンダリング後まで遅らせるhook・外部システムと同期させるためのHook
                - 副作用
                    - 依存関係にあるものに応じた処理を実行するHooks
                        - コンポーネントのレンダリング時に副作用を与える
                            - 実行したい処理がある時が副作用
                    - 第一引数
                        - 副作用として実行される関数
                    - 第二引数
                        - 副作用を実行するタイミングをコントロールする依存関係
            - useCallback
                - 関数をメモ化するHooks
                - 依存関係にある値が変化した場合のみ再計算される
                - 依存関係に変化がなければ同じものを返す
                    - 対象：
                        - 特定の関数コンポーネントをメモ化する
                    - 目的：
                        - パフォーマンス向上のために使う
                    - 構文：
                        - useCallback(メモ化したい関数,[依存関係])
            - useMemo
                - 値のメモ化する
                    - 計算コストが高い時に使う処理
                        - 計算結果をメモ化する
                    - 構文：
                        - const 関数名 = () ⇒ {
                        const 関数名 = () ⇒ {
                        useMemo(() => hogeMemoFunc(), [])
                            - propeを渡したい場合には1つ目の関数に引数としてpropsを渡す
                - useCallbackとuseMemoの違い
                    - 関数自身をメモ化するか、関数の計算結果自身をメモ化するか？
            - useRef
                - DOMを参照するHooks
                    - スクロール処理の際に特定の要素をFocusする
                        - Focusした値をコンポーネント内で保持
                    - 構文：
                        - const inputElement = useRef(null)
                        ref={inputElement}
            - useContext
                - データをグローバルとみなす
            - useReducer
                - 状態を管理するHook
                    - useStateが内部実装されている
                        - 複数の状態管理が可能
                        - 構文：
                            - const [state, dispatch] = useReducer(reducer,'初期値')
            - useActionState
                - useActionState は、フォームアクションの結果に基づいて state を更新するためのフックです。
            - useTransition
                - useTransition は、UI を部分的にバックグラウンドでレンダーするための React フックです。

        - よく使う５つのHooks
            - useState
                [useStateの関数コード](https://www.notion.so/useState-1a6972e6c96080df9a2bdfc0ef9ca8fd?pvs=21)
                - 状態を管理するためのHook
                    - データの状態
                        - クライアント側のデータの状態
                            - 例えば、トグルが閉じてるor開いている
                                - 動的なページにおいてデータは一定ではなく変化するもの
                    - 状態という概念
                        - Reactは状態が変わった時をトリガーとしてレンダリングを行う
                            - 状態の変化に応じてレンダリングを行う
                            
                            ```jsx
                            const [管理したい状態,更新する関数]　= useState(isOpen)
                            ```
                            
                            [useStateというHooksの例](https://www.notion.so/useState-Hooks-194972e6c96080a19578e637b44dcc5f?pvs=21) 
                            
                - 関数などを使ってデータに変化を持たせた場合
                    - 実行する事でデータ自体は変化しているが表示画面が更新されないため実際の表示画面に変化が起きない
                        - データに変更が起きた時にページをレンダリングする役割を持つのがuseStateになる
                            
                            ```jsx
                            const handleClick = () => { 
                            	setCount(count + 1);
                            };
                            ```
                            
                - ページのレンダリングされる理由
                    - 仮想DOMを使っている
                        - 前の状態
                        - 後の状態
                            - 変更が起きたと検知したら前と後の差分を検証する
                                - 変更された要素のみを仲介しているReactがReal DOMへレンダリングする
                        - 必要な部分のみがレンダリングされるためパフォーマンスに良い
            - useEffect
                
                [useEffect関数のコード](https://www.notion.so/useEffect-1a6972e6c9608007a307d0dcb243bb43?pvs=21)
                
                - 副作用を処理するHooks
                    - 副作用とはデータの取得、特定の値に変化が起きた際に処理が発火するもの
                        - コンポーネントが画面に表示が本来の仕事である
                            - 画面の表示の副作用(追加の処理)としてuseEffectが使われる
                - データの取得、特定の値が変わった時に処理を行う
                    - 依存配列を使う
                        - 空の場合には初回のレンダリングで一回のみ実行される
                            - ページが表示される瞬間にページを取得する
                        - 値が入っている場合
                            - 依存関係にある状態変数の状態が変化した時に何らかの処理を行う
                    - 副作用があるためできるだけ使わない
                        - 最後の手段になる
                            - 何らか副作用が起きる
                                - React外のものと同期する際には必要になってくる
                - 発火のタイミングを決める事ができる
                    - マウント前
                    - マウント後など
                - 厳格なモードだと2回発火してしまう
                    - React.StrictMode
                - useEffectの記載例
                    
                    ```jsx
                    依存配列が空のuseEffect
                    →画面のレンダリング時に一度発火する
                    useEffect(() => {
                      console.log("Hello Hooks");
                    },[]);
                    
                    依存配列に依存関係となる変数が入っているuseEffect
                    →依存関係にある変数の状態が変化した時に発火する
                    useEffect(() => {
                      console.log("Hello Hooks");
                    },[count]);
                    ↑
                    発火するタイミングは引数内の第2引数に入っている状態変数に由来する
                    依存関係を作成する
                    useEffect内でset関数を使ってしまうと無限ループになってしまうので注意が必要
                    set関数を使いたい場合には関数を挟む必要あり
                    
                    useEffect(() => {
                      /* 第1引数には実行させたい副作用関数を記述*/
                      console.log('副作用関数が実行されました！')
                    },[依存する変数の配列]) // 第2引数には副作用関数の実行タイミングを制御する依存データを記述
                    
                    useEffect(() => { 実行したい処理　} ,[トリガーとなる値]);
                    ```
                    
                - useEffectの動作手順
                    - 依存関係が空のuseEffectの場合
                        - JSXがHTMLに変換されて画面にレンダリングされクライアントの端末に表示される
                        - useEffectが発火して処理内容が実行される
                    - 依存配列に依存関係になる変数がある場合
                        - JSXがHTMLに変換されて画面にレンダリングされクライアントの端末に表示される
                        - クライアントの操作などによって依存関係にある変数の状態が変わった時に処理が発火する
                - クリーンアップ関数
                    - 例えば、コンポーネントの表示と共にタイマーが開始される機能を作成する場合
                        - カウントを開始した後にコンポーネントの表示が終了した際に処理を終了したい
                            - 終了しない事で裏側で常に処理が走ってしまいリソースの無駄になってしまう
                                - useEffectの最後にクリーンアップ関数”return () => {};”を記載する事で終了できる
                    
                    ```jsx
                    import React, {
                      useEffect,
                      useState,
                    } from "react";
                    
                    export function App() {
                      const [count, setCount] = useState(0);
                    
                      useEffect(() => {
                        // ここでカウントアップを開始する
                        const timer = setInterval(() => {
                          setCount(
                            (prevCount) => prevCount + 1
                          );
                          //set関数を使うためsetInterval関数を挟んでいる
                        }, 1000);
                    
                        // 👇 このコンポーネントが画面から消えた時に実行される
                        return () => {
                          // ここでタイマーを解除
                          clearInterval(timer);
                        };
                      }, []);
                    
                      return <div>{count}</div>;
                    }
                    
                    ```
                    
                - 依存関係を使ってAPIからデータを取得する
                    
                    ```jsx
                    import {　useEffect,　useState,　} from "react";
                    
                    function Todo({ id }) {
                    //idをPropsとして渡す
                      const [todo, setTodo] =　useState(null);
                      //useStateをsetTodoをトリガーとしてtodoの値で管理する。初期値はnullとする
                    
                    	//useEffectを定義する
                      useEffect(() => {
                    	  //fetch APIを使ってHTTPリクエストを行う
                    	  //取得したいデータを{id}を使ってユーザーのリクエストに応じてリクエストする
                        fetch(`/api/mock/todo/${id}`)
                    	    //thenを使って実行する関数へ引数を渡す
                    	    //response.jsonにresponseを引数として渡す
                          .then((response) =>response.json())
                          //setTodo(json)にjsonを引数として渡す
                          .then((json) => setTodo(json));
                      }, [id]); // 👈 ここにidを指定する(第二引数)
                    
                    	//もし、todoの中身がnullなどのfalseと同等の場合にはreturn nullとして処理を終了する
                    	//もし、todoの中身がある場合（true）には処理を実行しない
                      if (!todo) {
                        return null;
                      }
                      //todoのtitleとcompletedに応じて完了or未完了を表示する
                      return (
                        <div className="todo">
                          <h1>{todo.title}</h1>
                          <p>
                            {todo.completed
                              ? "完了"
                              : "未完了"}
                          </p>
                        </div>
                      );
                    }
                    
                    export function App() {
                      const [id, setId] = useState("1");
                    
                      const handleChange = (e) => {
                        setId(e.target.value);
                      };
                    
                      return (
                        <div>
                          <div className="selectbox">
                            <select
                              onChange={handleChange}
                              value={id}
                            >
                              <option value="1">
                                Todo 1
                              </option>
                              <option value="2">
                                Todo 2
                              </option>
                              <option value="3">
                                Todo 3
                              </option>
                              <option value="4">
                                Todo 4
                              </option>
                            </select>
                          </div>
                          <Todo id={id} />
                        </div>
                      );
                    }
                    
                    ```                    
            - useRef
                
                [useRefの関数コード](https://www.notion.so/useRef-1a6972e6c9608066ac58ff2c8513977a?pvs=21)
                
                - 指定したHTMLタグの値を参照する事ができるHooks
                    - Ref
                        - レファレンスの略
                            - 参照するという意味
                    - 例：
                        - input属性のcurrent value属性を参照すると入力された文字列を取得できる
                - ミュータブルなもの
                    - レンダリング間で値を保持する事が可能
                        - 値が更新されてもレンダリングされない
                    - useStateとuseRefの違い
                        - useStateは値の更新が起きるとコンポーネントのレンダリングが起きてしまう
                        - useRefはレンダリング間で値を保持する事が可能になる
                - 値の更新、保持、参照
                    - 値を更新すると共にレンダリングする
                        - useState
                            - useStateはレンダリングで値を保持できない
                                - レンダリングがトリガーされてしまう
                    - レンダリングは起こしたくないけど値を保持したい
                        - useRefを使う
                            - .currentプロパティの使用
                                - useRefで更新した値は.currentプロパティに保存される
                                    - 値を更新する場合には.currentプロパティを更新する形とする
                    - 値の参照
                        - Refの値は.currentプロパティを使って値を取得する
                            - .current
                                - 値を参照をして、そこに代入する事で値の更新を行う
                - 記載方法
                    
                    ```jsx
                    import { useRef } from "react";
                    
                    seRefはuseStateと同じように任意の初期値を引数として渡す事ができる
                    const 変数 = useRef(初期値);
                    初期値を0とするuseRef
                    const ref = useRef(0);
                    
                    const ref = useRef(0);
                    console.log(ref.current); // 0
                    
                    .currentプロパティに対して値を代入する事で値の更新を行う
                    ref.current = 1;
                    
                    ```
                    
                - 注意点（useEffect）
                    - useEffectの依存配列としてuseRefは入れても意味がないため注意する必要がある
                        - useRefは状態の変化が起きてもレンダリングされてない
                - DOM要素に直接アクセスする
                    - useRefの意味は参照する(レファレンス)という意味である
                        - DOM要素の参照もする事が可能である
                    - ボタンを押すとテキスト入力欄にフォーカスされるコード
                    
                    ```jsx
                    import React, { useRef } from "react";
                    
                    export function App() {
                      // useRefを使って、DOM要素の参照を保持する
                      const inputRef = useRef(null);
                    
                      const handleClick = () => {
                        // input要素にフォーカスを当てる
                        inputRef.current.focus();
                      };
                    
                      return (
                        <div>
                          {/* inputRefをinput要素のrefプロパティに渡す */}
                          <input
                            ref={inputRef}
                            type="text"
                          />
                          {/* handleClickをbutton要素のonClickプロパティに渡す */}
                          <button onClick={handleClick}>
                            フォーカスする
                          </button>
                        </div>
                      );
                    }
                    ```
                    
                - 基本的な流れ
                    - 初期値を引数として渡す際にDOM要素を参照する場合にはnullを使用するのが一般的
                        - useRefで定義した変数を参照したい要素にref属性とする事でアクセスする事ができる
                    
                    ```jsx
                    import React, { useRef } from "react";
                    const 変数 = useRef(初期値);
                    const inputRef = useRef(null);
                    ```
                    
                    - inputタグにref属性をつける
                        - inputRef変数を使ってinput要素へアクセスする
                    
                    ```jsx
                    <input ref={inputRef} type="text" />
                    ```
                    
                    - 参照する
                    
                    ```jsx
                    console.log(inputRef.current); // <input type="text" />
                    ```
                    
                    - フォーカスを当てる方法
                    
                    ```jsx
                    inputRef.current.focus();
                    ```
                    
                    - Chart.jsを使ってグラフを表示する
                    
                    ```jsx
                    import Chart from "chart.js/auto";
                    import React,{ useRef,useEffect } from "react";
                    
                    const backgroundColor = [
                      "rgba(255, 99, 132, 0.2)",
                      "rgba(54, 162, 235, 0.2)",
                      "rgba(255, 206, 86, 0.2)",
                      "rgba(75, 192, 192, 0.2)",
                      "rgba(153, 102, 255, 0.2)",
                      "rgba(255, 159, 64, 0.2)",
                    ];
                    
                    const borderColor = [
                      "rgba(255, 99, 132, 1)",
                      "rgba(54, 162, 235, 1)",
                      "rgba(255, 206, 86, 1)",
                      "rgba(75, 192, 192, 1)",
                      "rgba(153, 102, 255, 1)",
                      "rgba(255, 159, 64, 1)",
                    ];
                    
                    export function VoteChart({ data, labels, label }) {
                      const chartRef = useRef(null);
                    
                      useEffect(() => {
                        if (!chartRef.current) {
                          return;
                        }
                        const myChart = new Chart(chartRef.current, {
                          type: "bar", // チャートの種類を選択
                          data: {
                            labels,
                            datasets: [
                              {
                                label,
                                data,
                                backgroundColor,
                                borderColor,
                                borderWidth: 1,
                              },
                            ],
                          },
                        });
                    
                        return () => myChart.destroy();
                      }, []);
                    
                      return (
                        <div>
                          <canvas ref={chartRef}></canvas>
                        </div>
                      );
                    }
                    ```                   
            - useCallBack
                
                [useCallbackの関数コード](https://www.notion.so/useCallback-1a6972e6c9608005ab97d1b30501c5db?pvs=21)
                
                - メモ化されたCallBack関数を返すHooks
                    - 関数そのものを返す
                        - 依存配列が存在する
                            - 依存配列が変更しない場合には再利用する
                                - 依存配列が変更された場合には再生成する
                                    - useMemoは値をメモ化する
                - ラッピングして第2引数に依存関係を状態変数で作成する事でレンダリング時に実行されないようにする事ができる
                    - レンダリング時に関数を実行されないようにする事ができる
                        - メモ化された関数が実行されて状態変数に変化が起きた際に再計算を行うメソッド
                - Reactは親コンポーネントが実行された際に子コンポーネントも一緒に実行されるという仕組みがあり、親コンポーネントの実行時に必ず、子コンポーネントも一緒に実行されるのを防ぐ
                    - 子コンポーネントを実行しない場合にuseCallBackを使用する
                    
                    ```jsx
                    useCallback(メモ化する関数, [依存関係となる状態変数]);
                    ```                   
            - useMemo
                
                [useMemoの関数コード](https://www.notion.so/useMemo-1a6972e6c96080069f6cc3fc4f5e467d?pvs=21)
                
                - 計算にコストがかかる再計算を防ぐ
                    - 処理のメモ化をするHooks
                - Reactのパフォーマンスを上げるためのHooks
                    - ブラウザのキャッシュに保存する事をメモ化するという
                        - ブラウザに保存する事で簡単に値を取得する事ができる
                    - setCountが呼び出された時に差分を確認するためにコードを全て読み込む
                        - 必要な時のみに実行されるようにする
                            - 依存関係を作成して依存関係にないものが読み込まれた際にはブラウザににある以前のメモリにあるキャッシュを呼び出すようにする
                - 使う時に全体をラッピングする
                    - 第2引数に依存関係を作成する
                - プロジェクトの大きさによって使用の有無が出てくる
                    - デプロイしてから処理が重いとなったら原因をuseMemoにする
                        - 全ての処理をuseMemoにするとブラウザのメモリがオーバーヘッドになってしまう
                - 計算結果をメモ化する事でコストをセーブする
                    - 再レンダリング時に関数が再計算される事を防ぐ
        - 5つ以外にもHooksは多くあり全部で20〜30種類程ある
            - useContext
                
                [useContext](https://www.notion.so/useContext-1a6972e6c960803e85cec574c7c1b79b?pvs=21)
                
                - Reduxという概念と近い
                    - Reactではコンポーネントを多く使う
                        - コンポーネントは親と子の関係になっている
                            - コンポーネント間はPropsを使ってデータを受け渡している
                                - Propsのバケツリレーではデータの出所がわからなくなってしまう。
                    - useContextを使用する事で直接データを渡す事ができる
                        - 以前はReduxという空間に入れていた
                - useContextを使用する際の変数は1番最初も大文字で始める
                    - Globalで使いたいデータを変数でまとめる
                        - まとめた変数にuseContextで使用できるようにしたとわかる変数に代入する
                            - const ShinCodeContext = creatContext(shincodeInfo);
                    - 全体で使えるようにするためにはコンポーネントをProviderで囲む
                        - valueとしてデータを入れた変数を指定する必要あり
                            - export defalut としておく
                - 使いたいコンポーネントで変数を定義し、useContext(変数とする)
                    - 使いたい場所で変数名.プロパティ名とする事で使うことができる
                        - どののコンポーネントでも共通して使いたい情報などがある場合に使用される
                            - ユーザのログイン情報などなど
            - useReducer
                
                [useReducerの関数コード](https://www.notion.so/useReducer-1a6972e6c9608046a32de284e6062d33?pvs=21)
                
                - 複数の値や状態を1つの関数でまとめて管理するHooks
                    - 複雑な状態管理を1つの関数でまとめる事でコードをシンプルに保つ
                        - 関数コンポーネントを作成し処理をswitch文を使う事が多い
                            - swich
                                - caseで条件に応じた処理を行う
                                - defaultで条件に合わない場合に対応する
                - Reducerという概念
                    - データや状態の倉庫
                        - UIからのアクションやペイリードをEvent HandlerがDispatchを作りStoreに入る。
                        - Reducerに情報が入る
                        - StateからRedcerに現在の状態が参照される
                        - Dispatchからきた更新する情報とRedcerの現在の情報を合わせて結果を返す
                            - 作成できる機能の例として
                                - swichを使い条件に応じて
                                    - 足し算される場合
                                    - 引き算される場合
                                    - 何もない場合を作る事などが可能
                - UseReducerの処理の流れ
                    - 下の図であれば
                        - UIでEventが発火する
                        - Event HandlerでDispatchを作成
                        - DispatchでAction Objectが作成されてReducerに送られる
                        - Reducerでstateの現在の状態とStateの更新をする情報が作成されstateに渡される
                        - Stateでイベント発生前の状態を参照して更新された情報を合わせてコンポーネントへ返す
                        - レンダリングされて表示される
                        
                        ![スクリーンショット 2025-02-19 22.28.35.png](attachment:f36ebfae-50ca-43b3-96b6-f30362ab0e74:スクリーンショット_2025-02-19_22.28.35.png)
                        
                - useStateと似ているHooks
                    - useStateと似ているHooksだが、useReducerは状態を更新する関数の定義や複雑な状態管理を行う事ができる
                - 実際の記載例（カウンターアプリ）
                    - シンプルなカウンターアプリ
                        - ーと＋のボタンがあるアプリでクリックに応じて数値が増減する
                            - UseReducerのインポート
                            - Reducer関数の定義
                                - 今回であればcounterReducerの部分
                                    
                                    ```jsx
                                    function 状態更新関数(現在の状態, アクション) {
                                      switch (アクション.type) {
                                        case "アクションの種類":
                                          // アクションの種類に応じた状態更新の処理
                                          return 新しい状態;
                                        default:
                                          return 現在の状態;
                                      }
                                    }
                                    ```
                                    
                            - 実際の記載例として
                                - counterReducerは引数としてstate,actionを取る
                                    - state=カウントの状態
                                    - action=新しい状態
                                        - INCREMENT　カウントを1増やす
                                        - DECREMENT　カウントを1減らす
                                        - default  何もない場合には現在の状態をそのまま返す
                                    
                                    ```jsx
                                    const counterReducer = (state, action) => {
                                      switch (action.type) {
                                        case "INCREMENT":
                                          return state + 1;
                                        case "DECREMENT":
                                          return state - 1;
                                        default:
                                          return state;
                                      }
                                    };
                                    ```
                                    
                        - シンプルなカウンターアプリのソースコード
                            - useReducerのインポート
                            - Reducer関数の定義
                                - state, actionを引数に取る
                                    - state→現在の状態
                                    - action→アクションの内容
                                - switch分でaction.typeに応じて返す処理を分岐する
                                    - INCREMENTの場合
                                        - stateに1を足してreturnする
                                    - DECREMENTの場合
                                        - stateを1減らしてreturnする
                                    - caseに一致するものがない場合
                                        - state（現在の状態）を返す
                            - useReducerフックの定義
                                - useReducerは引数にReducer関数と初期値を取る
                                - このフックを呼び出す事で状態変数とdispatchを得る事ができる
                                
                                ```jsx
                                **・基本構文
                                const [状態, dispatch] = useReducer(
                                	状態更新関数, 
                                	初期状態, 
                                	初期化関数
                                	);**
                                ```
                                
                            - useReducerで取得したdispatchに関数を呼び出しアクション内容などを渡す
                                
                                ```jsx
                                <button onClick={() => dispatch({ type: "INCREMENT" })}>+</button>
                                <button onClick={() => dispatch({ type: "DECREMENT" })}>-</button>
                                
                                dispatch(/* ここに変更内容を書く */);
                                ```
                                
                        
                        ```jsx
                        import { useReducer } from "react";
                        
                        function counterReducer(state, action) {
                          switch (action.type) {
                            case "INCREMENT":
                              return state + 1;
                            case "DECREMENT":
                              return state - 1;
                            default:
                              return state;
                          }
                        }
                        
                        export function App() {
                          const [count, dispatch] = useReducer(
                            counterReducer,
                            0
                          );
                        
                          return (
                            <div className="counter-box">
                              <div className="counter-header">
                                <div className="counter-header-inner">
                                  <h3 className="counter-title">
                                    Counter
                                  </h3>
                                  <p className="counter-text">
                                    下のボタンを押してみよう👇
                                  </p>
                                </div>
                              </div>
                              <div className="counter-actions">
                                <button
                                  onClick={() =>
                                    dispatch({
                                      type: "DECREMENT",
                                    })
                                  }
                                  className="counter-button"
                                >
                                  -
                                </button>
                                <div className="counter-count">
                                  {count}
                                </div>
                                <button
                                  onClick={() =>
                                    dispatch({
                                      type: "INCREMENT",
                                    })
                                  }
                                  className="counter-button"
                                >
                                  +
                                </button>
                              </div>
                            </div>
                          );
                        }
                        
                        ```
                        
                - Reducerを使う利点
                    - useReducerを使う事で複数の状態を管理しない場合などには複数のuseStateが必要になるものがまとめる事ができ、複数の状態を一つのオブジェクトとして管理する事ができる
                        - 特にHooksの中で関数を定義せずにHooksの外で純粋な関数としてロジックを組む事ができる
                            - 使い回す事やテストなどが楽になる利点もある
                    - useStateの場合
                    
                    ```jsx
                    //3つのusestateが必要
                    const [name, setName] = useState("");
                    const [age, setAge] = useState(0);
                    const [email, setEmail] = useState("");
                    ```
                    
                    - useRecucerの場合
                        - Reducer関数の定義
                            - 現在の状態stateとaction内容を引数に取り
                        - switch分でaction内容に応じて呼び出し元に返す内容を分岐させる
                            - ...state（現在の状態を展開）にnameをプロパティとして、action.payloadから送られてきたデータを対応する値として新しい状態を返す
                        - フックを呼びだす
                            - 現在の状態とdispatchによって処理されるアクション内容を受け取る
                            - useReducerの引数にはReducer関数であるuseReducerと初期値initialStateが入る
                    
                    ```jsx
                    const userReducer = (state, action) => {
                      switch (action.type) {
                        case "SET_NAME":
                          return { ...state, name: action.payload };
                        case "SET_AGE":
                          return { ...state, age: action.payload };
                        case "SET_EMAIL":
                          return { ...state, email: action.payload };
                      }
                    };
                    
                    const [state, dispatch] = useReducer(userReducer, initialState);
                    ```                   
            - カスタムフックス
                - 自分で作成したい機能を作る事ができる特別なHooks
                    - useStateやuseEffectなどのReactが提供しているフックを組み合わせて作る
                - 複数箇所で使うロジックなどをカスタムフックにまとめる事で複数回同じコードを記載する必要がなくなり、ロジックをコンポーネント間で共有する事ができる
                - カスタムフックを作成する場合にはuse…と関数の名前をつける
                    - useから始める事でReactがフックであると認識できる
                    
                    ```jsx
                    function useMosyaCustomHook() {
                    	//useStateをstateを監視する変数としてsetStateをトリガーとしてレンダリングを行う
                      const [state, setState] = useState(null);
                    
                    	//useEffectを定義してuseMosyaCustomHookが発火した時に一度のみ発火する処理を定義する
                      useEffect(() => {
                        // 何らかの処理
                      }, []);
                    
                    　//クリーンアップ関数を定義する事でStateの値を呼び出し元に返した上でreturnによって処理を終了する
                      return state;
                    }
                    ```
                    
                    - カスタムフックを使う利点
                        - 再利用がしやすい
                            - 変更箇所が少なくなる
                            - メンテナンスも楽になる
                        - 機能毎に分ける事ができる
                            - 構造が明確になって可読性が高くなる
                                - 開発効率が向上する
                    - カスタムフック作成時に参考になるライブラリー
                        - ‣
    - Reactに備わっている機能(関数、イベント、演算子)
        - オプショナルチェイニング
            - プロパティが存在しない可能性のあるオブジェクトに安全にアクセスする方法
                - そもそも、プログラム内で意図的にデータをnullやundefinedにする事がある。
                    - nullやundefinedにしたデータを使用してしまうとエラーが発生してしまう。
                        - そもそも、データがnullの場合などにはデータが存在しないためエラーになってしまう
                            - user.address?.city
                            - user.address?.postcode
                - null
                    - わざと空にした値
                - undefined
                    - まだ何も設定されていない状態
            - ?. という記号を使う
                - プロパティがnull,undefinedの場合にはundefinedを返してエラーを防ぐことができる
        - 条件演算子（　？　：　）
            - 単純にYes or No で答えられるような条件の場合に使用される
                - if文を使用するよりも短く記載することができる
                
                ```jsx
                var seijin = (age < 20) ? "未成年です":"成人しています";
                変数 = 条件 ? 値１ : 値２;
                変数が条件に一致する or しない
                する場合　値1を使い
                しない場合には値2を使う
                ```
                
        - pushuメソッド
            - Array インスタンスのメソッド
                - 配列の末尾に指定した要素を追加するメソッド
                    - また、返り値として配列の新しい長さを返す事もできる
        - Null 合体演算子
            - ?.だけの場合、プロパティに対応するデータが存在しない場合にはなにも表示されてない
                - JavaScript の演算子である??を使う
                
                ```jsx
                左辺の式 ?? 右辺の式
                ```
                
            - 左辺の式が`null`または`undefined`では**ない場合** : 左辺の式の値が結果となる
            - 左辺の式が`null`または`undefined`で**ある場合** : 右辺の式の値が結果となる
                - デフォルトの値を設定する際などにも活用される事が多い
                    - ?.でエラーを表示しないように対策を行い
                    - ??でユーザー側にメッセージを送る事ができる
        - Fragmentについて
            - **Fragment**
                - プログラムにおける部品、カケラ、断片
            - **ReactにおけるFragmentとは？**
                - 複数の要素を一つにまとめるためのもの
                    - divタグを使う事で複数の要素をまとめる事も可能だがdivタグを使いすぎてしまう事で形が崩れてしまう可能性などがある
                        - 例えば、ログインしている状態とログインしていない状態で表示を分けたい場合に使われる
                        
                        ![image.png](attachment:956068a6-4888-4b71-8fad-fc70529d3881:image.png)
                        
                        - isLoggedInがtrueでない場合にはFragmentタグで囲まれたログインボタン、新規登録ボタンを表示する
                        - isLoggedInがtrueの場合にはマイページへのボタンを表示する
                        
                        ```jsx
                        import { Fragment } from "react";
                        
                        export function TermsList({ items }) {
                          return (
                            <dl>
                              {items.map((item) => (
                                <Fragment key={item.term}>
                                  <dt>{item.term}</dt>
                                  <dd>{item.definition}</dd>
                                </Fragment>
                              ))}
                            </dl>
                          );
                        }
                        ```
                        
                    - `Fragment`コンポーネントを使う方法
                        - 複数の要素を<Fragment></Fragment>で囲む
                            - `Fragment`にはkeyを設定する事ができる
                                - 特に、リスト表示などをする際に使用する
                    - `<>`と`</>`（空のタグ）を使う方法
                        - <> </>で囲む
                            - keyを設定する事はできない
                                - リストなどの表示ではない場合に使用する
        - onClick関数
            - カードをクリックするとカードの名前を元に特定のメッセージが表示されるようにするようなロジックを組む
                - hanndle ClickとしてonClickが発火した時にどのような処理を発火させるか？
            - 
        - readOnly
            - オブジェクトを直接変更できないようにする
            - ネストされたオブジェクトにreadOnlyは必要ない
                - Reactはイミュータブルな言語である
                    - 直接的にオブジェクトを変更する事は好ましくない
                        - そのためreadOnlyが必要なオブジェクトにはエラーが発生するようになる
        - onChange
            - フォーム入力内容などの状態が変化した際に発生するイベント
                - フォームの入力内容が変更などに対応する事ができる
                    - useStateを使って状態の管理
                        
                        ```jsx
                        //textをsetTextをトリガーとして管理するuseState
                        function App() {
                          const [text, setText] = useState("");
                        }
                        
                        //inputタグのtypeはtextにする
                        //valueをtextとする事でuseStateのtextとリンクさせる
                        //onChangeはイベントオブジェクトのtarget.valueを受け取る
                        //target.valueは現在のテキストボックス内容である
                        <input 
                        	type="text" 
                        	value={text} 
                        	onChange={
                        		(e) => setText(e.target.value)} 
                        />
                        
                        //textとして管理された値を表示する
                        <p>入力された内容 </p>
                        <div>{text}</div>
                        
                        ```
                        
        - コールバック関数
            - 渡す引数に応じて処理内容を変える事ができる関数
                - 親関数に対して引数を渡してcallback関数を定義する
                - 子関数(callback関数を引数とする関数)を定義する
                - 親関数を子関数の引数として呼び出す
            - コールバック関数の役割
                - 同じ内容の関数であってもコールバック関数の内容を変える事で処理内容を変更できる
                - 特定のタイミングで処理を実行する事ができる
        - 配列に対して操作を行うメソッド
            - 条件を一つのみ取得する場合
                - find関数
            - 条件を全て取得したい場合
                - filter関数
            - 配列内、全ての要素に対して処理を行いたい場合
                - map関数
                    - 配列をリストとして表示する(map関数)
                        - map関数を使って配列のデータをリストに変換する
                            - Reactでリストを作成する場合にはリストの各項目にkeyという属性を追加する必要がある
                                - リスト内のアイテムが追加、削除、編集される時
                                    - リスト全てをチェックするのではなく、keyを見て変更を把握する
                            - keyの書き方
                                - key={}と記載する
                                    - keyの値は一意の値を入れる
                                - keyの値を入れない場合にはインデックス番号が使われる
                                    - 基本、一意のデータを入れるようにする。
                            - オブジェクトの配列をリストにする
                                - map関数を使ってオブジェクトからデータを取り出す
                                    
                                    ```jsx
                                    function App() {
                                      return (
                                        <ul>
                                          {fruits.map((fruit) => (
                                            <li key={fruit.id}>{fruit.name}</li>
                                          ))}
                                        </ul>
                                      );
                                    }
                                    ```
                                    
                                - 配列に対してmap関数を使う
                                - 配列内の要素を変数fruitに代入する
                                - li要素を用意する
                                - 用意した要素にkeyをmap関数でオブジェクトが代入された変数のidプロパティに対応する値とする
                                - map関数で代入されたオブジェクトのnameプロパティに対応する値を代入する
        - 処理が終了する特定のタイミング
            - returnは実行するとその関数の処理は終了したという事になる
                - プログラムを記載する順番を注意する
    - React Router
      - React Routerにおいてページ間の遷都を管理できるようにする事が重要である
        - historyオブジェクト
          - history.push('/home');
            - 新しいエントリを履歴スタックに追加し、その位置に遷移します。
          - history.replace('/home');
            - 現在のエントリを新しいもので置き換え、その位置に遷移します。
          - history.goBack();
            - 履歴スタックの前のエントリに遷移します。
          - history.goForward();
            - 履歴スタックの次のエントリに遷移します。
    - 動的なページを作成する
        - コンポーネントの表示を条件によって切り替える
            - 論理AND演算子
                - 条件に応じてコンポーネントを表示する、しないを設定する事ができる
                    - ＆＆(論理AND演算子)を使って条件がtrueの場合のみ表示する事ができる
                        - {条件 && <表示したいコンポーネント />;}
                            - trueの場合には表示したいコンポーネントが表示されて、falseの場合には何も表示されない
                - 変数の状態
                    - true or false
                - 例えば、ユーザーのログイン機能が実装されているシステムと仮定して
                    - ログイン済みのユーザー(true)
                        - ログインしています。
                    - ログインしていないユーザー(false)
                        - 表示されない
                    - ＆＆(論理AND演算子)を使用すると条件がtrueの場合のみ表示する事ができる
                        - これを活用することでユーザがログインしている時にだけ表示したい内容などを作成する
                        
                        ```jsx
                        const isLoggedIn = true;
                        //isLoggedInを先に定義する
                        //ログイン状態というものを定義しておいて条件が満たされた場合にログイン状態と定義する
                        export function App() {
                          return (
                            <div>
                              {isLoggedIn && (
                                <p>ログイン済みです</p>
                              )}
                              //isLoggedIn変数がtrueの場合には<p>ログイン済みです</p>が表示されるようにする
                            </div>
                          );
                        }
                        
                        ```
                        
                    - ログインしていないユーザー
                        - ログインしていません。
                            - などのように表示を切り替える事ができる
                                - `!`演算子で条件を逆にして、`&&`と一緒に使う
                        
                        ```jsx
                        import React from "react";
                        
                        // LoginStatusコンポーネントの定義
                        function LoginStatus(props) {
                          return (
                            <div>
                              {props.isLoggedIn && (
                              //propsプロパティ、isLoggedInがtrueの場合に表示する
                                <p className="message-box info">
                                  ログイン済みです
                                </p>
                              )}
                              {!props.isLoggedIn && (
                              //propsプロパティ、isLoggedInがtrueではない時に表示する
                                <p className="message-box error">
                                  ログインしていません
                                </p>
                              )}
                            </div>
                          );
                        }
                        
                        export function App() {
                          return (
                            <div>
                              <LoginStatus isLoggedIn={true} />
                              <LoginStatus isLoggedIn={false} />
                              //Appコンポーネント内でLoginStatusコンポーネントで定義したisLoggedIn関数を使う
                              //子コンポーネントで定義した内容を親コンポーネントで表示する
                            </div>
                          );
                        }
                        
                        ```
                        
            - 三項演算子を使ってコンポーネントの表示を切り替える
                - JavaScriptの三項演算子を使う方法
                    - 条件が真(true)or偽(false)を判定して、true or falseに応じたコンポーネントを返す
                        - コンポーネントにPropsを渡して、コンポーネント内で三項演算子を記載する
                - 実際の開発現場では、2つのみの開発現場は少ないため三項演算子を投げて記載する
                
                ```jsx
                function LoginInfo({ isLoggedIn }) {
                  return (
                    <div>
                      {isLoggedIn ? (
                        userType === "admin" ? (
                          <p>管理者としてログイン済みです</p>
                        ) : userType === "member" ? (
                          <p>会員としてログイン済みです</p>
                        ) : (
                          <p>ゲストとしてログイン済みです</p>
                        )
                      ) : (
                        <p>ログインしていません</p>
                      )}
                    </div>
                  );
                }
                
                ※注意点
                三項演算子を繋げて記載する事でコードがグチャちゃになる事があるため注意が必要
                
                ```
                
                ```jsx
                function LoginInfo({ isLoggedIn }) {
                  return (
                    <div>
                      {isLoggedIn ? (
                      userType === "admin" ? (<p>管理者としてログイン済みです</p>) 
                      : 
                      userType === "member" ? (<p>会員としてログイン済みです</p>)
                      : 
                      (<p>ゲストとしてログイン済みです</p>)) 
                      ↑
                      1つ目の三項演算子の中に三項演算子を繋げて記載する
                      isLoggedInがtrueの上であればuserTypeがadminか判定する
                	    adminがtrueであれば<p>管理者としてログイン済みです</p>を表示する
                	    adiminがfalseであればmemberがtrueであるかを判定する。
                	    trueであれば<p>会員としてログイン済みです</p>)を表示する
                	    falseであればisLoggedInがfalseと同じ(<p>ゲストとしてログイン済みです</p>)を表示する
                    </div>
                  );
                }
                
                ```
                
            - クラス名を情報を受け取り追加や切り替える
                - Propsを受け取る方法
                    - if文を使ってProps.roleのプロパティ名を受け取ってクラス名を追加する
                - clsx(クラスエックス)を使う方法
                    - Propsだとネストが深くなってしまい可読性が下がってしまう。
        - Webページに動きを作る（クリックアクション）
            - JavaScript では、onclickやonchangeに関数を渡す事でイベントを発生させる事ができる
            - ReactではJavaScriptと扱いが異なる
                - まずは、キャメルケースでイベントの種類を設定する
                - 例えばボタンがクリックされた時にボタンがクリックされましたとアラートを出す関数を設定する
                
                ```jsx
                //まず関数の作成(アロー関数)
                const handleClick = () => {
                  alert("クリックされました");
                };
                
                //作成した関数をボタンと紐づける
                <button onClick={handleClick}>クリック</button>
                
                //完成系
                export function App() {
                  // クリックしたときの処理を関数で書く
                  const handleClick = () => {
                    alert("クリックされました");
                  };
                  // その関数をボタンのonClickにセット
                  return (
                    <div>
                      <button onClick={handleClick}>
                        クリック
                      </button>
                    </div>
                  );
                }
                
                ```
                
        - Webページに動きを作る（配列などの複数の選択肢がある場合）
            - 配列など複数のものがある場合のクリックアクションをどのように作成するのか？
                
                ↓
                
                配列fruitsに対してmap関数を使い、ボタンを含む配列の一覧を作成している
                
                ```jsx
                const fruits = ["りんご","バナナ","ぶどう","いちご","メロン"]
                
                function App() {
                  return (
                    <div>
                      {fruits.map(f => (
                        <li key={f}>
                          {/* ここにクリックされたときにその果物名をアラートする処理を書きたい */}
                          <button>PUSH</button>
                        </li>
                      ))}
                    </div>
                  );
                }
                
                //上記のようなボタンを含むリストのボタンが押された際にonClicl関数を使う
                
                <ul>
                  {fruits.map(f => (<li key={f.name}>
                    <button onClick={() => { alert(`これは${f.name}だよ！`)}}>
                      PUSH
                    </button>
                  </li>))}
                </ul>
                
                //クリックイベントの内容の記載が長くなる場合には高階関数と呼ばれる関数に関数を返す方法が良い
                
                //関数handleFruitClickにfruit名を渡すとその名前を使ってアラートを出す関数が手に入る
                const handleFruitClick = (fruit) => () => {
                  alert(`${fruit}がクリックされました`)
                }
                
                ```               
    - DOMとは
        - **DOM**（ドム）は、「Document Object Model」の略である
            - HTMLで記載されたページや構造をJava Scriptを使って操作できるようにするための仕組み
                - JavaScriptではオブジェクト指向でプログラムを作る
                    - HTMLのタグで囲まれた階層構造の要素をツリー構造に変換する
                        - 変換された各要素はそれぞれをDOMノードと呼ばれる
        - JavaScriptでこのDOMノードにアクセスする事で操作する
            - 不要な要素を削除する
            - 新しい要素を追加する
            - クリックしたアクションを追加する　など
        - JavaScriptで要素を取得して操作を行う
            - **document.querySelector**（ドキュメント・クエリセレクター）
                - 取得した要素がしっかり動くかどうかなどの確認も行う
        - ReactDOM
            - Reactで作ったコンポーネントをWebページへ表示する際に必要なライブラリー
                - React内のコンポーネントの処理内容はJSXで記載されている
                    - Webページに表示するにはトランスパイルをしなければならない
                        1. Reactで作ったコンポーネントをWebページ上に表示する。
                        2. コンポーネントのデータが変わったときにそれをページにすぐに反映させる。
                        3. サーバー上でコンポーネントをHTMLに変換してブラウザーに送る。
        - ReactDOMでレンダリング
            - Reactインポート
            - ReactDOMのインポート
        - Reactで作成したコンポートネントを表示するには特定のHTML要素にコンポーネントを紐づける必要がある
            - html内にコンポーネントを表示するための場所を確保する
            - createRootを使ったレンダリング
                - createRoot関数とroot.render()というメソッドを使う
                
                ```jsx
                import { createRoot } from "react-dom/client";
                
                const root = createRoot(document.getElementById("root"));
                
                // ここで表示したいコンポーネントを指定
                root.render(<App />); 
                ```
                
                - document.getElementById("root")で、JavaScript を使って idがrootのdiv要素を取得し、createRoot関数に渡しています。
                    - HTML内でid属性がrootとなっている要素にAppコンポーネントが表示される
                - root.render(...)
                    - このコードで実際にHTML上にAppコンポーネントが表示される。
    - Reactのスタイリング方法
        - style属性をつけるときは文字列ではなくオプジェクトで宣言する
            
            ```jsx
            <nav className={className} style={{ marginTop: "10px" }}>
              ...
            </nav>
            ```
            
        - style属性を要素に直接指定する方法
            - style属性を使って要素に直接スタイルを適用する事ができる
                - 通常のHTMLと方法が似ているが違いがある
            - style属性を指定する場合にはJavaScriptのオブジェクトを渡す事でスタイルを定義する
                - {}の中に{}が入っている形になる
                
                ```jsx
                <div style={{ プロパティ名: "値"}}>
                	表示内容
                </div>;
                ```
                
                - {}の中に{オブジェクト}が入っている形
                    - {　プロパティ名：値　}
                        - style属性は{{}}二重括弧を使って指定する
                    - プロパティ名の変換
                        - ケバブケースはNG
                        - キャメルコードで記載するようにする
                        
                        | CSSのプロパティ名 | Reactでの対応プロパティ |
                        | --- | --- |
                        | background-color | backgroundColor |
                        | font-size | fontSize |
                        | text-align | textAlign |
                        | margin-top | marginTop |
                        | z-index | zIndex |
                    - 値は文字列で指定する
                        - 文字の大きさを指定したい場合
                            
                            <div style= {{ fontSize : 10px }}>
                            
                            ↓
                            
                            <div style= {{ fontSize : “10px” }}>
                            
                            - シングルクォート（`'`）とダブルクォート（`"`）どちらかで囲む
                        - 例外として単位が不要な数値の場合にはそのまま使用できる
        - JavaScriptから直接CSSを読み込む
            - React内だけで作成すると地味なWebページができてしまう。
                - HTMLと同様にCSSを使って内部スタイルシートを適用させる方法
                    - HTMLの場合
                        
                        ```html
                        <link rel="stylesheet" href="style.css" />
                        ```
                        
                    - JavaScriptの場合
                        - Webpackのようなビルドツールを使うことでJavaScript経由でファイルを読み込むことができる
                        
                        ```jsx
                        import "./style.css";
                        ```
                        
                        - ビルドツールを使っているとJavaScriptに直接importする事が可能になる
                            - CSSセレクタを使ってスタイルを適用させる 
        - Reactコンポーネントのスタイリング方法には大きく3つ方法がある
            - 「**Emotion**」
                - CSS in JSと呼ばれるJavaScriptの中にCSSを記載する方式のライブラリー
                    - 利点：
                        - コンポーネントとスタイルが同じ場所にあるので見通しが良いという点
                        - https://www.kuma-ui.com/
                        - https://panda-css.com/
                        
                        ```jsx
                        import { css } from "@emotion/react";
                        
                        export function App() {
                          return (
                            <div
                              css={css`
                                color: red;
                              `}
                            >
                              Hello
                            </div>
                          );
                        }
                        ```
                        
                        - まずは@emotionというライブラリからCSSという関数をインポートする
                        
                        ```jsx
                        import { css } from "@emotion/react";
                        ```
                        
                        - 実際の記載方法
                        
                        ```jsx
                        //バッククォートの中にCSSを記載できるようにする
                        <div **{css`color: red;`}**>
                        ```
                        
                - Emotionの機能の中にはJavaScriptの変数にスタイルを保存する機能もある
                    - 利点：
                        - スタイルを変数にする事で複数箇所で使う事ができる
                        - 変更箇所が少ない
                        - 見た目が統一される
                        - コード記載量が軽減する
                        - コードの可読性が高くなる
                - Emotionをオブジェクトスタイルで使用する
                    - CSSをオブジェクトスタイルで適用させる方法はTypeScriptと親和性が高い
                        - エディターでのエラー発見も精度が高くなる
                    - https://emotion.sh/docs/best-practices
                    
                    ```jsx
                    import { css } from "@emotion/react";
                    
                    function App() {
                      return (
                        <div
                          css={css({
                            color: "red",
                          })}
                        >
                          Hello
                        </div>
                      );
                    }
                    
                    通常の記載方法
                    **css={css`color: red;`}**
                    
                    オブジェクトスタイル
                    **css={css({color: "red"})}
                    
                    オブジェクトで記載する時にはプロパティはキャメルケースで記載する**
                    ```
                    
                - hoverなどの擬似クラスや擬似要素に対応する
                    - 記載方法
                    
                    ```jsx
                    import { css } from "@emotion/react";
                    
                    export function App() {
                      return (
                        <button
                          css={css`
                            border: none;
                            padding: 5px 10px;
                            color: white;
                            background-color: red;
                            &:hover {
                              background-color: blue;
                            }
                          `}
                        >
                          ホバーしてみてね
                        </button>
                      );
                    }
                    ```
                    
                    - 擬似クラスや擬似要素を使う場合には&で選択する範囲を指定する
                        - 上記のソースコードであればbuttonタグにhoverされた時という事になる
                    - Beforeの記載方法
                    
                    ```jsx
                    <div
                    css={css`
                      position: relative;
                      padding-left: 20px;
                      &:before {
                        content: "“";
                        position: absolute;
                        left: 0;
                        top: 0;
                        font-size: 2em;
                      }
                    `
                    }
                    >
                      引用の文章です
                    </div>
                    ```
                    
                    - Emotionがオブジェクトで指定されている時
                        - &:before {}の形はプロパティと値の関係になっていないのでエラーになってしまう
                            - “:hover”の形にした上で:の後に値を記載する方法を取る
                - レスポンシブデザイン
                    - メディアクエリーを使ってクライアント側の表示端末に合わせて表示内容を変更する方法
                        
                        ```jsx
                        CSS関数の場合の書き方
                        import { css } from "@emotion/react";
                        
                        function App() {
                          return (
                            <div
                              css={css`
                                color: red;
                                @media (min-width: 768px) {
                                  color: blue;
                                }
                              `}
                            >
                              Hello
                            </div>
                          );
                        }
                        ```
                        
                    - @media (min-width: 768px)
                        - メディアクエリーで、画面幅が768ピクセル以上の場合という事を示す
                        
                        ```jsx
                        オブジェクトスタイルで記載する場合
                        import { css } from "@emotion/react";
                        
                        function App() {
                          return (
                            <div
                              css={{
                                color: "red",
                                "@media (min-width: 768px)": {
                                  color: "blue",
                                },
                              }}
                            >
                              Hello
                            </div>
                          );
                        }
                        
                        "@media (min-width: 768px)": {color: "blue",}
                        メディアクエリーの条件をキーとしてスタイル内容をその後に記載するf
                        ```
                        
                - Emotionを使って動的なスタイリングを行う
                    - Emotionを使ったスタイリング
                        - 静的スタイリング
                            - 一度設定されると設定が変更されない
                        - 動的スタイリング
                    - useStateを使ってユーザの選択に応じたスタイリングを実施する
                        - JavaScriptで変数を定義する
                            - CSS内に変数を埋め込む
                                - バッククォート（` `）で挟む
                                    - テンプレートリテラル内で変数を`${変数名}`として埋め込む
                            - onClick関数にスタイリングなどの変更する関数を紐づけるようにする
                                - useStateのset関数が発火するようにして状態を管理する
                    
                    ```jsx
                    //useStateを設定する初期値を設定
                    const [color, setColor] = useState("red");
                    
                    //ユーザの処理、行動に応じてスタイリングが変更されるようにクリックイベントなどを設定する
                    Bottom onClick={()=>{setColor("blue")}}
                    ```
                    
            - 「**Tailwind CSS**」
                - 特定の機能に特化したクラスが用意されているユーティリティファーストのCSSフレームワーク
                    - 余白や文字の色などなど特定のスタイルがすでに用意されているフレームワーク
                        - 要素に対応するクラスをクラス名として指定する事で使う事ができる
                            - 事前に用意されているクラスを使用する事で1からスタイル構築する必要がない
                            - 再利用する事も可能になる
                                - mosyaの開発も**Tailwind CSSを使って開発されている**
                    - Tailwindが選ばれる理由
                        - **迅速なスタイリング** :
                            - 用意されたクラスを使って、すぐにWebページの見た目を整える事ができる
                                - CSSを書く時間を大幅に削減できる。
                        - **簡単なカスタマイズ** :
                            - プロジェクトのニーズに合わせて簡単にスタイルを変更できる。
                        - **レスポンシブ対応** :
                            - レスポンシブクラスが用意されている。
                                - さまざまな画面サイズに合わせて簡単に調整できる。
                        - **一貫性のあるUI** :
                            - 同じクラスを使って、プロジェクト全体で統一感のある見た目を作ることができる。
                    - クラスの命名規則
                        - 基本的にそのクラスが何をするのか？で命名される
                            - テキスト関連 text- 背景 bg-
                        - ここでのclassはclassNameではない
                            - **`class`**: クラスコンポーネントを定義するために使用される。
                                - class ⇒ 予約語
                    - 基本構文
                        - **プロパティ名 - 値の形で記載する**
                            - text - blue-500
                                - text⇒プロパティ
                                - blue-500⇒値
                        - 記載方法
                        
                        ```html
                        一つのクラスを適用させる場合
                        <p class="text-blue-500">これは青いテキストです。</p>
                        
                        複数のクラスを適用させる場合
                        クラス名の間をスペースで区切る
                        <div class="text-blue-500 m-4">
                          これは青色のテキストで、マージンが適用されたテキストです。
                        </div>
                        ```
                        
                        - JavaScriptでの記載方法
                        
                        ```jsx
                        return (
                         <button className="px-4 py-2 bg-blue-500 text-white font-bold rounded">
                           Click me
                         </button>
                        ```
                        
                        | **クラス名** | **意味** |
                        | --- | --- |
                        | px-4 | 左右のpaddingを0.25rem*4に設定（1は0.25remに相当） |
                        | py-2 | 上下のpaddingを0.25rem*2に設定（1は0.25remに相当） |
                        | bg-blue-500 | 背景色を`rgb(59 130 246)`に設定 |
                        | text-white | テキストの色を白に設定 |
                        | font-bold | フォントの太さを`bold`に設定 |
                        | rounded | 角を丸める |
                    - レスポンシブデザイン
                        - ブレイクポイントを使って画面サイズに合わせた表示に変更する]
                            - Emotionではレスポンシブデザインと呼んでいるがTailWindではブレイクポイントと呼ぶ
                            
                            **Tailwind CSSのブレイクポイント（デフォルト）**
                            
                            - `sm`（small）: 640px以上
                            - `md`（medium）: 768px以上
                            - `lg`（large）: 1024px以上
                            - `xl`（extra large）: 1280px以上
                            - `2xl`（2x extra large）: 1536px以上
                        - ブレイクポイントをプレフィックスとしてクラス名の前につける
                            - 指定したHTML要素が特定の画面幅で適用されるようになる
                            
                            ```jsx
                            <div class="text-sm md:text-base lg:text-lg">
                              画面のサイズによってテキストサイズが変わるよ！
                            </div>
                            
                            text-sm が基本のテキストサイズ
                            画面幅が768px以上のときはtext-base
                            画面幅が1024px以上のときはtext-lg
                            ```
                            
                        - フレックスボックス
                            - フレックスコンテナークラスを使ってレイアウトを柔軟にする
                                - アイテムの並び順
                                - 整列
                                - サイズ調整
                            - フレックスコンテナーの設定
                                - フレックスコンテナーは設定するとデフォルトでは左端から横並びになる
                            
                            ```jsx
                            <div class="flex">...</div>　
                            ```
                            
                            - 640px以下で縦方向（flex-col）に並ぶ記載例
                            
                            ```jsx
                            <div class="flex flex-col sm:flex-row">
                              <div>item 1</div>
                              <div>item 2</div>
                              <div>item 3</div>
                            </div>
                            
                            class="flex flex-col sm:flex-row"
                            flex
                            	フレックスコンテナーの設定
                            flex-col
                            	アイテムが縦方向に並ぶように設定
                            sm:flex-row
                            	sm:640px以上だった場合には
                            	flex-rowアイテムを横方向に並べる
                            ```
                            
                        - 表示と非表示を分ける
                            - 表示する画面（スマホ、パソコン）に応じて表示内容を変更する
                                - パソコンでは表示するけど、スマホでは表示を避けるなどの使い方
                            - **表示**（block、inline、inline-blockなど） : 特定の要素を表示するためのクラス。
                            - **非表示**（hidden）: 特定の要素を隠すためのクラス。
                                
                                ```jsx
                                <div class="hidden sm:block">
                                  この要素は640px以上の画面でのみ表示されます。
                                </div>
                                <div class="block sm:hidden">
                                  この要素は640px未満の画面でのみ表示されます。
                                </div>
                                ```
                                
                        - グリッドを使ったレスポンシブデザイン
                            - 画面サイズに応じて表示カラム数を変更する事ができる
                            
                            ```jsx
                            <div class="grid grid-cols-3">...</div>
                            
                            class="grid grid-cols-3"
                            grid
                            	グリッドクラスを使いグリッドコンテナーの設定をする
                            grid-cols-3
                            　grid-cols-(設定したいカラム数を入れる)でカラムを設定する
                            ```
                            
                            ```jsx
                            <div class="grid grid-cols-1 sm:grid-cols-2">
                              <div>アイテム1</div>
                              <div>アイテム2</div>
                              <div>アイテム3</div>
                            </div>
                            
                            class="grid grid-cols-1 sm:grid-cols-2"
                            grid-cols-1
                            	デフォルトではカラム数が1で表示される
                            sm:grid-cols-2
                            	640px以上の場合にはカラム数が2で表示される
                            ```
                            
                    - インタラクティブ(双方向)なスタイル：擬似クラスの実装
                        - ユーザー行動に応じてスタイルを変化させる
                            - hover -ホバー時
                                - 対象のクラスの前にhover:をプレフィックスとしてつける
                                
                                ```jsx
                                <button class="bg-blue-500 hover:bg-blue-700">ホバーしてね</button>
                                ```
                                
                            - focus -フォーカス（入力フォームにTabで移動した時など）
                                - 対象のクラスの前にfocus:をプレフィックスとしてつける
                                
                                ```jsx
                                <input class="border border-gray-300 focus:border-blue-500" />
                                ```
                                
                            - active: - アクティブ状態（例えば、ボタンがクリックされている時など）
                                - 対象クラスの前にactive:をプレフィックスとしてつける
                            - disabled: - 無効状態
                                - 対象クラスの前にdisabled:をプレフィックスとしてつける
                                    - 無効状態の場合にはopacityを50％減少するなど
                        - ダークモード対応
                            - tailwind.config.jsファイル内の`darkMode`プロパティを設定する事で対応可能になる
                                - `media`
                                    
                                    ```jsx
                                    module.exports = {
                                      darkMode: "media",
                                      //その他の設定
                                    };
                                    ```
                                    
                                    - ユーザーのシステム設定に応じて自動的にダークモードが適応される
                                - `class`
                                    
                                    ```jsx
                                    module.exports = {
                                      darkMode: "class",
                                      //その他の設定
                                    };
                                    ```
                                    
                                    - classを設定するとHTMLの中で最上位の要素のclassにdarkを指定する事でdarkモードが有効になる
                            - ダークモードとライトモードに応じてスタイルを設定する
                                
                                ```jsx
                                <div class="bg-white dark:bg-black">
                                  <p class="text-black dark:text-white">ようこそ、mosya Reactへ！</p>
                                </div>
                                ```
                                
                                - ダークモード切り替えをユーザがボタンで設定する事も可能
                                    
                                    ```jsx
                                    module.exports = {
                                      darkMode: "class",
                                      //その他の設定
                                    };
                                    
                                    classをconfigdファイルで設定する
                                    
                                    //JavaScriptでユーザのアクションに応じてdark classをクラスが無い場合には追加してすでに存在している場合には削除する
                                    function toggleDarkMode() {
                                      document.body.classList.toggle("dark"); 
                                    }
                                    
                                    Bottonに関数を紐づける
                                    <button onclick="toggleDarkMode()">ダークモード切り替え</button>
                                    
                                    ```
                                    
                        - 要素同士の関係性でスタイルを変更する
                            - group
                                - 親要素と子要素の関係性でスタイルを変更する方法
                                    - 親要素の状態に応じて子要素のスタイルが変更されるようにする
                                - 使い方
                                    - 親要素にgroupというクラス名をつける
                                        - 子要素の親要素の状態に応じて変化させたいスタイルの前にプレフィックスとしてgroup-目的とする状態をつける子要素の状態に変化が起きる
                                        - 
                                            - 親要素の状態が変化するとそれに合わせて
                                    
                                    ```jsx
                                    <div classNamne="group">
                                    	<div className="group-hover:text-blue-500">このテキストは親要素がホバーされた場合にテキストがblueになります。</div>
                                    </div>
                                    ```
                                    
                            - peer
                                - 要素同士を兄弟関係とおき、兄弟関係とおいた要素の状態の変化に応じてスタイルを変化させる方法
                                    - 特定の要素の状態に応じて対応する要素の状態も変化する方法
                                
                                ```jsx
                                <input type="e-mail" class="peer"...>
                                <p class="peer-invalid:visible ...">エラーメッセージ</p>
                                
                                ```
                                
            - 「**CSS Modules**」
                - CSSをモジュール化して一意のランダムな名前に変換するスタイリング方法
                    - バンドラーツールを使う方法
                        - viteやwebpackなどのビルドツールを使ってCSS Modulesを使う
                            - Module化の流れ：
                                - styles.module.cssでスタイル名とスタイル内容を指定する
                                
                                ```jsx
                                styles.module.cssファイル
                                ↓
                                .btn {
                                  background-color: blue;
                                  color: white;
                                }
                                
                                JSXファイル
                                ↓
                                import styles from "./styles.module.css";
                                
                                function Header() {
                                  return <button className={styles.btn}>...</button>;
                                }
                                ```
                                
                                - JSX(React等)でスタイル名を指定する
                                    - CSS
                                    - JavaScript
                                        - この2つに変換される
                                - JSXにスタイル名を指定した時にすでに一意な名前が生成されている
                        - スタイル内容はクラス名のオブジェクトになる
                            - CSSファイル内でプロパティはケバブケースで記載
                            - クラス名（セレクター）はキャメルケースで記載する
                                - JavaScriptでclassNameとして指定するため
                    - ブラウザで使う方法
                        - ブラウザにassert（アサート）というキーワードを使ってスタイルシートであると指示する事が必要になる
                        
                        ```jsx
                        <script type="module">
                          import styles from "./styles.module.css" assert { type: "css" };
                          document.adoptedStyleSheets = [styles];
                        </script>
                        ```
                        
                        - スタイルはCSSStyleSheetという特別なオブジェクトになる
                            - document.adoptedStyleSheetsに代入する必要がある
                        
                - 各ツールにおける導入方法
                    - vite
                        - 元々、対応しているため特別な設定は必要なし
                            - .module.css 拡張子を持つ CSS ファイルを作成する
                            - 作成した`.module.css`拡張子を持つCSS ファイルをコンポーネントでインポートする
                    - Webpack
                        - webpack.config.jsで必要な設定を記載する必要がある
                            
                            ```jsx
                            module.exports = {
                              // ...
                              module: {
                                rules: [
                                  // ...
                                  {
                                    test: /\.module\.css$/,
                                    use: [
                                      'style-loader',
                                      {
                                        loader: 'css-loader',
                                        options: {
                                          modules: true
                                        }
                                      }
                                    ]
                                  },
                                  {
                                    test: /\.css$/,
                                    exclude: /\.module\.css$/,
                                    use: ['style-loader', 'css-loader']
                                  }
                                  // ...
                                ]
                              }
                              // ...
                            };
                            ```
                            
                    - Next.js
                        - 元々、対応しているため特別な設定は必要なし
                            - .module.cssという拡張子をつける事でCSSのファイルにする
                            - CSSファイルをインポートする
                            - スタイル名を適用する事でスタイルが適用される
                    - https://ja.vite.dev/guide/features.html#css-modules
                    - https://nextjs.org/docs/app/getting-started/css
    - 様々なライブラリー
        - ライブラリー
            - 再利用できる機能やコードをまとめたもの
        - ReactはJavaSciptのライブラリであり、Reactには多くのライブラリがある
            - UIコンポーネントを作るためのものである
                - Webページ上のボタン、アコーディオンメニュー、スライダー
            - スライダー系ライブラリ
                - ‣
                - ‣
            - **カレンダー系ライブラリ**
                - ‣
                - ‣
            - **日付選択系ライブラリ**
                - ‣
                - ‣
            - 通知系ライブラリ
                - ‣
                - ‣
        - **Immer**
            - オブジェクトや配列の状態を直接変更できるようにするライブラリ
                - Immerでdraftと呼ばれる配列や要素のコピーを作成する事で直接変更する事が出来る
            - useImmerというHooksを使うとuseStateよりも便利に状態の更新を行える
            
            ```jsx
            import { useImmer } from "use-immer";
            
            const [tasks, updateTasks] = useImmer([
              { id: 1, title: "ランチの予約をする" },
              { id: 2, title: "美容院に行く" },
            ]);```
            
            function updateTaskTitle(id, newTitle) {
              updateTasks((draft) => {
                const task = draft.find((task) => task.id === id);
                if (task) task.title = newTitle;
              });
            }
            ```            
    - ローカル環境でReactを使う
        - Reactの雛形を作る手順
            - Reactに用意されている雛形に沿ってJavaScriptを記載する事でWebアプリを作成できる
                - Reactの雛形のディレクトリ構成
                    - モジュールディレクト
                    - publicディレクトリ
                        - index.html
                            - 空のroot属性がついたdivタグ
                    - srcディレクトリ
                    - package.json
                        - バージョン
                        - フィールド
        - Reactでビルドツールのviteを使う時に実行するコマンド
            
            ```html
            npx creat-react-app
            ↑
            このようにReactを1から作る方法もあるがviteを使った方が効率的である
            
            npx create vite@latest
            ↑
            viteを使って雛形を作成
            
            react-hooks-tutorial-yt
            ↑
            プログラム名を決定
            
            cd
            code .
            ↑
            ディレクトリを開く
            
            npm i
            ↑
            npmをインストールする
            
            npm run dev
            ↑
            viteの場合にはnpm startではなくrun devとする
            ```
            
        - Reactを使ってみる(Node.js)
            - Reactを使うにはNode.jsというツールが必要
                - Node.js
                    - 元来、サーバーサイドで動作するJavaScriptとして活躍していた
                        - Node.js内のパッケージ管理ツールのnpmの使い勝手が良くフロントエンドでも活用される
                        - TypeScriptをコンパイルする際にもNode.jsが使用される
                            - モダン（現代）の開発にはフロントエンドの開発にもNode.jsが必須になっている。
            - Node.jsのインストール
                
                ↓
                
            - ターミナルでコマンドを実施する
                
                npm create vite@latest
                
                ↓
                
            - ターミナルでプログラム名の入力など行う
                
                ↓
                
            - TypeScriptの選択も可能
                
                ↓
                
            - 出来上がったプロジェクトに移動して実行する
                
                cd vite-project
                npm install
                npm run dev
                
        - ローカル環境での立ち上げ方の違い
            - creat-react-appの場合
                - ターミナルでnpm startとする事で立ち上がる
            - React+vite
                - npm i
                - npm run dev
    - イミュータブルに変数や配列、オブジェクトを扱う
        - Reactは**イミュータブル**にオブジェクトを扱う事が求められる
            - 変数の更新などを行なった場合には状態の更新をする変数を直接、状態の更新をするのではなく状態の更新を行なった上で変数へ一度、コピーしてからコンポーネントの更新を行う
                - ミュータブルに直接、状態を更新するのではなく、状態の更新を行なった変数をuseStateで更新する
        - 要素を追加する場合
            - 例：
                - 配列をリスト形式にしてコンポーネントとして表示している場合
                    - pushメソッドなどで配列に要素を加えたのちにuseStateを使い状態の更新をそのまま行なってもコンポーネントにレンダリングがおきないため画面の更新が起きない
                        - Reactが変更に気づく事ができない
                            - 参照している配列が同じ配列を参照している
                    - …変数, コピーしたい変数の形を取った上でuseStateを使って状態を更新する事でレンダリングされると画面表示も更新されるようになる
                        - スプレッド構文などを使って変数にコピーをしてからuseStateなどを使って更新する
                            - 元の配列は変えずに更新する
        - 要素を削除する場合
            - よくない例：
                - 一見削除ができているように見えるコードでもset関数でuseStateを発火する時に変更前のstateを参照しているため変更をReactが管理できない
                    - 変更後のstateを変数へ代入してからuseStateを発火させる
                
                ```jsx
                const [tasks, setTasks] = useState([
                  { id: 1, title: "掃除をする" },
                  { id: 2, title: "洗濯をする" },
                ]);
                
                //関数コンポーネント、引数にidを取る
                function removeTask(id) {
                　//変数indexを定美する
                　//配列tasksに対して,findIndexメソッドを使いtaskを引数に取りtask.idとidが厳格に等しいものを代入する
                  const index = tasks.findIndex((task) => task.id === id);
                　//spliceメソッドを使って配列tasksの中で定数indexの正の順で1になるstateを削除する
                	//indexで定義した配列taskの中でtask.idとidが厳格に等しいオブジェクトを削除する
                  tasks.splice(index, 1);
                  //setTasksを指定したオブジェクトが削除されたtasksを引数にとり実行してuseStateを発火させる
                  setTasks(tasks);
                }
                ```
                
        - 配列の要素を更新する場合
            - Reactでは配列の要素の更新を直接する事は推奨されない
                - 例：
                    - 要素の更新をする関数を作成する場合
                        - find関数で対象となる要素を取得する
                        - 取得した要素にプロパティを指定して直接要素を更新する
                        - set関数を使いuseStateを発火させる
                    - このような流れだとset関数で状態を参照した際に更新前の状態が参照されてしまう
                    - useStateを発火させたとしても要素の更新が反映されない
            - 望ましい配列の要素の更新の流れ
                - 配列の要素を参照して要素の更新を行うもののみに要素の更新を行う
                    - 三項演算子
                - 再度、配列を作成する
                    - コピーする
                - コピーした変数をトリガーにuseStateを発火させる
    - fetch
        - サーバーとのデータのやり取りをする際に使う関数
            - サーバーからデータを受け取る
                - 取得したいAPI(ソフトウェアのインターフェース)のURLをfetchに代入する事で使用できる
                    
                    ```jsx
                    fetch(
                      "https://example.com/api/weather"
                    );
                    ```
                    
                    - 受け取ったデータはthenを使いjsonに変換する
                        - そして変換したデータをさらに処理する
                            - json
                                - JavaScriptのデータフォーマット
                                    - キー:値という形で記載される
                    
                    ```jsx
                    fetch("https://example.com/api/weather")
                      .then((res) => res.json()) //データをjsonに変換
                      .then((json) => {
                        // ここで取得したデータを処理します。
                      });
                    ```
                    
                - Reactコンポーネント内でuseEffectを使ってfetchを使う
                コンポーネントのレンダリング時などにAPIからデータを取得する
                    - useEffectがマウントされた時に実行するようにする
                        - 依存配列を空にする事でコンポーネントのレンダリング時に実行される
                    
                    ```tsx
                    useEffect(() => {
                      fetch("/api/example/weather")
                        .then((res) => res.json())
                        .then((json) => {
                          setWeather(json.weather);
                        });
                    }, []);
                    ```
                    
                - 非同期処理という課題：useEffectは単体では非同期処理を実行できない
                    - `useEffect`関数では`async`を使った非同期関数を直接実行することができない
                        
                        ```tsx
                        useEffect(async () => {
                          const res = await fetch("https://jsonplaceholder.typicode.com/todos/");
                          const json = await res.json();
                          setItems(json);
                        }, []);
                        
                        ↓
                        useEffect内でfetch関数を定義する事でasyncメソッドを使い非同期処理をコンポーネントのレンダリング時に実行する
                        
                        useEffect(() => {
                          const fetchItems = async () => {
                            const res = await fetch("https://jsonplaceholder.typicode.com/todos/");
                            const json = await res.json();
                            setItems(json);
                          };
                          fetchItems();
                        }, []);
                        
                        ```
                        
            - サーバーにデータを送る
                - fetch関数を使ってサーバーへデータを送る
                    - サーバーへデータを送信する際には
                        - 第1引数：リクエストパラメーター（APIのURL）
                        - 第2引数：methodを指定する（HTTPメソッド）
                            - サーバーへ送る場合はpost
                            - 送るデータはbodyに指定する
                                - JSON.stringifyはbodyに指定するデータを文字列にする
                                JSのオブジェクトはサーバーへ送れないため注意が必要
                    
                    ```tsx
                    const data = {
                      name: "会議資料を作成する",
                      dueDate: "2023/1/2",
                    };
                    fetch("/api/todo", {
                      method: "POST",
                      // 👆データを送信したい場合はmethodにPOSTを指定する
                      body: JSON.stringify(data),
                      // 👆送信したいデータを文字列としてbodyに指定する
                    });
                    ```
                    
                    - APIによって第2引数の中にデータのタイプを`headers`で指定することが必要な場合もある
                        - sonを送信する際にサーバーにどのようなタイプのデータを送るheadersで指定する
                    
                    ```tsx
                    const comment = {
                      username: "user1",
                      text: "mosya最高ですよねー😀",
                    };
                    fetch("/api/comments", {
                      method: "POST",
                      // 👆データを送信したい場合はmethodにPOSTを指定する
                      body: JSON.stringify(data),
                      // 👆送信したいデータを文字列としてbodyに指定する
                      headers: {
                        "Content-Type": "application/json",
                      },
                    });
                    ```                   
    - Suspense（サスペンス）　：　データ取得中のUI
        - データのローディング中に別の特定の画面を表示させる機能
            - ローディング用の画面から表示用の画面に移動する方法
        
        注意：
        
        ReactはSuspenseをSWRやReact Queryなどのデータ取得系のライブラリと組み合わせて利用することを推奨していない。
        
        サーバーサイドレンダリングの結果とクライアントサイドのレンダリング結果のHTMLのミスマッチが発生する可能性があるなどの問題点がある
        
        - Suspenseの導入前：
            - 手書きでローディング中の画面などを作成する必要があった
            
            ```ruby
            export function App() {
              const { data } = useSWR("/api/movie");
              if (!data) {
                return <Loading />;
              }
            
              return (
                <div>
                  {data.map((item) => (
                    <div key={item.id}>{item.name}</div>
                  ))}
                </div>
              );
            }
            ```
            
            変数dataを定義する
            
            変数dataの中でuesSWRとしてif文でdataの取得中（false）の場合にコンポーネントを返す
            
        
        - Suspenseの導入後：
            - Suspenseを使うと、Suspenseコンポーネントのfallbackプロップにローディング画面を指定するだけで、データの取得中に自動的にローディング画面を表示してくれるようになる
            
            ```ruby
            function Data() {
              const { movie } = useSWR("/api/movie", {
                suspense: true, // 👈 SWRでSuspenseを有効にするためにはsuspenseオプションをtrueにする
              });
              return (
                <div>
                  {data.map((item) => (
                    <div key={item.id}>{item.name}</div>
                  ))}
                </div>
              );
            }
            
            export function App() {
              return (
                <Suspense fallback={<Loading />}>
                  <Movie />
                </Suspense>
              );
            }
            
            状態
            　データの取得中
            　データの取得後
            ``            
    - react-error-boundary　：　データ取得時のエラー発生時のUI
        - Reactにおいて特定のコンポーネントでエラーが発生するとReact全体が止まってしまう。
            - コンポーネントのエラーが発生してもエラー発生時のためのコンポーネントを定義する事でアプリ全体が止まらないようにする事ができる機能
                - エラーハンドリングが簡単になる
        - 実装方法：
            - エラーをキャッチする
                - ErrorBoundaryでラップしたコンポーネントでエラーが発生した場合
                    - fallbackに渡しているコンポーネントが表示される
                        - fallbackに渡しているコンポーネントでは引数としてerrorを受け取るようにする
                            - errorはthrow newと定義してエラーを発生するコンポーネントとする
                                - エラー表示がされるコンポーネントが表示される
                - エラーを発生するコンポーネント
                
                ```tsx
                const BrokenComponent = () => {
                  throw new Error(
                    "エラーが発生しました"
                  );
                };
                ```
                
                - エラーが発生した時に表示するコンポーネント（エラーメッセージの表示）
                
                ```tsx
                function ErrorFallback({ error }) {
                  return (
                    <div>
                      <p>エラーが発生しました 😭</p>
                      <pre>{error.message}</pre>
                    </div>
                  );
                }
                
                error（BrokenComponent）の中のを
                ```
                
                - BrokenComponentをErrorBoundaryでラップする
                
                ```tsx
                import { ErrorBoundary } from 'react-error-boundary';
                
                function App() {
                  return (
                    <div>
                      <div>ここはエラーが発生しても表示される🙌</div>
                      <ErrorBoundary fallback={<ErrorFallback />}>
                        <BrokenComponent />
                      </ErrorBoundary>
                    </div>
                  );
                }
                
                ```
                
        - suspenseと組み合わせる事でデータ取得中にエラーが発生した場合の表示を切り替える事ができる
            - suspenseはデータ取得中の画面を表示する機能だが、エラー発生時には対応できない
                - データを取得するコンポーネントがあった場合
                    - suspenseでラップしてデータ取得中の画面表示をする
                        - さらにそのsuspenseをラップしてエラー発生時の画面を表示する
    - mutate関数
        - SWRを使ってAPIからのデータを取得する際に、古いキャッシュのデータではなく、最新のデータを取得できる
        - 使い方は２通りある
            - APIを使って自動で更新する方法
                - useSWRを使ってAPIからユーザーのデータを取得する
                    - データ取得、読み込み中の状態、エラー情報、mutate関数が返される
                    
                    ```tsx
                    function useUser(id: string) {
                      const { data, error, isLoading, mutate } = useSWR(`/api/user/${id}`, fetcher);
                    }
                    ```
                    
                    - ユーザ情報の更新
                        - asyncとawitを使って非同期処理を実行する
                            - HTTPメソッドがPUTでAPIへデータを送る
                        - mutate関数をその後に呼び出す事でデータを最新の状態にする事ができる
                    
                    ```tsx
                    const updateUser = async (
                      id,
                      name
                    ) => {
                      await fetch(`/api/user/${id}`, {
                        method: "PUT",
                        body: JSON.stringify({ name }),
                      });
                      mutate();
                    }
                    ```
                    
            - 手動でキャッシュを更新する方法
                - APIを非同期的に呼び出し、最新の情報を引数に渡した後に手動でデータを最新に保つ
                    - mutate関数は第２引数にfalseを渡す事でAPIを呼び出さないようにできる
                        - 第１引数に{ ...data, name }とする事で
                            - dataをスプレッド構文としてnameプロパティを更新する
                
                ```tsx
                mutate({ ...data, name }, false);
                ```
                
                - 手動で更新するとAPIの負担を減らす事ができる
    - JSXの中でJavaScriptを使う
        - JavaScriptに戻る
    - リスト(fot文,map関数),繰り返し処理
        - コンポーネントのリストをレンダーする
            - forループや配列のmap関数と行ったJSの機能を使っている
                - 繰り返し処理を行う場合にはkey属性が重要になる事に注意が必要
    - コンポーネント間でデータを共有する
        - 複数のコンポーネント間でデータを共有し常に一緒に更新する場合
            - 状態を一個上の階層においておき、それらを含む最も近いコンポーネントに入れる
    - ３目並べなどにおいて順番に応じて表示内容を変更する方法
      - 先手がデフォルトでXになるようにする
        - プレイヤーの着手と共に真偽値が反転しstateの更新が起こるstateを定義する
        - ```Ruby
          if (xIsNext) {
            nextSquares[i] = "X";
          } else {
            nextSquares[i] = "O";
          }
        ```
    - 早期リターン
      - 処理(クリックイベントや条件分岐など)を行う際に前提条件をif文などで定義する事で事前に値のチェックをできる
        - 事前に値をチェックする事ができれば、前提条件に合わせて処理を行う事ができる
          ```JavaScript
          function handleClick(i) {
            if (squares[i]) {
              return;
            }
            const nextSquares = squares.slice();
            //...
          }
          ```
    - ゲーム終了時の定義
      - ゲームが終了するタイミングを定義する
        - 3目並べ
          - 勝者が決定した場合
          - それ以上、マス目に置く事ができなくなったタイミング
            - 9つのマス目の配列を受け取って勝者を判定する。
              - 'X'、'O' または null を返す
                - calculateWinner という名前のヘルパー関数を定義する
    - 過去履歴の保存
      - 配列をミューテートしていた場合
        - 過去履歴として保存する事は難しい
          - 参照元を変化させている
      - 配列をsliceメソッドを使って新しい配列を作る事で更新しているため過去履歴を保存する事ができる
        - 過去に変更された配列全てのバージョンをhistoryという状態として定義して管理する
          - もう一度リフトアップする
            - 新しいトップレベルのコンポーネントを定義する
              - 
    - mosya演習(要件定義と処理)
        - JSXに変数を埋め込もう演習
            
            レッスンを進める際にかく事
            ・要件
            
            コードの初めの方で定義されている変数をProfileCardコンポーネントのJSXの部分に埋め込んでみよう！
            
            ![image.png](attachment:37ccec08-21c1-4c15-80b2-f4a7f5d27bb5:image.png)
            
            ・ユーザー体験
            
            　　なし
            ・処理
            
            - すでに定義されている定数
                - name
                - banner
                - avatar
                - bio
            - ページ上では
                - banner画像
                - avator画像
                - name
                - bio
                    - の順に表示されるようにしたい
            - すでに用意されているコードに
                - imgタグにはsrc属性を変数を埋め込む形で指定
                - "profile-card-content"クラスには
                    - h3タグには定数name
                    - pタグには定数bio　　を指定する
            
            ```jsx
            import React from "react";
            import { createRoot } from "react-dom/client";
            
            const name = "mosyabo";
            const banner = "https://static.mosya.dev/react-jsx-vars/bg.png";
            const avatar = "https://static.mosya.dev/react-jsx-vars/mosyabo.png";
            const bio =
              "僕はフロントエンド技術を学習したAIロボットだよ！もし質問があればなんでも聞いてね！";
            // ☝️ 上で宣言した変数を使って、プロフィールカードを作成しましょう！
            // 採点のために上の変数の内容は書き換えないでね！
            
            export default function ProfileCard() {
              return (
                <div className="profile-card">
                  <img
                    alt="Profile banner"
                    className="profile-card-banner"
                    height="200"
                    width="300"
                  />
                  <div className="profile-card-avatar-wrap">
                    <img
                      alt="Avatar"
                      className="profile-card-avatar"
                      height="80"
                      width="80"
                    />
                  </div>
                  <div className="profile-card-content">
                    <h3 className="profile-card-name"></h3>
                    <p className="profile-card-bio"></p>
                  </div>
                </div>
              );
            }
            
            export const root = createRoot(document.getElementById("root"));
            root.render(<ProfileCard />);
            
            ```
            
        - スタイルを適用させてみよう
            
            ・要件
            
            - import文を使ってstyle.cssを読み込んでみる
            - スタイルの調節をする
            
            ・ユーザー体験
            
            - なし
            
            ・処理
            
            - styleをimportして適用させる
            - スタイルを指示された通りに適用させる
        - コンポーネント内のtitl属性の値に途中で改行を入れる　答え見た
            - 要件
                - cardコンポーネントのtitle属性の値の文字列を途中で改行する
            - ユーザー体験
                - なし
            - 処理
                - cardコンポーネント内のtitle属性内の改行したいポイントに<br />を入れる
                    - ただ、そのまま直に記載する事ができないため
                    - 全体を一度{}でラッピングする
                    - Fragmentを使って一つの親要素にまとめる
                    - 改行したいポイントでbrを入れる
        - 用意されたタブに連なっているテキストをタブの選択によって表示、非表示にする
            - 要件
                - 複数のタブボタンが設定されている
                - 選択したタブに関連する情報のみ表示してそれ以外の情報は表示しないようにする
                - タブにはactiveクラスを設定してタブの選択をわかるようにする
            - ユーザー体験
                - 選択したタブによって表示内容が変更される
            - 処理
                - タブを選択してクリックする事でactiveになり表示が切り替わる
                    - 初期値はタブ1としておく
                    - onClickでタブがactiveになるようにする
                    - activeになるタブが選択されたタブとわかるようにする
                - useStateを用意する
                    - 管理したい値　tab-panel
                    - トリガーとなる変数
                    - 初期値
                - activeクラスを追加する事でクラスの表示を変更する
        - 色のボタンをクリックしたら色コードがコンソールに出力されるようにする
            - 要件
                - 色のボタンをクリックした際に色コードがコンソールに出力されるようにする
            - ユーザー体験
                - ボタンをクリックするとコンソールに色コードが出力される
            - 処理
                - handleClick関数を作成する
                - ボタンにonClick={handleClick}として関数を紐づける
            
            [回答できず答えみた](https://www.notion.so/192972e6c96080c0bd10fc16957fc0d7?pvs=21)
            
        - 条件に応じてクラス名を変更する
            - コンポーネント間はPropsを使って情報の受け渡しをしている
                - HTMLのクラス名を要求に応じて
                - 変更する事で必要なPropsの受け渡しやスタイルの適用などができる
            - 例えば、if文を使って条件分岐でクラス名を指定する場合
                - 条件分岐の量に応じてコードが読みづらくなってしまう
                
                ```jsx
                function App(props) {
                  let className = "button";
                
                  if (props.role === "admin") {
                    className += "red";
                  } else if (props.role === "user") {
                    className += "blue";
                  } else {
                    className += "gray";
                  }
                
                  return <button className={className}>Click</button>;
                }
                
                ```
                
            - **clsxを使ってクラス名を指定する方法**
                - clsxはクラス名を簡単に組み合わせるライブラリー
                    - クラス名をオブジェクトを使って指定する
                
                ```jsx
                import clsx from "clsx";
                
                function App(props) {
                  const className = clsx({
                    red: props.role === "admin", // 管理者の場合、クラス名に"red"を追加
                    blue: props.role === "user", // 一般ユーザーの場合、クラス名に"blue"を追加
                    gray: props.role !== "admin" && props.role !== "user", // それ以外の場合、"gray"を追加
                  });
                
                  return <button className={className}>Click</button>;
                }
                
                ```
                
                - clsxのインポート
                    - import clsx from “clsx”;
                - clsxを使ってクラス名を指定する
                    - const classNameとしてclsx (基本となるクラス名を文字列で指定する,{キー: 条件});
                        - 基本となるクラスは条件に関係なく常に適用される
                    
                    ```jsx
                    const className = clsx("button", {
                      red: props.role === "admin",
                      blue: props.role === "user",
                      gray: props.role !== "admin" && props.role !== "user",
                    });
                    ```
                    
                - https://mosya.dev/react/lessons/react-clsx/challenge
            - 演習
                - clsxを使って条件に応じてコンポーネントの表示を切り替える
                    
                    ・要件
                    ・ユーザー体験
                    ・処理
                    
            - 配列をリストとして表示する
                
                ```jsx
                import React from "react";
                
                export function Toc({ title, items }) {
                  return (
                    <div className="toc">
                      <div>{title}</div>
                      <ol>
                        {items.map(({ id, title }) => (
                          <li key={id}>
                            <a href={`#${id}`}>{title}</a>
                          </li>
                        ))}
                      </ol>
                    </div>
                  );
                }
                ```
                
        - `BusinessCard`コンポーネントをカスタマイズしてみましょう！
            
            レッスンを進める際にかく事
            ・要件
            
            - BusinessCardコンポーネントがnameとtitleとimageをpropsとして受け取り、それを適切に表示できるようにしましょう。
            
            ・ユーザー体験
            
            - なし
            
            ・処理
            
            - business-card-imgクラスを持つimg要素のsrc属性に、受け取ったimageを表示する
            - business-card-nameクラスを持つdiv要素内に、受け取ったnameを表示する
            - business-card-titleクラスを持つdiv要素内に、受け取ったtitleを表示する
        - カードコンポーネントがクリックされた時に特定の名前が表示されるようにする
            
            ```jsx
            import React from "react";
            
            export function ProfileCard({ name, nickname, bio, avatarUrl }) {
              // 👇 この下にボタンがクリックされたときの関数を作ってください
            
              return (
                // ボタンに関数を紐付けてください
                <button className="profile-card">
                  <img
                    alt={`${name}'s avatar`}
                    className="profile-card__avatar"
                    src={avatarUrl}
                  />
                  <div className="profile-card__info">
                    <h2 className="profile-card__name">{name}</h2>
                    <p className="profile-card__nickname">@{nickname}</p>
                    <p className="profile-card__bio">
                      {bio ?? "まだ情報が入力されていません。"}
                    </p>
                  </div>
                </button>
              );
            }
            ```
            
            - 要件
                - カードコンポーネントがクリックされた時に特定の情報が表示されるようにする
            - ユーザー体験
                - カードコンポーネント部分をクリックする
            - 処理
                - まずは関数の定義をする
                    - handleClick関数の定義を行う
                        - const handleClick = () => {表示したい内容;};
                            - 表示したい内容はpropsでnameとして受け取っているデータを挿入する
                            - ${name}
                    - ボタンに関数を紐づける
                        - <button className="profile-card" onclick={handleClick}>に紐づける
        - Fragment
            
            Fragmentを使って、各カードのタイトルを2行に分けましょう！
            
            タイトルの「。」の後に改行を加えて、見本のようにタイトルが2行になるようにしてみてください。
            
            ```jsx
            export default function App() {
              return (
                <div>
                  {/* Fragmentを使って、タイトルに改行を追加してください */}
                  <Card hasNew title="Reactとは。なぜReactを使うのか？">
                    この記事では、Reactの魅力や特徴、使い方を解説します。
                  </Card>
                  {/* Fragmentを使って、タイトルに改行を追加してください */}
                  <Card title="ReactとVueの違い。どっちを使うべき？">
                    この記事では、ReactとVueの違いについて解説します。
                  </Card>
                </div>
              );
            }
            ```
            
        - Null 合体演算子
            
            プロフィールカードを完成させましょう！
            
            ただし、bio（自己紹介文）というPropsが空のときは、「自己紹介はまだありません」と表示するようにしてください。
            
            ```jsx
            <div>
                  <ProfileCard
                    avatarUrl="https://static.mosya.dev/react-nullish-check/yamada.png"
                    bio="フロントエンドエンジニアです。"
                    name="Yamada Hanako"
                    nickname="yamada_hanako"
                  />
                  <ProfileCard
                    avatarUrl="https://static.mosya.dev/react-nullish-check/suzuki.png"
                    name="Suzuki Taro"
                    nickname="suzuki_taro"
                  />
                </div>
                
               
              ↑
              {bio ?? "自己紹介はまだありません"}
            ```
            
        - オプショナルチェイニングの演習
            1. `image.size`が定義されていない場合は、`width`や`height`に`undefined`を設定してください。
                - オプショナルチェイニングを使って配列名.プロパティ名?の形になるようにする
                    - **<img src="" alt="" width="" height="">**
                        - src = {image.src}
                        - alt={image.alt}
                        - width= {image.size?.width}
                        - height=  {image.size?.height}
                            
                            ↑
                            
                            オプショナルチェイニングを適用されたいプロパティの後ろに？を記載する
                            
            2. `image.alt`が定義されている場合は、その値を画像の`alt`属性に設定してください。
                - altはどちらも存在しているため設定するようにする
            
            ```jsx
            <div className="card">
                  <div className="card-image">
                    {/* 👇 ここに画像を表示してください。ただし、alt,width,heightは存在すれば設定してください */}
            
                  </div>
                  <div className="card-title">{title}</div>
                  <div className="card-content">{children}</div>
                  <div className="card-meta">
                    <div className="card-date">2030/01/01</div>
                    {hasNew && <span className="card-new">NEW</span>}
                  </div>
                </div>
            ```
            
            <img src={image.src} alt={image.alt} width={image.size?.width} height={image.size?.height} />
            
        - コンポーネントをimportしよう
            
            レッスンを進める際にかく事
            ・要件
            
            すでに定義された関数コンポーネントをimportして実際に使ってみよう
            
            ・ユーザー体験
            
            　　なし
            ・処理
            
            card.jsxで定義されたcardコンポーネントをすでに用意されているdiv要素内にimportしてscriptで表示する
            
            コンポーネントの表示方法
            
            <コンポーネント名 />
            
        - 簡単なクイズアプリを作る　詰まって考えたが難しかった回答を見た
            
            ・要件
            
            - 簡単なクイズアプリを作成する
                - 答えとして設定された文字列が入力された場合に正解の場合と不正解の場合でメッセージを表示する
            
            ・ユーザー体験
            
            - クイズに回答し正解だった場合には正解のメッセージ表示
            - 不正解だった場合には不正解のメッセージが表示される
            
            ・処理
            
            input
            
            onChangeを使いe.target.valueのイベントを活用してansewの値を更新する
            
            Button
            
            onclick
            
            正解だった場合の表示
            
            不正解だった場合の表示
            
            if文使う？
            
            富士山 === true
            
            ```jsx
            import React, { useState } from "react";
            import { createRoot } from "react-dom/client";
            
            export default function App() {
              const [answer, setAnswer] = useState("");
              const [success, setSuccess] = useState(false);
              const [answered, setAnswered] = useState(false);
              return (
                <div className="quiz-wrap">
                  <h1 className="quiz-title">クイズ</h1>
                  <p className="quiz-question">Q.日本で一番高い山は？</p>
                  <input placeholder="回答を入力" type="text" value={answer} onChange={(e) => setAnswer(e.target.value)}/>
                  <button
                    onClick={() =>{
                      if (富士山 === true){
                        setSuccess(true);
                      }else{
                        setAnswered(false);
                      } 
                        setAnswered(true);
                    }}
                  >回答する</button>
                  {/* 👇正解の場合と不正解の場合、それぞれに対して下にメッセージを表示するようにしてください */}
                  {success && answered && <p className="result">正解！</p>}
                  {!success && answered && <p className="result">不正解！</p>}
                </div>
              );
            }
            
            export const root = createRoot(document.getElementById("root"));
            root.render(<App />);
            
            ```
            
        - 画像を表示するAppコンポーネントを作ってみましょう！
            
            レッスンを進める際にかく事
            
            ・要件
            
            画像を表示する`App`コンポーネントを作ってみましょう！
            
            ・ユーザー体験
            
            なし
            
            ・処理
            
            すでに存在しているAppコンポーネントにAppというクラス名を持つdiv要素を用意しimgタグを使いdivタグ（親要素）の中に画像を2つ表示できるようにする。
            
            1. returnでAppコンポーネントが呼び出された際に画像の要素を返すようにする
            2. imgタグを2つ使って画像を表示する
        - クリックできる色のボタンをクリックするよクリックした色に指定した部分が変化するシステム
            
            ・要件
            
            - 用意されているcolors配列の色を特定の場所の下に1つづつ表示する
            - 表示されている色はボタンにしてクリックされると特定の部分がクリックした色に変化する
            
            ・ユーザー体験
            
            - 自分がクリックした色に応じて特定の部分の色が変化する
            
            ・処理
            
            ```jsx
            const colors = ["#EF4444", "#F59E0B", "#10B981", "#3B82F6", "#6366F1"];
            
            const [color, setColor] = useState(colors[0]);
            
            const handleSelectColor = (color) => {
            	setColor(color)
            }
               
            {colors.map((color) => (
                      <ColorButton color={color} key={color} onSelect={handleSelectColor} />))}
            ```
            
            - すでに定義されているプログラム
            - handleSelectColor関数を親コンポーネント内で作成する
                - setColor(選択された色)
            
            ```jsx
            子コンポーネント
            
            <button
                  className="w-6 h-6 rounded-lg"
                  // ここから下に背景色にcolorを指定するコードを書いてください
                  style={{backgroundColor:{ color }}}
                  // また、クリックされた時にonSelectにcolorを渡してください
                  //←❌　無限ループに陥ってしまう記載方法（直接関数を渡してしまっている）
                  onClick={onSelect(color)}
                  // クリックイベントを設定する際にページのレンダリング時にuseStateが実行されてしまう
            	    // useStateが実行されると再度ページがレンダリングされるため無限ループに陥ってしまう
            	    // クリックイベントを設定する際にはアロー関数で関数と引数を渡す事が無限ループの予防になる
            	    // アロー関数にする事で無名関数が呼ばれた時に関数を返すという動きにできる
            	    onClick={() => onSelect(color)}
                />
            ```
            
            https://zenn.dev/kisukeyas/articles/9af27eab7122ce
            
            - 関数を呼び出す　実行する　←→ 関数自身を渡す
                - この棲み分けをする事を意識する
        - EmotionのCSSを使ってみよう
            - 要件
                - EmotionのCSSを実際に使う
                - Emotionをオブジェクトスタイルで使用する
            - ユーザー体験
                - なし
            - 処理
                - 指定された内容を変更、適用する
                
                | **プロパティ名** | **値** |
                | --- | --- |
                | `display` | クリックしてテキストをコピー |
                | `width` | クリックしてテキストをコピー |
                | `height` | クリックしてテキストをコピー |
                | `overflow` | クリックしてテキストをコピー |
                | `box-shadow` | クリックしてテキストをコピー |
                | `border-radius` | クリックしてテキストをコピー |
                
                `.animal-name`には、以下のスタイルを適用してください
                
                | **プロパティ名** | **値** |
                | --- | --- |
                | `font-size` | クリックしてテキストをコピー |
                | `margin-top` | クリックしてテキストをコピー |
                | `color` | クリックしてテキストをコピー |
                - キャメルケースではなくケバブケースで記載する
                - スタイルを適用させたい要素にCSSを適用させるようにする
        - 擬似クラスと擬似要素を使う
            - 要件
                - Style属性でスタイリングされている要素をCSS関数を使ってスイリングする
                - マウスオーバー（hover）した時の擬似スタイルを適用する
                    - `.twitter-card`
                    - `.like-button`
                    - `.retweet-button`
            - ユーザー体験
                - hover時にスタイリングが変化する
            - 処理
                - &hoverで擬似要素を追加する
                    - &hover使用時にはCSS関数を使用する形にしないと動作しない
        - レスポンシブデザイン　Emotion
            - 要件
                - style属性で記載されたCSSをEmotionのCSS関数に書き換える
                - 追加するスタイリングを適用させる
            - ユーザー体験
                - なし
            - 処理
                - CSS関数を使ってスタイリングを行う
                - スタイリングに条件を追加する
                    - 768px以下の時
                    - 481px以上の時
        - Emotionで動的なページを作成する
            - 要件
                - AnimalCardコンポーネントを作成する
                    - .animal-card には指定されたスタイルを適用する
                    
                    ```jsx
                    text-align: center;
                    background-color: propsとして受け取った`color`の値;
                    padding: 20px;
                    
                    {color}とする事でPropsを受け取る
                    ```
                    
                - props として受け取った`image`の値を img 要素の`src`属性に設定する
                    - src={`${image}`}とする
                - props として受け取った`name`の値を表示する
                    - 指定されたスタイルを適用する
                    
                    ```jsx
                    font-size: 16px;
                    margin-top: 10px;
                    color: #666;
                    
                    css={css`font-size: 16px;margin-top: 10px;color: #666;`}
                    オブジェクトスタイルでCSS関数を使う   
                    
                    ```
                    
            - ユーザー体験
                - なし
            - 処理
                - 同上
        - Tailwind CSSを使ってスタイルを適用させる
            - 要件
                - **Tailwind CSSを使って指定されたスタイルを適用させる**
            - ユーザー体験
                - なし
            - 処理
                - JavaScript内に**Tailwind CSSのクラスを使ってスタイリングを行う**
                    - 適用させたい要素にclassName=”クラス名”とする
        - Tailwind CSSを使ってレスポンシブデザインを適用する
            - 要件
                - 前任者から記事一覧のレスポンシブデザインを引き継いだシチュエーション
                    - 画面幅が`1280px`以上の時は4カラム
                    - 画面幅が`1024px`以上の時は3カラム
                    - 画面幅が`768px`以上の時は2カラム
                    - 画面幅が`768px`未満の時は1カラム
            - ユーザー体験
                - 表示画面に応じて表示内容が変わる
            - 処理
                - gridクラスを設定する
                    - 画面幅が`1280px`以上の時は4カラム
                        - xl:grid-cols-4
                    - 画面幅が`1024px`以上の時は3カラム
                        - lg:grid-cols-3
                    - 画面幅が`768px`以上の時は2カラム
                        - md:grid-cols-2
                    - 画面幅が`768px`未満の時は1カラム
                        - デフォルト grid-cols-1
        - Tailwind CSSを使ってインタラクティブなスタイルを適用する
            - 要件
                - innput.textarea要素に指定されたスタイルを適用する
                    - `ring-2`　ボックスシャドーを使ったフォーカスリングを表示する
                    - `ring-offset-2`　フォーカスリングの要素からの距離を指定する
                    - `outline-none`　アウトラインを無効にする
                - ボタン要素に指定されたスタイルを適用する
                    - ボタンがクリックされたときは、背景色を `bg-blue-700` に変更してください。
                    - ホバー状態のときは、背景色を `bg-blue-600` に変更してください。
            - ユーザー体験
                - 上記で設定したスタイルが利用時に適用される
            - 処理
                - input.textarea
                    - `ring-2`　ボックスシャドーを使ったフォーカスリングを表示する
                        - focus: ring-2
                    - `ring-offset-2`　フォーカスリングの要素からの距離を指定する
                        - focus: ring-2 ring-offset-2
                    - `outline-none`　アウトラインを無効にする
                        - disabled: outline-none
                - Bottom
                    - ボタンがクリックされたときは、背景色を `bg-blue-700` に変更してください。
                        - active: bg-blue-700
                    - ホバー状態のときは、背景色を `bg-blue-600` に変更してください。
                        - hover: bg-blue-600
        - 指定された要素に対してダークモード時のスタイルを追加する
            - 要件
                - 指定された要素に対して指定されたダークモード時のスタイルを適用する
                    - data-testidセレクター	ダークモード時のスタイル
                    twitter-card	　　　　　背景色がgray-800
                    twitter-name	テキストがwhite
                    twitter-handle	テキストがgray-300
                    twitter-tweet	テキストがwhite
                    twitter-actions	テキストがwhite
                    twitter-actionsの中のボタン	ホバーしたら背景色がgray-700
            - ユーザー体験
                - ダークモード時とライトモード時でスタイルが変化する
            - 処理
                - tailwind.config.js内のdarkModeプロパティを確認する
                    - class or media　どちらの設定か
                        - class設定の場合には最上位のタグにクラスを追加する
                            - dark:bg-black
                - プリフィックスとしてdark:をつけた上でダークモード時に適用させたいスタイルを追加する
        - 現在、スタイル属性で指定されているスタイルをスタイル属性ではなくCSS Modulesで設定する
            - 要件
                - スタイル属性で指定されているスタイル内容をCSS Modulesに変更しスタイル属性を使わない
            - ユーザー体験
                - なし
            - 処理
                - スタイル属性で指定されている内容を確認する
                - style.module.cssファイルに現在スタイル属性として指定されている内容を記載する
                - CSS Modulesの内容が記載されているmodule.cssファイルをインポートする
                    - style.スタイル名と記載を変更する
        - 論理AND演算子の演習
            
            〇⚫️〇コードの流れが一部把握できないかった演習〇⚫️〇
            
            2月17日更新
            
            ```jsx
            import React, { useState } from "react";
            import { createRoot } from "react-dom/client";
            
            export default function App() {
              const [answer, setAnswer] = useState("");
              const [success, setSuccess] = useState(false);
              const [answered, setAnswered] = useState(false);
              return (
                <div className="quiz-wrap">
                  <h1 className="quiz-title">クイズ</h1>
                  <p className="quiz-question">Q.日本で一番高い山は？</p>
                  <input placeholder="回答を入力" type="text" value={answer} onChange={(e) => setAnswer(e.target.value)}/>
                  <button
                    onClick={() =>{
                      if ( answer === "富士山"){
                        setSuccess(true);
                      }else{
                        setAnswered(false);
                      } 
                        setAnswered(true);
                    }}
                  >回答する
                  </button>
                  inputタグに入力された内容が
                  "富士山"の場合
                  setSuccess(true)となりsuccessのuseStateの初期値がtrueに更新される
                  setAnswered(true)となりansweredのuseStateの初期値がtrueに更新される
                  success=true
                  answered=true
                  "富士山"以外の場合
                  setAnswered(false)となりansweredのuseStateの初期値がfalseに更新される
                  setAnswered(true)となりansweredのuseStateの初期値がtrueに更新される
                  success=false
                  answered=true
                  {/* 👇正解の場合と不正解の場合、それぞれに対して下にメッセージを表示するようにしてください */}
                  論理AND演算子を使う
                  {success && answered && <p className="result">正解！</p>}
                  succsessがtrueかつansweredがtrueの場合には<p className="result">正解！</p>を表示する
                  {!success && answered && <p className="result">不正解！</p>}
            	    !successがfalseかつansweredがtrueの場合<p className="result">不正解！</p>を表示する
                  ↓
                  JSX内でJavaScriptを記載して参照している
                  returnで表示される内容をsuccessとansweredでを使って表示される内容に変化させている
                </div>
              );
            }
            
            export const root = createRoot(document.getElementById("root"));
            root.render(<App />);
            ```
            
        - useEffectの演習（タイマーの作成）
            - 要件
                - useEffectを使って画面表示から分:秒の形で表示されるタイマーを作成する
                - アンマウント(表示を終了)した際にはタイマー機能を終了する
            - ユーザー体験
                - 画面表示と共にタイマーが作動し時間を計測する
            - 処理
                - useEffectを依存配列を空にして使い画面表示と共に発火するようにする
                - setCountとしてカウント内容を記載する
                - set関数を変数で囲む
                    - 無限ループを避ける
                - クリーンアップ関数を記載する
        - useRefの演習（カウント回数に応じてアラートを発火するuseRef）
            - 要件
                - useRefを使ってボタンが10回クリックされるとアラートが発されるようにする
            - ユーザー体験
                - ボタンを10回クリックするとアラートが発火する
            - 処理
                - useRefの初期値を0とする
                    - const ref = useRef(0);
                - ボタンをクリックする毎に初期値が更新されるようにする
                    - useRefの値は.currentプロパティに保存される
                        - onClick関数を使いクリック毎に値が更新されるようにする
                            - onClick={() => ref.current++}
                - useRefの値が10になった場合（10回クリックする）にアラートを発火させる
                    - if ref.current = 10 alert('クリックしすぎです！');
                    - alertCurrent
                
                ```jsx
                手順
                1.useRefを定義する
                	ーconst Ref = useRef(0);
                2.BottonにhandleClick関数を紐つける
                	ー<botton onClick={handleClick}>
                3.handleClick関数を定義する
                	-クリックされると.currentプロパティに1追加される
                	-クリックが10回された場合にアラートを発火する
                		-const handleClick = () => {
                		  Ref.current++
                		  if (Ref.current === 10){
                			  alert("クリックしすぎです！");
                		  };}
                ```
                
        - useRefを使ってDOM操作を行いChartを使いグラフにして表示するー答えみたー
            - 要件
                - useRefとChartというライブラリを使ってデータをグラフに描出する
            - ユーザー体験
                - なし
            - 処理
                - 作成したいグラフ
                    - 縦軸
                        - 投票数
                    - 横軸
                        - 投票対象（色）
                    - 表示される投票結果の構成
                        - バックグラウンドカラー
                        - ボーダーカラー
                - 手順：
                    - チャートに独自のコンテナーを用意する
                    - キャンバス要素を取得する
                    - チャートの種類や必要な情報を記載していく
                    
                    ```jsx
                    <script>
                      const ctx = document.getElementById('myChart');
                    
                      new Chart(ctx, {
                        type: 'bar',
                        data: {
                          labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                          datasets: [{
                            label: '# of Votes',
                            data: [12, 19, 3, 5, 2, 3],
                            borderWidth: 1
                          }]
                        },
                        options: {
                          scales: {
                            y: {
                              beginAtZero: true
                            }
                          }
                        }
                      });
                    </script>
                    ```
                    
                - 答えみた　コードリーディング
                    
                    ```jsx
                    export function VoteChart({ data, labels, label }) {
                    	//参照したい要素をuseRefとして定義する
                      const chartRef = useRef(null);
                    
                    　//空の依存関係のuseEffectを定義する
                      useEffect(() => {
                    	  //もし、chartRef.currentがnullの場合(参照したい要素がない場合)useEffectはretrunして終了する
                    	  //もし、chartRef.currentがnullではない場合にはreturnしない
                        if (!chartRef.current) {
                          return;
                        }
                        //チャートの定義
                        myChartと定義してchartRef.current(ref属性が指定されたcanvasタグ)を引数として渡す
                        const myChart = new Chart(chartRef.current, {
                          type: "bar", // チャートの種類を選択
                          data: {
                            labels,
                            datasets: [
                              {
                                label,
                                data,
                                backgroundColor,
                                borderColor,
                                borderWidth: 1,
                              },
                            ],
                          },
                        });
                        //クリーンアップ関数を作成する
                        //myChartをdestroyメソッドで削除する
                        return () => myChart.destroy();
                      }, []);
                    
                      return (
                        <div>
                          <canvas ref={chartRef}></canvas>
                          //useRefで参照するためref属性を付ける
                        </div>
                      );
                    
                    ```
                    
        - useEffectを使って値の変更に応じた処理を行う
            - 要件
                - useEffectを使って動画の再生と停止を再生ボタンでコントロールできるようにする
                    - useEffectを使いpropsのisPlayingが
                        - trueの時に、videoRef.current.play()を実行
                        - falseの時にvideoRef.current.pause()を実行
            - ユーザー体験
                - 再生ボタンで動画の再生、停止をコントロールできる
            - 処理
                - useEffectの依存関係に再生ボタンを置く
                - 再生ボタンを押すことでisPlayingを操作する(treu or false)
                - 再生ボタンとハンドル系の関数を紐つける
        - カスタムフックを使って値を保存する機能を作成する
            - 要件
                - 現在記載されている関数をuseStorageというカスタムフックに変更する
                    - `key`と`defaultValue` を受け取りlocalStorageに値を保存する
                        - 帰り値には現在の値と値を更新するための関数が返ってくる
            - ユーザー体験
                - CSSなど選択したタブに応じて処理が変更される
            - 処理
                
                ```jsx
                //useStorageを定義する。引数としてkey, defaultValueを渡す
                export function useStorage(key, defaultValue) {
                	//useStateを定義する。valueを管理する変数とおきsetValueをトリガーとする
                	//useStateの初期値はdefaultValueにする
                  const [value, setValue] = useState(defaultValue);
                  //onChange関数を定義する。
                  //引数をnewValueとしてsetValueの引数にnewValueを渡してuseStateの値を更新する
                  const onChange = (newValue) => {
                	  //localStorage.setItemとする事でブラウザーにデータを保存する
                	  //key, newValueをuseStorageに保存する
                    localStorage.setItem(key, newValue);
                  };
                
                	//useEffectの定義
                  useEffect(() => {
                	  //useEffectを定義する
                	  //date変数をkeyを引数としてlocalStorage.getItemでブラウザに保存されたデータを取得する
                    const data = localStorage.getItem(key);
                    //もし、dateがtrueの場合には
                    if (data) {
                	    //setValueの引数にdataを渡してuseStateの値を更新する
                      setValue(data);
                    }
                	   //依存関係にある変数はkeyとする
                  }, [key]);
                
                  return [value, onChange];
                }
                ```
                
        - useReducer
            - 要件
                - Todoアプリの状態管理部分をuseReducerを使って実装する
                    - 新しい TODO を追加できる。
                    - 各 TODO には一意の ID とタイトルが含まれる。
                    - TODO を削除できる
                    - 登録済みの TODO のタイトルを変更できる
            - ユーザー体験
                - Todoの追加、削除、編集が可能になる
            - 処理
                - Stateの内容
                
                ```jsx
                [
                  { id: 1, title: "TODO1" },
                  { id: 2, title: "TODO2" },
                  { id: 3, title: "TODO3" },
                ];
                
                ```
                
                - 追加するaction
                
                ```jsx
                Todoの追加
                { type: 'ADD', title: 'TODO'の名前 }
                Todoの削除
                { type: 'REMOVE', id: 削除するTODOのID }
                Todoの編集
                { type: 'UPDATE', id: 変更するTODOのID, title: 変更後のタイトル }
                ```
                
                - Reducer関数の定義
                - useReducerフックを呼び出す
                - ボタンにaction内容を紐つける
            - 自分で記載したコード
            
            ```jsx
            switch(action.type){
                case "ADD":
                  return {
                    ...state,
                    title,
                  };
                case "REMOVE":
                  return {id, id:action.payload};
                case "UPDATE":
                  return {id: id.action.payload, title: title.action.payload}
                default:
                  return state;
            ```
            
            - 正解のコード
            
            ```jsx
            　switch (action.type) {
                case "ADD":
                  return [...state, { id: String(Math.random()), title: action.title }];
                  //...stateで現在の状態を展開
                  //id: String(Math.random())で文字列であり整数の値をランダムに生成する
                  //title: action.titleとしてactionから受け取ったtitleを値として代入する
                  //最終的に展開された状態へ、ランダムに生成された整数のidとアクションから受け取ったtitleが代入される
                case "REMOVE":
                  return state.filter((todo) => todo.id !== action.id);
            	    //filter関数を使ってtodoを引数として受け取りtodo.idとaction.idが一致しないもの全て取得する
            	    //todo.idとaction.idが一致するstateはreturnされない
                case "UPDATE":
                  return state.map((todo) =>
                    todo.id === action.id ? { ...todo, title: action.title } : todo);
            	      //stateをmap関数で変数todoへ代入する
            	      //条件としてtodo.idとaction.idが厳格に等しいか判別する
            		      // ? { ...todo, title: action.title } : todo)としてtodo.id === action.idが等しい場合には
            		      //展開したtodoにaction.titleをtitleをプロパティとした時の値とする
            	      //todo.id === action.idが等しい場合にはアクションから受け取ったtitleに更新する
                default:
                  return state;
                  caseに合致しない場合には現在の状態を返す
              }
            };
            ```
            
        - 配列messagesにメッセージを追加する
            - 要件
                - 配列massagesにメッセージ（要素を追加する）
                - すでに一意なIDは作成されている
            - ユーザー体験
                - メッセージを送信するとチャットに追加される
            - 処理
                - add関数を作成する
                - 作成したuseStateにトリガーとなっているstateをスプレッド構文で展開する
                - 展開したstateにコピーする
                - 展開しコピーしたstateをreturnする
        - メッセージ削除用の関数を作成する
            - 要件
                - メッセージを追加する関数を実装する
                - メッセージを削除する関数を実装する
            - ユーザー体験
                - なし
            - 処理
                - add関数
                    - 配列に対してfindIndexを条件式を選択したオブジェクトのidと引数としてリクエストから受け取ったidが等しいかチェックする
                    
                    ```jsx
                     function addMessage({ text, position, avatar }) {
                        const id = generateId();
                        // 👇 この関数の続きを実装してください
                        setMessages([...messages,{ text, id, position, avatar }])
                      }
                    
                    const handleAddMessage = () => {
                        const text = inputRef.current?.value;
                        if (text) {
                          // 👇 ここに処理を追加してください
                          addMessage({text, avatar, position: "right" });
                          inputRef.current.value = "";
                        }
                      };
                    ```
                    
                - remove関数
                    - 削除したい関数を除いた配列を作成する
                        - filter関数を使いidとmessage.idが厳格に等しいものを！＝＝で省く
                            - リクエスト元から送られてきたidと等しい
                        
                        ```jsx
                        function removeMessage(id) {
                            // 👇 この関数の中身を実装してください
                            setMessages(messages.filter((message) => message.id !== id));
                          }
                          
                         const handleRemove = (id) => {
                            // 👇 ここに処理を追加してください
                            removeMessage(id);
                          };
                        ```
                        
        - 配列の要素を更新する
            - 要件
                - チャットアプリを作成する
                    - 実装する機能
                        - メッセージの新規作成
                        - メッセージの削除
                        - メッセージの編集
            - ユーザー体験
                - チャット機能としてメッセージの送信、削除、編集を行うことができる
            - 処理
                - add関数
                    - メッセージの新規作成
                        - pushメソッドを使い配列にデータを追加する
                            - set関数の引数に新しいオブジェクトを作成する
                                - スプレッド構文を使いuseStateのトリガーになっている変数を展開する
                                - 引数として受け取っているものを展開した変数のプロパティとして渡す
                            - 変数をコピーする
                        - 受け取る引数
                            
                            ```jsx
                            {
                              "text": "メッセージの内容",
                              "id": generatedId(),
                              "createdAt": new Date(),
                              "user": {
                                "name": "ユーザー名",
                                "avatarUrl": "アバターのURL"
                              }
                            }
                            ```
                            
                - remove関数
                    - メッセージの削除
                        - 受け取る引数
                            - idを引数として受け取り受け取った引数のstateを削除する
                - update関数
                    - メッセージの編集
                        - update関数を定義する
                            - 配列のデータを取得する
                            - 三項演算子でidを使う
                            - 条件に一致しないデータは触らずに一致するデータの要素を更新する
                            - 更新した配列をuseStateのトリガーとなっている変数にコピーする
                            - useStateを発火させてレンダリングすることで要素を編集する
                    - 受け取る引数
                        - 第一引数にメッセージのid、第二引数に更新するメッセージを受け取る
                        - `messages`の配列から第一引数で受け取ったidのメッセージを探し、第二引数で受け取ったメッセージで上書きします。
        - fetch
            - 要件
                - APIを使いデータを取得しビューに表示する
            - ユーザー体験
                - なし
            - 処理
                - useEffect関数でfetchメソッドを使いAPIを介してデータを取得する
                - 配列になっているデータをMUSICLISTとして表示する
                    
                    ```tsx
                    {
                      musics: [
                        {
                          id: 1,
                          title: "曲のタイトル",
                          artist: "アーティスト名",
                          image: "画像のURL",
                        },
                        ...
                      ]
                    }
                    ```
                    
                    - MUSICLIST内のコンポーネントはMUSICITEMとする
                    
                    ```tsx
                    <MusicList>
                      {musics.map((music) => (
                        <MusicItem key={music.id} music={music} />
                      ))}
                    </MusicList>
                    ```
                    
                    ```tsx
                    	useEffect(() => {
                        fetch("/api/mock/music")
                          .then((response) => response.json())
                          .then(({ musics }) => setMusics(musics));
                      }, []);
                    
                      return (
                        <div className="bg-black p-8">
                          <h2 className="text-white text-3xl font-bold mb-6">ヒットソング</h2>
                          <MusicList>
                            {musics.map((music) => (
                              <MusicItem key={music.id} music={music} />
                            ))}
                          </MusicList>
                        </div>
                      );
                    
                    ```
                    
            
        - Suspence
            - 要件
                - APIから情報を取得する。
                    - 情報の取得中にはSusoenceを使って別の表示画面を作成する
            - ユーザー体験
                - データのローディング中に別の表示画面が表示される
            - 処理
                - データローディングを実行するコンポーネントをSuspenceタグでラップする
                    - ローディング中に表示したい画面はfollow backで記載する
            
            ```
            import useSWR from "swr";
            
            import type { Music } from "./types";
            
            export function useMusics() {
              // ここでuseSWRを使ってデータを取得する処理を書いてみよう！
              // さらにsuspenseを有効にしてみよう！
              const { data } = useSWR<{ music:Music }>(
                "/api/mock/music",
                {
                  suspense: true,
                }
              )
              return {
                data,
              };
            }
            ```
            
        - react-error-boundary
            - 要件
                - /api/mock/musicの通信中にエラーが発生した場合に画面全体が影響を受けないようにする
            - ユーザー体験
                - エラーが発生した場合でも対象のコンポーネントのみがエラー表示になるようになる
            - 処理
                - ErrorBoundaryを使い、エラーが発生した場合に対象のコンポーネントのみがエラー表示されるようにする
            
        - fetch関数を使ってサーバーへデータを送信する
            - 要件
                - Todoリストを表示、追加できるアプリを作成する
                - 準備されているソースコード
                
                ```tsx
                import { useEffect, useState } from "react";
                
                type Todo = {
                  id: number;
                  title: string;
                };
                
                export function useTodos() {
                  const [todos, setTodos] = useState<Todo[]>([]);
                
                  const addTodo = (title: string) => {
                    // addTodoを実装してください
                  };
                
                  const refetch = () => {
                    fetch("/api/mock/todo")
                      .then((response) => response.json())
                      .then(({ todos }) => setTodos(todos));
                  };
                
                  useEffect(() => {
                    refetch();
                  }, []);
                
                  return { todos, addTodo };
                }
                ```
                
            - ユーザー体験
                - Todoの追加ができる
            - 処理
                - addTodoを定義する
                    - 引数に型をstringに指定したtitleを受け取る
                    - fetch関数を使いapiを指定する
                        - 指定したAPIにデータを送信する
                            - methodをPOSTに指定する
                            - bodyを指定しJSON.stringifyをtitleに指定して文字列に変換する
                        - thenを使い、アロー関数（無名関数）を使ってreftchを発火させてコンポーネントのレンダリングを行い一覧表示を更新する
                        
                        ```tsx
                        import { useEffect, useState } from "react";
                        
                        type Todo = {
                          id: number;
                          title: string;
                        };
                        
                        export function useTodos() {
                          const [todos, setTodos] = useState<Todo[]>([]);
                        
                          const addTodo = (title: string) => {
                            // addTodoを実装してください
                            fetch("/api/mock/todo",{
                              method: 'POST',
                              body: JSON.stringify({ title }),
                            }).then(() => 
                              refetch());
                          };
                        
                          const refetch = () => {
                            fetch("/api/mock/todo")
                              .then((response) => response.json())
                              .then(({ todos }) => setTodos(todos));
                          };
                        
                          useEffect(() => {
                            refetch();
                          }, []);
                        
                          return { todos, addTodo };
                        }
                        
                        ```
                        
- 概念
    - イミュータブルなフレームワーク
        - Reacrではイミュータブルに変数を扱う
            - ミュータブルに扱うとデータが追いづらくなる
                - パフォーマンスが悪くなる
                    - 全てのプロパティを追わないといけない
                        - 例えばuseStateでも直接的に値は変更せずに値を変更する関数を挟んで再レンダリングする事で表示を更新する
    - Hot Reroading
        - コード側で保存せずにコンソールでは変更内容が表示される仕組み
    - 高階関数
        - 関数から関数を返す方法
            - () => () =>という書き方で、一つの関数から別の関数を返します。
    - 状態stateについて
        - コンポーネントが持っているデータの事を状態と呼ぶ
            - Reactでは状態に応じて表示内容が変化する
        - 通常の関数を更新した場合には表示画面に変化は起きない
            - 表示画面に変化を起こすためにはuseStateというHooksを使う必要がある
                - useStateはStateの保持をした上で関数の結果を反映する事ができる
            
            ```jsx
            import { useState } from "react";
            
            export function App() {
            	//useStateをsetCountをトリガーにしてcountを管理する
              const [count, setCount] = useState(0);
            
            //handleClick関数を定義
              const handleClick = () => {
                setCount(count + 1);
              };
            
              return (
                <button onClick={handleClick}>
                  <img
                    className="icon"
                    src="https://static.mosya.dev/react-state/good-icon.png"
                  />
                  <span className="bubble">
                    good!
                  </span>
                  <span className="count">
                    {count}
                  </span>
                </button>
              );
            }
            
            ```
            
            - useStateはReactの関数コンポーネント内でしか使用する事ができない
        - 関数を使った状態の更新には2種類の方法がある
            - 通常の方法
                
                ```jsx
                const handleClick = () => {
                    setCount(count + 1);
                    setCount(count + 1);
                    setCount(count + 1);
                    };
                ```
                
                - 例えば、3回分関数を増やそうとしても1回分（最初のcountを使ってしまう）
            - 関数を使う方法
                
                ```jsx
                //毎回前のcountを取ってきて計算をする
                setCount((prevCount) => prevCount + 1);
                
                setCount((prevCount) => prevCount + 1);
                setCount((prevCount) => prevCount + 1);
                setCount((prevCount) => prevCount + 1);
                ```
                
                - 前回の値をpreする事で値の更新をする事ができる
        - useStateを使ってテキストの表示、非表示を切り替える事ができる
        
        ```jsx
        import React, { useState } from "react";
        
        export function App() {
          const [isVisible, setIsVisible] = useState(false);
        
          return (
            <div className="container">
              <input
                type={
                  isVisible
                    ? "text"
                    : "password"
                }
                placeholder="パスワードを入力"
                className="password-input"
              />
              <button
                onClick={() =>
                  setIsVisible(!isVisible)
                }
                className="toggle-button"
              >
                {isVisible
                  ? "非表示にする"
                  : "表示する"}
              </button>
            </div>
          );
        }
        
        ```       
    - 簡単なTodoアプリを作成する際に必要な思考回路（Youtube）
        - コンポーネントの理解
            - TodoアプリにおいてTodoListコンポーネントというものが必要になる
                - TodoListコンポーネントはどんなコンポーネント？
                    - いくつかのTodoコンポーネントを格納しているコンポーネント
                        - タスクに対して各々にコンポーネントに対応させる
                            - タスクを一つ一つ取り出す
                                - map関数を使って一つずつ取り出す
                            - 取り出したタスクのコンポーネントを作成する
                                - コンポーネントをtodoとして作成する
                            
                            ```jsx
                            const TodoList = ({todos}) => {
                             return todos.map((todo) => <Todo todo={todo} />);
                             };
                            ```
                            
        - データの流れの理解
            - App.JS
                - Appコンポーネントのファイル
                    - index.htmlでAppコンポーネントとしてBodyに表示される
                - TodoListにPropsでtodosを渡す
                    - <TodoList todos={todos} />
                        - todosは初期値として2つの値が用意されている
            - TodoList.js
                - TodoListコンポーネントはPropsとしてtodosを受け取る
                
                ```jsx
                const TodoList = ({todos}) ⇒ {
                	return todos.map{(todo) => <Todo todo={todo} />};
                	};
                ```
                
                - Todosには初期値として2つの値が入っているため初期値をmap関数を使って1つずつ取り出す
                    - 取り出した値に対してさらにTodoコンポーネントでTodoをPropsで渡す
            - Todo.JS
                - TodoにPropsで渡されたTodoをTodo.JSでTodoと定義して表示する
                
                ```jsx
                const Todo = ({todo}) => {
                	return <div>{todo}</div>;
                };
                ```
                
            - Propsのバケツリレー
                - Propsを順番に渡す流れの事をPropsのバケツリレーという
                    - 好ましくない記載方法である
            - map関数を使う際のエラー、注意点
                - Todoコンポーネントが2つある状態
                    - どちらも同じ名前(Todo)になっているのでコンピューター側で判別が不可になっている状態
                        - Keyという形で名前をつける事で一意に判別する事が可能にする事で解決できる
                            - key={todo}
                        - uniqueなKeyをつける事が必要
                            - 一意のKeyをつける事を意識する
            - App.jsでTodosを定義しているが、状態変数はオブジェクトとして定義する事ができる
                - オブジェクトとして定義した場合には表示する際にプロパティ名を指定する事が必要
                
                ```jsx
                App.jsでオブジェクトとしてtodosを定義
                ↓
                function App() {
                 const [todos. setTodos] = useState([
                  { id: 1,name: "Todo1", completed: false },]
                  };
                 
                 TodoListでTodoコンポーネントにオブジェクトを代入したTodo.jsで表示するためにjsx内に
                 プログラムを記載する場合にはプロパティを指定しないとエラーになってしまう。
                 jsx内ではオブジェクトとしてではなく、値を扱うようにする
                 ↓
                 return <div>{todo.name}</div>
                ```
                
        - Todoをタスクになるようにデザインする
            
            ```html
             Todoコンポーネントの内容
             
             return 
            	 <div>
            		 <label>
            			 <input type="chekbox" checked={todo.completaed} readOnly />
            		 <label>
            		 {todo.name}
            	 </div>
            ```
            
            chekboxの後にcheckedというプロパティを使って、true or falsでチェックがされるかされないかを変化させる
            
        - buttonタグに対して属性を指定する
            
            ```jsx
            import { useState, useRef } from "react";
            
            function App() {
             const [todos. setTodos] = useState([
              { id: 1,name: "Todo1", completed: false },
              ]);
              
              const todoNameRef = useRef();
              ↑
             定数の定義
              
              //Appコンポーネント内で定義する事を忘れないように
              const handleAddTodo = () => {
            	  //タスクを追加する
            	  const name = todoNameRef.current.value
            	  setTodos((prevTodos) => {
            		  return [...prevTodods,{id "1", name: name, completad: false}];
            	  }];
            	  todoNameRef.current.value = null;
              };
              ↑
              current valueに出力される
              console.log(todoNameRef.current.value);
              
              return (
            	  <>
            		  <TodoList todos={todos} />
            		  <input type="text" ref={todoNameRef}>
            		  <button onClick={handleAddTodo}>タスクを追加</button>
            		  <button>完了したタスク</button>
            		  <div>残りのタスク</div>
            };
            ```
            
            - handleAddTodo関数を定義する
                - handleAddTodoをアロー関数で定義する
                - name（Todoの内容）を定義する
                    - todoNameRef.current.value
                        - todoNameRef
                            - todoNameをRef（レファレンス：参照する）という意味を持つ定数
                                - const todoNameRef = useRef();
                                    - useRefというHooksを使って指定したHTMLの要素を参照できる
                                        - 今回はinputタグにref属性としてtodoNameRef**を値にしている**
                        - current.value
                            - ref属性で指定されたinputタグから入力された要素はcurrent内のvalueに格納される
                                - current内のvalueに格納された値を取得する
                - setTodos((prevTodos) => {return [...prevTodods,{id "1", name: name, completad: false}];}];
                    - setTodos
                        - useStateでトリガーとした変数
                    - (prevTodos) => {return [...prevTodods,{id "1", name: name, completad: false}];}
                        - prevTodos
                            - Todosをprev(プレビュー：参照)するという意味を持つ引数
                        - ...prevTodods
                            - …　スプレッド構文
                                - 変数として格納されているオブジェクトを展開しスプレッド構文にする
                                    - 値の橋渡しをする
                            - ...prevTododsで展開した変数に引数として渡されているprevTodosの値を代入する
                                - ここまでの処理をsetTodosが呼びだれた際にはretrunする
                                    - setTodosはuseStateのトリガーになっており、Todosの値を更新してレンダリングする
                    - todoNameRef.current.value = null;
                        - inputタグに入力されたcurrent.valueをnullにする
                - todoNameRef.current.value = null;
        - handleAddTodo関数を定義する
            - inputタグに入力されたものをタスクとして登録したい
                - useRefというhooksを使う
                    - useRefはinputに入力された文字列(要素)を取得する事ができる
                        - 取得先の指定方法はrefで指定したフィールドからデータを取得する事ができる
                            - 今回はinputに入力された文字列を取得したい
                        - useRefをtodoNameRefとして定義する
                            - inputにref属性を追加し{todoNameRef}名前を取得する
                - 変数を用意する
                    - const todoNameRef = useRef();
        - setTodos関数
            - タスクの追加、変更、削除などをする関数
                - useStateのトリガーとなる関数
                    - setTodos関数の引数にメソッドや関数を入れる事でTodosが更新される
                        - スプレッド構文
                        
                        ```jsx
                        (関数名) => {} return [...関数名, {オブジェクト}];
                        ↑
                        関数名の前に...をつける事でスプレッド構文に変化する
                        配列にしてカンマで間を区切る
                        ```
                        
                - prevTodos関数
                    - Todosの前の状態をプレビューするという意味の関数
                        - スプレッド構文で配列を展開しカンマで区切ったオブジェクトをその配列に追加するという流れになる
        - エラー
            - キーの重複がエラーになってしまう
                - key部分にはuuidというライブラリーを使う事がおすすめ
                    - ターミナルでインストールする
            - uuidの使用方法
                - ターミナルでnpm install
                    - import
                        - import { v4 as uuidv4 } from “uuid”;
                    - App.jsのAppコンポーネントのidプロパティの値をuuidv4()に変更する
                    - その後、Todoのid部分をprops.idにする
        - エラー
            - チェックボックスの機能を実装する
            - App.jsのAppコンポーネントで
            
            ```
            const toggleTodo = (id) => {
                const newTodos = [...todos];
                const todo = newTodos.find((todo) => todo.id === id);
                //findメソッドは条件に合う最初の要素を返す
                //条件に合う要素がない場合はundefinedを返す
                //条件に合う要素が複数ある場合は最初に見つかった要素を返す
                //条件に合う要素が見つかった時点で探索を終了する
                //idは引数に渡されたid
                todo.completed = !todo.completed;
                //反転されたデータで更新する
                setTodos(newTodos);
                }; 
            ```
            
            - チェックボックスを反転させる関数を作成する
        - チェックボックスの作成
            
            ```jsx
            const toggleTodo = (id) => {
            	const newTodos = [...todos];
            	//状態関数を直接触るのは良くないのでスプレッド構文として広げて代入する
            	const todo = newTodos.find((todo) => todo.id === id);
            	//idとtodo.idが合致するtodoを探索する
            	todo.completed = !todo.completed;
            	//todo.completedを現在の状態から論理否定を使い反転させる
            	//trueの場合、falseを返し　falseの場合にはtrueを返す
            	setTodos(newTodos);
            	//todo.completedが反転した状態のnewTodos(find関数で取得したtodo)をuseStateのトリガーとなっているsetTodosを使って更新する
            	};	
            ↑
            引数にはidを渡す
            find関数は条件式と合致するオブジェクトを選択する
            
            Propsで受け渡す
            App.js
             Appコンポーネント内のTodoListに渡す
             <TodoList todos={todos} toggleTodo={toggleTodo} />
            TodoList.js
            	TodoListでPropsを受け取り、さらにTodoコンポーネントに渡す
            	const TodoList = ({todos, toggleTodo}) ⇒ {
            	return todos.map{(todo) => <Todo todo={todo} key={todo.id} toggleTodo={toggleTodo} />};
            	};
            
            Todo.js
            	Todoコンポーネントに渡す
            const Todo = ({ todo, toggleTodo }) => {
            	const handleTodoClick = () => {
            		toggleTodo(todo.id);
            		//inputタグに値が入力された場合にonChange関数を使って入力に応じてhandleTodoClickが発火するようにする
            		//todo.idは自分自身としてtoggleTodoへ引数として渡す。
            		//find関数を使いtodo.idとidが一致する場合にtodosを取得する
            		//completedの状態を！を使い反転する
            		//setTodosをトリガーとしてnewTodosを更新する
            	};
            
            	return (
            	 <div>
            		 <label>
            			 <input type="chekbox" checked={todo.completaed} readOnly onchange={handleTodoClick} />
            		 <label>
            		 {todo.name}
            	 </div>
            	 );
             };
            ```
            
        - 残りのタスクの表示
            - 要件
                - チェックボックスにチェックが入っていないものを数えたい
            - 処理
                - Todoコンポーネントが全て入っている親コンポーネント内のチェックボックスにチェックが入っていないTodoコンポーネントの数を数えて表示したい
                    - Todoコンポーネントが全て入っている親コンポーネント内
                        - Todos
                    - チェックが入っていないTodoコンポーネントの数を数えて表示したい
                        - チェックが入っていないTodoコンポーネント
                            - !todo.completaed
                                - completedの反対であるコンポーネント
                            - 条件に一致するものを全て取得する関数
                                - filter関数を使う
                        - 数を数える
                            - ドット記法でlengthとする事で数える事ができる
            
            ```jsx
            return (
            	  <>
            		  <TodoList todos={todos} />
            		  <input type="text" ref={todoNameRef}>
            		  <button onClick={handleAddTodo}>タスクを追加</button>
            		  <button　onClick={handleClear}>完了したタスク</button>
            		  <div>残りのタスク:{todos.filter((todo) => !todo.completaed).length}}</div>
            		  todos.filter
            			  //todosというtodoコンポーネントが入っているコンポーネントに対してfilter関数を使う
            		  (todo) => !todo.completaed).length
            			  //filter関数の条件式を用意する
            			  //アロー関数としてtodoを引数としてtodo.completaedのオペランドがtrueの場合にはfalseを返しそれ以外の場合にはtrueを返すようにする
            			  //今回の場合にはチェックボックスにチェックが入っている状態はcompletaedがtrueの場合になる
            			  //trueのfilterに一致するものを.lengthとして数える
            ```
            
        - タスクの削除（論理否定を使ったレンダリング）
            - ボタンを押した時にチェックボックスにチェックが入っているものを全て削除する
                - completedがtrueであるタスクを全て削除する
                    - todos（TodoList）をcompletedがfalseのものを残したい
                        - filter関数でcompletedがfalseのコンポーネントが残るように条件を設定する
                            - 論理否定を使う
                                - trueになる条件がcompletedがfalseの時＝!todo.completed
            
            ```jsx
            const hanndleClear = () => {
            	const newTodos = todos.filter((todo) => !todo.completed);
            	setTodos(newTodos);
            };
            //newTodosと定義してtodoコンポーネントが入っている変数を更新する
            //todos.filter
            	//todosに対してfilter関数を使い条件に一致するものを全て取得する
            //条件として(todo) => !todo.completed)を用意する
            	//アロー関数としてtodoを引数として渡し!todo.completedと処理する事でcompletedがtrueの場合にはfalseとなり、
            　//completedがfalse（チェクボックスにチェックが入っていない状態）のものがtrueとなる
            //setTodos(newTodos)
            	//setTodosとする事でuseStateを発火させ引数にnewTodosとする事でTodoListを更新する
            	//結果的に完了したタスク=todo.completed(true)が取り除かれて未完了のタスク=todo.completed(false)のみが残り
            	//完了したタスクが削除されたようなレンダリング内容になる
            	
            return (
            	  <>
            		  <TodoList todos={todos} />
            		  <input type="text" ref={todoNameRef}>
            		  <button onClick={handleAddTodo}>タスクを追加</button>
            		  <button　onClick={handleClear}>完了したタスク</button>
            			//完了したタスクにhandleClearとしてonClickで発生するイベントにする
            ```
            
            - !はJavaScriptにおいて論理否定と呼ばれる
                - 単一のオペランド（数値など）がtrueに見られる時にはfalseを返してそのほかの場合にはtrueを返す役割
        - 空白のタスクが追加されないようにする
            
            ```jsx
            const handleAddTodo = () => {
            	  //タスクを追加する
            	  const name = todoNameRef.current.value
            	  if (name === "") return;
            	  //name === ""がtrueであればreturnする
            	  //falseであれば処理を実行しない
            	  setTodos((prevTodos) => {
            		  return [...prevTodods,{id "1", name: name, completad: false}];
            	  }];
            	  todoNameRef.current.value = null;
              };
            ```
            
        - Propsのバケツリレーをする
            
            ```jsx
             <TodoList todos={todos} toggleTodo={toggleTodo} />
            ```
            
            - TodoListコンポーネントへPropsとして渡す
            
            ```jsx
            const TodoList = ({ todos, toggleTodo}) => {
              return todos.map((todo) => <Todo todo={todo} key={todo.id} toggleTodo={toggleTodo} />);
            };
            ```
            
            - TodoListコンポーネントでmap関数で一つづつ取り出した要素に対してPropsで渡す
            
            ```
            const Todo = ({ todo, toggleTodo }) => {
                const handleTodoClick = () => {
                    toggleTodo(todo.id);
                };
            
                return (
                <div>
                    <label>
                      <input
                        type="checkbox" 
                        checked={todo.completed} 
                        readOnly 
                        onChange={handleTodoClick} 
                      />
                    </label>
                    {todo.name}
                </div>);
            };
            ```
            
            - TodoへPropsとしてtoggleTodoを渡す
            - Todoコンポーネント内でonChange={handleTodoClick} とする事で発火するトリガーを設定する
- 今後進めるもの    
    [**Reactアプリ100本ノック**](https://www.notion.so/React-100-186972e6c9608084bec7e94f82cd9512?pvs=21)   
- その他(便利機能)
    - VS code
        - rafce
            - コンポーネントの雛形を作る事ができるVS codeの拡張機能
                - constとアロー関数で宣言した関数コンポーネントの雛形を一瞬で作成してくれる
                - ファイル名がそのままコンポーネント名となる
    - キャメルケース
        - 先頭以外の単語が大文字になる
- Reactがビルドされるまで
    - ビルドに関わる重要な機能
        - Webpack
            - モジュールバンドラーツール
                - https://webpack.js.org/
                - https://zenn.dev/sprout2000/articles/9d026d3d9e0e8f
                - https://zenn.dev/antez/articles/58307946cf4f3e
        - Babel
            - JavaScriptのコンパイラ
                - ES6以上のコードをES5に変換できる
                    - アロー関数はES6以降の機能だが、ES5でも変換してくれるため利用可能になる
                    - https://babeljs.io/docs
                    - https://zenn.dev/crsc1206/articles/0b0960fa306d71
    - 大まかなビルドの流れ
        - tsc
            - TypeScriptのコンパイラ
                - TypeScriptの型変換なども行う
        1. JSX や TypeScript を何かしらのツールで JavaScript に変換する
            - その際に、ES6 以上のコードを ES5 に変換する
        2. 変換された JavaScript を Webpack などのモジュールバンドラ で一つのファイルにまとめる
        3. ビルドされた JavaScript を実行する
    - アプリ作成
        
        例：npx create-react-app my-app --template typescript
        
        ↑
        
        `webpack.config.js` や `babel.config.js` などの設定ファイルはない
        
        ↑
        
        “node_modules”や”babel”,”Webpack”に関連するパッケージを使うためにはnpm run ejectというコマンドが必要
        
        例：npm run eject
        
        `config` ディレクトリ配下に`webpack.config.js`が作成される
        
        - webpack.config.js
            - 型チェック
                - tsconfig.jsonが存在する場合にはForkTsCheckerWebpackPluginを実行している
            - コンパイル
                - `paths.appSrc` = `src`ディレクトリ以下の`js|mjs|jsx|ts|tsx`ファイルを対象に、実行される
            - エントリーポイント
                - バンドルの開始点
                    - 開始点を基準に依存関係を辿っていく
        - Create React App したものがビルドされるまでの流れ
            1. Webpack のプラグイン`fork-ts-checker-webpack-plugin`が型チェックを行う
            2. Webpack のプラグイン`babel-loader`が Babel の`@babel/preset-react`を使ってコンパイルを行い、JSX や TypeScript を JavaScript に変換する
            3. Webpack が`build`フォルダ配下にバンドルしたファイルを出力する
- 概念の理解
    - 言葉で説明する
        - ちゃんとプログラムを日本語にできる？
            - プログラム書く前
    - 状態を意識する
        - そのプログラムの状態
            - 状態に依存してプログラムで表示する内容が決定される(特にフロント)
                - データの取得中
                    - fallback
                - データの取得後
                    - map関数
    - 概念の理解が弱い
        - fetch関数
        - useSWR
            - 何でfetchではなくてuseSWRを使うのか？
                - 何ができてできない
- tabの切り替え   
    ```jsx
    import clsx from "clsx";
    import React, { useState } from "react";
    import { createRoot } from "react-dom/client";
    
    export default function App() {
      const [tab, setTab] = useState(0);
      const handleTabClick = (index) => () => {
        setTab(index);
      };
      return (
        <div className="tab" role="tab">
          <div className="tab-list" role="tablist">
            <button
              className={clsx({ active: tab === 0 })}
              onClick={handleTabClick(0)}
            >
              タブ1
            </button>
            <button
              className={clsx({ active: tab === 1 })}
              onClick={handleTabClick(1)}
            >
              タブ2
            </button>
            <button
              className={clsx({ active: tab === 2 })}
              onClick={handleTabClick(2)}
            >
              タブ3
            </button>
          </div>
          {tab === 0 && (
            <div className="tab-panel" role="tabpanel">
              ここにタブ1のコンテンツが入ります。
            </div>
          )}
          {tab === 1 && (
            <div className="tab-panel" role="tabpanel">
              ここにタブ2のコンテンツが入ります。
            </div>
          )}
          {tab === 2 && (
            <div className="tab-panel" role="tabpanel">
              ここにタブ3のコンテンツが入ります。
            </div>
          )}
        </div>
      );
    }
    
    export const root = createRoot(document.getElementById("root"));
    root.render(<App />);
    ```    
- **React JavaScript TypeScriptの関係性（AIまとめ）**    
    React、JavaScript、TypeScriptは、それぞれ異なる役割を持ちながらも密接に関係している。
    
    **1. JavaScript**
    
    - **定義**: プログラミング言語。Webアプリケーションの動的な動作を記述するために使用される。
    - **Reactとの関係**: ReactはJavaScriptライブラリであり、JavaScriptの上で動作する。
    - **TypeScriptとの関係**: TypeScriptはJavaScriptのスーパーセット（拡張版）であり、JavaScriptのコードをそのまま動作させることができる。
    
    **2. TypeScript**
    
    - **定義**: JavaScriptを拡張した静的型付き言語。JavaScriptに型の概念を加えたもの。
    - **Reactとの関係**:
        - ReactアプリをTypeScriptで書くことで、型の安全性を向上させることができる。
        - JSX（Reactの構文拡張）をTypeScriptと組み合わせた **TSX（.tsx）** を利用することで、より型安全なコンポーネント開発が可能になる。
    - **JavaScriptとの関係**:
        - TypeScriptはJavaScriptの構文を含むため、JavaScriptのコードをそのまま使える。
        - TypeScriptは最終的にJavaScriptにコンパイルされるため、ブラウザはTypeScriptを直接実行できない。
    
    **3. React**
    
    - **定義**: Facebook（現Meta）が開発したUI構築用のJavaScriptライブラリ。
    - **JavaScriptとの関係**:
        - ReactはJavaScriptの上で動作し、JSX（JavaScriptの拡張構文）を使用する。
        - Reactコンポーネントは通常、JavaScriptで記述される。
    - **TypeScriptとの関係**:
        - ReactコンポーネントをTypeScriptで記述することで、型のサポートを受けられ、開発時のエラーを減らせる。
        - `React.FC<Props>` などの型定義を使うことで、コンポーネントのPropsを明確にできる。
    
    **まとめ:**
    
    - 要素役割関係 **JavaScript**プログラミング言語Reactの基盤 / TypeScriptの元になる
    - **TypeScript**JavaScriptの拡張（静的型付け）JavaScriptを型安全にし、Reactと相性が良い
    - **React**UI構築ライブラリ JavaScript / TypeScriptのどちらでも使える
    
    **結論**:
    
    - ReactはJavaScriptのライブラリであり、JavaScriptまたはTypeScriptのいずれかで開発できる。
    - TypeScriptを使うことでReact開発の安全性が向上する。

- Reactクイックスタート
    - チュートリアル：三目並べ　＝＞　クイックスタートで学んだ事を活かして実装
        - このチュートリアルで、小さな三目並べゲーム (tic-tac-toe) を作成する。
        - このチュートリアルを読むにあたり、React に関する事前知識は一切必要ない。
        - このチュートリアルで学ぶ技法は React アプリを構築する際の基礎となるもの
        - マスターすることで React についての深い理解が得られます。

    - React の流儀
        - Reactでは設計を考える方法や構築方法を変える
            - 設計の流れ
                - UIをコンポーネントへ分割
                - 視覚情報の記述をする
                - 複数のコンポーネントを接続する
                - コンポーネント間がデータを流れるようにする
    - インストール
        - Reactは段階的に導入できる設計になっている
            - 少ない設計でも大きな複雑な設計でも導入する事ができる
        - React アプリの作成
            - フレームワークを使用する
                - フルスタックフレームワーク
                    - SPA
                    - SSG
                        - サーバーを必要としない
        - ゼロからの React アプリ構築
            - フレームワークを使用する方法
                - ゼロからReactを使用する
        - 既存プロジェクトに React を追加する
            - 既存のプロジェクトにReactをレンダーする事ができる
                - 全てをReactで書き直す必要はない
    - セットアップ
        - エディタのセットアッ
        - TypeScript の使用
        - React Developer Tools
          - Chromeには拡張機能React Developer Toolsとして用意されている
    - UI の記述
        - 初めてのコンポーネントの書き方
          - Reactアプリケーションはコンポーネントと呼ばれる独立したUIのパーツで作成されている
            - マークアップを添える事ができるJavaScript関数
              - ボタン程の小さな部品の場合やページ全体を指す場合もある
        - コンポーネントファイルを複数に分ける理由とその方法
          - 一つのファイルに多くのコンポーネントを宣言する事もできる
            - しかし、1つのファイルに多く宣言してしまうと膨大になってしまう
              - そのため、コンポーネント毎にファイルを分割しエクスポートする事で別のファイルでも使えるようにしている
        - JSX を使って JavaScript にマークアップを追加する方法
          - 各コンポーネントはマークアップを含んだJavaScript関数である
            - JSXという拡張構文を使う
              - HTMLに似た構文の言語だがHTMLよりも厳密な言語になっている
                - また、動的なページを作成するのにも貢献する
        - JSX 内で波括弧を使って JavaScript の機能にアクセスする方法
          - JSX内に{}波括弧を記載してJavaScriptを記述する
            - JavaScriptへの窓を開ける事ができる
        - コンポーネントを props を使ってカスタマイズする方法
          - 親コンポーネントからPropsを使ってどんなものでも渡す事ができる
            - JSX,オブジェクト、配列など
        - コンポーネントを条件付きでレンダーする方法
          - JSXでJavaScriptの演算子を使って表示内容を切り替える
            - 条件に応じてレンダーされるJSXが変わる
        - 複数のコンポーネントを同時にレンダーする方法
          - データの集まり（データの配列や、コンポーネントの配列）をmap()やfilter()を使って配列のフィルタリングする事やコンポーネントの配列に変換する事ができる
            - 配列の各要素にはkeyを指定する必要がある
              - 通常、DBのidカラムを指定することになる
                - DBのidカラムであれば順番が変わった場合にも一意のidを保つ事ができる
        - コンポーネントを純粋に保つことで混乱を避ける方法
          - いくつかのJavaScriptは純関数になっている
            - 自分の仕事に集中する
              - 呼び出される前に存在していたオブジェクトや変数を変更しない。
            - 同じ入力には同じ出力
              - 同じ入力を与えると常に同じ値を返す
        - UI をツリーとして理解することが有用である理由
          - Reactはモジュール、コンポーネントの関係性をツリー構造で示す
            - コンポーネントの親子関係を示す
              - ツリーの上はTopレベルのコンポーネント=>Root component
                - コンポーネントの分類を理解するのがデータと処理の流れを理解するのに重要である
    - インタラクティビティの追加
      - ユーザー行動に応じて更新されていくもの
        - 画像ギャラリーを選択するとアクティブな画像が切り替わるなど
          - 時間と共に変わっていくものをstateと呼ぶ
            - 任意のコンポーネントにstateを追加する事ができる
              - 必要に応じて更新する事ができる
        - ユーザが発生させるイベントの扱い方
          - Reactではイベントハンドラー（エンジニア側が設定できる）を設定する事ができる
            - クリック
            - ホバー
            - フォーカス
              - など
            - ユーザーインタラクションに応答してトリガーされる
        - state でコンポーネントに情報を 「記憶」させる方法
          - state:コンポーネントのメモリ
            - ユーザー行動に応じて表示内容を変更する必要がある
              - コンポーネントは状態を保持する
                - 現在の入力値、現在の画像、ショッピングカートの状態
                  - useStateを使うとstate変数を宣言する事ができる
                    - ペアとしてstateセッタ関数のペアを返す
        - React が 2 段階で UI を更新する仕組み
          - コンポーネントは画面に表示される前にReactにレンダーされる必要がある
            - コンポーネントは厨房に立つ料理人のような存在
              - レンダーのトリガ（お客様の注文を厨房に伝える）
              - コンポーネントのレンダー（厨房で注文の品を料理する）
              - DOM へのコミット（テーブルに注文の品を提供する）
        - 変更後すぐに state が更新されない理由
          - JavaScriptの変数などとは違いstateはスナップショットである
            - setした場合にも更新されずに再レンダリングが起きる
              - 小さなバグを回避する事ができる
        - 複数の state の更新をキューに入れる方法
          - 複数のset関数を一度に発火させてもstateの更新が保持されない
            - setScore(score + 1) ==>> setScore(s => s + 1)
              - 更新用の関数を挟む必要がある　＝＞　イミュータブルな関数
        - state 内のオブジェクトを更新する方法
          - ReactではJavaScriptのオブジェクトを値として保持する事ができる
            - どんなstateのオブジェクトでも保持可能
              - オブジェクトを直接変更する事は望ましくない
                - 代わりに新しいオブジェクトを作成（または既存のもののコピーを作成）する。
                  - それを使って state をセットする必要がある。
        - state 内の配列を更新する方法
          - 配列
            - JavaScriptのミュータブルなオブジェクトの一種
              - React内部ではイミュータブルに扱う必要がある
                - オブジェクト同様にコピーするor新しいオブジェクトを作成する
                  - 新しいものをstateとしてセットする
    - state の管理　=>　stateの管理方法　=>　ロジックで計画的に考える
        - UI の変化を state の変化として捉える方法
          - Reactではコードから直接UIを変更する事はしない
            - そのかわりにコンポーネントの視覚状態に対して表示したいUIを記述してstateの変更をトリガーする
              - デザイナーがUIを考える部分に似ている
        - state を適切に構造化する方法
          - 適切なコンポーネントの構造化
            - stateに対して冗長、重複した情報を持たせていないか？という事が重要な点になる
              - 不要なstateがあると存在に気づかず更新できない事でバグになる
                - 不要なstateをリファクタリングして計算で表現するなど
                  - 多くのバグがstateの管理に関するものになる事が多い
        - コンポーネント間で state を共有するために状態を “リフトアップ” する方法
          - 2つのコンポーネントの状態を同時に変更する
            - 変更したいコンポーネントのstateを削除する
              - 最も近い親からstateをprops経由で渡す
        - state が保持されるかリセットされるかを制御する方法
          - コンポーネントを再レンダーする
            - Reactはツリー構造で保持する部分と破棄する部分を選択している
              - 保持するツリー
                - レンダー前の状態と一致するツリー
            - 時にはこの特性が良い方向に向かない場合もある
        - 複雑な state ロジックを関数にまとめる方法
          - useReducer
            - イベントハンドラーに跨ってstateの更新コードが含まれるコンポーネントの理解は難しい
              - リデューサ (reducer) と呼ばれる単一の関数を作成して全てのstateの更新ロジックを集約する事ができる
        - ”props の穴掘り作業” なしで情報を渡す方法
          - 通常、親コンポーネントから子コンポーネントへの情報の受け渡しはpropsを使って行われる
            - しかし、多数の中間コンポーネントを介さないといけない点がある
              - コンテクストを使う事で深さに関わらず任意のコンポーネントに渡す事ができる
        - アプリの成長に合わせて state 管理をスケーリングする方法
          - リデューサーを使う事でstateの更新ロジックを集約する
          - コンテクストを使う事でコンポーネントに対して深く情報を渡す
            - リデューサーとコンテクストを活用することで複雑なコンポーネント管理を実装する事ができる
    - 避難ハッチ
      - Reactの外に踏み出して外部システムと接続する方法 
        - コンポーネントによってReact外のシステムに対して制御、同期が必要になる事がある
          - ブラウザAPIを使用して入力フィールドにフォーカスを当てる
            - Reactを使用せずにビデオプレイヤーの再生、一時停止を行うなど
              - Reactの外に踏み出し外部システムと同期する方法を学ぶ
        - 再レンダーせずに情報を「記憶」する方法
          - コンポーネントに情報を持たせる際に再レンダーさせない方法
            - refを使用する
          - useRef
            - useRefはレンダー間でStateを保持する
              - useStateはstateが更新されるとレンダリングされる
                - useRefはレンダリングされない
                  - ref.currentプロパティに値が保存される
        - React が管理している DOM 要素にアクセスする方法
          - refでDOM要素を操作する
            - ReactにおいてDOM要素を直接操作する事は少ない
              - 例外：
                - フォーカスを当てる
                - スクロールをさせる
                - サイズや位置の測定
                  - これらを実現する機能はrefにしかない
        - コンポーネントを外部システムと同期させる方法
          - 一部のコンポーネントは外部システムと同期させる方法がある
            - useEffect
              - レンダー後にコードを実行する事ができる
                - コンポーネントの同期をする事ができる
                  - 多くのコンポーネントは実行後に自身をクリーンアップする
                    - クリーンアップ関数を返す
        - 不要なエフェクトをコンポーネントから削除する方法
          - エフェクトはReactパラダイム空の避難ハッチ
            - React外に踏み出す時に使用するもの
              - 逆にReact内部で完結する事ができる時には使用しない
                - useEffectがない事でコードの可読性が高くなる事や実行速度が向上する、エラーを防ぐ事ができるなどがある
                  - 実際の例：
                    - レンダーのためのデータ変換
                    - ユーザイベントの処理
                - useEffect => 外部システムとの連携で使用する
        - エフェクトのライフサイクルとコンポーネントのライフサイクルの違い
          - 通常のコンポーネントが持つライフサイクル
            - マウント
            - 更新
            - アンマウント
          - useEffectが持つライフサイクル
            - 同期の開始
            - 同期の停止
              - propsやstateに依存し、それらの変化に伴ってこのサイクルが繰り返して発生される
        - 値がエフェクトを再トリガするのを防ぐ方法 => まだ実装されていないAPI
          - イベントハンドラ
            - 同じインタラクションを再度実行した場合のみ再実行される
          - useEffect 
            - イベントハンドラーと異なる
              - propsやstate変数のような読み取る値が前回のレンダー時と異なる時に再同期を行う
          - リアクティブ:反応性
            - 読み込むリアクティブな値が再レンダーによって変更された場合
              - 再実行される
        - エフェクトの再実行頻度を下げる方法
          - リンタはエフェクトが読み取る全てのリアクティブな値がエフェクトの依存値リストに含まれているかをチェックする
            - このチェックによってコンポーネントの差分が発見されてレンダリングが起こりコンポーネントが最新状態を保つ
              - しかし、不要な依存関係があると無駄なレンダリングや、無限ループが発生する事がある
                - 不要な値を出来るだけ取り除く事がコードをまもる事につながる
          - optionsを使ってレンダリングをエスケープする
        - コンポーネント間でロジックを共有する方法
          - カスタムHookでロジックを共有する
            - 組み込み型のHookがReactには存在するが、より特定の機能に特化したアプリケーションの要求に答えるHookを作成する事ができる
              - カスタムHookを使って組み合わせる事でデータの受け渡し、コンポーネント間での再利用をする事が可能になる
                - コードの記述量の減少など手作業での作業を減らす事が可能になる