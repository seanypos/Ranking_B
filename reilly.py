"""
Hello my Name Is reilly Keating-Wood and 
for ranking team B i am CFO. The 
Chief Financial Officer
"""

#from flask import Flask
#from flask import json
import json
from pprint import pprint
#from flask import jsonify
#app = Flask(__name__)

'''
def test_connection(self):
    with app.app_context():
        return
'''

#data = json.load(open('link_analysis.json'))
#@app.endpoint("/")
#def test_json():
#@app.route('/todo/api/v1.0/data', methods=['GET'])
def getPageRank():
     data = json.load(open('link_analysis.json'))
     return data
    


if __name__ == "__main__":
    #test_connection(app)
    print("test")
    #app.run(debug=True)
    #data = getPageRank()
    data = getPageRank()
    #pprint(data)
    pprint(data['test'])