# FastAPI

## 概要

FastAPI は、Python のモダンな Web フレームワークで、高速な API 開発が可能。

## 参考記事

- [FastAPI のテストコードを書いて DI の重要性を知った話](https://zenn.dev/lancers/articles/1bff9ebffdbd89)

---

## 依存性注入（DI: Dependency Injection）

### DI とは

関数内で生成したり直接参照したりしそうなオブジェクト（DB セッション、外部 API クライアントなど）を、**外側から引数として「注入」してもらう**設計パターン。

FastAPI では`Depends`がこの仕組みを実現している。

### なぜ DI が重要なのか

- テスト時に依存関係を簡単に差し替えられる
- コードの結合度が下がり、保守性が向上する
- `monkeypatch`で複数の関数を差し替える手間が不要になる

---

## Depends の使い方

### 基本的な使用例

```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db

router = APIRouter()

@router.post("/something")
def my_function(
    db: Session = Depends(get_db),  # ★ Depends で依存性を注入
):
    # db を使った処理
    return result
```

**ポイント:**

- エンドポイント関数の引数に`Depends(依存関数)`を指定
- 関数内部で直接 DB セッションを生成するのではなく、外から注入される

### 注意点

⚠️ **`Depends`はエンドポイント関数にのみ使用可能**  
エンドポイント以外の関数で使用するとエラー表示はされないが、予期せぬバグに繋がる可能性がある。

---

## テストコードでの活用

### dependency_overrides による依存性の上書き

テスト時に本番の DB を使わず、テスト用 DB に差し替える方法。

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from .main import app
from .database import get_db  # 上書き対象の依存関数

# テスト用のDBを準備
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

test_db = TestingSessionLocal()

@pytest.fixture(autouse=True)
def override_get_db():
    # テスト用の get_db を定義
    def _get_test_db():
        try:
            yield test_db
        finally:
            test_db.close()

    ### ここで依存性を上書きする ###
    app.dependency_overrides[get_db] = _get_test_db

    yield

    # 後片付け（テスト実行後に元に戻す）
    app.dependency_overrides.clear()

client = TestClient(app)

def test_my_function():
    response = client.post("/something", json={...})
    assert response.status_code == 200
```

### 仕組みの流れ

1. **テスト開始前**: `@pytest.fixture(autouse=True)`により、すべてのテストで自動実行
2. **依存性の上書き**: `app.dependency_overrides[get_db] = _get_test_db`
3. **テスト実行**: エンドポイントが`get_db`を呼び出すと、実際には`_get_test_db`が実行される
4. **後片付け**: `app.dependency_overrides.clear()`で元に戻す

### メリット

✅ 本番環境の DB に影響を与えない  
✅ `monkeypatch`で複数の関数を差し替える必要がない  
✅ コードの変更に強い（依存関係が明示的）  
✅ テストコードがシンプルになる

### monkeypatch との比較

| 方法                               | メリット                                           | デメリット                                                     |
| ---------------------------------- | -------------------------------------------------- | -------------------------------------------------------------- |
| **Depends + dependency_overrides** | ・シンプル<br>・保守性が高い<br>・依存関係が明示的 | ・事前に DI を意識した設計が必要                               |
| **monkeypatch**                    | ・既存コードを変更せずに使える                     | ・差し替え対象が多いと煩雑<br>・コード変更時に更新漏れのリスク |

---

## ベストプラクティス

### テストの独立性を保つ

各テストの前後でテーブルを作成・削除することで、完全に独立したテスト環境を保証する。

```python
from .database import Base

@pytest.fixture(autouse=True)
def override_get_db():
    # テーブルを作成
    Base.metadata.create_all(bind=engine)

    def _get_test_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = _get_test_db
    yield

    # テスト後にテーブルをドロップ（クリーンアップ）
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()
```

### DI を意識した開発

- DB セッション、外部 API クライアントなど、依存の強いオブジェクトは`Depends`で注入する
- エンドポイント関数の引数として明示的に受け取る
- 関数内部で直接生成・参照しない

---

## まとめ

- FastAPI の`Depends`は依存性注入（DI）を実現する仕組み
- テスト時に`dependency_overrides`で依存関係を簡単に差し替えられる
- DI を意識した設計により、テストしやすく保守性の高いコードになる
- 実際に体験してみることで、DI の重要性を理解できる

---

## 公式ドキュメント

- [Dependencies - FastAPI](https://fastapi.tiangolo.com/ja/tutorial/dependencies/)


# そもそも、FastAPIとは？

## 基本定義

FastAPIは、**標準のPython型ヒントに基づいてAPIを構築するための、モダンで高速なWebフレームワーク**です。

Python 3.7以降の型ヒントを活用し、自動的なバリデーション、シリアライゼーション、ドキュメント生成を実現します。

## 主な特徴

### 1. 高速なパフォーマンス

- NodeJSやGoと同等の性能を発揮
- 利用可能なPythonフレームワークの中で**最速クラス**
- STARLETTEとPydanticという高速なライブラリをベースに構築

### 2. 開発効率の向上

- 機能開発の速度を約**200%〜300%向上**
- 人為的なエラーを約**40%削減**
- コードの記述量が少なく、読みやすい

### 3. 優れた開発者体験

- **エディタの強力なサポート**: 型ヒントにより、IDE上で完全な補完機能が利用可能
- **学習コストが低い**: 標準的なPython型ヒントを使用するため、新しい構文を学ぶ必要がない
- **直感的なAPI設計**: Pythonの標準的な書き方で記述可能

### 4. 自動的なドキュメント生成

- **OpenAPI（旧Swagger）仕様**に完全準拠
- **JSON Schema**による型定義
- **対話型APIドキュメント**が自動生成される
  - Swagger UI（`/docs`でアクセス）
  - ReDoc（`/redoc`でアクセス）

### 5. プロダクション対応

- 本番環境での使用を前提とした堅牢な設計
- 大規模システムでの採用実績が豊富
- 自動バリデーションによるセキュリティ向上

### 6. 標準準拠

- **OpenAPI**と**JSON Schema**に完全互換
- 既存のツールやライブラリとの統合が容易
- API仕様のエクスポート・共有が簡単

## 技術的な基盤

### Pydantic

FastAPIの型バリデーションとデータシリアライゼーションは**Pydantic**ライブラリに依存しています。

**Pydanticの利点:**

- Python型ヒントを使用したデータバリデーション
- 高速な処理速度（C言語で実装された部分あり）
- 明確なエラーメッセージ
- 複雑なデータ構造のサポート

**例:**

```python
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: int
    name: str
    email: str
    joined: date
```

### Starlette

FastAPIは**Starlette**をベースにしており、ASGIフレームワークの機能を継承しています。

- 非同期処理（`async`/`await`）の完全サポート
- WebSocketのサポート
- バックグラウンドタスク
- セッション管理とCookie

## 基本的な使用例

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# リクエストボディの型定義
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# エンドポイントの定義
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

## 他のフレームワークとの比較

| フレームワーク | 特徴                                       | パフォーマンス | 学習コスト |
| -------------- | ------------------------------------------ | -------------- | ---------- |
| **FastAPI**    | 型ヒント、自動ドキュメント、モダン設計     | 非常に高速     | 低         |
| **Django**     | フルスタック、ORM、管理画面                | 中程度         | 中〜高     |
| **Flask**      | シンプル、軽量、柔軟性が高い               | 中程度         | 低         |
| **Tornado**    | 非同期、WebSocket、長時間接続に強い        | 高速           | 中         |
| **Sanic**      | 非同期、Flaskライクな構文                  | 高速           | 低〜中     |

## パフォーマンス最適化のヒント

### 1. 高速化ライブラリの導入

```bash
pip install uvloop httptools
```

- `uvloop`: asyncioのイベントループを高速化（2〜4倍のスループット向上）
- `httptools`: HTTPパーシングの高速化

### 2. 高速なJSONシリアライザの使用

```python
from fastapi.responses import ORJSONResponse

@app.get("/data", response_class=ORJSONResponse)
def get_data():
    return {"data": "high performance"}
```

- `ORJSONResponse`: 標準のJSONより20〜50%高速

### 3. Pydanticの最適化

- `model_validate_json()`を使用（`json.loads()`→`model_validate()`より高速）
- 不要な箇所では`Any`型を使用してバリデーションをスキップ
- Tagged Unionを使用して型判別を高速化

## FastAPIが適しているケース

✅ **RESTful API開発**  
✅ **マイクロサービスアーキテクチャ**  
✅ **機械学習モデルのAPI化**  
✅ **高速なプロトタイピング**  
✅ **大規模で保守性が重要なプロジェクト**  
✅ **型安全性を重視する開発**

## 公式リソース

- **公式ドキュメント（日本語）**: https://fastapi.dokyumento.jp/
- **公式ドキュメント（英語）**: https://fastapi.tiangolo.com/
- **GitHubリポジトリ**: https://github.com/fastapi/fastapi
- **公式Twitter**: @fastapi

## まとめ

FastAPIは、**現代的なPython開発のベストプラクティスを体現したWebフレームワーク**です。

型ヒントを活用することで、開発効率とコード品質を同時に向上させ、自動ドキュメント生成やバリデーションといった実用的な機能を提供します。

高速なパフォーマンスと優れた開発者体験により、スタートアップから大規模プロジェクトまで幅広く採用されています。
