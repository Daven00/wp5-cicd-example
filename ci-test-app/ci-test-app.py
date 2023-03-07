#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)


@app.route("/hello")
def apicall_hello():
    return "Hello world!\n"

@app.route("/commit-id")
def apicall_commit_id():
    with open("COMMIT_ID") as f:
        return f.readline()

@app.route("/targetplatform")
def apicall_targetplatform():
    with open("TARGETPLATFORM") as f:
        return f.readline()


app.run(host="0.0.0.0", port=5050)
