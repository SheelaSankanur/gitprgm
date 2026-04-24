from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run(debug=True)