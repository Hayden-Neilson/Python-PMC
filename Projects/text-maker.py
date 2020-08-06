def sentence_maker(phrase):
    interrogatives = ("how", "what", "where", "why")
    capitilized = phrase.capitilize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitilized)
    else:
        return "{}.".format.(capitilized)

results = []

while True:
    user_input = input("Say Something:")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))














