from Position import Position
from Organism import Organism
import pygame
import World
import WorldBox
from random import seed
from random import randint


class Plant(Organism):
    def findSpotForNewPlant(self, babyPlantPos):
        option = 0
        allOptions = []
        for xMove in [-1, 2, 1]:
            for yMove in [-1, 2, 1]:
                tmp = Position(self.position.getX(), self.position.getY())
                tmp.move(xMove, yMove)
                if tmp.IsCorrect() and self.box.getOrganism(tmp.getX(), tmp.getY()) is None:
                    allOptions.append(Position(tmp.getX(), tmp.getY()))
                    option += 1
        if option > 0:
            random = randint(0, option-1)
            babyPlantPos.setPosition(allOptions[random])
            return True
        else:
            return False
