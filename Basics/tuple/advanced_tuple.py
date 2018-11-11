"""タプルのアンパック"""
# タプルは個別の変数にアンパック(展開)することができる
unpack_tuple = (1, 2, 3, 4)
print('unpack_tuple:', unpack_tuple)
unpack_one, unpack_two, unpack_three, unpack_four = unpack_tuple
print('unpack_one:', unpack_one)
print('unpack_two:', unpack_two)
print('unpack_three:', unpack_three)
print('unpack_four:', unpack_four)



"""タプルの合計値"""
# タプルはその中身が全て数値であれば合計値を出すことができる
sum_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('sum_tuple:', sum_tuple)
print('sum_tupleの合計値:', sum(sum_tuple))
# sum()は合計値を返すので、変数に入れることもできる



"""リストをタプルへ"""
# リストはタプルに変換することができる
game_list = ['FNaF', 'BH', 'BioShock', 'サイコブレイク']
print('game_list:', game_list)
print('リストからタプルへ:', tuple(game_list))
# tuple()は合計値を返すので、変数に入れることもできる



"""タプルをソート"""
# タプルの中にある値を特定の順番にソートすることができる
need_sort_tuple = ('a', 'z', 'g', 'i', 'o', 'w')
# しかし、そのままソートをリストになってしまう
sort_var = sorted(need_sort_tuple)
# tupleに変換
sort_tuple = tuple(sort_var)
print('ソートされたタプルを出力:', sort_tuple)



"""タプルをスライス"""
# タプルは文字列やリストと同様にスライスで特定の範囲を抽出することができる
num_tuple = 5, 3, 1, 9, 6, 7, 4, 8, 2
print('index1~3までのタプルを出力:', num_tuple[1:4])



"""要素内の最大値を求める"""
max_tuple = (10, 4, 5, 8, 11, 45, 21)
print('タプルの最大値を出力:', max(max_tuple))



"""要素内の最小値を求める"""
min_tuple = (10, 4, 5, 8, 11, 45, 21)
print('タプルの最小値を出力:', min(min_tuple))



"""要素の長さを調べる"""
len_tuple = (3, 8, 41, 23, 80, 15, 33)
print('タプルの長さを出力:', len(len_tuple))
