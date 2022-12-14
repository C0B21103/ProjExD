import tkinter as tk
import tkinter.messagebox as tkm


def click_number(event): #イベント発生時に呼び出される関数(ここでは左クリック)
    btn = event.widget #btnはウィジェットを表す
    num = btn["text"] #numはさらにそのウィジェットのテキスト属性の値を表す
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num) #位置に文字列を挿入、tkinter.ENDで位置を入力欄の末尾にする

def click_equal(event): #イベント発生時に呼び出される関数(ここではイコールボタンが押されたとき)
    eqn = entry.get() #入力された式を参照
    res = eval(eqn) #式を計算(四則演算が可能な事は確認済み)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)
root = tk.Tk() # Tk()ウィンドウウィジェットの作成
root.geometry("300x500")#インスタンスメソッド、ウィンドウのサイズを設定する

def click_c(event):
    entry.delete(0, tk.END)
    
def click_percent(event):
    pe = int(entry.get())
    peres = pe * 0.01
    entry.delete(0, tk.END)
    entry.insert(tk.END, peres)
    
#テキスト入力欄
r, c = 0, 0
entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
#width:入力文字数（半角）で入力欄の幅を指定、justify = rightで右寄せで表示
entry.grid(row=0, column=0, columnspan=3)
#grid(行数,列数):行数と列数を指定して配置する
#columnspanを指定し複数の列にまたがってウィジェット(ここでは入力欄)を配置

#0~9のボタン
r, c = 1, 0 # r: 行を表す変数／c：列を表す変数
#numbers = list(range(9, -1, -1)) #[9,8,7,6,5,4,3,2,1,0]のリストを作成
#operators = ["+","-","*","/"] #演算子のリスト
BUTTON=[
    ["(", ")", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["C", "0", "."]
]

for i in BUTTON:
    for j in range(len(i)):
        num = i[j]    
        btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
        if (num == "C"):
            btn.bind("<1>", click_c)
        elif (num == "%"):
            btn.bind("<1>", click_percent)
        else:
            btn.bind("<1>", click_number)
        btn.grid(row=r, column=c)
        c += 1
        if j == 3:
            r += 1
            c = 0

btn = tk.Button(root, text = f"=", font=("", 30), width = 4, height = 2)
btn.bind("<1>", click_equal)
btn.grid(row = r, column = c)
root.mainloop()
if __name__ == '__main__':
    root()