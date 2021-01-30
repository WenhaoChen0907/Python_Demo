# 元组和列表之间的转换
# 注意：这两个函数不会修改原有的变量类型，而是返回一个新的变量
# 使用 list 函数可以把元组转换成列表
# list(元组)
info_tuple = (1, 1.25)
info_list = list(info_tuple)
print(info_tuple)
print(info_list)
# 使用 tuple 函数可以把列表转换成元组
# tuple(列表)