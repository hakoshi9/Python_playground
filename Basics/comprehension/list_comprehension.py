"""リスト内包表記"""
# Pythonには内包表記という、普段なら数行で
# 書かないといけない処理を1行にする構文があります
# また、普通の処理よりも内包表記の方がプログラムのランタイムが短いです

# リスト内包表記の基本宣言
# [処理 for i in 配列など]
compre_list = [i for i in 'comprehension']
print(compre_list)


# 上記を通常に作る
empty_list = []
for i in 'comprehension':
    empty_list.append(i)

print(empty_list)