'''ルーレットで使う計算機能

現在いろいろ触ってまわっている  2018/7/27'''
from random import randint


class Roulette_calculator():

    def __init__(self):
        self.roulette_numbers = [
                                    ['0', '1', '3', '5', '7', '9', '12', '14', '16', 
                                     '18', '19', '21', '23', '25', '27', '30', '32', '34', '36'],
                                    ['00', '2', '4', '6', '8', '10', '11', '13', '15', 
                                     '17', '20', '22', '24', '26', '28', '29', '31', '33', '35']
                                ]
        self.red_table = {1: '1', 2: '3', 3: '5', 4: '7', 5: '9', 6: '12', 7: '14', 8: '16', 9: '18', 
                          10: '19', 11: '21', 12: '23', 13: '25', 14: '27', 15: '30', 16: '32', 17: '34', 18: '36'}
        self.black_table = {1: '2', 2: '4', 3: '6', 4: '8', 5: '10', 6: '11', 7: '13', 8: '15', 9: '17', 
                            10: '20', 11: '22', 12: '24', 13: '26', 14: '28', 15: '29', 16: '31', 17: '33', 18: '35'}



    def lottery(self):
        '''当選番号を返す関数'''
        red_or_black = randint(0,1)
        number = randint(0, 18)

        return self.roulette_numbers[red_or_black][number]



    def player_choice(self):
        '''プレイヤーがどこに賭けるかを選ぶ機能'''
        choose_color = int(input('まず賭けたい色を選択してください\n1.0    2.00    3.赤    4.黒'))
        
        if choose_color == 1:
            print(self.roulette_numbers[0][0])
        elif choose_color == 2:
            print(self.roulette_numbers[1][0])
        elif choose_color == 3:
            red_numbers = [print(i) for i in self.red_table.values]
            pick_number = input('赤のどれを選ぶ？')
            print('あなたが選んだ数字: 赤・{0}'.format(pick_number))
        elif choose_color == 4:
            black_numbers = [print(i) for i in self.black_table.values]
            pick_number = input('黒のどれを選ぶ？')
            print('あなたが選んだ数字: 黒・{0}'.format(pick_number))






if __name__ == '__main__':
    roulette = Roulette_calculator()
    print(roulette.lottery())
    red = [print(value) for key, value in roulette.red_table.items()]
    black = [print(value) for key, value in roulette.black_table.items()]
    red
    black