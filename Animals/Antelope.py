from Position import Position
from Organism import Organism
import pygame
import World
import WorldBox
from Animals.Animal import Animal
from random import seed
from random import randint


class Antelope(Animal):
    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 4, 4, 'A', True, False, box, 0)

    def spawnBaby (self, partner):
        babySpace = Position(0, 0)
        if self.findPlaceToSpawnBaby(babySpace, partner.getPosition()):
            baby = Antelope(self.box, babySpace)
            self.box.addOrganism(baby)

    def action(self):
        for i in range(2):
            option = 0
            allOptions = []
            for xMove in [-1, 0 , 1]:
                for yMove in [-1, 0, 1]:
                    tmp = Position(self.position.getX(), self.position.getY())
                    tmp.move(xMove, yMove)
                    if tmp.IsCorrect():
                        allOptions.append(Position(tmp.getX(), tmp.getY()))
                        option += 1
            if option > 0:
                random = randint(0, option-1)
                newTmp = allOptions[random]
                npc = self.box.getOrganism(newTmp.getX(), newTmp.getY())
                if npc is None or npc is None:
                    self.position.setPosition(newTmp)
                else:
                    self.collision(npc)
        self.ageing()

    def collisionSpecial(self, npc):
        random = randint(0, 2)
        escaped = False
        if random == 1:
            option = 0
            allOptions = []
            tmp = Position( self.position.getX(), self.position.getY())
            for xMove in [-1, 0, 1]:
                for yMove in [-1, 0, 1]:
                    tmp.move(xMove, yMove)
                    if tmp.IsCorrect() and self.box.getOrganism(tmp.getX(), tmp.getY()) is None:
                        allOptions[option] = Position(tmp.getX(), tmp.getY())
                        option += 1
            if option > 0:
                comment = "Antolepe managed to escape the fight !!!"
                random2 = randint(0, option)
                self.box.addComment(comment)
                npc.setPosition(self.position)
                self.setPosition(allOptions[random2])
                escaped = True
        if not escaped:
            if self.strength > npc.getStrength():
                comment = self.box.getOrganismName(npc) + " was eaten by " + self.box.getOrganismName(self)
                self.box.addComment(comment)
                self.box.putOnGraveyard(npc.getX(), npc.getY())
            else:
                comment = self.box.getOrganismName(self) + " was eaten by " + self.box.getOrganismName(npc)
                self.box.addComment(comment)
                self.box.putOnGraveyard(self.getX(), self.getY())
                npc.setPosition(self.position)

    def GetOrganismsName(self):
        return "Antelope"

    @staticmethod
    def drawConsole():
        print("A", end = " ")
