from Position import Position
from Organism import Organism
import pygame
import World
import WorldBox
from Animals.Animal import Animal
from random import seed
from random import randint


class Turtle(Animal):
    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 1, 2, 'T', True, False, box, 0)

    def spawnBaby(self, partner):
        babySpace = Position()
        if self.findPlaceToSpawnBaby(babySpace, partner.getPosition()):
            baby = Turtle(self.box, babySpace)
            self.box.addOrganism(baby)

    def action(self):
        random = randint(0, 4)
        if random == 0:
            option = 0
            allOptions = []
            for xMove in [-1, 0, 1]:
                for yMove in [-1, 0, 1]:
                    tmp = Position(self.position.getX(), self.position.getY())
                    tmp.move(xMove, yMove)
                    if tmp.IsCorrect():
                        allOptions.append(Position(tmp.getX(), tmp.getY()))
                        option += 1
            if option > 0:
                random1 = randint(1, option-1)
                newTmp = allOptions[random1]
                npc = self.box.getOrganism(newTmp.getX(), newTmp.getY())
                if npc is None or npc == self:
                    self.position.setPosition(newTmp)
                else:
                    self.collision(npc)
        self.ageing()

    def collisionSpecial(self, npc):
        if npc.getStrength() > 5:
            comment = self.box.getOrganismName(self) + " was eaten by " + self.box.getOrganismName(npc)
            self.box.addComment(comment)
            self.box.putOnGraveyard(self.getX(), self.getY())
            npc.setPosition(self.position)

    def GetOrganismsName(self):
        return "Turtle"

    @staticmethod
    def drawConsole():
        print("T", end=" ")
