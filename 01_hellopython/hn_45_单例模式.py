class MusicPlayer(object):

    # 定义类属性记录单例对象引用
    instance = None

    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1.如果第一次创建对象就分配空间
        if cls.instance is None:
            cls.instance =  super().__new__(cls)


        # 2.以后再创建对象把第一次的内存返回就可以
        return cls.instance

    # 初始化方法也执行一次
    def __init__(self):

        if not MusicPlayer.init_flag:
            print("初始化音乐播放器")

            MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)