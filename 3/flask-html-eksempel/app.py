from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/articles/')
def articles():
    return render_template("articles.html")


@app.route('/graph/')
def dashboard():
    return render_template("graph.html")


@app.route('/profile/')
def profile():
    return render_template("profile.html")


@app.route('/login/')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()
