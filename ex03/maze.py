import tkinter as tk

root = tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")
#キャンバスエリア
canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
#塗りつぶし
#canvas.create_rectangle(0, 0, 1500, 900, fill = 'black')
#キャンバス配置
canvas.place(x=0, y=0)

#こうかとんの画像のインスタンスを生成
tori = tk.PhotoImage(file = "ex03/fig/0.png")
#グローバル変数cx,cyは，こうかとんの現在地を表す変数である
#cxは横座標,cyは縦座標
cx, cy = 300, 400
#Canvasにおける横：300，縦：400䛾座標に表示
canvas.create_image(cx, cy, image = tori, tag = "tori")
root.mainloop()