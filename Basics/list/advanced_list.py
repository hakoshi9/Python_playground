"""+=で複数の値を一度に追加"""
# 要素を1つずつ追加するのではなく複数を一度に追加する
multi_add_list = []
multi_add_list += 'Fallout4', 'Biohazard7'
print(multi_add_list)



"""extend()でリストを別のリストに追加"""
# リストを別のリストと結合する時に使える
multi_add_list.extend(["Assassin's Creed4: Black flag", 'Titan Fall2',])
print(multi_add_list)



"""リストの要素数を調べる"""
# リストの中にある要素の数を返す
print('リストの要素数を出力', len(multi_add_list))



"""リストの中にある特定の要素が何個存在するかを数える"""
# リスト内の重複している要素の個数を調べることができる
multi_element_list = ['Apple', 'Banana', 'Mango', 'Bluebarry', 'Apple', 'Apple', 'Mango',]
apple_count = multi_element_list.count('Apple')
banana_count = multi_element_list.count('Banana')
mango_count = multi_element_list.count('Mango')
orange_count = multi_element_list.count('Orange')
print('Apple count:', apple_count)
print('Banana count:', banana_count)
print('Mango count:', mango_count)
print('Orange count:', orange_count)



"""要素のスライス"""
# リスト内の要素を、範囲を指定して取り出すことができる
slice_list = [1 ,3 ,5 ,7, 9, 11,]
print('スライス@全て:', slice_list[:])
print('スライス@index1からindex3の手前まで:', slice_list[1:3])
print('スライス@最初からindex4手前まで:', slice_list[:4])
print('スライス@index2から最後まで:', slice_list[2:])



"""スライスを飛ばす"""
# 特定の条件でスライスを飛ばして取り出すことができる
jump_list = [2, 4, 6, 8, 10, 12,]
print('Show every other list:',jump_list[::2])



"""要素の挿入"""
# 要素を特定の位置に挿入することができる
insert_list = ['Joshua', 'Ted', 'Shino', 'Kubo', 'Suganen', 'Mattsun',]
insert_list.insert(0, 'Kensei')
print('リストのindex0に要素を挿入:', insert_list)



"""リストの中身の合計"""
# リストの中の要素が全て数値の場合に限り、要素の合計値を求めることができる
sum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
print('リストの合計値を出力:', sum(sum_list))



"""タプルからリストを作る"""
# タプルをリストに変換することができる
to_list_tuple = 10, 20, 30, 40
print('タプルから作られたリスト:', list(to_list_tuple))



"""setからリストを作る"""
# setをリストに変換することができる
to_list_set = {1, 2, 3, 4}
print('setから作られたリスト:', list(to_list_set))



"""文字列からリストを作る"""
# 文字列をリストに変換することができる
# これには2つの方法が存在する
# [list()メソッドを使う]
str1 = "abcdefg"
print('str1からリストを作成:', list(str1))
# [split()メソッドを使う]
str2 = 'これは、文字列、を、リスト、に、するため、の、文字列、です'
print('str2からリストを作成:', str2.split('、'))



"""リストをソートする"""
# リストの中身をある法則で並べ換える
# リストの中身が同じ型でなくても、デフォルトの法則で並び替える
sort_list = [5, 3, 1, 9, 6, 7, 4, 8, 2,]
sort_list.sort() # sort()メソッドは戻り値が無いためそのまま出力することができない
print('sort_listをソート', sort_list)
sort_list.reverse() # reverse()メソッドは戻り値が無いためそのまま出力することができない
print('それを逆にソート:', sort_list)



"""リストのアンパック"""
unpack_list = ['apple', 'grape', 'banana', 'strawbarry',]
unpack_var1, unpack_var2, unpack_var3, unpack_var4 = unpack_list
print('unpack_var1:', unpack_var1)
print('unpack_var2:', unpack_var2)
print('unpack_var3:', unpack_var3)
print('unpack_var4:', unpack_var4)



"""特定要素のインデックスの検索"""
index_search1 = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1,]
index_search2 = ['apple', 'grape', 'banana', 'strawbarry', 'water melon', 'mango']
print('指定した要素がリストのどのインデックスかを返す1:', index_search1.index(3)) # ただし、最初に引っかかるものを返す
print('指定した要素がリストのどのインデックスかを返す2:', index_search2.index('strawbarry'))
print('指定した値から先の指定した要素のインデックスを返す:', index_search1.index(3, 4)) # 第一引数->開始, 第二引数->検索要素



"""要素の検索"""
search_list = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1,]
# [in演算子を使う]
# True, Falseが返される
print('apple' in search_list)
print(5 in search_list)
# [if構文を使う]
# 上記をifにしただけ。やってることは同じ
if 8 in search_list:
    print('exist')
else:
    print('does not exist')



"""リストのコピー"""
# [リストは参照型のためコピーをしないといけない,]
copy_list1 = [1, 2, 3, 4, 5,]
copy_list2 = copy_list1
copy_list2[1] = 100
print('copy_list2[1]に100を代入すると参照しているcopy_list1の[1]も変わってしまう')
print('copy_list1:', copy_list1)
print('copy_list2:', copy_list2)
copy_list3 = copy_list1.copy()
copy_list3[3] = 200
print('copy_list1をcopy_list3にコピーしたのちcopy_list3[3]を200に変更')
print('copy_list1:', copy_list1)
print('copy_list2:', copy_list2)
print('copy_list3:', copy_list3)



"""要素内の最大値を求める"""
max_list = [10, 4, 5, 8, 11, 45, 21,]
print('リストの最大値を出力:', max(max_list))



"""要素内の最小値を求める"""
min_list = [10, 4, 5, 8, 11, 45, 21,]
print('リストの最小値を出力:', min(min_list))
