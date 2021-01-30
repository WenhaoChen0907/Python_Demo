# +=运算符对于列表来说本质是在执行extend方法


def demo(num, num_list):

    print("函数内部代码")

    # num = num + num
    num += num

    # num_list.extend(num_list) 由于是调用方法，所以不会修改变量的引用
    # 函数执行结束后，外部数据同样会发生变化
    num_list += num_list

    print(num)
    print("函数内部%d 的地址是%d" % (num,id(num)))
    print(num_list)
    print("函数内部 的地址是%d" % id(num_list))
    print("函数代码完成")


gl_num = 9
gl_list = [1, 2, 3]
print("函数外部%d 的地址是%d" % (gl_num,id(gl_num)))
print("函数内部 的地址是%d" % id(gl_list))
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)