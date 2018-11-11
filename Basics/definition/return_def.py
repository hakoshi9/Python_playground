"""戻り値を返す関数"""
# 関数は戻り値を返すことができる
# 戻り値を返す関数は関数内で行った処理によってできた値を返すことができる
# 変数などに入れる形で関数を実行するとその変数に返ってきた値が代入される

# 戻り値を持った関数の宣言
# return_def():
#     return val
def return_two():
    s = 2
    return s

returned = return_two() + 2
print('return_two()+2:', returned)