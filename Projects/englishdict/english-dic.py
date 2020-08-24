import json

data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data(word)
    else:
        return "the word is not in the dictionary. Please try another word!"


word = input("Enter word: ")

print(translate(word))
