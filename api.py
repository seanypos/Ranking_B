from flask import Flask, request
import json
app = Flask(__name__)

import reilly

@app.route('/ranking', methods=["POST"])
def ranking():
    content = request.get_json(silent=True) 
    # TODO: Parse content to get query
    # TODO: Call indexing and link analysis APIs and then rank webpages
    data = {'query_id': 1, 'urls' : [{'docId': 'google.com', 'rank': 1}]}
    # TODO: data = ranked webpages
    return json.dumps(data)

@app.route('/stats', methods=["POST"])
def stats():
    content = requests.get_json(silent=True)
    # TODO: update dictionary of clicks to use in weighting algorithm
    return 0

if __name__ == '__main__':
    app.Debug = True
    app.run(host='0.0.0.0', port=5000)
