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
print(str_key_dict['job'])
print(int_key_dict[5])

# mix_dictの中身を確認
for key, value in mix_dict.items():
    print('{key}: {value}'.format(key=key, value=value))