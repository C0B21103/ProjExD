from itertools import cycle
import tkinter as tk
import tkinter.messagebox as tkm
#maze_makerモジュールは迷路を生成するためのモジュール
import maze_maker
import sys



global mx, my, build, canvas, root, cx, cy, times
times = 1

root = tk.Tk() #ウィンドウを生成
root.title("迷えるこうかとん") #タイトル名
root.geometry("1500x900") #ウィンドウのサイズ
def initmake():
    global build, canvas, root, cx, cy, mx , my    

    #キャンバスエリア
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")

    #キャンバス配置
    canvas.place(x=0, y=0)

    #maze_makerモジュールは迷路を生成するためのモジュール
    #maze_makerモジュールのmake_maze関数を呼び出す
    #第一引数：横方向のマス数、第二引数：縦方向のマス数
    #戻り値：第一引数ｘ第二引数の二次元リスト、要素「１」は壁で「０」は床を意味する
    build = maze_maker.make_maze(15, 9)     
    maze_maker.show_maze(canvas, build)

    #塗りつぶし
    canvas.create_rectangle(100, 100, 200, 200, fill = 'green')
    canvas.create_rectangle(1300, 700, 1400, 800, fill = 'red')

    #こうかとんの画像のインスタンスを生成
    tori0 = tk.PhotoImage(file = "ex03/fig/0.png")

    #グローバル変数cx,cyは，こうかとんの現在地を表す変数である
    #cxは横座標,cyは縦座標
    #global cx, cy
    #cx, cy = 300, 400
    #Canvasにおける横：300，縦：400䛾座標に表示
    mx = 1
    my = 1
    cx = mx * 150
    cy = my * 150
    canvas.create_image(cx, cy, image = tori0, tag = "tori0")


    #変数keyを空文字""で初期化する
    key = ""
    #KeyPressイベントと紐づけ
    root.bind("<KeyPress>", key_down)
    
    #KeyReleaseイベントと紐づけ    
    root.bind("<KeyRelease>", key_up)
    
    root.mainloop()
#keysymで押されたキーの値を取得する
#main_proc関数は矢印キーが入力されたときにのみ処理される
def key_down(event):
    key = event.keysym
    if times >= 3:
        temp_proc(key)
    else:
        main_proc(key)


#どのキーも押されていない時に呼び出す
def key_up(event):
    key = ""


#押された矢印キーによって画像を移動させる関数
#移動先が床(buildの要素が「0」の時)ならば移動する
#ウィンドウの端に来たら止まるようにする
def main_proc(key):
    global cx, cy, mx, my, times
    if (key == "Up"):
        if(my != 0):
            if (build[my - 1][mx] == 0):
                my -= 1
                cy =50 + my * 100
                canvas.coords("tori0", cx, cy) 
    elif (key == "Down"):
        if(my !=8):
            if (build[my + 1][mx] == 0):
                my += 1
                cy = 50 + my * 100
                canvas.coords("tori0", cx, cy) 
    elif (key == "Left"):
        if(mx != 0):
            if (build[my][mx - 1] == 0):
                mx -= 1
                cx = 50 + mx * 100
                canvas.coords("tori0", cx, cy) 
    elif (key == "Right"):
        if(mx != 14):
            if (build[my][mx + 1] == 0):
                mx += 1
                cx = 50 + mx * 100
                canvas.coords("tori0", cx, cy)     
    if (mx == 13):
        if (my == 7):
            times += 1
            ret = tkm.askyesno("クリアしました", "もう一度遊びますか？")
            if ret == False:
                sys.exit()
            else:
                canvas.delete("all")
                initmake()
                
def temp_proc(key):
    global cx, cy, mx, my, times
    if (key == "Up"):
        if(my != 0):
            if (build[my + 1][mx] == 0):
                my += 1
                cy =50 + my * 100
                canvas.coords("tori0", cx, cy) 
    elif (key == "Down"):
        if(my !=8):
            if (build[my - 1][mx] == 0):
                my -= 1
                cy = 50 + my * 100
                canvas.coords("tori0", cx, cy) 
    elif (key == "Left"):
        if(mx != 0):
            if (build[my][mx + 1] == 0):
                mx += 1
                cx = 50 + mx * 100
                canvas.coords("tori0", cx, cy) 
    elif (key == "Right"):
        if(mx != 14):
            if (build[my][mx - 1] == 0):
                mx -= 1
                cx = 50 + mx * 100
                canvas.coords("tori0", cx, cy)     
    if (mx == 13):
        if (my == 7):
            times += 1
            ret = tkm.askyesno("クリアしました", "もう一度遊びますか？")
            if ret == False:
                sys.exit()
            else:
                canvas.delete("all")
                initmake()     
initmake()
