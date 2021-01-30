class Tool(object):

    # 定义类属性
    count = 0

    # 定义类方法
    @classmethod
    def show_tool_count(cls):

        print("工具对象的个数是 %d" % cls.count)

    def __init__(self, name):

        # 这是实例属性
        self.name = name

        # 利用类属性记录创建了多少个实例
        Tool.count += 1

futou = Tool("斧头")
dingpa = Tool("钉耙")

# 调用类方法
Tool.show_tool_count()
