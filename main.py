import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route("/request-fetch", methods=["GET"])
def fetch_and_response():
    from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
    try:
        response = requests.get(request.headers.get("Origin"))
        response.raise_for_status()
    except (HTTPError, ConnectionError, Timeout, RequestException) as err:
        return (err.__str__(), 500, {"Content-Type": "text/plain"})
    return ("Hello, Iscra-chan", {"Content-Type": "text/plain"})

if __name__ == "__main__":
    app.run()

