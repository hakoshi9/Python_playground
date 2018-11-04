"""変数の基礎"""
#変数は値などを格納しておく箱のようなもの
#変数はプログラミングにおける基本中の基本
#変数に入れる値には型というものが存在する
#通常、変数は格納されている値の型がアサインされる
#Pythonにおける変数は「動的型付け」で変数の型を決める
#つまり、変数に値を入れた時点でその値をもとに変数の型を決める

#Pythonにおける変数の宣言は下記のように行う
variable = 'This is a variable'
#変数名とそれに入る値をイコールで結ぶ

#これが実際に入っているかを「print()」を使って確認する
print(variable)

#変数にはあらゆる値を入れることができる
#文字列型(str)
string = 'This is a string'
#整数型(int)
integer = 20
#浮動小数点型(float)
double = 2.6
#真偽型(boolean)
is_bool = True
#ここで覚えておかなければいけないのは、「整数型」と「浮動小数点型」は別の型であるということ

#Pythonでは変数名はスネークケース(_で単語を繫げる)で書く
var_str = 'This is a string variable'
var_num = 25
open_file = True




"""変数を使った計算"""
#変数同士を使った値の計算をすることができる
#しかし、ルールとして基本的に、
#文字列型 + 文字列型
#整数型 + 整数型
#整数型 + 浮動小数点型
#浮動小数点型 + 浮動小数点型
#のペアでした計算をすることができない
#これ以外のペアの計算は基本的にできない
#また、
#整数型 + 整数型
#整数型 + 浮動小数点型
#浮動小数点型 + 浮動小数点型
#の3つに関しては「+(加算)」「-(引算)」「*(掛算)」「/(割算)」「%(余り)」の計算をすることができる
num_int_one = 10
num_int_two = 25
num_float_one = 1.8
num_float_two = 2.5
#整数型 + 浮動小数点型
print(num_int_one + num_float_two)
#浮動小数点型 + 浮動小数点型
print(num_float_one + num_float_two)
#整数型 + 浮動小数点型
print(num_int_one + num_float_one)

#また、変数の計算を変数に格納することができる
#整数型 + 整数型
plus = num_int_one + num_int_two
#整数型 - 整数型
minus = num_int_one - num_int_two
#浮動小数点型 * 浮動小数点型
times = num_float_one * num_float_two
#整数型 / 浮動小数点型
devide = num_float_two / num_int_two
#整数型 % 整数型
remainder = num_int_two % num_int_one
print(plus)
print(minus)
print(times)
print(devide)
print(remainder)
#文字列型 + 文字列型は加算のみ可能
str_one = 'Hello'
str_two = 'Joshua'
print(str_one + ' ' + str_two) #' '(空白)を足すことで文字列と文字列の間に空白を入れることができる
#文字列の詳しい操作は「string」フォルダを参照してください




"""定数の宣言"""
#Pythonには、文法的に定数というものが存在しない
#なので、Pythonでは定数は変数名を全て大文字にすることで表現する
#変数名が全て大文字のものは値を変えないのが通例となっている
CONSTANT = 'Never change a variable that the name is all capitalized'