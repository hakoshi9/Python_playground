
# 変数に*をつけると、変数の数より多い値はリストとなる
list_var1, *list_var2 = 1, 2, 3, 4, 5
print('list_var1:', list_var1)
print('list_var2:', list_var2) #1より先は全てリストとしてlist_var2に入る



# １つの変数に,区切りの値を入れるとタプルとなる
tuple_var1 = 10, 11, 12
print('tuple_var1:', tuple_var1)
tuple_var2 = (1, 2, 3)
print('tuple_var2:', tuple_var2)