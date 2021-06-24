class Player():
    def __init__(self,num):
        self.x = 0
        self.y = 0
        self.num = num

class Game():
    def __init__(self):
        self.p1 = Player(0)
        self.p2 = Player(1)
        self.turn = 10
        self.field = [[1,0,2,0],[0,0,0,0],[1,0,1,0],[0,0,1,0]]
    
    def dump(self):
        r = ""
        r += str(len(self.field))
        r += str(len(self.field[0]))
        for y in self.field:
            for x in y:
                r += str(x)
        return r
    
    def load(r):
        li = list(map(int,list(r)))
        h = li[0]
        w = li[1]
        f = li[2:]
        fie = []
        for y in range(h):
            fie.append([])
            for x in range(w):
                fie[y].append(f[y * w + x])
        
        for y in fie:
            for x in y:
                a = "⬜"
                if x == 1:
                    a = "🟨"
                elif x == 2:
                    a = "🔯"
                print(a,end="")
            print()

if __name__=="__main__":
    game = Game()
    d = game.dump()
    Game.load(d)