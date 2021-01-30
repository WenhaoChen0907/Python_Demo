# 一个类的属性可以是另一个类

class Gun:

    def __init__(self, model):

        # 枪的类型
        self.model = model

        # 枪的子弹数量默认是0
        self.bullet_count = 0

    def add_bullet(self, count):
        """装填子弹

        :param count: 装填数量
        """
        self.bullet_count += count

    def shoot(self):

        # 1.判断是否有子弹
        if self.bullet_count <= 0:

            print("%s 没子弹了.." % self.model)

            return

        # 2.子弹数量减一
        self.bullet_count -= 1

        # 3.提示发射了
        print("%s 突突突... 【%d】" % (self.model, self.bullet_count))

class Soldier:

    def __init__(self, name):

        # 1.士兵的姓名
        self.name = name

        # 2.士兵的枪-新兵没有枪
        self.gun = None

    def fire(self):

        # 1.判断士兵是否有枪
        if self.gun is None:

            print("%s 没有枪.." % self.name)

            return

        # 2.喊口号
        print("冲啊....【%s】" % self.name)

        # 3.装子弹
        self.gun.add_bullet(40)

        # 4.开枪
        self.gun.shoot()

# 1.创建枪对象
ak47 = Gun("AK47")

# 2.创建士兵
xusanduo = Soldier("许三多")

xusanduo.gun = ak47

xusanduo.fire()