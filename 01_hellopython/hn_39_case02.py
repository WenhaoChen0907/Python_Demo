class HouseItem:

    def __init__(self, name, area):

        self.name = name

        self.area = area

    def __str__(self):

        return "%s 的占地面积是 %.2f " % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type

        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具列表
        self.item_list = []

    def __str__(self):

        return ("户型：[%s]\n 总面积：[%.2f](剩余面积:%.2f)\n 家具:%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):

        print("添加了 %s " % item)

        # 1.判断家具的面积是否超过剩余房屋面积
        if item.area > self.free_area:

            print("%s 太大了，放不下..." % item.name)

            return

        # 2.添加到家具列表
        self.item_list.append(item.name)

        # 3.计算剩余的面积
        self.free_area -= item.area


# 1.创建家具

bed = HouseItem("席梦思", 4)

chest = HouseItem("衣柜", 2)

table = HouseItem("餐桌", 1.5)

print(bed)
print(chest)
print(table)

# 2.创建房子

my_house = House("两室一厅", 60)

my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)