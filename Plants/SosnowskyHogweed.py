from Position import Position
from Organism import Organism
from Plants.Plant import Plant
import pygame
import World
import WorldBox
from random import seed
from random import randint


class SosnowskyHogweed(Plant):
    def __init__(self, box: WorldBox, position: Position):
        if position is None:
            position = Position(randint(0, 20), randint(0, 20))
            while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 0, 10, '!', True, False, box, 0)

    def action(self):
        for xMove in [-1, 0, 1]:
            for yMove in [-1, 0, 1]:
                tmp = Position(self.position.getX(), self.position.getY())
                tmp.move(xMove, yMove)
                if tmp.IsCorrect():
                    npc = self.box.getOrganism(tmp.getX(), tmp.getY())
                    if npc is not None and npc.getIcon() is not ',' and npc.getIcon() is not '*' \
                            and npc.getIcon() is not '@' and npc.getIcon() is not '%' and npc.getIcon() is not '!':
                        comment = self.box.getOrganismName(npc) + " was near Sosnowsky Hogweed !! It died !!"
                        self.box.addComment(comment)
                        self.box.putOnGraveyard(npc.getX(), npc.getY())

    def collision(self, npc):
        comment = self.box.getOrganismName(npc) + " has eaten " + self.box.getOrganismName(self) \
                  + " It died afterward !!!"
        self.box.addComment(comment)
        self.box.putOnGraveyard(npc.getX(), npc.getY())
        self.box.putOnGraveyard(self.getX(), self.getY())

    @staticmethod
    def drawConsole():
        print('!', end=" ")

    def GetOrganismsName(self):
        return "Sosnowsky's hogweed"
