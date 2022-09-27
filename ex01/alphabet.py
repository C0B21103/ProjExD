import random
print("対象文字:")
chr_list = []
for i in range(10):
    chr_number = random.randint(65,90)
    chr_list += chr(chr_number)
    print(chr(chr_number), end = " ")

print('\n')
print("表示文字:")
x = 9    
for j in range(8):
    list_number = random.randint(0,x)
    x = x - 1
    print(chr_list.pop(list_number), end = " ")

print('\n')
print(len(chr_list))
#print("まだ完成してません")
flag_num = 0
while (flag_num == 0):
    answer = input("欠損文字はいくつあるでしょうか？:")
    if (len(chr_list) == answer):
        input("正解です。では、その欠損文字は？:")
        break
    else:
        print("不正解です。やりなおし。")