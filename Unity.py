

import threading

import numpy
import requests
import itchat
from bs4 import BeautifulSoup


class Human:
    def __init__(self):
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
        self.attribute = numpy.random.choice(attribute)
        print("云从虎，风从龙，龙湖英雄傲苍穹")

    def walk(self):
        print("你走了，我们吃什么？")

    def Attack(self):
        print("强敌我斩，坚甲我摧")

    def compare(self):
        attribute = ['soFree', 'CH圈', 'OP', '米卫兵', '独立女性', '孙吧黄牌', '神神', '粉红', '黄毛', '精神小妹']
        attribute_sort = sorted(attribute, key=lambda
            x: 1 if x == '独立女性' else 2 if x == 'OP' else 3 if x == '米卫兵' else 4 if x == '孙吧黄牌' else 5 if x == '精神小妹' else 6 if x == '黄毛' else 7 if x == '神神' else 8 if x == 'soFree' else 9 if x == 'CH圈' else 10)
        print(f'从拉到夯{attribute_sort}')
    def YSQD(self):
        if self.attribute=='OP':
            print('米叠的恩情还不完')
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
class YourGirlFriend(Human):
    def __init__(self):
        super().__init__()

    def MeetYellowHair(self,name):
        self.Owner=name
        print(f'我是{name}大人的狗')

meteor_shower = Human()
meteor_shower.attribute, meteor_shower.voice = "soFree", "萝莉音"
meteor_shower.location = "library"

if hasattr(meteor_shower, "location") and meteor_shower.location == "library":
    print("家人们谁懂啊")
    setattr(meteor_shower, "down-head-man", True)
    del meteor_shower
    guaranteed_postgraduate_admission_elixir = True
    print("赢麻了")

def behave():
    a,b,c,d='牢魏','延庆区长','刘金³习²','🐔仲谋'
    if a and d:
        print(f'{a}，有没有吃的')
        print('我的🐔breast你吃不吃')
    if b in ['D1-308'] and [a,c] not in['D1-308']:
        print('🦌')
        print('石传说')
    if c and d:
        print(f'{d}')
        print(f'{c}纯human&chicken')
        
if 'attack_shift' in dir(meteor_shower) and threading.active_count() > 2:
    itchat.auto_login()
    rooms = itchat.get_chatrooms()
    for room in rooms:
        if '禁水群' in room['NickName']:
            room.send('我爱gx')
            break
