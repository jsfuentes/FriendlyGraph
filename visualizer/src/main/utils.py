import json 

PATH = "../parser/result.json"
def getFriendData():
    with open(PATH) as f:
        data = json.load(f)
    result = []
    for k, v in data.items():
        v["msg_diff"] = v["number_received"]-v["number_sent"]
        v["word_diff"] = v["words_received"]-v["words_sent"]
        maxCount = 0
        maxWord = None
        for word, count in v["dict_sent"].items():
            if count > maxCount:
                maxCount = count
                maxWord = word 
        v["most_common_sent_word"] = maxWord
        for word, count in v["dict_received"].items():
            if count > maxCount:
                maxCount = count
                maxWord = word 
        v["most_common_received_word"] = maxWord
        result.append(v)
    
    return result