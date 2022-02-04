import random

r = random.randint(1,100)

while True:
    num = input('請輸入猜測的數字(1~100): ')
    num = int(num)
    if num == r:
        print('你猜對了')
        break
    elif num > r:
        print('你猜的比答案大')
    elif num < r:
        print('你猜的比答案小')