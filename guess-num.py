import random

r = random.randint(1,100)
count = 0
while True:
    count += 1 # count = count + 1
    num = input('請輸入猜測的數字(1~100): ')
    num = int(num)
    if num == r:
        print('你猜中了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('你猜的比答案大')
    elif num < r:
        print('你猜的比答案小')
    print('這是你猜的第', count, '次')