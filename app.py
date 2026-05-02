from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "0.0.1")


@app.route("/")
def index():
    return jsonify({"message": "Hello from Flask", "version": VERSION})


@app.route("/health")
def health():
    return jsonify({"status": "ok", "version": VERSION})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
