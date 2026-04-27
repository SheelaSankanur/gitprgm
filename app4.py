from flask import Flask, request, render_template

app = Flask(__name__)

entries = []


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        entries.append({"name": name})
        # Show the form again (or you can redirect /entries later)
        return render_template("form.html", saved_name=name)

    return render_template("form.html")

@app.route("/entries")
def show_entries():
    return render_template("entries.html", entries=entries)