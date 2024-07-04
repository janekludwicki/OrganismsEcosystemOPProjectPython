from Position import Position
from Organism import Organism
import pygame
import World
import WorldBox
from random import seed
from random import randint


class Animal(Organism):
    def findPlaceToSpawnBaby(self, baby_pos: Position, partner_pos: Position):
        option = 0
        allOptions = []
        for xMove in range(-1, 2):
            for yMove in range(-1, 2):
                tmp = self.position
                tmpPart = partner_pos
                tmp.move(xMove, yMove)
                tmpPart.move(xMove, yMove)
                if tmp.IsCorrect() and self.box.getOrganism(tmp.getX(), tmp.getY()) is None:
                    allOptions[option].setPosition(tmp)
                    option += 1
                if tmpPart.IsCorrect() and self.box.getOrganism(tmpPart.getX(), tmpPart.getY()) is None:
                    allOptions[option].setPosition(tmpPart)
                    option += 1
        if option > 0:
            random = randint(0, option)
            baby_pos.setPosition(allOptions[random])
            return True
        else:
            return False

    def action(self):
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
            random = randint(1, option-1)
            newTmp = allOptions[random]
            npc = self.box.getOrganism(newTmp.getX(), newTmp.getY())
            if npc is None or npc is None :
                print("setting new position from " + str(self.position.getX()) + "," + str(self.position.getY()))
                print("to " + str(newTmp.getX()) + "," + str(newTmp.getY()))
                self.position.setPosition(newTmp)
            else:
                self.collision(npc)

    def collision(self, npc):
        npcPos= Position(npc.getX(), npc.getY())
        if npc.getIcon() == self.characterIcon:
            if self.box.getNumberOfOrganisms() < 400:
                self.spawnBaby(npc)
        elif npc.getIcon() == '@':
            npc.collision(self)
        elif npc.getIcon() == '%':
            npc.collision(self)
        elif npc.getIcon() == '!':
            npc.collision(self)
        elif npc.getIcon() == 'A':
            npc.collisionSpecial(self)
        else:
            if self.strength >= npc.getStrength() :
                if npc.getIcon() == 'T':
                    npc.collisionSpecial(self)
                    if self.strength <= 5:
                        comment = self.box.getOrganismName(npc) + " has blocked the attack of " \
                                  + self.box.getOrganismName(self) + " !!!"
                        self.box.addComment(comment)
                else:
                    comment = self.box.getOrganismName(npc) + " was eaten by " + self.box.getOrganismName(self)
                    self.box.addComment(comment)
                    self.box.putOnGraveyard(npcPos.getX(), npcPos.getY())
                    npc.setPosition(npcPos)
            else:
                comment = self.box.getOrganismName(self) + " was eaten by " + self.box.getOrganismName(npc)
                self.box.addComment(comment)
                self.box.putOnGraveyard(self.position.getX(), self.position.getY())
        self.ageing()

    def spawnBaby(self, partner):
        pass
