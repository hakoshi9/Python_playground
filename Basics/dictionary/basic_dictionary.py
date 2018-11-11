"""辞書の基礎"""
# 辞書は、値をキーと共に登録するリストのようなもの
# リストとの違いは、
# 1)インデックスでの値の取り出しができない。代わりにキーによる取り出し
# 2)リストにはその要素に順番があるが、辞書には順番という概念がない

# 辞書の宣言
# {key: value, key: value, key: value}
# キーは文字列でも数字でも大丈夫。変数を使うこともできる。しかしそれ以外はキーにならない
# 値(バリュー)は基本的になんでも入れることができる
empty_dict = {}
str_key_dict = {'name': 'Foo Bar', 'age': 22, 'job': 'Programmer',}
int_key_dict = {1: 'one', 5: 'five', 9: 'nine', 3: 'three', 7: 'seven',}
var_key = '辞書用'
mix_dict = {'work_at': 'Tokyo', 'lover': True, 'str_dict': str_key_dict, var_key: '変数をキーとして指定。変数の中身がキーとして出力される'}

# 辞書の中身の取得
# インデックスではなくキーを指定
print(str_key_dict['job'])
print(int_key_dict[5])

# mix_dictの中身を確認
# items()関数を使ってkeyもvalueも取り出す
for key, value in mix_dict.items():
    print('{key}: {value}'.format(key=key, value=value))


# 要素の追加
add_dict = {}
add_dict['name'] = 'Foo'
add_dict['age'] = 35
print('要素を追加された辞書を出力:', add_dict)


# 要素の書き換え
rewrite_dict = {'name': 'Foo Bar', 'age': 22, 'job': 'Programmer',}
rewrite_dict['name'] = 'Hoge'
rewrite_dict['age'] = 18
rewrite_dict['job'] = 'YouTuber'
print('要素を書き換えられた辞書を出力:', rewrite_dict)


# 辞書の要素を削除
# 辞書にある要素の削除
delete_dict = {'name': 'Joshua Hashimoto', 'age': 23, 'job': 'programmer', 'gender': 'Male'}
# [要素を受け取って削除]
print('popで値を受け取る:', delete_dict.pop('gender'))
print('要素がpopされた後の辞書を確認:', delete_dict)
# [辞書そのものを消す]
print('clear():', delete_dict.clear())