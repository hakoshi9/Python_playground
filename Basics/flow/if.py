"""if構文で遊ぶ"""


"""通常"""
x = -10
if x < 0:
    print('negative')


"""if-else"""
y = 10
if x < 0:
    print('negative')
else:
    print('positive')


"""elif"""
name = 'Ted'
if len(name) < 5:
    print('Less then 5 letters')
elif len(name) < 10:
    print('Less then 10 letters')
else:
    print("More then 10 letters:", len(name)-1, 'letters')


"""入れ子"""
a = 5
b = 10
if a > 0:
    print('a is positive')
    if b > 0:
        print('b is also positive')


"""検索inとnot"""
my_name = 'Joshua Hashimoto'
if 'e' in my_name:
    print("There is a letter 'e' in my name")
elif 'e' not in my_name:
    print("There is not a letter 'e' in my name")


"""論理演算子の結合"""
num = 22
if 13 < num < 19:
    print('I am a teenager')
elif 20 < num < 29:
    print("I'm in my 20's")
elif 30 < num < 39:
    print("I'm in my 30's")
else:
    print('too old for me')