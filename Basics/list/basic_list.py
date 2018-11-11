"""リストの基礎"""
# リストは複数の値を保持することことができる
# リストの中の値は全て同じである必要はない(これはPythonの特徴の1つ)
# 通常の値(3, 'string'etc)の他のも、オブジェクト(リストやset, 関数etc)も入れることもできる

# リストの宣言
# [要素, 要素, 要素]
empty_list = []
str_list = ['apple', 'banana', 'grape']
int_list = [1, 3, 5, 7, 9]
mix_list = [4, 'mix', True, int_list]
print('empty_listの出力:', empty_list)
print('str_listの出力:', str_list)
print('int_listを出力:', int_list)


# リストの追加
add_list = []
add_list.append('Destiny2')
add_list.append('Borderlands2')
print('リスト追加を出力:', add_list)


# 要素の書きかえ
override_list = ['apple', 'grape', 'banana', 'strawbarry', 'water melon', 'mango']
override_list[4] = 'melon'
print('index4を書きかえ出力:', override_list)
override_list[1:4] = [1, 2, 3]
print('スライスによる書きかえ出力:', override_list)


# 要素の削除
del_list = ['Joshua', 'Ted', 'Shino', 'Kubo', 'Suganen', 'Mattsun']
print('del_list:', del_list)
# [最後の要素を取り出して削除(取り出した値を受け取れる)]
del_list.pop()
print('リストの最後の要素を取り出して削除:', del_list)
# [指定した箇所の要素を取り出して削除(取り出した値を受け取れる)]
del_list.pop(3)
print('指定した箇所の要素を取り出して削除:', del_list)
# [通常の削除 del]
del del_list[-1]
print('一番最後の要素をdelを使って削除(list[index]で要素を指定):', del_list)
# [通常の削除 remove(要素)]
del_list.remove('Joshua')
print('特定の要素を指定して削除:', del_list)
# [要素の全削除]
del_list.clear()
print('リストの中身を全て削除:', del_list)