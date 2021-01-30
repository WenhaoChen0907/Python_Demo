# 注意1：缺省参数必须放在多个参数末尾


def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 同学的名字
    :param gender: True 默认男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("【%s】%s 是 %s" % (title, name, gender_text))


print_info("小明")
# 注意2：只传递一个缺省参数，需要在值前面加上参数的名字，类似的有sort(reserve=True)是一个用法
print_info("小美", gender=False)