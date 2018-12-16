from flask import Blueprint, render_template, request, flash, redirect, url_for

main = Blueprint('main', __name__)

def getSampleData():
    data = {
        "Hansoo Kim": {
          "number_sent": 1,
          "dict_sent": {
            "desk!!": 1,
            "interested": 1,
            "in": 1,
            "I'm": 1,
            "Hi,": 1,
            "your": 1,
            "buying": 1
          },
          "words_sent": 40,
          "dict_received": {},
          "number_received": 0,
          "friend_coef": 41,
          "words_received": 0
        }
    }
    finalData = []
    for key, value in data.items():
        value["name"] = key 
        finalData.append(value)
    return finalData 
    
@main.route('/')
def index():
    friends = getSampleData()
    return render_template("index.html", friends = friends)