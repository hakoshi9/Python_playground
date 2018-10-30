'''プレイヤー'''
import random
from . import hero_calculator as hero_cal

class Hero():

    def __init__(self, name):
        self.name = name
        self.MAX_HP = 100
        self.hp = 100
        self.MAX_MP = 50
        self.mp = 50
        self.attack = hero_cal.attack_random()
        self.defense = hero_cal.defense_random(self.attack)
        self.luck = hero_cal.luck_random()
        self.money = 100


    '''攻撃を指示する関数'''
    def attack_enemy(self):
        pass


    '''休憩を指示する関数'''
    def rest(self, sec):
        self.hp += sec
        if self.hp >= self.MAX_HP:
            self.hp = self.MAX_HP
        print(self.hp)



    '''アイテム使用を指示する関数'''
    def item(self):
        pass


    '''逃亡を指示する関数'''
    def run(self):
        pass



