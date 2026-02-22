# python-project-template

Python プロジェクトテンプレート。GitHub の「Use this template」で新規プロジェクトを即座に開始できます。

## 含まれるもの

- **uv** によるパッケージ管理 (`uv sync --locked`)
- **ruff** によるリント & フォーマット
- **mypy --strict** による型チェック
- **pytest** + pytest-xdist + pytest-cov によるテスト
- **GitHub Actions CI** (Python 3.10-3.13 マトリクス)
- **Cloud Run** デプロイワークフロー (Service / Job)
- **Docker** マルチステージビルド (uv ベース)
- **セキュリティ**: Bandit (SAST) + Gitleaks (シークレット検出)
- **Dependabot**: Actions + pip 自動更新
- **pre-commit**: ruff + gitleaks + bandit
- **CLAUDE.md**: AI エージェント開発ガイドライン

## クイックスタート

```bash
# 1. テンプレートから新規リポジトリを作成
#    GitHub で「Use this template」→「Create a new repository」

# 2. クローン
git clone https://github.com/your-org/your-new-repo.git
cd your-new-repo

# 3. セットアップ
uv sync --group dev
uv run pre-commit install

# 4. テスト実行
uv run pytest tests/ -v

# 5. 品質チェック
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/
uv run mypy src/
```

## プロジェクト構成

```
src/myproject/          # メインパッケージ（リネームしてください）
tests/myproject/        # テスト（src/ をミラー）
deploy/Dockerfile       # マルチステージ Docker ビルド
.github/workflows/      # CI/CD ワークフロー
```

## セットアップ手順

テンプレートから作成後の手順は [TEMPLATE_SETUP.md](TEMPLATE_SETUP.md) を参照してください。

## License

MIT
