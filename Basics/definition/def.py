
# 通常の宣言
def say_something():
    print('say_something()の実行:', 'hi')

# 宣言は関数名()で行うことができる
say_something()

# 変数に代入することもできる
var = say_something
# その場合は変数名()と実行する
var()


# def print_result_defName(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return print('{0}の実行: {1}'.format(func.__name__, result))
#     return wrapper

# @print_result_defName
# def hi(word):
#     return word

# hi('Joshua Hashimoto')