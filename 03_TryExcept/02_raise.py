# 主动抛出异常
# 定义 input_password 函数，提示用户输入密码
# 如果用户输入长度 < 8，抛出异常
# 如果用户输入长度 >=8，返回输入的密码

def input_password():

    # 1.提示用户输入密码
    pwd = input("请输入密码：")

    # 2.判断密码长度 >= 8 返回用户输入密码
    if len(pwd) >= 8:
        return pwd

    # 3.如果< 8 主动抛出异常
    print("主动抛出异常")
    # 1>创建异常对象  - 可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")

    # 2>主动抛出异常
    raise ex

# 捕获异常
try:
    print(input_password())
except Exception as result:
    print(result)