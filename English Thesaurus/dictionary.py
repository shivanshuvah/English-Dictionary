import json
from difflib import get_close_matches

data = json.load(open("data.json","r"))# load the data into dict datatype

def translate(word):
    word = word.lower() # convert to lowercase for all difference word cases
    if word in data:
        return data[word]
    elif word.title() in data: # if user enters delhi or DELHi
        return data[word.title()]
    elif word.upper() in data: # for words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0: # check if similar word exists
        choice=input("I found your illogical word closest to {}. Type Y for yes and N for no: ".format(get_close_matches(word, data.keys())[0]))
        if choice == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == 'N':
            return "Hard luck! Please do no invent words of your own!"
        else:
            return "invalid choice" 
    else:
        return "Hard luck! Please do no invent words of your own!" # if no similar word exists, return a message
    

word = input("Here to learn something? Shoot :  ") #program main execution
output=translate(word)
if type(output)==list: # formatting the output in case of multiple definitions
    for definition in output:
        print(definition)
else:
    print(output) # prit the error string
