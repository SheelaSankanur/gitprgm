import { BrowserRouter, Routes, Route, Link, useParams } from "react-router-dom";

function TodoItem({ id, text }) {
  return (
    <div>
      <Link to={`/todo/${id}`}>{text}</Link>
    </div>
  );
}

function TodoList() {
  const todos = [
    { id: 1, text: "Learn React basics" },
    { id: 2, text: "Build a small app" },
  ];

  return (
    <div>
      <h1>Todos</h1>
      {todos.map(todo => (
        <TodoItem key={todo.id} id={todo.id} text={todo.text} />
      ))}
    </div>
  );
}

function TodoDetails() {
  const { id } = useParams();
  return (
    <div>
      <h1>Todo Detail</h1>
      <p>Todo ID: {id}</p>
      <Link to="/todos">← Back to list</Link>
    </div>
  );
}


function App() {
  return (
    <BrowserRouter>
      <nav style={{ marginBottom: "16px" }}>
        <Link to="/todos">Todos</Link>
      </nav>

      <Routes>
        <Route path="/todos" element={<TodoList />} />
        <Route path="/todo/:id" element={<TodoDetails />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;