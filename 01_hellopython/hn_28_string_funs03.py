# 假设以下文本是从网络上抓取的（文本中有空白字符）
# 要求顺序并居中输出
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流\n",
        "欲穷千里目",
        "更上一层楼"]

for temp_str in poem:
    # 先使用strip方法去除两端空白字符
    # 再使用center方法对齐
    print("|%s|" % temp_str.strip().center(10, "　"))


