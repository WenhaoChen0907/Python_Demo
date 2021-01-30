# 因为字典是一个无序的数据集合，所以用print函数输出字典数据和定义字典时数据的顺序是
# 可能不一致的
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            }
# 1.查看
print(xiaoming["name"])
# 2.增加/修改
xiaoming["name"] = "小小明"
xiaoming["height"] = 1.70
# 3.删除
xiaoming.pop("age")
# 4.统计键值对数量
print(len(xiaoming))
# 5.合并字典
new_dit = {"girfriend": "小小美"}
xiaoming.update(new_dit)
# 6.清空字典
# xiaoming.clear()

print(xiaoming)