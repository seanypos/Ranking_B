"""
main file that will have functions that will perform our ranking 
algotithm, and create json that will be handed off to other components
of our search engine sytem
"""


import json
import time
import requests
from pprint import pprint



#weights = {} # urls mapped to its weights
clicks =  {} # urls mapped to the number of times clicked 

'''Function add clicks to our global clicks dictionary that contains the 
   popularity of the webpage on the given query'''
def addClicks(json_clicks):
    url = json_clicks["clickthrough"]
    if url in clicks: #URL has been seen before
        clicks[url] +=1
    else: #Add to dictionary
        clicks[url] = 1
'''        
function grabs "fake" clicks (popularity Json) from Querying component
'''
def getClicks():
    data = json.load(open('clicks.json'))
    return data

'''
Function that grabs our "fake" test json from the link_analysis team
'''
def getPageRank():
     data = json.load(open('link_analysis.json'))
     # data = requests.post('http://teamk.cs.rpi.edu:8080/pageRank', json=webpages)
     # data = requests.json()
     return data
 
'''
Function that retrieves our "fake" test json from the indexing team
'''
def getIndexing():
    data = json.load(open('tests/index-average.json'))
    return data

'''
Function that retrievs "fake" json from the querying team
'''
def getQuery():
    data = json.load(open('querying.json'))
    return data

'''Function creates json that will be posted to index '''
def create_indexing_json(querying):
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
    for item in link_analysis["webpages"]:
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
def create_query_json(sorted_keys, indexing, querying):
    ID = querying["search_id"] 
    query_dict = {}
    query_dict["ID"] = ID
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
    
'''Function that takes information from the clicks dictionary and 
   applies this information to our weights '''
def clicks_to_weights():
    for url in clicks:
        weights[url] += (clicks[url] * 20)
        

    

'''
Function creates Json that will be handed off to Link Analysis
'''
def create_link_json(urls):
    link_json = {}
    link_json["webpages"] = urls
    json_string = json.dumps(link_json)
    return json_string
    
'''Function that creates a list from the top 8 urls in another list '''
def get_top_eight(urls):
    if len(urls) < 9:
        return urls
    top_eight = []
    for x in range(8):
        top_eight.append(urls[x])
    return top_eight

'''Function sorts the top 8 by most recently updated and adds weight from there'''
def top_eight_update(top_eight,link_analysis):
    top_with_date = [] #Contains url with date last
    for item  in top_eight:
        for doc in link_analysis['webpages']:
            if doc['webpage'] == item:
                top_with_date.append((item,doc['dateLastUpdated']))
    top_with_date.sort(key=lambda tup: tup[1],reverse=True)  # sorts in place
    just_url =[]
    for item in top_with_date:
        just_url.append(item[0])
    return just_url

''' Add date updated weight '''
def add_date_weight(weights,urls):
    i = 1 #
    for url in urls:
        add = 8 - i
        weights[url] += (add * .2)
        i+=1
    return weights
        
        

if __name__ == "__main__":
    ###Ranking Simulation### 
    print("Ranking Team B Simulation!")
    
    ##Recive Information from Querying##
    print("Receiving JSON from Querying...")
    time.sleep(2)   # delays for 5 seconds. You can Also Use Float Value.
    querying = getQuery()
    print(querying)
    print()
    print()
    time.sleep(3)
    
    ###Send Information to Indexing##
    print("Sending Indexing JSON list of tokens from Querying")
    to_indexing = create_indexing_json(querying)
    print(to_indexing)
    print()
    print()
    time.sleep(3)
    
    ##Recieve information from indexing ##
    print("Receiving JSON from Indexing")
    indexing = getIndexing()
    print(indexing)
    print()
    print()
    time.sleep(3)
    
    weights, urls = create_dict(indexing)
    
    
    
    ##Send JSON to link_anylisis##
    print("Send JSON to Link Analysis")
    send_link_anlysis = create_link_json(urls)
    print(send_link_anlysis)
    print()
    print()
    time.sleep(3)
    
    ##Receive JSON from Link Analysis##
    print("Receive JSON from Link Analysis")
    link_analysis = getPageRank()
    print(link_analysis)
    print()
    print()
    time.sleep(3)
    
    ##Perform Ranking algorithm##
    print("Peforming Ranking Algorithm...")
    print()
    print()
    time.sleep(3)
    
    weights = add_weight(indexing, link_analysis, urls, weights)
    sorted_keys = sorted(weights, key=weights.get, reverse = True)
    #popularity = getClicks()
    #weights = add_popularity(popularity)
    top_eight = get_top_eight(sorted_keys)
    update_eight = top_eight_update(top_eight,link_analysis)
    weights = add_date_weight(weights,update_eight)
    
    print("Send JSON to Querying")
    print(create_query_json(sorted_keys, indexing,querying))
    time.sleep(3)
    
    
    print("Receiving clicks JSON from Querying")
    clicks_json  = getClicks() 
    print(clicks_json)
    print()
    print()
    time.sleep(3)
    
    print("Updating weights based off clicks")
    addClicks(clicks_json)
    clicks_to_weights()
    print()
    print()
    time.sleep(3)
    
    print("Result from clicks")
    sorted_keys = sorted(weights, key=weights.get, reverse = True)
    print(create_query_json(sorted_keys, indexing,querying))
    
    
