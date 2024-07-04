from Position import Position
from Organism import Organism
import pygame
import World
import WorldBox
from Animals.Animal import Animal
from random import seed
from random import randint


class Fox(Animal):
    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 7, 3, 'F', True, False, box, 0)

    def spawnBaby(self, partner):
        babySpace = Position(0, 0)
        if self.findPlaceToSpawnBaby(babySpace, partner.getPosition()):
            baby = Fox(self.box, babySpace)
            self.box.addOrganism(baby)

    def action(self):
        option = 0
        allOptions = []
        for xMove in [-1, 0, 1]:
            for yMove in [-1, 0, 1]:
                tmp = Position(self.position.getX(), self.position.getY())
                tmp.move(xMove, yMove)
                if tmp.IsCorrect():
                    npc = self.box.getOrganism(tmp.getX(), tmp.getY())
                    if npc is None or npc.getStrength() <= self.strength:
                        allOptions.append(Position(tmp.getX(), tmp.getY()))
                        option += 1
        if option > 0:
            random = randint(1, option-1)
            newTmp = allOptions[random]
            npc = self.box.getOrganism(newTmp.getX(), newTmp.getY())
            if npc is None or npc == self:
                self.setPosition(newTmp)
            else:
                self.collision(npc)
        self.ageing()

    def GetOrganismsName(self):
        return "Fox"

    @staticmethod
    def drawConsole():
        print("F", end=" ")

