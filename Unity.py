import numpy
import requests
from bs4 import BeautifulSoup

class Human:
    def __init__(self):
        self.voice=[]
        attribute = ['soFree','CH圈','OP','米卫兵','独立女性','孙吧黄牌','神神','粉红','黄毛','精神小妹']
        self.attribute=numpy.random.choice(attribute)
        print('云从虎，风从龙，龙湖英雄傲苍穹')
    def walk(self):
        print('你走了，我们吃什么？')
    def Attack(self):
        print('强敌我斩，坚甲我摧')
    def compare(self):
        attribute = ['soFree', 'CH圈', 'OP', '米卫兵', '独立女性', '孙吧黄牌', '神神', '粉红', '黄毛', '精神小妹']
        attribute_sort=sorted(attribute, key=lambda x: 1 if x == '独立女性' else 2 if x == 'OP' else 3 if x == '米卫兵' else 4 if x == '孙吧黄牌' else 5 if x == '精神小妹' else 6 if x == '黄毛' else 7 if x == '神神' else 8 if x == 'soFree' else 9 if x == 'CH圈' else 10)
        print(attribute_sort)
    def shrimp_head_guy(self):
        response = requests.get("https://www.shift-journal.org/library")
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.get_text())

meteor_shower=Human()
meteor_shower.attribute,meteor_shower.voice='soFree', '萝莉音'

