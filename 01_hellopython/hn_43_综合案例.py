# 类方法 实例方法 静态方法 的综合案例
class Game(object):

    # 游戏历史最高分
    top_score = 0

    def __init__(self, player_name):

        # 记录当前游戏的玩家姓名
        self.player_name = player_name

    @staticmethod
    def show_help():

        print("游戏帮助...")

    @classmethod
    def show_top_score(cls):

        print("历史最高分为 %d" % cls.top_score)

    def start_game(self):

        print("%s 开始游戏了..." % self.player_name)
        Game.top_score = 99


# 1.查看帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 3.开始游戏
wangzhe = Game("小明")
wangzhe.start_game()

# 4.再次查看历史最高分
Game.show_top_score()