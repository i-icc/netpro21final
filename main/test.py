import tkinter as tk

class Application(tk.Frame):
    def __init__(self):
        self.root = tk.Tk()
        self.make_display()

    def make_display(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("title")
        self.root.geometry("300x300")
        super().__init__(self.root)
        self.pack()

def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()