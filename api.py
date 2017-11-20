from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/sendquery/<uuid>', methods=["POST"])
def getinvertedindex(uuid):
    content = request.get_json(silent=True)
    print(content['urls'])
    # TODO: parse json
    return uuid

if __name__ == '__main__':
    app.Debug = True
    app.run(host='localhost', port=5000)
