"""関数の引数"""
# 関数にはデフォルトの機能として、引数というものを使うことができる
# 引数を使用することで中の処理に好きな値を入れることができる
# つまり、1つの処理でも柔軟に対応することができる
# この引数の宣言にはいくつか存在する

# [引数が1つ]
# def 関数名(arg):
#     処理
def what_is_this(color):
    print("what_is_this('{}')の実行:".format(color), color)
what_is_this('red')


# [引数が複数]
# def 関数名(arg, arg, arg):
#     処理
# 引数の数に制限はない
def add_two_num(num_one, num_two):
    print('add_two_num(2, 3)の実行:', '{0} + {1} ='.format(num_one, num_two), num_one + num_two)
add_two_num(2, 3)


# [デフォルト値]
# def 関数名(arg=default):
#     処理
# 引数にデフォルトで入れる値を設定できる
# こうすることで、引数を入れない状態で関数を実行してもエラーにならずデフォルト値を使って処理を行う
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
time_to_wake() # 引数なし
time_to_wake(13) # 引数あり


# [キーワード]
# def 関数名(arg):
#     処理
# 宣言そのものは通常の引数あり関数と変わらない
# 実行の際に引数名を直接指定して値を渡すことができる
# これがキーワード引数と呼ばれるもの
def introduction(first_name, last_name):
    print('introduction()の実行:', first_name + ' ' + last_name)
# 引数の順番がひっくり返ってもキーワードで引数を指定しているためエラーにならずに処理が通る
introduction(last_name='Hashimoto', first_name='Joshua')


# [可変長引数]
# def 関数名(*arg):
#     処理
# 引数の前に*をつけることで実現可能
# 0個以上の引数をタプルとして受け取る
# つまり複数の値を1つとして受け取ることができる
# 慣例として可変長引数は「*args」と表記する
def person_data(*data):
    print('可変長引数を使用した関数の実行:', data)
person_data('Joshua', 22, 'Programmer')


# [キーワード付き可変長引数]
# def 関数名(**arg):
#     処理
# 引数の前に**をつける
# 0個以上のキーワード付き引数を辞書として受け取る
# キーワード付き引数なのでkey=valueで渡す
# 慣例としてキーワード付き可変長引数は「**kwargs」と表記する
def dict_arg(**my_data):
    print('dict_arg()の実行:', my_data)
# 変数がキーに、値がバリューになる
dict_arg(name='Joshua', age=22, job='Programmer', lover=False)