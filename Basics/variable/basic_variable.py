"""変数宣言で遊ぶ"""


"""複数の変数を一括でそれぞれに値を持たせる"""
num1, num2, num3 = 5, 7, 9
print('num1:', num1)
print('num2:', num2)
print('num3:', num3)



"""左辺の変数の数と右辺の値の数が合わないとエラーになる"""
# num1, num2, num3 = 100
# print(num1)
# print(num2)
# print(num3)



"""複数の変数に一括で同じ値を入れる"""
num4 = num5 = num6 = 100
print('num4:', num4)
print('num5:', num5)
num6 = 200
print('num6:', num6)



"""変数に*をつけると、変数の数より多い値はリストとなる"""
num7, *num8 = 1, 2, 3, 4, 5
print('num7:', num7)
print('num8:', num8) #1より先は全てリストとしてnum5に入る



"""１つの変数に,区切りの値を入れるとタプルとなる"""
num9 = 10, 11, 12
print('num9:', num9)



"""変数の複数宣言がクラスの__init__でもできるのか試す"""
class VarTest(object):
    def __init__(self):
        self.num10, self.num11 = 10, 20


var_test = VarTest()
print('num10:', var_test.num10)
print('num11:', var_test.num11)



"""これらは実際にコードを綺麗にするのが一概に目的ではない"""