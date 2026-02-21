import os
import sys
import logging
import requests
from flask import Flask, request, jsonify

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
app = Flask(__name__)

@app.route("/<path:path>")
def index1(path):
    return "Hello, Iscra-chan!"

@app.route("/request-fetch", methods=["POST"])
def fetch_and_response():
    from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout

    logging.info(request.data)
    url_to_fetch = request.get_json(silent=True)
    logging.info(url_to_fetch)
    if url_to_fetch is None:
        return (jsonify("Bad JSON"), 400)
    try:
        response = requests.get(url_to_fetch)
        response.raise_for_status()
    except (HTTPError, ConnectionError, Timeout, RequestException) as err:
        # DEBUG:
        logging.info(err)
        return (jsonify(err.__str__()), 500)
    return jsonify("Hello, Iscra-chan")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
