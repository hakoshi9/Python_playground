'''ブラックジャックのフィールド'''
from . import blackjack_calculator as blackjack_cal

class Blackjack():

    def __init__(self):
        
        self.bet_money = 0
        self.player = blackjack_cal.Blackjack_calculator()
        self.dealer = blackjack_cal.Blackjack_calculator()
        # 関数を実行せずに変数に代入することでその変数自体を関数として扱える
        self.player_hit_card = blackjack_cal.Blackjack_calculator().player_hit_card
        # 関数を実行せずに変数に代入することでその変数自体を関数として扱える
        self.dealer_hit_card = blackjack_cal.Blackjack_calculator().dealer_hit_card
        self.continue_game = True



    def play_blackjack(self, model):
        print('ブラックジャックへようこそ！')
        
        bet = int(input("まず、いくら賭けるか入力してください"))
        self.bet_money += bet
        model.money -= bet
        print('賭け金:', self.bet_money)
        print('残金:', model.money)

        for i in range(2):
            self.player.hit_card()
            self.dealer.hit_card()

        self.player.show_hand(self.player, "プレイヤー") # プレイヤーの手を表示する
        self.dealer.show_hand(self.dealer, "ディーラー") # ディーラーの手を表示する

        if sum(self.player.points_with_eleven) == 21:
            print('ブラックジャック！あなたの勝ちだ！')
            model.money += self.bet_money*3
            self.continue_game = False
        elif sum(self.dealer.points_with_eleven) == 21:
            print('ディーラーのブラックジャック！あなたの負けだ！')
            print('賭け金が2倍持っていかれた！')
            model.money -= self.bet_money
            self.continue_game = False



        print('まずはプレイヤーの動き')
        while self.continue_game:
            # プレイヤーがバストするかスタンドするまで動かす
            while True:
                action = int(input("[1.ヒット(もう一枚引く)    2.レイズ(賭け金を増やしてもう一枚引く)    3.スタンド(勝負する)]"))
                if action == 1:
                    self.player_hit_card(self.player, self.dealer)
                    if sum(self.player.points_with_one)>21:
                        self.continue_game = False
                        print('バスト！あなたの負けだ！')
                        break
                elif action == 2:
                    bet = int(input("いくら追加で賭けますか？"))
                    self.bet_money += bet
                    model.money -= bet
                    self.player_hit_card(self.player, self.dealer)
                    if sum(self.player.points_with_one)>21:
                        self.continue_game = False
                        print('バスト！あなたの負けだ！')
                        break
                elif action == 3:
                    break
                else:
                    print('必ず3つのうちの一つを選んでね！')

            # ここでFalseになった時点で
            if self.continue_game == False:
                break


            print('勝負！')
            # ディーラーの手が17を超えるまでカードを引く
            while sum(self.dealer.points_with_one)<17:
                self.dealer_hit_card(self.player, self.dealer)
                if sum(self.dealer.points_with_one)>21:
                    print('ディーラーバスト！あなたの勝ちだ！')
                    model.money += self.bet_money*2
                    self.continue_game = False
                    break

            player_sum_one = sum(self.player.points_with_one)
            player_sum_eleven = sum(self.player.points_with_eleven)
            dealer_sum = sum(self.dealer.points_with_one)

            if sum(self.dealer.points_with_one)>21:
                break


            if player_sum_one == dealer_sum:
                print('引き分けだ！')
                model.money += self.bet_money
                self.continue_game = False
            elif player_sum_eleven < dealer_sum or player_sum_one < dealer_sum:
                print('あなたの負けだ！')
                self.continue_game = False
            elif player_sum_one > dealer_sum or player_sum_eleven > dealer_sum:
                print('あなたの勝ちだ！')
                model.money += self.bet_money*2
                print('+{}ゴールド'.format(self.bet_money*2))
                self.continue_game = False


                
        
        
        # 渡されたmodelを返す
        return model








