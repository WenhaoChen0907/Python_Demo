# 所有名片的列表
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("*" * 50)


def new_card():
    """新建名片"""
    print("===新建名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输出姓名：")
    phone_str = input("请输出电话：")
    qq_str = input("请输出qq：")
    email_str = input("请输出邮箱：")

    # 2.使用信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.将字典添加到列表
    card_list.append(card_dict)
    # print(card_list)
    # 4.提示用户添加成功
    print("添加%s的名片成功" % name_str)


def show_all():
    """显示所有名片"""
    print("===显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并返回
    if len(card_list) == 0:
        print("当前没有任何的名片记录")
        return

    # 1.打印表头
    for header in ["姓名", "电话", "QQ", "邮箱"]:
        print(header, end="\t\t")
    print("")

    # 2.打印分割线
    print("=" * 50)

    # 3.遍历输出名片
    for temp_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (temp_dict["name"],
                                        temp_dict["phone"],
                                        temp_dict["qq"],
                                        temp_dict["email"]))


def search_card():
    """搜索名片"""
    print("===搜索名片")

    # 1.提示用户输入要搜索的用户姓名
    find_name = input("请输入要搜索的姓名：")

    # 2.遍历所有名片，查询要搜索的姓名，如果没有找到提示用户

    for temp_dict in card_list:

        if temp_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (temp_dict["name"],
                                            temp_dict["phone"],
                                            temp_dict["qq"],
                                            temp_dict["email"]))
            # 针对找到的名片执行修改删除操作
            deal_card(temp_dict)

            break

    else:
        print("抱歉，没有找到 %s" % find_name)


def deal_card(find_card):
    """处理查找到的名片

    :param find_card: 找到的名片
    """
    # print(find_card)

    # 提示用户输入操作
    action_str = input("请输入您需要的操作 "
                       "【1】修改 【2】删除 【0】返回上级菜单:")

    # 修改名片
    if action_str == "1":

        find_card["name"] = input_card_info(find_card["name"], "新姓名【回车不修改】")
        find_card["phone"] = input_card_info(find_card["phone"], "新电话【回车不修改】")
        find_card["qq"] = input_card_info(find_card["qq"], "新QQ【回车不修改】")
        find_card["email"] = input_card_info(find_card["email"], "新邮箱【回车不修改】")

        print("修改名片成功！")

    # 删除名片
    elif action_str == "2":

        card_list.remove(find_card)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value: 字典中原有的值
    :param tip_message: 提示文字
    :return: 如果用户输入内容，返回内容，否则返回原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.根据用户输入进行判断，如果用户输入内容，返回结果
    if len(result_str) > 0:
        return result_str

    # 3.如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value

    # pass


