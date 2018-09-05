"""関数で遊ぶ"""


"""通常の宣言"""
def say_something():
    print('say_something()の実行:', 'hi')
say_something()



"""戻り値"""
def return_something():
    s = 'This text has been returned'
    return s
returned = return_something()
print('return_something()の実行:', returned)



"""引数"""
#[通常]
def what_is_this(color):
    print("what_is_this('{}')の実行:".format(color), color)
what_is_this('red')

#[複数]
def add_two_num(num_one, num_two):
    print('add_two_num(2, 3)の実行:', '{0} + {1} ='.format(num_one, num_two), num_one + num_two)
add_two_num(2, 3)

#[デフォルト値]
def time_to_wake(up_at = 8):
    print('time_to_wake()を実行:')
    if 0 < up_at < 6:
        print('You are up too early. Go back to bed')
    elif 6 < up_at < 12:
        print('Good morning!')
    elif 12 < up_at < 18:
        print('Good afternoon!')
    else:
        print('Good evening!')
time_to_wake() #引数なし
time_to_wake(13) #引数あり

#[キーワード]
def introduction(first_name, last_name):
    print('introduction()の実行', first_name + ' ' + last_name)
#引数の順番がひっくり返ってもキーワードで指定しているためエラーにならずに処理が通る
introduction(last_name='Hashimoto', first_name='Joshua')

#[可変長引数]
def person_data(*data):
    #0個以上の引数をタプルとして受け取る
    #引数の前に*をつける
    print('person_data()の実行', data)
person_data('Joshua', 22, 'Programmer')

#[キーワード付き可変長引数]
def dict_arg(**my_data):
    #0個以上のキーワード付き引数を辞書として受け取る
    #引数の前に**をつける
    print('dict_arg()の実行:', my_data)
#変数がキーに、値がバリューになる
dict_arg(name='Joshua', age=22, job='Programmer', lover=False)



"""関数内関数"""
def innerDefinition(a, b):
    def plus(c, d):
        return c + d
    #関数内で関数内関数を宣言する
    r = plus(a, b)
    print('innerDefinition()の実行。中のplus()が動いている:', r)
innerDefinition(2, 5)



"""クロージャー"""
def closerDefinition(a, b):
    def inner():
        return a + b
    #実行するのではなくinner関数のオブジェクトを返す
    return inner
#まずはouterを実行
f = closerDefinition(1, 2) #この時点ではinnerは実行されない
#ここで初めて実行される
r = f()
print("closerDefinition()の実行:", r)
#どういうときに使うかというと、今は実行したくないけどあとで実行したいときなど

#[closerの例]
print('クロージャ―の例------------------')
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area
cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.141592)
print('cal1:', cal1(17))
print('cal2:', cal2(17))



"""デコレーター"""
def print_info(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return print('デコレーター:', result)
    return wrapper

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        return print('result:', result)
    return wrapper

@print_more
@print_info
def add_num(a, b):
    return a + b
add_num(10, 20)

def my_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('my_deco:', result)
        return result
    return wrapper

@my_deco
def sub_num(a, b):
    return a - b
sub_num(10, 20)



"""ラムダ"""
daylist = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']
def change_words(words, func):
    for word in words:
        print('ラムダの実行:', func(word))
sample_func = lambda word: word.capitalize()
change_words(daylist, sample_func)



"""ジェネレータ"""
aisatsu = ['Good morning', 'Good afternoon', 'Good night']
def greeting():
    #要素を一個一個生成するのがジェネレーター
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
        #yieldがあるとpythonはジェネレーターとして扱う
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
#一気に処理をするのではなく、yieldで一回一回処理を呼び出す。
#一気に処理をせずに一回一回処理を施したい時に使う