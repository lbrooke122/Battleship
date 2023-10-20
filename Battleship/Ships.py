import pygame

class Ship:
    def __init__(self, name, pos, size, img = 0):
        self.ships = {5 : ("Carrier", 1),
                      4 : ("Battleship", 1),
                      3 : ("Destroyer", 1),
                      2 : ("Patrol Boat", 2),
                      1 : ("Submarine", 3)}

        self.placing_ships = True

    def draw(self, gameDislpay):
        pass

    def display_ships(self, gameDisplay):
        pass