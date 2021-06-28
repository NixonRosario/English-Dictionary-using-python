# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json  # built-in function which contains the word and it's meaning
from difflib import get_close_matches  # difflib is used to compare the other data types and find the data close to the word

data = json.load(open("data.json"))  # this the open the downloaded json file


def trans(w):
    w = w.lower()  # used to lower the text

    if w in data:
        return data[w]  # print the word which is present in the data
    elif len(get_close_matches(w, data.keys())) > 0:  # we take data of keys which is close to the data
        new = input("Did you mean %s instead?\n If YES enter y else enter n:- " % get_close_matches(w, data.keys())[0])
        new.lower()

        if new == 'y':
            return data[get_close_matches(w, data.keys())[0]]  # print the data which is close to the miss-spelled word
        elif new == 'n':
            return "Thank you!!"
        else:
            return "The word does not found"
    else:
        return "The word does not excites"


word = input('Enter the word:- ')
out = trans(word)
if type(out) == list:  # checks whether it is list format
    for items in out:
        print(items)  # print the which is in the "out" without square brackets
else:
    print(out)
