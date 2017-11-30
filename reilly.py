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

<<<<<<< HEAD
#return like so ~~
"""
    {
    "ranking": [
    {
    "url": "www.url.com",
    "rank": 1,
    "positions": {"query": [1, 55, 3000], "test": [5], "example": [2, 90], ... }
    },
    {
    "url": "www.secondurl.com",
    "rank": 2,
    "positions": {"query": [34], "test": [34, 78, 989, 234325], ... }
    },
    ... ]
    }
    """
=======
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
 
def getIndexing():
    data = json.load(open('indexing.json'))
    return data

def getQuery():
    return
>>>>>>> master



def checkweight(urls, weights):
    for item in urls:
        print(weights[item])
'''
Iterate through indexing Json and create dictionary with all url keys
'''
def create_dict(indexing):
    weights = {}
    #print(indexing["documents"][0]["documentID"])
    all_urls = []
    for x in range(len(indexing["documents"])):
        weights[indexing["documents"][0]["documentID"]] = 0
        all_urls.append(indexing["documents"][x]["documentID"])
    return weights, all_urls

'''
Function adds weight to the dictionary of urls for each url
'''
def add_weight(indexing, link_analysis, urls, weights):
    ## Add link_analysis weight will update multiplayer when testing
    print(len(link_analysis["test"]))
    for item in link_analysis["test"]:
        add = item["pageRankValue"] * .2
        print(add)
        weights[item["webpage"]] = add
        
    ## Add indexing weight multiplier
    
    
    checkweight(urls,weights)
if __name__ == "__main__":
    #test_connection(app)
    #app.run(debug=True)
    #data = getPageRank()
    link_analysis = getPageRank()
    indexing = getIndexing()
    weights, urls = create_dict(indexing)
    weights = add_weight(indexing, link_analysis, urls, weights)
    
    
    
    
    
    
    #pprint(data)
    #pprint(indexing)