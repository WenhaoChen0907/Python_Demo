name_list = ["zhangsan", "lisi", "wangwu", "xiaomei", "lisi"]

# len 函数，返回列表的长度
length = len(name_list)
print("长度为 %d " % length)

# count 方法，统计指定数据的次数
count = name_list.count("lisi")
print("出现了 %d 次" % count)

num_list = [8, 5, 1, 4, 20]
# sort方法 默认升序
# num_list.sort()

# 降序 sort(reserve=True) 降序
num_list.sort(reverse=True)

# 逆序（反转）
# num_list.reverse()

print(num_list)