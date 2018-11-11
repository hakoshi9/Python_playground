"""関数内関数"""
# 関数の中に関数を定義することができる

def inner_def(a, b):
    def plus(c, d):
        return c + d
    # 関数内で関数内関数を実行する
    r = plus(a, b)
    print('inner_def()の実行 -> 中のplus()が動いている:', r)


inner_def(2, 5)