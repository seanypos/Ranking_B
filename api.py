from flask import Flask, request
import json
app = Flask(__name__)

import reilly.py

@app.route('/ranking', methods=["POST"])
def ranking(uuid):
    content = request.get_json(silent=True) 
    # TODO: Parse content to get query
    # TODO: Call indexing and link analysis APIs and then rank webpages
    data = {'query_id': uuid, 'urls' : [{'docId': 'google.com', 'rank': 1}]}
    # TODO: data = ranked webpages
    return json.dumps(data)

@app.route('/stats', methods=["POST"])
def stats(uuid):
    content = requests.get_json(silent=True)
    # TODO: update dictionary of clicks to use in weighting algorithm
    return uuid

if __name__ == '__main__':
    app.Debug = True
    app.run(host='', port=5000)
