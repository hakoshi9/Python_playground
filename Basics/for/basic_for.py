"""forの基礎"""
# for構文はループ処理と言われる
# ループ処理は特定のものを元に、その回数分処理を実行する
# ループの対象は主にリストが使われる

# リストを使ったループ
# リストの中身を見たり、リストの中身分処理を回したりすることができる
some_list = ["Joshua", "Ted", "Shino", "Maira", "Honoka", "Sao"]
for i in some_list:
    print(i)

# range()関数を使い、処理の回数を指定することもできる
# range()関数に関してはotherフォルダを参照してください
# range_numをforの中で宣言してしまうと、ループを回るごとに0に初期化されてしまうため
# for構文の外に出している
range_num = 0
for i in range(51): #range(51)とすることで1~50までの範囲を取得できる
    range_num += i
    print(range_num)

# 純粋に回数を利用した処理
for i in range(10):
    print('Hello')