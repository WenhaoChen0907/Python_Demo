# 1.当函数有多个返回值时，可以使用元祖
def measure():
    """测量温度和湿度"""

    print("开始测量....")
    temp = 39
    wetness = 50
    print("开始结束....")

    # 元祖 可以包含多个数据，因此可以使用元祖让函数一次返回多个值
    # 在Python中，如果函数返回的是元祖，小括号建议省略
    # return (temp, wetness)
    return temp, wetness


# 2.在接收函数的返回值时，也类似使用多个变量同时接收
# 多个变量之间用逗号 分隔
# 注意：使用多个变量接收结果时，变量的个数应和元祖中元素个数一致
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)