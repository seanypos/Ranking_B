from flask import Flask, request
import json
app = Flask(__name__)

import reilly

@app.route('/ranking', methods=["POST"])
def ranking():
    content = request.get_json(silent=True)
    s_id = content['search_id']
    # TODO: Parse content to get query
    # TODO: Call indexing and link analysis APIs and then rank webpages
    data = {'search_id': s_id,
            'ranking' : [
                {
                    'url': 'www.google.com',
                    'rank': 1,
                    'positions': {
                        'token': 'google',
                        'location': [1]
                    }
                }
            ]
    }
    # TODO: data = ranked webpages
    return json.dumps(data)

@app.route('/stats', methods=["POST"])
def stats():
    content = requests.get_json(silent=True)
    # TODO: update dictionary of clicks to use in weighting algorithm
    data = {'status': 0}
    return json.dumps(data)

if __name__ == '__main__':
    app.Debug = True
    app.run(host='0.0.0.0', port=5000)
