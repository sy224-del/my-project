# my-project

FastAPIのバックエンドと、Vite + React + TypeScriptのフロントエンドで構成された学習用プロジェクトです。

## 構成

```text
.
├── backend/   # FastAPI APIサーバー
└── frontend/  # Vite + React フロントエンド
```

## 必要なもの

- Python 3.10以上
- Node.js
- npm

## セットアップ

### バックエンド

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m pip install pytest
```

### フロントエンド

```bash
cd frontend
npm install
```

## 開発サーバーの起動

### バックエンド

```bash
cd backend
source .venv/bin/activate
fastapi dev app/main.py
```

バックエンドは http://localhost:8000 で起動します。

### フロントエンド

別のターミナルで起動します。

```bash
cd frontend
npm run dev
```

フロントエンドは通常 http://localhost:5173 で起動します。

## API

現在のAPIは以下です。

| メソッド | パス | 内容 |
| --- | --- | --- |
| GET | `/api/health` | サーバーの動作確認 |
| GET | `/api/message` | フロントエンド向けのメッセージを返す |

## テスト

バックエンドのテストを実行します。

```bash
cd backend
source .venv/bin/activate
pytest
```

## ビルド

フロントエンドの本番用ビルドを作成します。

```bash
cd frontend
npm run build
```
