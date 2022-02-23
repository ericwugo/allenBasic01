import random
start = int(input("請輸入猜數字的開始整數值 :"))
end = int(input("請輸入猜數字的結尾整數值 :"))
r = random.randint(start, end)
count = 0
while True :
    count += 1
    num = int(input("請輸入所猜數字"))
    if num == r :
        print("恭喜 猜中了 !")
        print("這是你猜的第", count, "次")
        break
    elif num > r :
        print("比答案大點")
    elif num < r :
        print("比答案小點")


