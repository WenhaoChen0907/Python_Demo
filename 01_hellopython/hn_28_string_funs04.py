# 将字符串hello word输出为word hello
temp_str = "hello word"
# 1.将字符串以空白符为分割符分割
temp_list = temp_str.split()
print(temp_list)
# 2.反转列表元素
temp_list.reverse()
print(temp_list)
# 3.以空白符为连接符连接字符串
print(" ".join(temp_list))