"""入れ子"""
#ifのなかにもifを入れて、より細かい分岐を作ることができる
#利点として、ifの条件分岐を続けることができる
#難点として、階層が深くなるとコードが読みづらくなってしまうこと
a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is also positive')



"""検索inとnot"""
#in演算子を使った要素の検索
#notは逆
#英語的に使えるので初心者にもとっつきやすい演算子の1つであると言える
my_name = 'Foo Bar'
if 'e' in my_name:
    print("There is a letter 'e' in my name")
elif 'e' not in my_name:
    print("There is not a letter 'e' in my name")



"""論理演算子の結合"""
#条件式を数学的範囲で表す時
#結構便利
num = 22
if 13 <= num <= 19:
    print('I am a teenager')
elif 20 <= num <= 29:
    print("I'm in my 20's")
elif 30 <= num <= 39:
    print("I'm in my 30's")
else:
    print('too old for you')