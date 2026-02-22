# テンプレートセットアップ手順

「Use this template」で新規リポジトリを作成した後、以下の手順でセットアップしてください。

## 1. パッケージ名を変更

`myproject` を実際のプロジェクト名に置換します:

```bash
# ディレクトリ名を変更
mv src/myproject src/your_project_name
mv tests/myproject tests/your_project_name

# ファイル内の参照を一括置換
# 対象: pyproject.toml, src/, tests/, CLAUDE.md
grep -r "myproject" --include="*.py" --include="*.toml" --include="*.md" -l | \
  xargs sed -i 's/myproject/your_project_name/g'
```

## 2. pyproject.toml を更新

- `name`: パッケージ名
- `description`: プロジェクトの説明
- `dependencies`: 必要なパッケージを追加

## 3. 依存関係をインストール

```bash
uv sync --group dev
uv run pre-commit install
```

## 4. GCP デプロイを使用する場合

### Workload Identity Federation セットアップ

```bash
# TODO: プロジェクトに合わせて変更
export PROJECT_ID=your-gcp-project-id
export REPO=your-org/your-repo

# サービスアカウント作成
gcloud iam service-accounts create github-actions \
  --project=$PROJECT_ID \
  --display-name="GitHub Actions"

# Workload Identity Pool 作成
gcloud iam workload-identity-pools create github-pool \
  --project=$PROJECT_ID \
  --location=global \
  --display-name="GitHub Actions Pool"

# Provider 作成
gcloud iam workload-identity-pools providers create-oidc github-provider \
  --project=$PROJECT_ID \
  --location=global \
  --workload-identity-pool=github-pool \
  --display-name="GitHub Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository" \
  --issuer-uri="https://token.actions.githubusercontent.com"

# バインディング
gcloud iam service-accounts add-iam-policy-binding \
  github-actions@${PROJECT_ID}.iam.gserviceaccount.com \
  --project=$PROJECT_ID \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')/locations/global/workloadIdentityPools/github-pool/attribute.repository/${REPO}"
```

### GitHub Secrets 設定

| Secret | 値 |
|---|---|
| `GCP_WORKLOAD_IDENTITY_PROVIDER` | `projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/github-pool/providers/github-provider` |
| `GCP_SERVICE_ACCOUNT` | `github-actions@PROJECT_ID.iam.gserviceaccount.com` |

### deploy-service.yml / deploy-job.yml の env を更新

ワークフローファイル内の `TODO:` コメントを検索して値を設定してください。

## 5. GitHub Environment 作成

1. Settings → Environments → New environment → `production`
2. 必要に応じて保護ルール（Required reviewers 等）を設定

## 6. 動作確認

```bash
uv run pytest tests/ -v
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/
uv run mypy src/
uv run pre-commit run --all-files
```

## 7. このファイルを削除

セットアップ完了後、この `TEMPLATE_SETUP.md` を削除してください。
