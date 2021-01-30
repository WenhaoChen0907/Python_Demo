class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # 在初始化方法内部定义 属性，
        # 这样创建的对象默认会有该属性
        self.name = "TOM"



# 因为创建对象时，会自动调用初始化方法
tom = Cat()

print(tom.name)