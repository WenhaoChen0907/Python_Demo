name_list = ["zhangsan", "lisi", "wangwu"]

# 1.查看
print(name_list[1])
# 查看已知数据的索引
print(name_list.index("lisi"))
# 2.修改
name_list[1] = "李四"
# 3.增加
# append在列表的末尾增加数据
name_list.append("小妹")
# insert在指定索引位置插入数据
name_list.insert(1, "孙二")
# extend 把列表temp_list的数据追加到列表中
temp_list = ["孙悟空", "猪八戒"]
name_list.extend(temp_list)

# 4.删除
# remove 删除指定数据
name_list.remove("孙二")
# pop 默认删除列表最后一个数据
name_list.pop()
# pop 删除对应索引的数据
name_list.pop(1)
# clear 删除列表所有数据
name_list.clear()

print(name_list)


