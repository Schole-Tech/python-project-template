# プロジェクト開発ガイドライン

このリポジトリで Claude Code / AI エージェントが作業する際のルールです。

---

## テストルール（必須）

### 新規モジュール作成時

**新しい `.py` ファイルを `src/` 配下に作成した場合、対応するテストファイルも必ず作成すること。**

テストなしのモジュール追加は不完全な成果物とみなす。

### テストの配置

`src/` のディレクトリ構造を `tests/` にミラーする:

```
src/myproject/utils.py
  → tests/myproject/test_utils.py

src/myproject/services/auth.py
  → tests/myproject/services/test_auth.py
```

### テストの書き方

- フレームワーク: **pytest**
- 外部 API 呼び出しは **`unittest.mock` でモック化**
- 内部ロジックは実データでテスト
- テスト関数名: `test_<何をテストするか>_<期待結果>`（例: `test_parse_config_with_missing_key_raises_error`）
- 最低限のカバー対象:
  - 正常系 1 ケース
  - 異常系/エッジケース 1 ケース
  - 戻り値の型・構造の検証

### テスト実行

```bash
uv run pytest tests/ -v
uv run pytest tests/ --cov=src --cov-report=term-missing
```

### 既存モジュールの修正時

既存テストが壊れていないことを確認する。テストがないモジュールを修正する場合、修正のついでにテストを追加することを推奨（必須ではない）。

---

## コーディング標準

### Python

- フォーマッター: **ruff format**（Black 互換）
- リンター: **ruff check**
- 型ヒント必須（`mypy --strict` 準拠）
- docstring: Google 形式
- 行長上限: 100

### 品質チェック

```bash
uv run ruff check src/ tests/           # lint
uv run ruff format --check src/ tests/   # format check
uv run mypy src/                         # type check
```

### Git ワークフロー

- main ブランチに直接コミットしない
- フィーチャーブランチ: `feature/機能名`
- コミットメッセージ: 日本語OK、動詞から始める

---

## セキュリティ

- API キー・トークンをハードコードしない
- 環境変数または Secret Manager を使用
- ユーザー入力を直接 SQL / コマンドに渡さない
- 依存パッケージのバージョンを固定する

---

## プロジェクト構成

```
src/
└── myproject/           # メインパッケージ（TODO: リネーム）
    ├── __init__.py
    ├── py.typed          # PEP 561 マーカー
    ├── config.py         # Pydantic 設定
    └── core.py           # コアロジック
tests/                    # テスト（src/ をミラー）
deploy/                   # Docker / デプロイ設定
```

## 環境

- パッケージマネージャ: **uv**（pip ではない）
- Python: 3.10+
