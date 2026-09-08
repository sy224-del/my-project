import { useEffect, useState } from "react";
import {
  BrowserRouter,
  Link,
  Route,
  Routes,
  useParams,
} from "react-router";


// FastAPIから受け取る社員データの型
type Employee = {
  employee_id: number;
  name: string;
  ur_name: string;
};


// 社員一覧画面
function EmployeeList() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);


  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        const response = await fetch(
          "http://localhost:8000/api/employees"
        );

        if (!response.ok) {
          throw new Error("従業員情報の取得に失敗しました");
        }

        const data: Employee[] = await response.json();
        setEmployees(data);
      } catch (err) {
        if (err instanceof Error) {
          setError(err.message);
        }
      } finally {
        setIsLoading(false);
      }
    };

    fetchEmployees();
  }, []);


  if (isLoading) {
    return <p>従業員情報を読み込み中です...</p>;
  }

  if (error) {
    return <p>エラー：{error}</p>;
  }


  return (
    <main>
      <h1>従業員一覧</h1>

      <ul>
        {employees.map((employee) => (
          <li key={employee.employee_id}>
            社員ID：{employee.employee_id}、
            名前：{employee.name}、
            UR名：
            <Link to={`/employees/${employee.employee_id}`}>
              {employee.ur_name}
            </Link>
          </li>
        ))}
      </ul>
    </main>
  );
}


// 社員詳細画面
function EmployeeDetail() {
  // URLの「:employeeId」に入った値を取得する
  const { employeeId } = useParams();

  const [employee, setEmployee] = useState<Employee | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);


  useEffect(() => {
    const fetchEmployee = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/api/employees/${employeeId}`
        );

        if (!response.ok) {
          throw new Error("社員情報の取得に失敗しました");
        }

        const data: Employee = await response.json();
        setEmployee(data);
      } catch (err) {
        if (err instanceof Error) {
          setError(err.message);
        }
      } finally {
        setIsLoading(false);
      }
    };

    fetchEmployee();
  }, [employeeId]);


  if (isLoading) {
    return <p>社員情報を読み込み中です...</p>;
  }

  if (error) {
    return <p>エラー：{error}</p>;
  }

  if (employee === null) {
    return <p>社員が見つかりません。</p>;
  }


  return (
    <main>
      <h1>社員詳細</h1>

      <p>社員ID：{employee.employee_id}</p>
      <p>名前：{employee.name}</p>
      <p>UR名：{employee.ur_name}</p>

      <Link to="/">社員一覧へ戻る</Link>
    </main>
  );
}


// URLと表示する画面の対応を設定
function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* http://localhost:5173/ */}
        <Route path="/" element={<EmployeeList />} />

        {/* http://localhost:5173/employees/1 */}
        <Route
          path="/employees/:employeeId"
          element={<EmployeeDetail />}
        />
      </Routes>
    </BrowserRouter>
  );
}


export default App;
