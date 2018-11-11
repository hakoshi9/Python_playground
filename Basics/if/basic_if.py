"""if構文の基礎"""
# if構文は条件分岐に使用される
# 「if」の後に条件式を入れて、「:」でブロックを生成しその中にその条件に合う場合の処理を記述していく
# この時、条件式はTrueかFalseを返すものならなんでも良い
# 逆に、True, Falseを返さない(返せない)ものエラーとなる

# 通常のif
x = -10
if x < 0:
    print('negative')


# if-else
# elseは、その条件が合わなかった場合(Falseだった場合)に実行される。
# 受皿のような役割だと考えるとわかりやすい
y = 10
if x < 0:
    print('negative')
else:
    print('positive')


# elif
# ifの条件に対し、他の条件を設定する
# elseはifに対する受皿に対し、elif新しい特定の条件を設定できる
# より細かい条件分岐に使う
name = 'Foo'
if len(name) < 5:
    print('Less then 5 letters')
elif len(name) < 10:
    print('Less then 10 letters')
else:
    #長さ-1をしているのは、名前の余白を覗くため
    print("More then 10 letters:", len(name)-1, 'letters')




# if構文を使う上で気をつけないといけないのは、
# 条件をどこに置くか、である
# なぜなら、if構文は「最初にマッチした条件で処理を止めてしまう」、かつ
# 「プログラムは上から順番に処理される」ため
# 上に設定する条件をゆるくしてしまうと、想定していないところで処理が終わってしまう

# ex)
#アルコールを飲むことができるかを判定
age = 22
if 5 < age:
    print("I'm older then 5. I can't drink alcohol yet") #ここで条件にマッチしてしまい、ifを抜けてしまう。
elif 10 < age:
    print("I'm older then 10. I can't drink alcohol yet")
elif 15 < age:
    print("I'm older then 15. I can't drink alcohol yet")
elif 20 <= age: #<=や>=は、その値も含むという意味(≦や≧のこと)。この時、「=」は必ず右側にくる
    print("I'm older then 20. I can drink alcohol!")