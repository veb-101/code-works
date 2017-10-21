#! /usr/bin/python3
import pickle
from Player import Player

items = ['axe', 'sword', 'gun']

myObj = Player(1, "Veb", 100, items)
# creating an object of a custom class and dumping it a pkl file
print(myObj)

with open("Save2.pkl", "wb") as outFile:
    pickle.dump(myObj, outFile, pickle.HIGHEST_PROTOCOL)

print("=================")


newObj = None
# accessing that dumped obj and storing it in a newObj created
with open("Save2.pkl", "rb") as inFile:
    # newObj = pickle.load(inFile

print(newObj)
