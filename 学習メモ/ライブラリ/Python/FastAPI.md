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
