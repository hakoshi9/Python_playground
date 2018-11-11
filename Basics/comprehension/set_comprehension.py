"""集合内包表記"""
# Pythonには内包表記という、普段なら数行で
# 書かないといけない処理を1行にする構文があります
# また、普通の処理よりも内包表記の方がプログラムのランタイムが短いです

# 集合内包表記の基本宣言
# {処理 for i in 配列など}
# 辞書内包表記と似ているので注意
compre_set = {i for i in range(10)}
print(compre_set)


# 上記を通常に作る
generic_set = set()
for i in range(10):
    generic_set.add(i)

print(generic_set)