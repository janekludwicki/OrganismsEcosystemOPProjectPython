from Position import Position
from Organism import Organism
import pygame
import World
import WorldBox
from Animals.Animal import Animal
from random import seed
from random import randint


class Human(Animal):
    def __init__(self, box: WorldBox):
        position = Position(randint(0, 20), randint(0, 20))
        while box.getOrganism(position.getX(), position.getY()) is not None:
                position = Position(randint(0, 20), randint(0, 20))
        super().__init__(position, 4, 5, 'H', True, False, box, 0)
        self.boostTime = 0
        self.timeToBoost = 0
        self.isBoosted = False
        self.isBoostReady = True
        self.warning = ""

    def loadBoost(self):
        if not self.isBoosted and self.timeToBoost > 0:
            self.timeToBoost -= 1
        elif not self.isBoosted and self.timeToBoost == 0:
            self.isBoostReady = True

    def activateBoost(self):
        if not self.isBoosted and self.isBoostReady:
            self.box.addComment("Human has activated his ability MAGICAL POTION")
            self.boostTime = 5
            self.isBoosted = True
            self.isBoostReady = False
        else:
            message = "Ability not ready to use !"
            print(message)

    def fillWarning(self, warn):
        self.warning = warn

    @staticmethod
    def drawConsole():
        print("H", end=" ")

    def boost(self):
        if self.boostTime == 5:
            self.strength += self.boostTime
        elif self.boostTime >= 0 and self.isBoosted:
            self.strength -= 1

    def actionHuman(self, move):
        if self.isBoosted:
            self.boostTime -= 1
            if self.boostTime == 0:
                self.isBoosted = False
                self.timeToBoost = 5
        self.loadBoost()
        xMove = 0
        yMove = 0
        if move.key == pygame.K_SPACE:
            self.activateBoost()
        elif move.key == pygame.K_LEFT:
            xMove = -1
        elif move.key == pygame.K_RIGHT:
            xMove = 1
        elif move.key == pygame.K_UP:
            yMove = -1
        elif move.key == pygame.K_DOWN:
            yMove = 1
        self.boost()
        moved = Position(self.position.getX(), self.position.getY())
        moved.move(xMove, yMove)
        if moved.IsCorrect():
            if self.box.getOrganism(moved.getX(), moved.getY()) is None or self.box.getOrganism(moved.getX(),
                                                                                                moved.getY()) == self:
                self.position.setPosition(moved)
            else:
                npc = self.box.getOrganism(moved.getX(), moved.getY())
                self.collision(npc)
        self.ageing()

    def draw(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 14)
        icon = font.render(self.getIcon(), True, (255, 255, 255))
        screen.blit(icon, (30 + self.getX() * 10, 30 + self.getY() * 15))
        text = font.render("Special Ability :", True, (255, 255, 255))
        screen.blit(text, (40, 400))
        if self.isBoosted:
            text_2 = font.render("ON   Human strength: " + str(self.strength), True, (255, 0, 255))
            screen.blit(text_2, (170, 400))
        elif self.isBoostReady:
            text_2 = font.render("READY", True, (255, 255, 255))
            screen.blit(text_2, (170, 400))
        else:
            text_3 = font.render("NOT READY  Turns to boost: " + str(self.timeToBoost), True, (255, 0, 0))
            screen.blit(text_3, (170, 400))

    def setBoostTime(self, boostTime):
        self.boostTime = boostTime

    def GetOrganismsName(self):
        return "Human"

    def setTimeToBoost(self, timeToBoost):
        self.timeToBoost = timeToBoost