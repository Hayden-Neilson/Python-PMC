import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data(word)
    # if user entered "texas" this will check for "Texas" as well.
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = "Did you mean this instead? Enter Y if yes, or N if no" % get_close_matches(
            word, data.keys()[0])
        if yn == "Y":
            return data(get_close_matches(word, data.keys()[0]))
        elif yn == "N":
            return "the word is not in the dictionary. Please try another word!"
        else:
            return "we didnt understand yout entry "

    else:
        return "the word is not in the dictionary. Please try another word!"


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
    else:
        print(item)
