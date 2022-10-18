from itertools import cycle
import tkinter as tk
#maze_makerモジュールは迷路を生成するためのモジュール
import maze_maker

root = tk.Tk()
root.title("迷えるこうかとん")
root.geometry("1500x900")
#キャンバスエリア
canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
#塗りつぶし
#canvas.create_rectangle(0, 0, 1500, 900, fill = 'black')
#キャンバス配置
canvas.place(x=0, y=0)

#maze_makerモジュールは迷路を生成するためのモジュール
#maze_makerモジュールのmake_maze関数を呼び出す
#第一引数：横方向のマス数、第二引数：縦方向のマス数
#戻り値：第一引数ｘ第二引数の二次元リスト、要素「１」は壁で「０」は床を意味する
build = maze_maker.make_maze(15, 9)     
maze_maker.show_maze(canvas, build)

#こうかとんの画像のインスタンスを生成
tori = tk.PhotoImage(file = "ex03/fig/0.png")
#グローバル変数cx,cyは，こうかとんの現在地を表す変数である
#cxは横座標,cyは縦座標
global cx, cy
cx, cy = 300, 400
#Canvasにおける横：300，縦：400䛾座標に表示
canvas.create_image(cx, cy, image = tori, tag = "tori")

#変数keyを空文字""で初期化する
key = ""

#keysymで押されたキーの値を取得する
#main_proc関数は矢印キーが入力されたときにのみ処理される
def key_down(event):
    key = event.keysym
    main_proc(key)
#KeyPressイベントと紐づけ
root.bind("<KeyPress>", key_down)

#どのキーも押されていない時に呼び出す
def key_up(event):
    key = ""
#KeyReleaseイベントと紐づけ    
root.bind("<KeyRelease>", key_up)

#押された矢印キーによって画像を移動させる関数
#ウィンドウの端に来たら止まるようにする
def main_proc(key):
    global cx, cy
    if (key == "Up"):
        if(cy != 0):
            cy -=20
            canvas.coords("tori", cx, cy) 
    elif (key == "Down"):
        if(cy !=900):
            cy += 20
            canvas.coords("tori", cx, cy) 
    elif (key == "Left"):
        if(cx != 0):
            cx -= 20
            canvas.coords("tori", cx, cy) 
    elif (key == "Right"):
        if(cx != 1500):
            cx += 20
            canvas.coords("tori", cx, cy)     


root.mainloop()