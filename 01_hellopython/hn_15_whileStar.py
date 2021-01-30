# 输出小星星
# 方法一
"""
row = 1
while row <= 5:

    print("*" * row)

    row += 1
"""
# 方法二：循环嵌套
row = 1
while row <= 5:

    # 每一行打印的星星和当前行数是一致的
    # 增加一个循环，专门负责当前行中，每一列的星
    col = 1
    while col <= row:
        # print函数输出默认换行，想要去掉换行可以使用, end=""
        print("*", end="")
        col += 1

    # 一行打印完成时，添加换行
    print("")

    row += 1
