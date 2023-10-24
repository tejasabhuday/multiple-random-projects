import json
from difflib import get_close_matches
data= json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title()in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean%s" %get_close_matches(word,data.keys())[0])
        decide= input("if the answer is yes press y if the answer is no press n")
        if decide=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide=="n":
            print("sorry we don't have the definition we are working hard to make the app better")


    else:
        print("sorry we don't have the definition we are working hard to make the app better")

word= input("enter the word you want the meaning for")
word= word.strip()
output = translate(word)
print(output)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
