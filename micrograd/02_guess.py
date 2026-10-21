secret = 71      # 你心里想的数（1 到 100），改这里
low = 1          # 范围的左边
high = 100       # 范围的右边
guess = 0
count = 0

while guess != secret:
    guess = (low + high) // 2      # 猜正中间
    count = count + 1
    if guess < secret:
        print(count, ":", guess, "小了")
        low = guess + 1
    elif guess > secret:
        print(count, ":", guess, "大了")
        high = guess - 1

print("猜中了！是", guess, "，一共猜了", count, "次")