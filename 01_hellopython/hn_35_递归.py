def sum_numbers(num):

    print(num)

    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return

    sum_numbers(num - 1)

    print("%d 完成" % num)

sum_numbers(3)