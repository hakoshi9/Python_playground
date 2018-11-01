"""文字列の連結"""
str1 = "Python"
str2 = "3.6"
str3 = str1 + str2
print('str1とstr2を連結させたstr3:', str3)
print('+演算子がなくても連結させることができる:', 'Py''thon')



"""文字列のインデックス"""
print('str1のインデックス0を出力:', str1[0])



"""リスト/タプルを文字列へ連結"""
list1 = ['This', 'is', 'a', 'test']
tuple1 = ('One', 'Two', 'Three')
str4 = ' '.join(list1)
str5 = ','.join(tuple1)
print('list1を空白を使って連結:', str4)
print('tuple1を,を使って連結:', str5)



"""文字列を条件でリストへ"""
list2 = str4.split(' ')
print('str4を空白でsplitして作ったlist2:', list2)



"""文字列の一部を置換"""
str6 = 'Hello,My,Name,Is,Joshua.'
print(',を空白に置換:', str6.replace(',', ' '))



"""文字列のスライス"""
str7 = "スライス用文字列str7"
print('str7を2~4でスライス:', str7[2:5])
#スライスのルールはリストと一緒



"""文字列の検索"""
searchString = 'My name is Joshua. Joshua Hashimoto.Nice to meet you all at this beautiful day. '
#[特定の文字列から始まる]
is_start = searchString.startswith('My')
print(is_start)
is_start = searchString.startswith('Joshua')
print(is_start)
#[特定の文字列がその文字列のインデックス番号から返ってくるかを調べる]
print(searchString.find('Joshua')) #ただし、最初にその文字列に当たるものしか帰ってこない
print(searchString.rfind('Joshua')) #後ろの奴を探す
#[特定の文字列がいくつ入っているかを検索する]
print(searchString.count('Joshua')) #リストにもある



"""文字列の変更"""
change_size_string = "Joshua Hashimoto"
print(change_size_string.capitalize()) #最初は大文字になって残りは小文字になる
print(change_size_string.title()) #全てのワードの最初の文字を大文字にする
print(change_size_string.upper()) #全て大文字となる
print(change_size_string.lower()) #全て小文字となる



"""文字列の組み込み"""
first_name = 'Joshua'
last_name = 'Hashimoto'
age = 22
#format()と文字列中の{}を使うことで文字列に値を組み込むことができる
introduction_str = 'Hello, my name is {first_name} {last_name}. {age} years old.'.format(first_name=first_name, last_name=last_name, age=age)

