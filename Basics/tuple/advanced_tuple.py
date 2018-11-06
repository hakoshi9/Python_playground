"""タプルのアンパック"""
#タプルは個別の変数にアンパック(展開)することができる
unpack_tuple = (1, 2, 3, 4)
print('unpack_tuple:', unpack_tuple)
unpack_one, unpack_two, unpack_three, unpack_four = unpack_tuple
print('unpack_one:', unpack_one)
print('unpack_two:', unpack_two)
print('unpack_three:', unpack_three)
print('unpack_four:', unpack_four)




"""タプルの合計値"""
#タプルはその中身が全て数値であれば合計値を出すことができる
sum_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print('sum_tuple:', sum_tuple)
print('sum_tupleの合計値:', sum(sum_tuple))
#sum()は合計値を返すので、変数に入れることもできる




"""リストをタプルへ"""
#リストはタプルに変換することができる
game_list = ['FNaF', 'BH', 'BioShock', 'サイコブレイク']
print('game_list:', game_list)
print('リストからタプルへ:', tuple(game_list))
#tuple()は合計値を返すので、変数に入れることもできる




"""タプルをソート"""
#タプルの中にある値を特定の順番にソートすることができる
num_tuple = ('a', 'z', 'g', 'i', 'o', 'w')
#しかし、そのままソートをリストになってしまう
sort_num = sorted(num_tuple)
#tupleに変換
sort_tuple = tuple(sort_num)
print('num_tupleをソート:', sort_tuple)




"""タプルをスライス"""
#タプルは文字列やリストと同様にスライスで特定の範囲を抽出することができる
numTuple = 5, 3, 1, 9, 6, 7, 4, 8, 2
sliceTuple = numTuple[1:4]
print('index1~3までのタプル:', sliceTuple)
