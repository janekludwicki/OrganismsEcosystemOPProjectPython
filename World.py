from Animals.CyberSheep import CyberSheep
from WorldBox import WorldBox
import Position
import pickle
import pygame
from Animals.Antelope import Antelope
from Animals.Fox import Fox
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.Turtle import Turtle
from Animals.Wolf import Wolf
from Plants.Belladonna import Belladonna
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.SosnowskyHogweed import SosnowskyHogweed
from Plants.SowThistle import SowThistle


class World:
    def __init__(self):
        self.box = WorldBox()
        self.box.addOrganism(Wolf(self.box, None))
        self.box.addOrganism(Sheep(self.box, None))
        self.box.addOrganism(Antelope(self.box, None))
        self.box.addOrganism(Fox(self.box, None))
        self.box.addOrganism(Turtle(self.box, None))
        self.box.addOrganism(Grass(self.box, None))
        self.box.addOrganism(SowThistle(self.box, None))
        self.box.addOrganism(Belladonna(self.box, None))
        self.box.addOrganism(SosnowskyHogweed(self.box, None))
        self.box.addOrganism(Guarana(self.box, None))
        self.box.addOrganism(Wolf(self.box, None))
        self.box.addOrganism(Sheep(self.box, None))
        self.box.addOrganism(Antelope(self.box, None))
        self.box.addOrganism(Fox(self.box, None))
        self.box.addOrganism(Turtle(self.box, None))
        self.box.addOrganism(Grass(self.box, None))
        self.box.addOrganism(SowThistle(self.box, None))
        self.box.addOrganism(Belladonna(self.box, None))
        self.box.addOrganism(SosnowskyHogweed(self.box, None))
        self.box.addOrganism(Guarana(self.box, None))
        self.box.addOrganism(CyberSheep(self.box, None))
        self.box.addOrganism(Human(self.box))
        self.number_of_turns = 0

    def getWorldBox(self):
        return self.box

    def drawWorld(self):
        print("Turn : " + str(self.number_of_turns) + "   Number of organisms: "
              + str(self.box.getNumberOfOrganisms()))
        for y in range(20):
            for x in range(20):
                organism = self.box.getOrganism(x, y)
                if organism is not None:
                    organism.drawConsole()
                else:
                    print(".", end=" ")
            print("\n")
        pygame.init()
        screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("Virtual World")
        screen.fill((0, 0, 0))
        i = 0
        while i < self.box.getNumberOfOrganisms():
            if self.box.organisms[i].getIsAlive() is True and self.box.organisms[i].getWasBuried() is False:
                self.box.organisms[i].draw(screen)
            i += 1
        comment_x = 380
        comment_y = 75
        font = pygame.font.SysFont("arialblack", 16)
        font2 = pygame.font.SysFont("comicsansms", 16)
        title = font.render("VIRTUAL WORLD", True, (255, 0, 0))
        screen.blit(title, (380, 25))
        title_comment = font.render("COMMENTARY:      Turn: " + str(self.getNumberOfTurns()) + "   Organisms: " +
                                    str(self.box.getNumberOfOrganisms()), True, (255, 0, 0))
        screen.blit(title_comment, (380, 50))
        border_horizontal = font2.render("______________________", True, (0, 255, 255))
        screen.blit(border_horizontal, (22, 0))
        screen.blit(border_horizontal, (22, 320))
        border_vertical = font2.render("|", True, (0, 255, 255))
        k = 0
        r = 20
        while k < 16:
            screen.blit(border_vertical, (21, r))
            screen.blit(border_vertical, (240, r))
            k += 1
            r += 20
        font = pygame.font.Font('freesansbold.ttf', 12)
        j = 0
        while j < len(self.box.commentary):
            comment = font.render(self.box.commentary[j], True, (255, 255, 255))
            screen.blit(comment, (comment_x, comment_y))
            comment_y += 16
            j += 1
        pygame.display.update()
        self.box.getCommentary().clear()

    def takeTurn(self, move):
        for i in range(len(self.getWorldBox().getList())):
            if self.getWorldBox().getList()[i].getIsAlive() and not self.getWorldBox().getList()[i].getWasBuried():
                if self.getWorldBox().getList()[i].getIcon() == 'H':
                    self.getWorldBox().getList()[i].actionHuman(move)
                else:
                    self.getWorldBox().getList()[i].action()
        self.box.buryDead()
        self.number_of_turns += 1
        self.drawWorld()

    def save(self, filename):
        with open(filename, 'wb') as save_file:
            pickle.dump(self.box, save_file)

    def load(self, filename):
        with open(filename, 'rb') as save_file:
            self.box = pickle.load(save_file)

    def getNumberOfTurns(self):
        return self.number_of_turns
