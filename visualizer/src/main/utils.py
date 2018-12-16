import json 

PATH = "../parser/result.json"
def getFriendData():
    with open(PATH) as f:
        data = json.load(f)
    result = []
    for k, v in data.items():
        v["msg_diff"] = v["number_received"]-v["number_sent"]
        v["word_diff"] = v["words_received"]-v["words_sent"]
        result.append(v)
    
    return result