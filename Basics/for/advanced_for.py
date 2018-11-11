"""forのbreak/continue"""
some_list = ["Joshua", "Ted", "Shino", "Maira", "Honoka", "Sao"]
for name in some_list:
    if name == 'Ted':
        print(name + 'は帰ってしまった')
        continue
    if name == 'Honoka':
        break

    print('Who is here? ->',name)


"""for-else"""
fruits = ['Apple', 'Banana', 'Mango', 'Bluebarry', 'Apple', 'Apple', 'Mango']
for fruit in fruits:
    print('I ate ->', fruit)
else:
    # elseをつけると、ループを抜けた時の処理をかける
    # ただし、breakで抜けた場合は実行されない
    print('I ate all!')


"""enumerate関数"""
# [ようはforループで回しているリストのindexも返す関数]
# indexが先にくる
for index, fruit in enumerate(fruits):
    print('index number {index}: {fruit}'.format(index=index, fruit=fruit))


"""zip関数"""
days = ['Mon', 'Tue', 'Wen']
fruits = ['Apple', 'Banana', 'Orange']
drinks = ['Water', 'Coffee', 'Milk']
for day, fruit, drink in zip(days, fruits, drinks):
    print('{day}: drink {drink} and eat {fruit}'.format(day=day, fruit=fruit, drink=drink))


"""辞書のforループ"""
my_dict = {'name': 'Joshua Hashimoto', 'age': 23, 'job': 'programmer', 'sex': 'Male'}
# [通常はkeyのみが出力される]
for i in my_dict:
    print(i)
# [keyもvalueも取り出す場合]
for key, value in my_dict.items():
    print('{key}: {value}'.format(key=key, value=value))


"""range関数を使ったループ回数の指定"""
for i in range(0, 10):
    print('range:', i)