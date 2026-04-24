from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return """
    Hello Flask!
    <ul>
        <li><a href="/index">Go to Index</a></li>
        <li><a href="/about">Go to About</a></li>
    """

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is the about page.</p>"

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        return f"<h1>Thanks, {name}!</h1><a href='/'>Go back</a>"

    # GET request: show the form
    return """
    <h1>Fill this form</h1>
    <form method="POST">
        <label>Name: <input name="name" required></label><br><br>
        <button type="submit">Submit</button>
    </form>
    <a href="/">Go back to home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)