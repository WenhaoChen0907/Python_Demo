# 计算 0 ~ 100 之间所有数字的累计求和结果
result = 0  # 保存求和结果

i = 0  # 定义计数器

while i <= 100:

    result += i  # 求和

    i += 1  # 处理计数器

print("0 ~ 100 之间所有数字的累计求和结果: %d " % result)