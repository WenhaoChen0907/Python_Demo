# 格式字符串，格式化字符串后面的 () 本质上就是一个元组

info_tuple = ("小明", 18, 1.75)

print("%s 的年龄是 %d 身高是 %.2f" % info_tuple)

# 拓展：格式字符串可以拼接生成新的字符串
info_str = "%s 的年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)