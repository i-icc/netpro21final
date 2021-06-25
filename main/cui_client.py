import socket
from game import Game

class App():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 9999
        try:
            self.s.connect((self.host, self.port))
            self.p = int(self.s.recv(1024).decode('ascii'))
            print(f"あなたはプレイヤー {self.p} です。")
            print("対戦相手を待っています...")
            self.field = self.s.recv(1024).decode('ascii')
            if self.p == 1:
                print("あなたは後手(2P)です。")
                self.waiting()
            else:
                print("あなたは先手(1P)です。")
                self.move()
        except Exception as e:
            print("接続エラーが生じました",e)
            exit()

    def waiting(self):
        Game.load(self.field)
        print("相手の行動を待っています。")
        msg = self.s.recv(1024).decode('ascii')
        if msg[:4] == "flag":
            self.game_end()
        self.field = msg
        self.move()
        
    def move(self):
        Game.load(self.field)
        comand = None
        while True:
            comand = input("行動してください(u:up d:down r:right l:left):")
            if comand not in ["u","d","r","l"]:
                print("{u, d, r, l} の中から選んでください")
            else:
                break
        self.s.send(f"{comand}".encode('ascii'))
        self.waiting()


    def game_end(self):
        print("ゲームは終了しました。")
        print("最終場面")
        self.field = self.s.recv(1024).decode('ascii')
        Game.load(self.field)
        score = [self.field[4:].count("1"),self.field[4:].count("2")]
        print(f"Score\n1P : 2P\n{score[0]:2} : {score[1]:2}")
        msg = "win" if score[self.p] > score[1 - self.p] else "lose"
        if score[0] == score[1]: msg = "draw"
        print("you " + msg)
        self.s.close()
        exit()


if __name__ == "__main__":
    app = App()