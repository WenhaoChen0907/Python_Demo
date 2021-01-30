# 第一次打开 文件时，通常 文件指针会指向文件的开始位置
# 当执行了 read 方法后，文件指针 会移动到 读取内容的末尾
# 默认情况下会移动到 文件末尾

# 1.打开文件
file = open("README")

# 2.读取文件
text = file.read()
print(text)
print(len(text))


print("-" * 50)


text = file.read()
print(text)
print(len(text))

# 3.关闭文件
file.close()