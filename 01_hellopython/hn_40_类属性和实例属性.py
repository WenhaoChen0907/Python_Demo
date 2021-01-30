# 类属性 就是给 类对象 中定义的 属性
# 通常用来记录 与这个类相关 的特征
# 类属性 不会用于记录 具体对象的特征


class Tool(object):

    # 定义类属性使用赋值语句即可
    count = 0

    def __init__(self, name):

        # 这是实例属性
        self.name = name

        # 利用类属性记录创建了多少个实例
        Tool.count += 1


shuitong = Tool("水桶")
chanzi = Tool("铲子")

# 知道使用 Tool 类到底创建了多少个对象?（调用类属性）
print(Tool.count)