from Position import Position
import WorldBox
import pygame

class Organism:

    def __init__(self, position: Position, initiative, strength, characterIcon, isAlive, wasBuried, box: WorldBox, age):
        self.position = position
        self.initiative = initiative
        self.strength = strength
        self.characterIcon = characterIcon
        self.isAlive = isAlive
        self.wasBuried = wasBuried
        self.age = age
        self.box = box

    def getX(self):
        return self.position.getX()

    def getY(self):
        return self.position.getY()

    def getIsAlive(self):
        return self.isAlive

    def getIcon(self):
        return self.characterIcon

    def getStrength(self):
        return self.strength

    def getInitiative(self):
        return self.initiative

    def ageing(self):
        self.age += 1

    def getWasBuried(self):
        return self.wasBuried

    def kill(self):
        self.isAlive = False

    def bury(self):
        self.wasBuried = True

    def powerUpStrength(self):
        self.strength += 3

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position.setPosition(position)

    def save(self):
      return  self.getIcon() + " " + self.getX() + " " + self.getY() + " " + self.age  + " " + self.getStrength()

    def setAge(self, age):
        self.age = age

    def setStrength(self, strength):
        self.strength = strength

    def draw(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 14)
        icon = font.render(self.getIcon(), True, (255, 255, 255))
        screen.blit(icon, (30 + self.getX() * 10, 30 + self.getY() * 15))


