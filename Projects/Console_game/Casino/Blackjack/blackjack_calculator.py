'''ブラックジャックの計算機能'''
import random

class Blackjack_calculator():

    '''呼ばれた時に空リスト3つ、そしてカードの配列を生成'''
    def __init__(self):
        self.__pointList_with_one = []
        self.__pointList_with_eleven = []
        self.__hand = []
        #self.__cards = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def rand_card(self):
        rand = random.randint(0, 12)
        #二つの値を戻す
        return [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][rand], rand


    '''カードをhitする関数'''
    def hit_card(self):
        #luck = random.randint(0, 12)

        try:
            #what_card = self.__cards[luck]
            #二つの変数に戻ってきた値をそれぞれ入れる
            what_card, luck = self.rand_card()
            self.__hand.append(what_card)
            if luck == 0:
                self.__pointList_with_one.append(1)
                self.__pointList_with_eleven.append(11)
            elif 1 <= luck <= 9:
                self.__pointList_with_one.append(luck+1)
                self.__pointList_with_eleven.append(luck+1)
            elif 10 <= luck <= 12:
                self.__pointList_with_one.append(10)
                self.__pointList_with_eleven.append(10)

        except Exception as e:
            print(e.args)


    '''配列のsumを渡す関数が必要かと思ったが、そういう配列はPythonにデフォルト
       で存在する("sum(list)")ため、特に必要ない
       
       ・・・・Javaはめんどくさいという証拠・・・・・'''


    def show_hand(self, model, who):
        if 'A' not in model.hands:
            sum_hand = sum(model.points_with_one)
            print("{0}の手:".format(who), model.hands, '', '合計', sum_hand)
        elif 'A' in model.hands:
            sum_ace_as_one = sum(model.points_with_one)
            sum_ace_as_eleven = sum(model.points_with_eleven)
            print("{0}の手:".format(who), model.hands, '', '合計', sum_ace_as_one, 'or', sum_ace_as_eleven)


    def hit_another_card(self, model, player, dealer, bit_money, continue_game):
        player.hit_card()
        player.show_hand(player, 'プレイヤー')
        if sum(player.points_with_one)>21:
            print('バスト！あなたの負けだ！')
            continue_game = False
        elif sum(player.points_with_one)<21:
            dealer.hit_card()
            dealer.show_hand(dealer, 'ディーラー')
            if sum(dealer.points_with_one)>21:
                print('あなたの勝ちだ！')
                model.money = bit_money*2
                continue_game = False


    def raise_money(self, model):
        pass


    def stand(self, model):
        pass



    def player_hit_card(self, player, dealer):
        player.hit_card()
        player.show_hand(player, 'プレイヤー')
        dealer.show_hand(dealer, "ディーラー")


    def dealer_hit_card(self, player, dealer):
        dealer.hit_card()
        player.show_hand(player, 'プレイヤー')
        dealer.show_hand(dealer, "ディーラー")





    '''handを取得するgetter'''
    @property
    def hands(self):
        return self.__hand

    # '''cardsを取得するgetter'''
    # @property
    # def cards(self):
    #     return self.__cards

    '''Aceが出た時、それを1とした時のリストを取得するgetter'''
    @property
    def points_with_one(self):
        return self.__pointList_with_one

    '''Aceが出た時、それを11とした時のリストを取得するgetter'''
    @property
    def points_with_eleven(self):
        return self.__pointList_with_eleven
