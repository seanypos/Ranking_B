

from flask import Flask, request
import json
app = Flask(__name__)

import reilly.py as main

@app.route('/query/<uuid>', methods=["POST"])
def querying(uuid):
    content = request.get_json(silent=True) 
    # TODO: Parse content to get query
    # TODO: Call indexing and link analysis APIs and then rank webpages
    #data = {'query_id': uuid, 'urls' : [{'docId': 'google.com', 'rank': 1}]}
    
    link_analysis = main.getPageRank()
    indexing = main.getIndexing()
    weights, urls = main.create_dict(indexing)
    weights = main.add_weight(indexing, link_analysis, urls, weights)
    #checkweight(urls,weights)
    sorted_keys = sorted(weights, key=weights.get, reverse = True)
    test_json = main.create_query_json(sorted_keys, indexing)
    # TODO: data = ranked webpages
    return json.dumps(test_json)

@app.route('/clicks', methods=["POST"])
def clicks(uuid):
    content = requests.get_json(silent=True)
    # TODO: update dictionary of clicks to use in weighting algorithm
    return uuid

if __name__ == '__main__':
    app.Debug = True
    app.run(host='localhost', port=5000)
