def acronym(phrase):
    words = phrase.split()
    result = ""

    for word in words:
        result += word[0].upper()

    return result

user_phrase = input("takes a phrase: ")
print(" An acronym:", acronym(user_phrase))

