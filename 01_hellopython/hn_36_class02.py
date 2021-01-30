# 改造初始化方法，让创建对象更加的灵活
class Cat:

    def __init__(self, name):
        print("这是一个初始化方法")

        self.name = name

# 创建对象的同时，以参数的方式传递属性值


tom = Cat("TOM")


print(tom.name)

lazy_cat = Cat("蓝猫")

print(lazy_cat.name)