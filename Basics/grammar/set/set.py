"""setで遊ぶ"""



"""setの合計値"""
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sumSet = sum(set1)
print('set1:', set1)
print('set1の合計値:', sumSet)



"""setに値を追加"""
add_set = {1, 2, 3, 4, 5}
add_set.add(6)
print('add_setに6を追加:', add_set)



"""setの値を削除"""
#[特定の要素を削除]
delete_set = {1, 2, 3, 4, 5}
delete_set.remove(4)
print('delete_setから4を削除:', delete_set)
#[全ての要素を削除]
delete_set.clear()
print('delete_setを削除:', delete_set)