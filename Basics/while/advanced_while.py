"""ループを完全に抜けるbreak"""
#while文内で、ある条件時に「break」をするとwhile文全体から抜けることができる
num = 0
while num < 10:
    if num > 5:
        break
    print('num:', num)
    num += 1




"""ループをリセットするcontinue"""
#「continue」は実行された段階でそのループを中断しループを最初から実行する
number = 0
while number < 10:
    if number == 2:
        #「2」は表示されない
        number += 1
        continue
    print('number:', number)
    number += 1




"""while-else"""
#while文に「for文」のようなelseをつけると、while文を抜けた時の処理を実装できる
count_again = 0
while count_again < 10:
    print('count_again:', count_again)
    count_again += 1
else:
    #ただし、while-elseの注意点としてbreakでwhile処理を抜けた場合はこのelseは実行されない
    print('DONE')
