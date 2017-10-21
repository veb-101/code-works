#! /usr/bin/python3


class Player:
    def __init__(self, id, name, health, items):
        self.ID = id
        self.name = name
        self.health = health
        self.items = items

    def __str__(self):
        return "My ID: {0} \n My name: {1} \n My health: {2} \n \
        My items: {3} .".format(self.ID, self.name, self.health,  self.items)
