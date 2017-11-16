"""
Querying:
1. Receive queries and send sorted urls back
2. Receive clicks for urls
"""

#practice flask work things in here
import json
from flask import Flask,jsonify

data = json.load(open('qt.json'))
app = Flask (__name__)
# import qt

@app.route('/')
def home():
    return "Hello World"

@app.route('/pq', methods =["GET"])
def pQuery():
    return data



if __name__ == '__main__':
    app.Debug = True
    app.run(host='localhost',port=5000)