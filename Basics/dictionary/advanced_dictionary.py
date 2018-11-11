"""辞書のキーのみを取得する"""
# 指定した辞書にあるキーのみを取り出す
dict_key = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
print('Keyのみを取得:', dict_key.keys())



"""辞書の値のみを取得する"""
# 指定した辞書にあるバリューのみを取り出す
dict_value = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
print('Valueのみを取得:', dict_value.values())



"""辞書のアップデート"""
# 辞書にある要素の中身を更新する
update_dict = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
# [通常]
update_dict['age'] = 23
print('update_dictのageを23に変更:', update_dict)
# [複数]
update_dict.update({'name': 'Joshua Hashimoto', 'sex': 'Male'})
print('update_dictのアップデート:', update_dict)



"""辞書の中身の取得"""
# 辞書の中身の取得にも、通常ともう1つやり方がある
get_dict = {'name': 'Joshua', 'age': 22, 'job': 'programmer'}
# [通常(basic_dictionaryでもやった)]
# ただし、これは存在しないキーを指定した場合エラーになる
print('get_dict["name"]:', get_dict["name"])

# [.get()関数の使用]
# こちらは指定したキーが存在しない時にエラーにならない
# 要素が存在していない時はNoneが返ってくるため、要素の検索などで安全に取り出すことができる
print('get_dict.get("name"):', get_dict.get("name"))
print('get_dict.get("hobby"):', get_dict.get("hobby"))



"""要素の検索"""
#in演算子の使用
search_dict = {'name': 'Joshua Hashimoto', 'age': 23, 'job': 'programmer', 'sex': 'Male'}
print("'gender'キーがあるかを確認:", 'gender' in search_dict)



"""辞書のコピー"""
# リスト同様、辞書も参照型のため明示的に辞書をコピーしなければ元のデータが上書きされてしまう
copy_dict = {'name': 'Joshua Hashimoto', 'age': 23, 'job': 'programmer', 'gender': 'Male'}
recopy_dict = copy_dict.copy()
print('--------辞書もリストと同じで参照型のためコピーが必要--------')
print('copy_dictをコピーしたrecopy_dictのageを35に変更')
recopy_dict['age'] = 35
print('copy_dict:', copy_dict)
print('recopy_dict:', recopy_dict)