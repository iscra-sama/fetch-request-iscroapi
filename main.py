import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/<path:path>")
def index1(path):
    return "Hello, Iscra-chan!"

@app.route("/request-fetch", methods=["POST"])
def fetch_and_response():
    from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
    # DEBUG:
    print(request.headers.get("Origin"))
    try:
        response = requests.get(request.headers.get("Origin"))
        response.raise_for_status()
    except (HTTPError, ConnectionError, Timeout, RequestException) as err:
        return (err.__str__(), 400, {"Content-Type": "text/plain"})
    return ("Hello, Iscra-chan", {"Content-Type": "text/plain"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
