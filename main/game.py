class Game():
    def __init__(self):
        self.p1 = Player(0)
        self.p2 = Player(1)


class Player():
    def __init__(self,num):
        self.x = 0
        self.y = 0
        self.num = num