"""タプルで遊ぶ"""


"""タプルの宣言"""
tuple1 = 10, 20, 30
print('tuple1:',tuple1)


"""タプルのアンパック"""
tuple2 = (1, 2, 3, 4)
print('tuple2:', tuple2)
num1, num2, num3, num4 = tuple2
print('num1:', num1)
print('num2:', num2)
print('num3:', num3)
print('num4:', num4)


"""タプルの合計値"""
tuple3 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
sumTuple3 = sum(tuple3)
print('tuple3:', tuple3)
print('tuple3の合計値:', sumTuple3)