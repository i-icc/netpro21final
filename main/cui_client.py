import socket
from game import Game

class App():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 9999
        try:
            self.s.connect((self.host, self.port))
            msg = self.s.recv(1024).decode('ascii')
            print(f"あなたはプレイヤー {msg} です。")
            print("対戦相手を待っています...")
            self.field = self.s.recv(1024).decode('ascii')
            if msg == "1":
                print("あなたは後手です。")
                self.waiting()
            else:
                print("あなたは先手です。")
                self.move()
        except:
            print("接続エラーが生じました")
            exit()

    def waiting(self):
        Game.load(self.field)
        print("相手の行動を待っています。")
        self.field = self.s.recv(1024).decode('ascii')
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
        self.s.close()


if __name__ == "__main__":
    app = App()