"""setの合計値"""
sum_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('sum_set:', sum_set)
print('sum_setの合計値:', sum(sum_set))



"""setに値を追加"""
add_set = {1, 2, 3, 4, 5}
add_set.add(6)
print('add_setに6を追加:', add_set)



"""setの値を削除"""
# [特定の要素を削除]
delete_set = {1, 2, 3, 4, 5}
delete_set.remove(4) # インデックスではなく要素そのものを指定
print('delete_setから4を削除:', delete_set)
# [全ての要素を削除]
delete_set.clear()
print('delete_setを削除:', delete_set)



"""setの要素数を数える"""
# setはリスト、タプル、辞書と同じく要素数を調べることができる
len_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('setの要素数を調べる:', len(len_set))

