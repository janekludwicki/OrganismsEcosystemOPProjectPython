import Organism
from Animals import *


class WorldBox:

    def __init__(self):
        self.deaths = 0
        self.organisms = []
        self.commentary = []
        self.graveyard = []

    def addOrganism(self, organism):
        if len(self.organisms) == 0:
            self.organisms.append(organism)
        else:
            is_set = False
            for i in range(len(self.organisms)):
                tmp = self.organisms[i]
                if tmp.getInitiative() < organism.getInitiative():
                    self.organisms.append(organism)
                    is_set = True
                    break
            if not is_set:
                self.organisms.append(organism)
        comment = self.getOrganismName(organism) + " appeared in the world at X: " + str(organism.getX()) + " Y: " + \
                  str(organism.getY())
        self.addComment(comment)

    def getOrganism(self, x, y):
        for i in range(len(self.organisms)):
            tmp = self.organisms[i]
            if tmp.getX() == x and tmp.getY() == y and tmp.getIsAlive():
                return tmp
        return None

    def getNumberOfOrganisms(self):
        return len(self.organisms)

    def addComment(self, comment):
        self.commentary.append(comment)

    def getCommentary(self):
        return self.commentary

    def findHogweed(self):
        i = 0
        while i < self.getNumberOfOrganisms():
            if self.organisms[i].getIcon() == "!":
                return self.organisms[i]
            i += 1
        else:
            return False

    def getOrganismName(self, organism):
        if organism.getIcon() == 'H':
            return "Human"
        elif organism.getIcon() == 'W':
            return "Wolf"
        elif organism.getIcon() == 'S':
            return "Sheep"
        elif organism.getIcon() == 'T':
            return "Turtle"
        elif organism.getIcon() == 'A':
            return "Antelope"
        elif organism.getIcon() == 'F':
            return "Fox"
        elif organism.getIcon() == '*':
            return "Sow Thistle"
        elif organism.getIcon() == ',':
            return "Grass"
        elif organism.getIcon() == '@':
            return "Belladonna"
        elif organism.getIcon() == '%':
            return "Guarana"
        elif organism.getIcon() == '!':
            return "Sosnowsky Hogweed"
        else:
            return ""

    def putOnGraveyard(self, x, y):
        tmp = self.getOrganism(x, y)
        if tmp is not None:
            tmp.kill()
            self.graveyard.append(tmp)
            self.deaths += 1

    def getList(self):
        return self.organisms

    def buryDead(self):
        for i in range(self.deaths):
            if self.organisms.count(self.graveyard[i]) == 0:
                continue
            self.organisms.remove(self.graveyard[i])
            self.graveyard[i] = None
        self.deaths = 0
