# Claude Code on Desktop について

- Anthropic 社が Claude Opus 4.5 の発表と同時にリリースした、デスクトップアプリケーション版の Claude Code

- 特徴

  - Claude Desktop アプリケーション内で Claude Code セッションを実行可能
  - **複数のローカルおよびリモートセッションを並行実行**できる
    - 1 つ目のエージェント：バグ修正
    - 2 つ目のエージェント：GitHub でリサーチ
    - 3 つ目のエージェント：ドキュメント更新
      - 複数のインスタンスで同時に複数のタスクを進める事ができる
  - これまでの CLI 版に加え、ビジュアルで直感的なインターフェースを提供

- 技術スタック
  1.Electron アーキテクチャ - Claude Desktop は Electron ベースのアプリケーションとして構築されている。 - クロスプラットフォーム対応（Windows、macOS、Linux） - Web 技術（HTML/CSS/JavaScript）を活用した柔軟な UI - ネイティブアプリケーション的な体験を提供

  2.Git Worktrees - 並行開発の核心技術 - Git worktrees とは - 同一リポジトリの複数のブランチを別々のディレクトリで同時にチェックアウトできる Git の機能。 - 実際に使う時のイメージ - 各セッションが独自に隔離された git worktree を持つ - デフォルトの保存場所：`~/.claude-worktrees`（カスタマイズ可能） - 複数の Claude Code セッションが同じリポジトリで干渉せずに作業可能
  ```

            /Users/username/my-project/          # メインworktree（mainブランチ）
            ├── .git/                            # 実際のGitリポジトリ
            ├── src/
            └── package.json

            /Users/username/.claude-worktrees/
            ├── my-project-feature-a/            # 新しい物理フォルダ（feature-aブランチ）
            │   ├── .git                         # メインの.git/worktreesへのリンクファイル
            │   ├── src/
            │   └── package.json
            └── my-project-bugfix/               # 別の物理フォルダ（bugfixブランチ）
                ├── .git
                ├── src/
                └── package.json

            - 各worktreeは独立したファイル状態を持ち、1つのworktreeでの変更が他に影響しない。

  3.Model Context Protocol (MCP) - MCP とは - AI ツールが他のプログラムやデータソースに接続するためのオープンソース標準（Anthropic 作成）。 - ファイルシステムへのアクセス - データベース接続 - GitHub/GitLab 統合 - AWS、GCP などのクラウドプラットフォーム連携

  - Desktop Extensions（.mcpb ファイル）によってサーバーインストールの課題を解決

    - 開発者ツール（Node.js、Python など）が必要
    - JSON 設定ファイルの手動編集
    - 依存関係の解決
    - サーバーの発見メカニズムがない
    - 更新が複雑

    ↓

    - MCP サーバー全体を依存関係を含めて単一パッケージ化
    - ボタンクリックだけでインストール可能
    - 設定の GUI による管理
    - 非技術者でも利用可能

  4. .worktreeinclude ファイル

     - 新しい worktree を作成した際に基本的に.env ファイルなどは複製されない
       - その問題を解決するファイル
         - 自動的にコピーしてくれる仕組み

     ```
     # .worktreeinclude の例
     .env
     .env.local
     config/secrets.yml
     ```

     - 新しい worktree 作成時に、指定したファイルが自動的にコピーされる。

- 強み

  1. 並行開発ワークフローの革新

**複数セッションの独立管理：**

- 各セッションが独自の Git worktree で動作
- セッション間で相互干渉しない
- デモ用とメイン開発を並行して実行可能

**ユースケース例：**

- メインセッション：重要なリファクタリング作業
- 並行セッション：デモ用の短期開発タスク

### 2. クラウドセッションへのシームレスな移行

**機能：**

- ローカルセッションを中断して、ブラウザで継続可能
- エンタープライズプロキシの制限を回避
- 全てのコンテキストとパーミッション設定が保持される

**メリット：**

- 柔軟なワークフロー
- ネットワーク制限の回避

### 3. 統合された管理 UI

**特徴：**

- すべてのセッションを 1 つのウィンドウで管理
- 各セッションの進捗状況を視覚的に確認
- ユーザーフレンドリーなインターフェース

**CLI 版との違い：**
CLI 版では複数のターミナルウィンドウやタブを手動で管理する必要があったが、Desktop 版では一元管理が可能。

### 4. ファイル作成・編集機能の統合

**CLI 版：**

- ファイル作成・編集は外部エディタで行う必要あり
- 別のツールとの切り替えが必要

**Desktop 版：**

- Claude Desktop アプリ内でファイルを直接作成・編集可能
- シームレスな統合体験

### 5. 長い会話の継続性

**特徴：**

- セッションがアクティブである限り、コンテキストを保持し続ける
- CLI 版の再起動による制約から解放される

---

## CLI との比較

### Desktop 版でできないこと

#### 1. ターミナル統合と IDE 連携の深さ

**CLI 版の強み：**

- ターミナルに統合され、他のコマンドラインツールとシームレスに動作
- Vim、Emacs、VSCode などのエディタと緊密に連携
- エディタ固有のプラグインやショートカットを活用可能
- `.bashrc`や`.zshrc`でのカスタマイズ可能

**Desktop 版の制限：**

- サンドボックス化されたアプリ環境
- 外部エディタとの連携が限定的

#### 2. 自動化とスクリプティング

**CLI 版の強み：**

- CI/CD パイプラインに直接統合可能
- スクリプトからの呼び出しが容易
- コマンドライン引数とフラグによる細かい制御
- 例：`--dangerously-skip-permissions`でパーミッション確認をスキップ

**Desktop 版の制限：**

- プログラマティックな制御が困難
- 自動化パイプラインへの組み込みが限定的
- 非対話的な実行が難しい

#### 3. スキル（Skills）の管理

**CLI 版：**
ファイルシステムベース

```
~/.claude/skills/skill-name/           # 個人用スキル
./project/.claude/skills/skill-name/   # プロジェクトスキル
./plugin/skills/skill-name/            # プラグインスキル
```

各スキルディレクトリ内に`SKILL.md`ファイルを配置するだけ。バージョン管理（Git）との相性が良い。

**Desktop 版：**

- ファイルシステムアクセスなし
- `.zip`ファイルを Web UI またはアプリの設定からアップロード
- バージョン管理が難しい
- 共有や配布がやや煩雑

#### 4. パーミッション制御の柔軟性

**CLI 版：**

```bash
# デフォルト：各操作でパーミッション確認
claude

# パーミッションをスキップ（開発時の効率化）
claude --dangerously-skip-permissions

# プランモードで起動
claude --permission-mode plan
```

**Desktop 版：**

- GUI 経由でのパーミッション確認
- 細かいフラグ制御が不可
- 設定の永続化に制限

#### 5. リソース使用量とコスト

**注意点：**

- 複数の Claude セッションを並行実行すると、トークンを大量に消費
- Claude Pro サブスクリプションの使用制限を超える可能性
- Desktop 版の GUI オーバーヘッドにより、CLI 版よりシステムリソース使用量が増加する可能性

**コンテキストスイッチングの負荷：**

- 複数のエージェントを同時管理する精神的負荷は高い
- 各セッションに適切な入力を与え、進捗を監視する必要
- 特に Claude が両方のセッションで定期的に入力を必要とする場合、各セッションの操縦が難しくなる

**環境セットアップの考慮事項：**

- worktree ごとに`node_modules`などの依存関係は共有されない
- 各 worktree で環境セットアップが必要
- できるだけシンプルな環境設定を目指す
- `.worktreeinclude`を活用して環境変数ファイルを自動コピー

---

## まとめ

Claude Code on Desktop は、Git worktrees と MCP を核心技術として、Electron ベースの統合された GUI を通じて並行開発ワークフローを実現する革新的なツール。

### 技術スタック

- **Electron**：クロスプラットフォーム対応のアーキテクチャ
- **Git Worktrees**：並行セッション管理の核心技術
- **Model Context Protocol (MCP)**：拡張性を提供
- **Desktop Extensions (.mcpb)**：簡単なセットアップを実現

### Desktop 版の主な強み

- 複数の AI セッションを視覚的に管理
- 各セッションが独立したコンテキストを保持
- クラウドセッションへのシームレスな移行
- ファイル作成・編集機能の統合
- 長い会話の継続性

### 使い分け

- **Desktop 版**：ビジュアルで使いやすいインターフェース、複数セッションの管理に最適
- **CLI 版**：完全な制御、自動化、CI/CD 統合、詳細なパーミッション制御に最適

---

## 参考リンク

- [Claude Code on Desktop 公式ドキュメント](https://docs.anthropic.com/en/docs/build-with-claude/claude-code)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Git Worktrees 公式ドキュメント](https://git-scm.com/docs/git-worktree)
- [元記事（Zenn）](https://zenn.dev/kimkiyong/articles/8aa59e041c2410)
