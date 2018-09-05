
# 複数の変数を一括で宣言する
multi1, multi2, multi3 = 5, 7, 9
print('multi1:', multi1)
print('multi2:', multi2)
print('multi3:', multi3)



# 左辺の変数の数と右辺の値の数が合わないとエラーになる
# num1, num2, num3 = 100
# print(num1)
# print(num2)
# print(num3)



# 複数の変数に一つの値をいれる
same_val1 = same_val2 = same_val3 = 100
print('same_val1:', same_val1)
print('same_val2:', same_val2)
print('same_val3:', same_val3)

#ちゃんと個別に値が入っているかを確認
same_val1 = 50
same_val2 = 150
same_val3 = 250
print('same_val1に値を再代入:', same_val1)
print('same_val2に値を再代入:', same_val2)
print('same_val3に値を再代入:', same_val3)



# __init__で試す
class VarTest(object):
    def __init__(self):
        self.init1, self.init2 = 10, 20

var_test = VarTest()
print('init1:', var_test.init1)
print('init2:', var_test.init2)