#! /usr/bin/python3

import  card_tools

while True:

    # TODO(小明) 显示功能菜单
    card_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            card_tools.new_card()
        # 显示全部
        elif action_str == "2":
            card_tools.show_all()
        # 查询名片
        elif action_str == "3":
            card_tools.search_card()

        # 如果在开发中，不希望立刻编写分支内部代码，可以用pass关键字占位
        # 程序运行时，pass关键字不会执行任何操作
        # pass
    # 0退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
        # pass
    # 其他内容输入错误，提示用户
    else:
        print("您输入的不正确，请重新选择")