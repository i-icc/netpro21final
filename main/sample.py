import tkinter as tk 

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.mainloop()
        self.make_display()

    def make_display(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("title")
        self.root.geometry("300x300")
        self.root.mainloop()

def main():
    app = App()

if __name__ == "__main__":
    main()