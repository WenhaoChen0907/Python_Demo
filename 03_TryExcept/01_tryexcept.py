# 捕获异常的语法 及 异常的传递性
def demo1():
    return int(input("输入一个整数："))

def demo2():
    return demo1()


try:
    print(demo2())

except Exception as result:
    print("未知错误 %s" % result)