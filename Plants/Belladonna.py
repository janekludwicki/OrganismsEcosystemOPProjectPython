from Position import Position
from Organism import Organism
from Plants.Plant import Plant
import pygame
import World
import WorldBox
from random import seed
from random import randint


class Belladonna(Plant):

    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 0, 99, '@', True, False, box, 0)

    def collision(self, npc):
        comment = str(self.box.getOrganismName(npc)) + " has eaten " + str(self.box.getOrganismName(self)) \
                  + " It died afterward !!!"
        self.box.addComment(comment)
        self.box.putOnGraveyard(npc.getX(), npc.getY())
        self.box.putOnGraveyard(self.getX(), self.getY())

    def action(self):
        random = randint(0, 5)
        if (random == 0):
            newPlantSpot = Position(0, 0)
            if self.findSpotForNewPlant(newPlantSpot) and self.box.getNumberOfOrganisms() < 400:
                babyPlant = Belladonna(self.box, newPlantSpot)
                self.box.addOrganism(babyPlant)

    @staticmethod
    def drawConsole():
        print('@', end=" ")

    def GetOrganismsName(self):
        return "Belladonna"
