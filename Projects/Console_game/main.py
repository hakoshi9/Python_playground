import random
from Character import hero
from Casino import casino
from Adventure import adventure
from Shop import shop


def show_status(model):
    print('あなたのステータス:')
    print('     名前:', model.name)
    print('     HP:', model.hp)
    print('     最大HP:', model.MAX_HP)
    print('     MP:', model.mp)
    print('     最大MP:', model.MAX_MP)
    print('     攻撃力:', model.attack)
    print('     防御力:', model.defense)
    print('     運:', model.luck)
    print('     所持金:', model.money)



if __name__ == '__main__':
    keep_playing = True
    print("I'm at the main.py")
    print('-----------------------------')
    print('勇者、ようこそこの地へ')
    name = input('まずあなたのお名前を教えてください')
    hero = hero.Hero(name=name)
    show_status(hero)


    print('それでは{0}様、この地で何がしたいですか？'.format(hero.name))

    while(keep_playing):
        what_to_do = int(input('[1.冒険(実装中)    2.カジノ    3.買い物(実装中)    4.ゲームをやめる]'))
        
        if what_to_do == 1:
            pass
        elif what_to_do == 2:
            casino.Casino().casino(hero)
            print('''他に何をしますか？''')
            show_status(hero)
        elif what_to_do == 3:
            pass
        elif what_to_do == 4:
            keep_playing = False


    print('この地を離れるのですか？')
    print('それでは気をつけて行ってください。またお越しください。')


    # casino = casino.Casino()

    # casino.casino(hero)

    # print("戻ってきたheroの所持金は:", hero.money)
