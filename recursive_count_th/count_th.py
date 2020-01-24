'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word = "thethoath"

def count_th(word):

    global occurences_th


    print(occurences_th)

    if len(word) == 0:
        print(f"right before terminate: {occurences_th}")
        return occurences_th

    print(word[-2:])

    if word[-2:] == "th":
        occurences_th += 1
        print(occurences_th)
    word = word[:-1]
    return count_th(word)


occurences_th = 0
print(word, occurences_th)
# print(count_th("th"))
# print(count_th("thethe"))
print(f" WTF? {count_th(word)} " )

