from flask import Flask, request

app = Flask(__name__)

entries = []

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        entries.append({"name": name})
        return f"<h1>Thanks, {name}! Your data is saved.</h1>"

    return """
    <form method="POST">
        <label>Name: <input name='name' required></label>
        <button type='submit'>Submit</button>
    </form>
    """