'''カジノの入り口機能
   ここで実際のカジノゲームを呼び出す
   ゲームの選択等もここでやる'''
from .Blackjack import blackjack


class Casino():
    
    def __init__(self):
        print("I'm at the casino.py")
    
    def casino(self, model):
        game_choosed = True
        print('カジノへようこそ！')
        print('どのゲームを遊びたいか選んでね！')
        print('''''')

        while(game_choosed):
            print('現在の所持金:', model.money)
            game_to_play = int(input('[1.ブラックジャック    2.ルーレット(実装中)    3.ポーカー(実装中)    4.カジノを去る]'))


            if game_to_play == 1:
                blackjack.Blackjack().play_blackjack(model)
            elif game_to_play == 2:
                print('カジノのこの部分はまだ実装してないよ！別のゲームで遊んでね！')
            elif game_to_play == 3:
                print('カジノのこの部分はまだ実装してないよ！別のゲームで遊んでね！')
            elif game_to_play == 4:
                print('またカジノへお越しください！')
                game_choosed = False
            else:
                print('残念ながら選択肢を間違えたようです、もう一度入力してください')

        '''カジノで遊んだプレイヤーを返す
        while文を抜けないで返すとカジノのループを止めてしまう'''
        return model