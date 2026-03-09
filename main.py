from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="frontend",
    static_folder="frontend"
)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cities")
def cities():
    return "Cities page coming soon"

@app.route("/login")
def login():
    return "Login page coming soon"



if __name__ == "__main__":
    app.run(debug=True)