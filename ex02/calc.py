import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("ウィジェットの配置(grid)")     # ウィンドウタイトル
        self.master.geometry("300x500")       # ウィンドウサイズ(幅x高さ)

        #--------------------------------------------------------
        # ラベルの作成
        button1 = tk.Button(self.master, width = 4, height = 2, text = "1", font = ("Times New Roman", 30))
        button2 = tk.Button(self.master, width = 4, height = 2, text = "2", font = ("Times New Roman", 30))
        button3 = tk.Button(self.master, width = 4, height = 2, text = "3", font = ("Times New Roman", 30))
        button4 = tk.Button(self.master, width = 4, height = 2, text = "4", font = ("Times New Roman", 30))
        button5 = tk.Button(self.master, width = 4, height = 2, text = "5", font = ("Times New Roman", 30))
        button6 = tk.Button(self.master, width = 4, height = 2, text = "6", font = ("Times New Roman", 30))
        button7 = tk.Button(self.master, width = 4, height = 2, text = "7", font = ("Times New Roman", 30))
        button8 = tk.Button(self.master, width = 4, height = 2, text = "8", font = ("Times New Roman", 30))
        button9 = tk.Button(self.master, width = 4, height = 2, text = "9", font = ("Times New Roman", 30))
        button0 = tk.Button(self.master, width = 4, height = 2, text = "0", font = ("Times New Roman", 30))

        #--------------------------------------------------------
        # gridでウィジェットの配置
        button1.grid(row = 2, column = 2)
        button2.grid(row = 2, column = 1)
        button3.grid(row = 2, column = 0)
        button4.grid(row = 1, column = 2)
        button5.grid(row = 1, column = 1)
        button6.grid(row = 1, column = 0)
        button7.grid(row = 0, column = 2)
        button8.grid(row = 0, column = 1)
        button9.grid(row = 0, column = 0)
        button0.grid(row = 3, column = 0)
        #--------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()