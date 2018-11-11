

# 関数内関数
def innerDefinition(a, b):
    def plus(c, d):
        return c + d
    # 関数内で関数内関数を宣言する
    r = plus(a, b)
    print('innerDefinition()の実行。中のplus()が動いている:', r)


innerDefinition(2, 5)