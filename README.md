# my-project

FastAPIのバックエンドと、Vite + React + TypeScriptのフロントエンドで作成した社員情報表示アプリです。

バックエンドが社員データをAPIとして返し、フロントエンドがそのデータを取得して社員一覧画面と社員詳細画面を表示します。

## 現在の設計

```text
.
├── backend/
│   ├── app/
│   │   └── main.py          # FastAPIアプリケーション
│   ├── tests/
│   │   └── small/           # 小規模テスト
│   ├── pyproject.toml       # Python依存関係
│   └── pytest.ini           # pytest設定
└── frontend/
    ├── src/
    │   ├── App.tsx          # 画面とルーティング
    │   └── main.tsx         # Reactの起動処理
    ├── package.json         # npmスクリプトと依存関係
    └── vite.config.ts       # Vite設定
```

## 使用技術

### Backend

- Python 3.10以上
- FastAPI
- Pydantic
- pytest

### Frontend

- Node.js
- npm
- Vite
- React
- TypeScript
- React Router

## 画面構成

| URL | 内容 |
| --- | --- |
| `http://localhost:5173/` | 社員一覧画面 |
| `http://localhost:5173/employees/:employeeId` | 社員詳細画面 |

## API設計

バックエンドは `http://localhost:8000` で起動します。

| メソッド | パス | 内容 |
| --- | --- | --- |
| GET | `/api/health` | サーバーの動作確認 |
| GET | `/api/message` | 確認用メッセージを返す |
| GET | `/api/employees` | 社員一覧を返す |
| GET | `/api/employees/{employee_id}` | 指定した社員IDの社員情報を返す |

社員データの形式は以下です。

```json
{
  "employee_id": 1,
  "name": "岡田 秀弥",
  "ur_name": "okada_shuya"
}
```

## 構築手順

### 1. リポジトリを取得

```bash
git clone https://github.com/sy224-del/mytool.git
cd mytool
```

すでにこのフォルダで作業している場合は、上記の取得手順は不要です。

### 2. Backendのセットアップ

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install pytest
```

Windowsの場合、仮想環境の有効化は以下です。

```bash
.venv\Scripts\activate
```

### 3. Backendの起動

```bash
cd backend
source .venv/bin/activate
fastapi dev app/main.py
```

起動後、以下にアクセスして動作確認できます。

```text
http://localhost:8000/api/health
```

期待されるレスポンスです。

```json
{
  "status": "ok"
}
```

### 4. Frontendのセットアップ

別のターミナルを開いて実行します。

```bash
cd frontend
npm install
```

### 5. Frontendの起動

```bash
cd frontend
npm run dev
```

起動後、以下にアクセスします。

```text
http://localhost:5173/
```

## 開発時の起動順

1. Backendを `http://localhost:8000` で起動する
2. Frontendを `http://localhost:5173` で起動する
3. ブラウザで `http://localhost:5173/` を開く

フロントエンドはバックエンドのAPIを直接呼び出しているため、社員一覧を表示するには両方のサーバーを起動しておく必要があります。

## テスト

Backendのテストを実行します。

```bash
cd backend
source .venv/bin/activate
pytest
```

## Frontendの確認コマンド

### Lint

```bash
cd frontend
npm run lint
```

### Build

```bash
cd frontend
npm run build
```

### Preview

```bash
cd frontend
npm run preview
```

## CORS設定

開発中は、FrontendとBackendが別々のポートで動きます。

```text
Frontend: http://localhost:5173
Backend:  http://localhost:8000
```

そのため、Backendでは以下のオリジンからのアクセスを許可しています。

- `http://localhost:5173`
- `http://127.0.0.1:5173`
