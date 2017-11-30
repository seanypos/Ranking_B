from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/indexing/<uuid>', methods=["POST"])
def indexing(uuid):
    content = request.get_json(silent=True)
    print("indexing gives us: ", content)
    # TODO: parse json and add weights
    return uuid

@app.route('/querying/<uuid>', methods=["POST"])
def querying(uuid):
    content = request.get_json(silent=True)
    print("querying gives us: ", content)
    # TOOD: parse json and pass queries to indexing
    return uuid

@app.route('/pageranks/<uuid>', methods=["POST"])
def pageranks(uuid):
    content = request.get_json(silent=True)
    print("link analysis gives us: ",content)
    # TOOD: parse json and update weights
    return uuid



if __name__ == '__main__':
    app.Debug = True
    app.run(host='localhost', port=5000)
