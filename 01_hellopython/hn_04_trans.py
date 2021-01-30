# 1.输入苹果的单价
price_str = input("请输入苹果的单价：")
# 2.输入苹果的重量
weight_str = input("请输入苹果的重量：")
# 3.计算苹果的总金额
# 注意转换变量为数字类型
price = float(price_str)
weight = float(weight_str)

money = price * weight

print("需要支付%.02f元" % money)
