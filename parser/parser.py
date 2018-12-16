import json
import os
from tqdm import tqdm

PATH = '/Users/jfuentes/Desktop/facebook-100005512638771/messages/inbox/'
NAME = 'Jorge J Fuentes'

class FriendData:
    "Class to store all of the parsed data"
    friend_list = []
    friend_coef = {}
    # takes form {'name': {'words_sent':#, 'words_received':#, etc}}
    parsed_data = {}

    base_path = ''
    msg_file = '/message.json'
    my_name = ''

    def __init__(self, base_path, name):
        self.base_path = base_path
        self.my_name = name
        self.parseData()

    def countWords(self, msg, dict_store):
        for word in msg.split():
            if word in dict_store.keys():
                dict_store[word] += 1
            else:
                dict_store[word] = 1

    def getFriendName(self, data):
        if len(data['participants']) > 2:
            return 'GROUP_CHAT'
        else:
            return data['participants'][0]['name']
    
    def getFriendCoef(self, words_sent, words_received, number_sent, number_received):
        return words_sent + words_received + number_sent + number_received

    def parseData(self):
        for folder in tqdm(os.listdir(self.base_path)):
            if folder == '.DS_Store':
                continue
            with open(self.base_path + folder + self.msg_file) as f:
            # with open(base_path + 'JannyZhang_01t0vyPMNQ' + msg_file) as f:
                data = json.load(f)
                friend_name = self.getFriendName(data)
                if friend_name == 'GROUP_CHAT':
                    continue
                    # return
                words_sent, words_received = 0, 0
                dict_sent, dict_received = dict(), dict()
                number_sent, number_received = 0, 0
                for msg in data['messages']:
                    # There are some msgs with no content
                    # TODO: parse out calls and init msgs
                    try:
                        msg_content = msg['content']
                        msg_sender = msg['sender_name']
                    except:
                        continue
                        # return
                    if msg_sender == self.my_name:
                        words_sent += len(msg_content)
                        number_sent += 1
                        self.countWords(msg_content, dict_sent)
                    else:
                        words_received += len(msg_content)
                        number_received += 1
                        self.countWords(msg_content, dict_received)
                # print(friend_name)
                self.friend_list.append(friend_name)
                # print(words_sent, number_sent)
                # print(words_received, number_received)
                # print('\n'*2)
                friend_coef = self.getFriendCoef(words_sent, words_received, number_sent, number_received)
                self.friend_coef[friend_name] = friend_coef
                self.parsed_data[friend_name] = {'friend_name':friend_name,
                    'words_sent':words_sent, 
                    'words_received':words_received, 
                    'number_sent':number_sent, 
                    'number_received':number_received,
                    'dict_sent':dict_sent,
                    'dict_received':dict_received,
                    'friend_coef':friend_coef}
                    
if __name__ == "__main__":
    fd = FriendData(PATH, NAME)
    print(fd.friend_coef)
    with open('result.json', 'w') as f:
        json.dump(fd.parsed_data, f)