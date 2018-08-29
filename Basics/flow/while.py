"""while構文で遊ぶ"""


"""通常"""
count = 0
while count < 5:
    print('count:', count)
    count += 1


"""ループを完全に抜けるbreak"""
num = 0
while num < 10:
    if num > 5:
        break
    print('num:', num)
    num += 1


"""ループをリセットするcontinue"""
number = 0
while number < 10:
    if number == 2:
        print('2は表示されない')
        number += 1
    print('number:', number)
    number += 1


"""while-else"""
count_again = 0
while count_again < 10:
    print('count_again:', count_again)
    count_again += 1
else:
    #elseをつけると、ループを抜けた時の処理をかける
    #ただし、breakで抜けた場合は実行されない
    print('DONE')
