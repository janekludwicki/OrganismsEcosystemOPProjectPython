
class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Position1(self):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setPosition(self, position):
        self.x = position.x
        self.y = position.y

    def move(self, xMove, yMove):
        self.x += xMove
        self.y += yMove

    def IsCorrect(self):
        if 0 <= self.x < 20 and 0 <= self.y < 20:
            return True
        return False
