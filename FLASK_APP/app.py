from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/<name>")
def user(name):
    return f"hello {name}"


@app.route("/admin/")
def admin():
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True)

