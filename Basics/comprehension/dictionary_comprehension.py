"""辞書内包表記"""
# Pythonには内包表記という、普段なら数行で
# 書かないといけない処理を1行にする構文があります
# また、普通の処理よりも内包表記の方がプログラムのランタイムが短いです

# 辞書内包表記の基本宣言
# {key:value for i in 配列など}

# enumerate関数と併用
dict_list = ['apple', 'grape', 'banana', 'strawbarry', 'water melon', 'mango']
compre = {key+1: value for key, value in enumerate(dict_list)}
print(compre)


# 上記を通常に作る
empty_dict = {}
for key, value in enumerate(dict_list):
    empty_dict[key+1] = value

print(empty_dict)