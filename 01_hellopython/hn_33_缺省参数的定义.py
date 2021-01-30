

def print_info(name, gender=True):
    """

    :param name: 同学的名字
    :param gender: True 默认男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


print_info("小明")
print_info("小美", False)