import json 

PATH = "../parser/result.json"
def getFriendData():
    with open(PATH) as f:
        data = json.load(f)
    
    return list(data.values())