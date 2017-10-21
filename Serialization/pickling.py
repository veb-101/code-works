#!/usr/bin/python3

import pickle

dict1 = {"a": 100, "b": 200, "c": 100}

list1 = [400, 500, 600]

print(dict1)
print(list1)
# dumping created objects to a file
with open("Save.pkl", "wb") as output:
    pickle.dump(dict1, output, pickle.HIGHEST_PROTOCOL)
    pickle.dump(list1, output, pickle.HIGHEST_PROTOCOL)

print("======================")

inputFile = open("Save.pkl")
# accessing those objects and saving them in a different object
with open("Save.pkl", 'rb') as inputFile:
    dict2 = pickle.load(inputFile)
    list2 = pickle.load(inputFile)
print(dict2)
print(list2)
