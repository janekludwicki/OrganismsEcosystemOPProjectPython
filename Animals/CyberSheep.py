from Position import Position
from Organism import Organism
import pygame
import World
from WorldBox import WorldBox
from Animals.Animal import Animal
from random import seed
from random import randint


class CyberSheep(Animal):
    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 4, 11, 'C', True, False, box, 0)

    def action(self):
        tmp = self.box.findHogweed()
        if tmp is not None and tmp is not False:
            tmp_pos = Position(self.getX(), self.getY())
            if tmp.getX() > self.getX():
                if tmp.getY() > self.getY():
                    tmp_pos.move(1, 1)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
                elif tmp.getY() < self.getY():
                    tmp_pos.move(1, -1)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
                else:
                    tmp_pos.move(1, 0)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
            elif tmp.getX() < self.getX():
                if tmp.getY() > self.getY():
                    tmp_pos.move(-1, 1)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
                elif tmp.getY() < self.getY():
                    tmp_pos.move(-1, -1)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
                else:
                    tmp_pos.move(-1, 0)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
            else:
                if tmp.getY() > self.getY():
                    tmp_pos.move(0, 1)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
                elif tmp.getY() < self.getY():
                    tmp_pos.move(0, -1)
                    if tmp_pos.IsCorrect():
                        tmp_npc = self.box.getOrganism(tmp_pos.getX(), tmp_pos.getY())
                        if tmp_npc is None or tmp_npc == self:
                            self.setPosition(tmp_pos)
                        else:
                            self.collision(tmp_npc)
        elif tmp is False:
            option = 0
            all_options = []
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    tmp = Position(self.getX(), self.getY())
                    if x != 0 or y != 0:
                        tmp.move(x, y)
                        if tmp.IsCorrect():
                            all_options.append(tmp)
                            option += 1
            if option > 0:
                index = randint(0, option)
                new_tmp = all_options[index]
                npc = self.box.getOrganism(new_tmp.getX(), new_tmp.getY())
                if npc is None or npc == self:
                    self.position.setPosition(new_tmp)
                else:
                    self.collision(npc)

    def spawnBaby(self, partner):
        babySpace = Position(0, 0)
        if self.findPlaceToSpawnBaby(babySpace, partner.getPosition()):
            baby = CyberSheep(self.box, babySpace)
            self.box.addOrganism(baby)

    @staticmethod
    def drawConsole():
        print("C", end=" ")

    def GetOrganismsName(self):
        return "Cyber Sheep"
