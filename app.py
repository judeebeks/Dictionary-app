import json
from difflib import get_close_matches
data = json.load(open("data.json", "r"))#created a variable that contains json data file, and opened it

word = input("Input a word: ")

def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        option = input(f"Do you mean {get_close_matches(w, data.keys())[0]} instead? press Y to continue or N if no: ")
        if option == "Y":
            return get_close_matches(w, data.keys())[0]
        elif option == "N":
            return "Sorry the word could not be found"
        else:
            return "Wrong input"
    else:
        return "Word does not exist, please check and try again"

print(dictionary(word))

