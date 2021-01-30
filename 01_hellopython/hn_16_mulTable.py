# 九九乘法表
i = 1
while i <= 9:

    col = 1
    while col <= i:
        # \t 制表符，可以使文本 垂直对齐
        print(" %d X %d = %d" % (i, col, (i * col)), end="\t")
        col += 1

    print("")
    i += 1