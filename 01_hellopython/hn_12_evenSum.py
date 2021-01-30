# 计算 0 ~ 100 之间 所有 偶数 的累计求和结果
result = 0
i = 0

while i <= 100:

    # print(i)
    result += i
    i += 2

print("0 ~ 100 之间 所有 偶数 的累计求和结果: %d " % result)