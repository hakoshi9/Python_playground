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