import threading
import numpy as np
import itchat
import requests
from bs4 import BeautifulSoup


class Human:
    def __init__(self,name):
        self.name=name
        self.voice = []
        attribute = [
            "soFree",
            "CH圈",
            "OP",
            "米卫兵",
            "独立女性",
            "孙吧黄牌",
            "神神",
            "粉红",
            "黄毛",
            "精神小妹",
        ]
        self.attribute = np.random.choice(attribute)
        print("云从虎，风从龙，龙湖英雄傲苍穹")

    def walk(self):
        print("你走了，我们吃什么？")
    def __repr__(self):
        return self.name
    def Attack(self):
        print("强敌我斩，坚甲我摧")

    def compare(self):
        attribute = [
            "soFree",
            "CH圈",
            "OP",
            "米卫兵",
            "独立女性",
            "孙吧黄牌",
            "神神",
            "粉红",
            "黄毛",
            "精神小妹",
        ]
        attribute_sort = sorted(
            attribute,
            key=lambda x: (
                1
                if x == "独立女性"
                else (
                    2
                    if x == "OP"
                    else (
                        3
                        if x == "米卫兵"
                        else (
                            4
                            if x == "孙吧黄牌"
                            else (
                                5
                                if x == "精神小妹"
                                else (
                                    6
                                    if x == "黄毛"
                                    else (
                                        7
                                        if x == "神神"
                                        else (
                                            8
                                            if x == "soFree"
                                            else 9 if x == "CH圈" else 10
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            ),
        )
        print(f"从拉到夯{attribute_sort}")

    def YSQD(self):
        if self.attribute == "OP":
            print("米叠的恩情还不完")

    def shrimp_head_guy(self):
        response = requests.get("https://www.shift-journal.org/library")
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup.get_text())

    def singel_attack_shift(self):
        while True:
            requests.get("https://www.shift-journal.org/library")
            print("发送1次请求")

    # 很刑的函数，不建议使用
    def attack_shift(self, thread_num):
        for i in range(thread_num):
            t = threading.Thread(target=self.singel_attack_shift)
            t.start
    def make(self):
        self.Attack()
        self.walk()


class YourGirlFriend(Human):
    def __init__(self,name="你的女友"):
        super().__init__(name)

    def MeetYellowHair(self, name):
        self.Owner = name
        print(f"我是{name}大人的狗")


def behave():
    a, b, c, d = "牢魏", "延庆区长", "刘金³习²", "🐔仲谋"
    if a and d:
        print(f"{a}，有没有吃的")
        print("我的🐔breast你吃不吃")
    if b in ["D1-308"] and [a, c] not in ["D1-308"]:
        print("🦌")
        print("石传说")
    if c and d:
        print(f"{d}")
        print(f"{c}纯human&chicken")
    return [a, b, c]

class dormitory:
    def __init__(self):
        self.equitment=['寝室门', '阳台门', '晾衣杆']
class D1_308(dormitory):
    def __init__(self):
        super().__init__()
        self.people = ['牢魏','蒋神',"延庆区长", "刘金³习²"]
        self.vistors=[]
        self.activity = ""
        self.sentences = [
            "对面纯轮椅",
            "累挺",
            "有人去打水吗",
            "哎呀！今天洛克王国还没打呢",
            "晾衣叉在你柜子里",
            "老蒋,打mc吗",
            "我今天有点累，不是很想打，但我没说我不打",
            "你阿诺吧",
            "烫烫烫",
            "锟斤拷",
        ]
        a=behave()
        a.append('MC阻塞器')
        for i in a:
            self.people.append(Human(i))
    def talk(self):
        for i in range(100):
            for j in range(len(self.sentences)):
                print(self.sentences[j])
    def vistor(self,person):
        self.vistors.append(person)
    def speak(self):
        behave()
        for i in range(10*len(self.people)):
            print(f'{np.random.choice(self.people)}:{np.random.choice(self.people+self.vistors)}{np.random.choice(self.sentences)}')
    def play_mc(self):
        print('91 tp White\nSEDEX gamemode creative\n')
        print('91 kill K '*99)
    def compare_credibility (self):
        print(f"{self.people[2]}>{self.people[0]}={self.people[1]}>>{self.people[3]}")


meteor_shower = Human("流星雨")
meteor_shower.attribute, meteor_shower.voice = "soFree", "萝莉音"
meteor_shower.location = "library"
d1_308=D1_308()
d1_308.speak()

def destroy(meteor_shower,d1_308):
    print(f'我真不知道{meteor_shower.name}把{d1_308.equitment[0]}弄坏对他有啥好处')
    print(f'我真不知道{meteor_shower.name}把{d1_308.equitment[1]}弄坏对他有啥好处')
    print(f'{meteor_shower.name}为啥把{d1_308.equitment[2]}放他柜子里')


if hasattr(meteor_shower, "location") and meteor_shower.location == "library":
    print("家人们谁懂啊")
    setattr(meteor_shower, "down-head-man", True)
    del meteor_shower
    guaranteed_postgraduate_admission_elixir = True
    print("赢麻了")


if "attack_shift" in dir(meteor_shower) and threading.active_count() > 2:
    itchat.auto_login()
    rooms = itchat.get_chatrooms()
    for room in rooms:
        if "禁水群" in room["NickName"]:
            room.send("我爱gx")
            break

