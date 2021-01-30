# 遍历 就是 从头到尾 依次 从 列表 中获取数据
# 在 循环体内部 针对 每一个元素，执行相同的操作
name_list = ["zhangsan", "lisi", "wangwu", "xiaomei", "lisi"]

for name in name_list:
    print("我的名字叫 %s " % name)