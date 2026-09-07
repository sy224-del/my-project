import { useEffect, useState } from "react";


// FastAPIから受け取る従業員データの型
type Employee = {
  employee_id: number;
  name: string;
  ur_name: string;
};


function App() {
  // 取得した従業員一覧を保存する
  const [employees, setEmployees] = useState<Employee[]>([]);

  // データを取得中かどうかを保存する
  const [isLoading, setIsLoading] = useState(true);

  // エラーメッセージを保存する
  const [error, setError] = useState<string | null>(null);


  useEffect(() => {
    // FastAPIから従業員一覧を取得する関数
    const fetchEmployees = async () => {
      try {
        const response = await fetch(
          "http://localhost:8000/api/employees"
        );

        // HTTPステータスが200番台以外ならエラーにする
        if (!response.ok) {
          throw new Error("従業員情報の取得に失敗しました");
        }

        // JSONをJavaScriptの配列へ変換する
        const data: Employee[] = await response.json();

        // 取得した従業員一覧をstateに保存する
        setEmployees(data);
      } catch (err) {
        // エラー内容を画面表示用のstateに保存する
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError("予期しないエラーが発生しました");
        }
      } finally {
        // 成功・失敗にかかわらず、読み込み状態を終了する
        setIsLoading(false);
      }
    };

    // 従業員データの取得を開始する
    fetchEmployees();
  }, []);


  // データ取得中に表示する内容
  if (isLoading) {
    return <p>従業員情報を読み込み中です...</p>;
  }

  // エラー発生時に表示する内容
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
            UR名：{employee.ur_name}
          </li>
        ))}
      </ul>
    </main>
  );
}


export default App;
