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
    data = json.load(open('querying.json'))
    return data

'''Function creates json that will be posted to index '''
def create_Indexing_json(querying):
    to_index = {}
    to_index["tokens"] = querying["transformed"]["transformed_tokens"]
    return to_index

'''Helper function to print weights of dictionary'''
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
        weights[indexing["documents"][x]["documentID"]] = 0
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
            occurence_count = len(doc["locations"])
            add = occurence_count * token_size * .2
            weights[doc["documentID"]] += add 
    return weights

'''
Function creates a position dictionary that will be used for query json
Will help querying identify locations for the snippets they will be outputing
'''
def get_position(url, indexing):
    position_dict = {}
    for item in indexing["tokens"]:
        n_gram = item["token"] 
        for doc in item["documentOccurences"]:
            if doc["documentID"] == url:
                locations = []
                for loc in doc["locations"]:
                    locations.append(loc)
                position_dict[n_gram] = locations
    return position_dict

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
        position = get_position(url,indexing) #helper position dictionary
        inside_dict["position"] = position
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
    querying = getQuery()
    link_analysis = getPageRank()
    indexing = getIndexing()
    weights, urls = create_dict(indexing)
    weights = add_weight(indexing, link_analysis, urls, weights)
    #checkweight(urls,weights)
    sorted_keys = sorted(weights, key=weights.get, reverse = True)
    print(create_Indexing_json(querying))
    #print(create_link_json(urls))
    #print(create_query_json(sorted_keys, indexing))
    
    
