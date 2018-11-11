"""forのbreak/continue"""
# breakとcontinueはwhile構文と同じく動作する
# breakは現在の処理を「完全に」抜ける
# continueは、そこで処理を一旦止めて(そこより下は処理しないで)次のループに入る
some_list = ["Joshua", "Ted", "Shino", "Maira", "Honoka", "Sao"]
for name in some_list:
    if name == 'Ted':
        print(name + 'は帰ってしまった')
        continue
    if name == 'Honoka':
        break

    print('Who is here? ->',name)



"""for-else"""
# elseをつけると、ループを抜けた時の処理を記述することができる
# これはforループをbreakで抜けない限りは、ループが終わったときに必ず実行される
fruits = ['Apple', 'Banana', 'Mango', 'Bluebarry', 'Apple', 'Apple', 'Mango']
for fruit in fruits:
    print('I ate ->', fruit)
else:
    print('I ate all!')



"""enumerate関数"""
# [ようはforループで回しているリストのindexも返す関数]
# indexが先にくる
for index, fruit in enumerate(fruits):
    print('index number {index}: {fruit}'.format(index=index, fruit=fruit))



"""zip関数"""
# 2つ以上のリストを同時に回すことができる関数
# 死ぬほど便利
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
# このとき、keyが必ず先に取り出される
for key, value in my_dict.items():
    print('{key}: {value}'.format(key=key, value=value))
