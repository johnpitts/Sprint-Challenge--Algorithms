'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word = "thethothath"



def count_th(word):

    occurences_th = 0

    if len(word) == 0:
        print(f"right before terminate: {occurences_th}")
        return 0

    print(word[-2:])

    if word[-2:] == "th":
        occurences_th += 1
    word = word[:-1]
    return occurences_th + count_th(word)


print(f" WTF? {count_th(word)} " )

