# + 运算符 和 extend方法、append方法的区别
# 1.+运算符 拼接后会生成一个新的列表，不会改变原列表，
# 而extend方法、append方法会改变原列表
print([1, 2] + [3, 4])
# 2.extend会把参数里面的元素追加到原列表
temp_list = [1, 2]
temp_list.extend([3, 4])
print(temp_list)
# 3.append会把参数当做一个整体追加到原列表
temp_list.append([5, 6])
print(temp_list)