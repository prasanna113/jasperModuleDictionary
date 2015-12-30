import unirest
import random
import re

WORDS = ["DEFINE", "DEFINITION"]

def handle(text, mic, profile):
    app_id = "PYZp3gynW4msh6f1mOO60KaV6JAPp1x4peHjsnmT1OXwcopmmc"
    response = unirest.get("https://montanaflynn-dictionary.p.mashape.com/define?word=%s" % text, 
                           headers={"X-Mashape-Key": app_id,
                           "Accept": "application/json"}
                           )
    
    body = response.body
    messages = [body["definitions"][0]["text"],
                body["definitions"][1]["text"]]
    
    message = random.choice(messages)
    mic.say(message)
    
def isValid(text):
    if re.search(r'\bdefine\b', text, re.IGNORECASE):
        return True
    elif re.search(r'\bdefinition\b', text, re.IGNORECASE):
        return True
    else:
        return False
