"""ジェネレータ内包表記"""
# Pythonには内包表記という、普段なら数行で
# 書かないといけない処理を1行にする構文があります
# また、普通の処理よりも内包表記の方がプログラムのランタイムが短いです

# ジェネレータ内包表記の基本宣言
# (処理 for i in 配列など)

compre_gen = (print(i) for i in range(10))

next(compre_gen)
next(compre_gen)
next(compre_gen)
next(compre_gen)
next(compre_gen)
next(compre_gen)
next(compre_gen)
next(compre_gen)
next(compre_gen)
next(compre_gen)
