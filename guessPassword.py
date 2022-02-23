password = "a123456"
i = 3
while i > 0 :
    i = i - 1
    pwd = input("你有三次機會 請輸入正確密碼 :")
    if pwd == password :
        print("登入成功")
        break
    else:
        print("密碼錯誤")
        if i > 0 :
            print("還有", i , "次機會")
        else:
            print("密碼3次全部錯誤, 沒機會嘗試了 !")
