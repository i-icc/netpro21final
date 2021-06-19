import tkinter as tk
import socket
import time

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # ウィンドウタイトルを決定
        self.title("Tkinter change page")
        # ウィンドウの大きさを決定
        self.geometry("800x600")
        # ウィンドウのグリッドを 1x1 にする
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ホーム画面
        self.main_frame = tk.Frame()
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        # タイトル
        self.titleLabel = tk.Label(self.main_frame, text="アプリ名", font=('Helvetica', '35'))
        self.titleLabel.pack()
        # 接続ボタン
        self.changePageButton = tk.Button(self.main_frame, text="サーバーに接続する", command=lambda : self.connect())
        self.changePageButton.pack()

        # エラー画面
        self.error = tk.Frame()
        self.error.grid(row=0, column=0, sticky="nsew")
        # タイトル
        self.titleLabel = tk.Label(self.error, text="エラーが生じました", font=('Helvetica', '35'))
        self.titleLabel.pack()
        # ボタン
        self.changePageButton = tk.Button(self.error, text="ホームへ戻る", command=lambda : self.changePage(self.main_frame))
        self.changePageButton.pack()

        # ホーム画面表示
        self.changePage(self.main_frame)

    def connect(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.host = "localhost"
            self.port = 9999
            self.s.connect((self.host, self.port))
            msg = self.s.recv(1024).decode('ascii')
            self.field = self.s.recv(1024).decode('ascii')
            self.s.close()
            print(self.field)
            # ゲーム画面へ
            if msg == "0":
                print(msg,0)
                self.req()
            else:
                print(msg,1)
                self.rec()
        except Exception as e:
            print(e)
            self.changePage(self.error)

    def rec(self):
        # 待機画面
        self.rec_frame = tk.Frame()
        self.rec_frame.grid(row=0, column=0, sticky="nsew")
        # タイトル作成
        self.titleLabel = tk.Label(self.rec_frame, text=f"{self.field}", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # タイトル作成
        self.titleLabel = tk.Label(self.rec_frame, text=f"相手の行動を待っています。", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.field = self.s.recv(1024).decode('ascii')
        self.s.close()
        self.req()

    def req(self):
        # 行動選択画面
        self.req_frame = tk.Frame()
        self.req_frame.grid(row=0, column=0, sticky="nsew")
        # タイトル作成
        self.titleLabel = tk.Label(self.req_frame, text=f"{self.field}", font=('Helvetica', '35'))
        self.titleLabel.pack(anchor='center', expand=True)
        # 移動ボタン
        self.upButtun = tk.Button(self.req_frame, text="↑", command=lambda : self.send("u"))
        self.upButtun.pack()
        self.downButtun = tk.Button(self.req_frame, text="↓", command=lambda : self.send("d"))
        self.downButtun.pack()
        self.rightButtun = tk.Button(self.req_frame, text="→", command=lambda : self.send("r"))
        self.rightButtun.pack()
        self.leftButtun = tk.Button(self.req_frame, text="←", command=lambda : self.send("l"))
        self.leftButtun.pack()

    def send(self,comand):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        msg = self.s.send(f"{comand}".encode('ascii'))
        self.s.close()
        self.rec()

    def changePage(self, page):
        page.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()