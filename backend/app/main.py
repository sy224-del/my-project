from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# 社員データ
employees = [
    Employee(
        employee_id=1,
        name="岡田 秀弥",
        ur_name="okada_shuya",
    ),
    Employee(
        employee_id=2,
        name="山田 太郎",
        ur_name="yamada_taro",
    ),
    Employee(
        employee_id=3,
        name="佐藤 花子",
        ur_name="sato_hanako",
    ),
]


# 社員一覧を返すAPI
@app.get("/api/employees", response_model=list[Employee])
def get_employees():
    return employees


# 指定された社員IDの社員情報を返すAPI
@app.get("/api/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    # 社員一覧からIDが一致する社員を探す
    employee = next(
        (
            employee
            for employee in employees
            if employee.employee_id == employee_id
        ),
        None,
    )

    # 社員が見つからなかった場合
    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="社員が見つかりません",
        )

    return employee
