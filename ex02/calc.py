import tkinter as tk
import tkinter.messagebox as tkm


def click_number(event): # 練習3
    btn = event.widget
    num = int(btn["text"])
    #tkm.showinfo(f"{num}", f"{num}のボタンが押されました")
    entry.insert(tk.END, num)
root = tk.Tk() # 練習1
root.geometry("300x500")

r, c = 0, 0
entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 # r: 行を表す変数／c：列を表す変数
for i, num in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
root.mainloop()