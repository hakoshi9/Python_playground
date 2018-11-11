

# クロージャー
def closerDefinition(a, b):
    def inner():
        return a + b
    # 実行するのではなくinner関数のオブジェクトを返す
    return inner
# まずはouterを実行
f = closerDefinition(1, 2) # この時点ではinnerは実行されない
# ここで初めて実行される
r = f()
print("closerDefinition()の実行:", r)
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