import numpy
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