a=input("是否有钱坐公交？是/否？")
b=input("是否有座位？ 是/否？")
if a == "是":
    print("有钱坐公交")
    if b == "是":
        print("有座位，冲！")
    else:
        print("没座位，爬..")
else:
    print("没钱你上什么公交啊")