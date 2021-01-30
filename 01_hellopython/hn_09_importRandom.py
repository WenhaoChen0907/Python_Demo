# 导入工具包
import random

# 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请输入要出的拳 石头（1）／剪刀（2）／布（3）："))
# 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
# computer = 1
# 使用整数随机函数
computer = random.randint(1, 3)

# 显示玩家和电脑出的拳
print("玩家出 %d -- 电脑出 %d " % (player, computer))
# 比较胜负
# 1	石头 胜 剪刀
# 2	剪刀 胜 布
# 3	布 胜 石头
# 玩家胜利的条件
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("电脑输了")

# 平局
elif player == computer:
    print("平局")

else:
    print("玩家输了")