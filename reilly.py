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
 
def getIndexing():
    data = json.load(open('indexing.json'))
    return data

def getQuery():
    return



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
        weights[item["webpage"]] = add
        
    
        
    ## Add indexing weight multiplier
    for item in indexing["tokens"]:
        token_size = item["ngramSize"]
        for doc in item["documentOccurences"]:
            count = len(doc["locations"])
            add = count * token_size * .2
            weights[doc["documentID"]] += add 
    return weights

'''
Create json to hand off to querying
'''
def create_query_json(sorted_keys, indexing):
    query_dict = {}
    rank = 1
    url_info = []
    for url in sorted_keys:
        inside_dict = {}
        inside_dict["url"] = url
        inside_dict["rank"] = rank
        rank+=1
        url_info.append(inside_dict)
    
    query_dict["ranking"] = url_info
    json_string = json.dumps(query_dict)
    return json_string
    
       

'''
Function creates Json that will be handed off to Link Analysis
'''
def create_link_json(urls):
    link_json = {}
    link_json["webpages"] = urls
    json_string = json.dumps(link_json)
    return json_string
    
if __name__ == "__main__":
    #test_connection(app)
    #app.run(debug=True)
    #data = getPageRank()
    link_analysis = getPageRank()
    indexing = getIndexing()
    weights, urls = create_dict(indexing)
    weights = add_weight(indexing, link_analysis, urls, weights)
    checkweight(urls,weights)
    sorted_keys = sorted(weights, key=weights.get, reverse = True)
    #print(create_link_json(urls))
    print(create_query_json(sorted_keys, indexing))
    
    
    
    
    
    #pprint(data)
    #pprint(indexing)