from Position import Position
from Organism import Organism
from Plants.Plant import Plant
import pygame
import World
import WorldBox
from random import seed
from random import randint


class SowThistle(Plant):

    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 0, 0, '*', True, False, box, 0)

    def action(self):
        for i in range(0, 4):
            random = randint(0, 10)
            if random == 0:
                newPlantSpot = Position(0, 0)
                if self.findSpotForNewPlant(newPlantSpot) and self.box.getNumberOfOrganisms() < 400:
                    babyPlant = SowThistle(self.box, newPlantSpot)
                    self.box.addOrganism(babyPlant)

    def GetOrganismsName(self):
        return "Sow thistle"

    @staticmethod
    def drawConsole():
        print('*', end=" ")
