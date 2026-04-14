import { useState } from "react";

function TodoList() {
  const [todos, setTodos] = useState([
    { id: 1, text: "Learn React basics", completed: false },
    { id: 2, text: "Build a small app", completed: false },
  ]);

  const [newText, setNewText] = useState("");

  const handleTextChange = (event) => {
    setNewText(event.target.value);
  };

  const addTodo = () => {
    if (!newText.trim()) return;

    const newTodo = {
      id: Date.now(),
      text: newText.trim(),
      completed: false,
    };

    setTodos([...todos, newTodo]);
    setNewText("");
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      addTodo();
    }
  };

  const toggleComplete = (id) => {
    setTodos(
      todos.map(todo =>
        todo.id === id ? { ...todo, completed: true } : todo
      )
    );
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div>
      <h2>Todo List</h2>

      <div style={{ marginBottom: "16px" }}>
        <input
          type="text"
          value={newText}
          onChange={handleTextChange}
          onKeyPress={handleKeyPress}
          placeholder="Add a new task"
        />
        <button onClick={addTodo}>Add</button>
      </div>

      <ul>
        {todos.map(todo => (
          <li
            key={todo.id}
            style={{
              margin: "4px 0",
              textDecoration: todo.completed ? "line-through" : "none",
              opacity: todo.completed ? 0.6 : 1,
            }}
          >
            <label>
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => toggleComplete(todo.id)}
              />
              {todo.text}
            </label>
            <button
              onClick={() => deleteTodo(todo.id)}
              style={{ marginLeft: "8px" }}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

function App() {
  return (
    <div>
      <TodoList />
    </div>
  );
}

export default App;