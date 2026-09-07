# FastAPIの本体をインポート
# APIアプリケーションを作成するために使用する
from fastapi import FastAPI

# CORSを設定するためのミドルウェアをインポート
# Reactなど、異なるオリジンからAPIへアクセスできるようにする
from fastapi.middleware.cors import CORSMiddleware


# FastAPIアプリケーションを作成
# このappにURLや処理を登録していく
app = FastAPI()


# CORSの設定
# ReactとFastAPIは開発中に異なるポートで動くため、この設定が必要
#
# React:   http://localhost:5173
# FastAPI: http://localhost:8000
app.add_middleware(
    CORSMiddleware,

    # FastAPIへのアクセスを許可するフロントエンドのURL
    # 指定していないURLからのアクセスはブラウザによって制限される
    allow_origins=["http://localhost:5173"],

    # CookieやAuthorizationヘッダーなどの認証情報を
    # フロントエンドから送信できるようにする
    allow_credentials=True,

    # 許可するHTTPメソッド
    # "*"はGET、POST、PUT、DELETEなど、すべてを許可する
    allow_methods=["*"],

    # フロントエンドから送信されるすべてのHTTPヘッダーを許可する
    allow_headers=["*"],
)


# GETリクエストを受け付けるAPI
# URL: http://localhost:8000/api/health
#
# サーバーが正常に動作しているか確認するためのAPI
@app.get("/api/health")
def health_check():
    # Pythonの辞書は自動的にJSONへ変換される
    return {"status": "ok"}


# Reactへメッセージを返すGET API
# URL: http://localhost:8000/api/message
@app.get("/api/message")
def get_message():
    # React側には以下のJSONとして返される
    # {
    #   "message": "FastAPIからこんにちは"
    # }
    return {"message": "FastAPIからこんにちは"}
