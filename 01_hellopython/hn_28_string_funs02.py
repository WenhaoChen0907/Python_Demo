# 1.判断字符串中是否只包含空格（这里的空格还包含转义字符\t\r\n）
str1 = "   \t"
print(str1.isspace())

# 2.判断字符串中是否包含数字(不能用来判断小数)
str2 = "一千"

print(str2)
print(str2.isdecimal())  # 判断纯数字
print(str2.isdigit())  # 判断纯数字和unicode数字
print(str2.isnumeric())  # 判断纯数字和unicode数字和大写中文数字

# 3.检查字符串是否以*开头
str3 = "hello word"
print(str3.startswith("he"))
# 4.检查字符串是否以*结尾
print(str3.endswith("word"))
# 5.查找指定字符串
# index查找的字符串如果不存在会报错
# find查找字符串如果不存在会返回-1
print(str3.find("ab"))
# 6.替换字符串
# 注意：replace不会修改原变量，而是返回一个替换后的新变量
print(str3.replace("word", "python"))