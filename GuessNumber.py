# # print("hello world")
#
# x=1
# while x < 100:
#     print(x)
#     x += 1
from random import randint

a = int(input("请输入最小数"))
b = int(input("请输入最大数"))

num1 = randint(a, b)
# print(num1)
score = 0
while True:
    num2 = int(input("请输入%d到%d之间的数字:" % (a, b)))
    score = +1
    if num2 > num1:
        print("大了大了")
    elif num2 < num1:
        print("小了小了")
    else:
        print("答对了")
        break
print("游戏结束恭喜得分:", score)



