import json

base_path = '/Users/arjunsridhar/Downloads/facebook-arjunsridhar125/messages/inbox/'
msg_file = 'alanzhang_il2gvgknva/message.json'
with open(base_path + msg_file) as f:
    data = json.load(f)
    for v in data["messages"]:
        print(v)
    