"""デコレーター"""
# デコレーターはその名の通り、関数を装飾するための関数である
# 複数の関数にまたがる処理を一つにまとめて、デコレーターとして実行
# することで同じ記述をしなくてすむ
# しかし、慣れるのに時間がかかる構文でもあるため、使える機会があれば積極的に使っていきたい構文でもある
# また、関数を装飾するための関数なので、デコレータ作成時は必ず関数を引数として渡す必要がある

# デコレーターの宣言
# def デコレータ名(func):
#     def wrapper(*args, **kwargs):
#         関数の実行は -> 関数(*args, *kwargs) 
#         処理
#         return 返す結果
#     return wrapper
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

# デコレータは、@デコレータ名で関数を装飾することができる
# 複数のデコレータで装飾することも可能
# 一番上のデコレータから実行されていく
@print_more
@print_info
def add_num(a, b):
    return a + b
#デコレートされた関数の実行方法はそのまま
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



def print_result_defName(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return print('{0}の実行: {1}'.format(func.__name__, result))
    return wrapper

@print_result_defName
def hi(word):
    return word

hi('Joshua Hashimoto')