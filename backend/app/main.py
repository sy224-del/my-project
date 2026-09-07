from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

# 動作確認用API
@app.get("/api/health")
def health_check():
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

# 従業員1人分のデータ形式
class Employee(BaseModel):
    employee_id: int
    name: str
    ur_name: str

# 従業員一覧をJSON形式で返すAPI
@app.get("/api/employees", response_model=list[Employee])
def get_employees():
    return [
        {
            "employee_id": 1,
            "name": "岡田 秀弥",
            "ur_name": "okada_shuya",
        },
        {
            "employee_id": 2,
            "name": "山田 太郎",
            "ur_name": "yamada_taro",
        },
        {
            "employee_id": 3,
            "name": "佐藤 花子",
            "ur_name": "sato_hanako",
        },
    ]
