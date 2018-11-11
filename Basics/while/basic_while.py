"""while文の基礎"""
# while文は、「条件式がTrueの間はずっと処理を実行する」文です。
# 注意点として、条件式をFalseになるようにしないとwhile文は永遠に実行され続けることになる

# 条件式となる変数countを定義
count = 0
# 「while 条件式:」で式を実行できる
# countが5以下の間はwhile文内の処理を実行する
while count < 5:
    # countを表示する
    print('count:', count)
    # countに1追加する
    count += 1
# countが5になるまでこの処理は実行される