a = 6
b = 100

# 要求：交换两个数字

# 方法1 使用其他变量
# c = a
# a = b
# b = c

# 方法2 不使用临时变量
# a = a + b
# b = a - b
# a = a - b

# 方法 3  Python专有--利用元祖
# a, b = (b, a) 小括号可省略
a, b = b, a

print(a)
print(b)