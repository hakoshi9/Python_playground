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
