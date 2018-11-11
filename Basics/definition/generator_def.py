"""ジェネレータ"""
# ジェネレーターは、一回一回処理を行うための関数
# 処理を一回一回止めて行うことができるため、処理の途中で別の処理を挟みたいときなどに使用する
# yieldを記述しているとPythonはジェネレータとして扱う

aisatsu = ['Good morning', 'Good afternoon', 'Good night']
def greeting():
    # 要素を一個一個生成するのがジェネレーター
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

for i in greeting():
    print('ジェネレーターの実行:', i)
g = greeting()
print('１つずつ表示される:', next(g))
print('@@@@@@@@@@@')
print('１つずつ表示される:', next(g))
print('@@@@@@@@@@@')
print('１つずつ表示される:', next(g))

def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# 一気に処理をするのではなく、yieldで一回一回処理を呼び出す。
# 一気に処理をせずに一回一回処理を施したい時に使う