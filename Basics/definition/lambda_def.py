"""lambda関数"""
# ラムダ関数は別名無名関数とも呼ばれる。
# その名の通り、名前をつける必要のない関数として使える
# 1行で収まるような簡単な関数を使いたいときや、
# その場でしか使わない(繰り返し使用しない)簡単な関数のときに使う
# 逆に言えば、複数行にまたがるような処理は書くことはできない

# lambda式を使わずに通常の関数を用いる場合
def func(price,tax):
    return price + (price * tax)
 
payment1 = func(100,0.08)
print(payment1)
 
# lambda式を用いる場合
# lambda 引数: 処理
price_with_tax = lambda price, tax: price + (price*tax)
#宣言は通常の関数と同じ
print(price_with_tax(100,0.08))