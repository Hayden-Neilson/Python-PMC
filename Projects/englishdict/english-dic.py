import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data(word)
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean this instead?" % get_close_matches(word, data.keys()[0])

    else:
        return "the word is not in the dictionary. Please try another word!"


# learned how to add a matcher for mispelled words
word = input("Enter word: ")

print(translate(word))
