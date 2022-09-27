import random
print("問題:")
question_list = [0, 1, 2]
question_number = random.choice(question_list)

if (question_number == 0):
    print("サザエの旦那の名前は？")
elif (question_number == 1):
    print("カツオの妹の名前は？")
else:
    print("タラオはカツオから見てどんな関係？")
    
def check_answer():
    answer = input("解答を入力してください:") 
    answer_list0 = ["ますお", "マスオ"]
    answer_list1 = ["ワカメ", "わかめ"]
    answer_list2 = ["甥", "おい", "甥っ子", "おいっこ"]
    print("答えのチェックをします")
    if (question_number == 0):
        if (answer in answer_list0):
            return "正解"
        else:
            return "不正解"
    elif (question_number == 1):
        if (answer in answer_list1):
            return "正解"
        else:
            return "不正解"
    else:
        if (answer in answer_list2):
            return "正解"
        else:
            return "不正解"   
true_or_false = check_answer()
print(true_or_false)
