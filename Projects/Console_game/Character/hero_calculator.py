'''プレイヤーで使う各種計算用'''

import random

def attack_random():
    return random.randint(5, 15)


def defense_random(atk):
    if atk < 8:
        return atk + 10
    else:
        return 10


def luck_random():
    return random.randint(0, 10)
