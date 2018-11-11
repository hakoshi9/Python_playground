"""クロージャ"""
# クロージャは一見無意味な関数の記法に思うかもしれない
# クロージャは、事前に関数を宣言しておくための仕組み
# 利点として、関数を変数などに代入した時点では実行されないため、
# 今は使いたくないがあとで関数を実行したい時などに使う
# 例えば、最初に引数で固定値として何かを渡す
# → その後、その固定値を使った関数を実行できる
# 固定値を柔軟に決定する利点を得ながら、使用は後回しにできる利点も得られる
# ただし、裏を返せば関数を(実際は少し違うが)2回実行する必要がある
# 1回目) 変数などに関数を代入
# 2回目) その変数を関数として実行

# クロージャーの宣言
# def outter(あれば引数):
#     def inner(あれば引数):
#         return 処理
#     return inner
def closure_def(a, b):
    def inner():
        return a + b
    # 実行するのではなくinner関数のオブジェクトを返す
    return inner
# まずはouterを実行
f = closure_def(1, 2) # この時点ではinnerは実行されない
# ここで初めて実行される
r = f()
print("closure_def()の実行:", r)
# どういうときに使うかというと、今は実行したくないけどあとで実行したいときなど


# [closerの例]
print('クロージャ―の例------------------')
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area
cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)
print('cal1:', cal1(17))
print('cal2:', cal2(17))