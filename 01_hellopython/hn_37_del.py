# 当一个对象被销毁前，会自动调用__del__方法
# 如果希望在对象销毁前，再做一些事情，可以考虑该方法

class Cat:

    def __init__(self, name):

        self.name = name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 走了" % self.name)


tom = Cat("TOM")
print(tom.name)

print("-" * 50)
# 执行完所有的代码，系统才销毁对象，
# 所以先输出分割线，才调用__del__内置方法