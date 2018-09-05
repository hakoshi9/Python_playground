"""ディクショナリで遊ぶ"""


"""辞書のキーのみを取得する"""
dict_key = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
print('Keyのみを取得:', dict_key.keys())



"""辞書の値のみを取得する"""
dict_value = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
print('Valueのみを取得:', dict_value.values())



"""辞書のアップデート"""
update_dict = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
#[通常]
update_dict['age'] = 23
print('update_dictのageを23に変更:', update_dict)
#[複数]
update_dict.update({'name': 'Joshua Hashimoto', 'sex': 'Male'})
print('update_dictのアップデート:', update_dict)



"""辞書の中身の取得"""
get_dict = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
#[通常]
print('get_dict["name"]:', get_dict["name"]) #ただし、これは存在しないキーを指定した場合エラーになる
#[指定したキーが存在しない時にエラーにならない]
print('get_dict.get("name"):', get_dict.get("name"))
print('get_dict.get("hobby"):', get_dict.get("hobby"))



"""辞書の要素を削除"""
delete_dict = {'name': 'Joshua Hashimoto', 'age': 23, 'job': 'programmer', 'sex': 'Male'}
#[要素を受け取って削除]
print('popで値を受け取る:', delete_dict.pop('sex'))
print('要素がpopされた後の辞書を確認:', delete_dict)
#[辞書を消す]
print('clear():', delete_dict.clear())



"""要素の検索"""
search_dict = {'name': 'Joshua Hashimoto', 'age': 23, 'job': 'programmer', 'sex': 'Male'}
print("'sex'キーがあるかを確認:", 'sex' in search_dict)



"""辞書のコピー"""
copy_dict = {'name': 'Joshua Hashimoto', 'age': 23, 'job': 'programmer', 'sex': 'Male'}
recopy_dict = copy_dict.copy()
print('--------辞書もリストと同じで参照型のためコピーが必要--------')
print('copy_dictをコピーしたrecopy_dictのageを35に変更')
recopy_dict['age'] = 35
print('copy_dict:', copy_dict)
print('recopy_dict:', recopy_dict)