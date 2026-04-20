export function Home() {
  return (
    <div>
      <h1>Home</h1>
      <p>Welcome to my React learning app!</p>
    </div>
  );
}

export function Blog() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts");
        const data = await response.json();
        setPosts(data.slice(0, 10));
      } catch (error) {
        console.error("Error fetching posts:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  if (loading) {
    return <div>Loading blog posts...</div>;
  }

  return (
    <div>
      <h1>My Blog</h1>

      {posts.map(post => (
        <article
          key={post.id}
          style={{
            border: "1px solid #ccc",
            margin: "16px 0",
            padding: "12px",
            borderRadius: "8px",
          }}
        >
          <h2 style={{ margin: "0 0 8px 0", fontSize: "1.3rem" }}>
            {post.title}
          </h2>
          <p style={{ margin: "0" }}>
            {post.body}
          </p>
        </article>
      ))}
    </div>
  );
}

const App = () => {
  return (
    <div>
      <Home/>
      <Blog/>
    </div>
  )
}

export default App
