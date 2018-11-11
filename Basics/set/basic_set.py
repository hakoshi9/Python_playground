"""setの基礎"""
# setはタプルやリストと同じく複数のデータを持つことができる
# 他の二つと違う特徴は、setは「重複した値を保持できない」
# set内の要素が重複できないので、同じ値を保持させたくないときに使う
# また、インデックスを使って要素を取り出すことができない

# setの定義
# {要素, 要素, 要素}
first_set = {'banana', 'apple', 'grape', 'strawberry'}
second_set = {1, 2, 3, 4, 5, 6}
# setにはリストやディクショナリを追加することはできない
# 理由として、リストやディクショナリは後から変更でき、かつ参照型であるため


# setの基本機能 -和集合-
# setAとsetBを足したsetを作る
# このとき、重複している要素は1つとしてsetに含まれる
prime = {2, 3, 5, 7, 13, 17}
fib = {1, 1, 2, 3, 5, 8, 13}
prime_fib = prime | fib
print('和集合:', prime_fib)


# setの基本機能 -差集合-
# setAの要素からsetBに含まれている要素を引いたsetを作る
dice = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6, 8, 10}
dice_even = dice - even
print('差集合', dice_even)


# setの基本機能 -交わり-
# setAとsetBの重複しているしている要素からsetを作る
prefs = {'北海道', '青森', '秋田', '岩手'}
capitals = {'札幌', '青森', '秋田', '盛岡'}
pref_cap = prefs & capitals
print('交わり:', pref_cap)


# setの基本機能 -対象差-
# setAとsetBの重複している要素を取り除いた要素からsetを作る
pref_cap2 = prefs ^ capitals
print('対象差:', pref_cap2)
# 和集合は重複した値を二つ要素に入れないだけでset自体には入れている
# しかし、対象差は重複した要素そのものをsetに含めない

