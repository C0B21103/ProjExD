import tkinter as tk

root = tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")
#キャンバスエリア
canvas = tk.Canvas(root, width = 1500, height = 900)
#塗りつぶし
canvas.create_rectangle(0, 0, 1500, 900, fill = 'black')
#キャンバス配置
canvas.place(x=0, y=0)
root.mainloop()