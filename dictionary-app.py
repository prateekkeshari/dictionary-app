import json
from difflib import get_close_matches #import for auto suggesting misspelled words

dict_file = json.load(open("data.json")) #load the dictionary's json file

def define(word):
    word = word.lower()
    if word in dict_file:
        return dict_file[word]
    elif word.title() in dict_file: #checking for words like New York or Berlin
        return dict_file[word.title()]
    elif word.upper() in dict_file: #checking for words like USA or NATO
        return dict_file[word.upper()]
    elif len(get_close_matches(word, dict_file.keys())) > 0: # condition to check if the string returns an auto-suggestion
        answer = input(f"Did you mean {get_close_matches(word, dict_file.keys())[0]} instead? Say Y for yes or N for no.\n")
        if answer.upper() == "Y":
            return dict_file[get_close_matches(word, dict_file.keys())[0]]
        elif answer.upper() == "N":
            return "Sorry, the word doens't exist."
        else:
            return "Oops, I didn't understand."
    else:
        return ("Looks like the word doesn't exist.")

user_word = input("What's the word? \n") #take on user input
output = (define(user_word))
if isinstance(output, list): #condition to ensure it doesn't loop through regular string outputs
    for item in output: 
        print (item)
else:
    print (output)
