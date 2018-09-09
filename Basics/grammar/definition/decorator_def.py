

# デコレーター
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