from Position import Position
from Organism import Organism
import pygame
import World
import WorldBox
from Animals.Animal import Animal
from random import seed
from random import randint


class Wolf(Animal):
    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 5, 9, 'W', True, False, box, 0)

    def spawnBaby(self, partner):
        babySpace = Position(0, 0)
        if self.findPlaceToSpawnBaby(babySpace, partner.getPosition()):
            baby = Wolf(self.box, babySpace)
            self.box.addOrganism(baby)

    def GetOrganismsName(self):
        return "Wolf"

    @staticmethod
    def drawConsole():
        print("W", end=" ")
