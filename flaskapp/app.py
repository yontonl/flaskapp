from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    name = request.args.get("name") or "World"
    return f"Hello, {name}!"
