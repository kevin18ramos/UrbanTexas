from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return Flask.render_template("index.html")

@app.route("/cities")
def cities():
    return "Cities page coming soon"

@app.route("/login")
def login():
    return "Login page coming soon"


if __name__ == "__main__":
    app.run(debug=True)