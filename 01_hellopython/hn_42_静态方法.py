# 如果一个方法内部 即不使用类属性、类方法，也不使用实例属性和方法
# 就可以定义为静态方法


class Dog(object):

    # 定义静态方法
    @staticmethod
    def run():

        print("小狗要跑...")


# 调用静态方法
Dog.run()