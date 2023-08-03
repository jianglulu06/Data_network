# 飞机
class Airplan:
    # 名字
    name = ""
    # 颜色
    color = ""

    # self.变量名是类默认赋值的，方法里面的变量是传递的数据
    def set_color(self, color):
        self.color = color
        print(f"飞机的颜色是:{self.color}")

    def set_name(self, name):
        self.name = name
        print(f"飞机的名字是:{self.name}")


# 民用机（继承Airplan）
class CivilAirplan(Airplan):
    zhongliang = "1"

    def load_person(self, num):
        print(f"民用机载人数量为{num}")

    def set_name(self, name):
        print("民用机的set_name")


# 军用机
class JunYAirplan(Airplan):
    name = '军用机1'

    def set_name(self, name1):
        print(f"当前{self.name}名称：{name1}")


civilAir = CivilAirplan()
civilAir.set_color("民用机颜色：红色")
civilAir.load_person(100)
civilAir.set_name("民用机1号")
print(civilAir.zhongliang)

JunYair = JunYAirplan()
JunYair.set_name("军用机2号")

# air1 = Airplan()
# air1.set_name("第一架飞机")
# air1.set_color("蓝色")
#
# air2 = Airplan()
# air2.set_name("第二架飞机")
# air2.set_color("紫色")

