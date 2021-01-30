class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        print("分配空间...")

        return super().__new__(cls)

    def __init__(self):
        print("开始播放了")

player = MusicPlayer()

print(player)