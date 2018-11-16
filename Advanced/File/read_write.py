string = """\
AAA
BBB
CCC
DDD
"""

# 'w'のままだと、例えば書き込んだ後に読み込んだりすることができない
# そんな時は、'w+'モードにする。こうすると、書き込んだ後に読みこむことができる
# 先に読み込みをしたい時は'r+'にする
# 要は、'先に行いたいモード+'の形
with open('file_three.txt', 'w+') as f:
    f.write(string)
    # 読み込む前にseekを使ってインデックスを0にしないといけない
    # 書き込んだ直後はインデックスが一番最後で何も見ることができない
    f.seek(0)
    # ちなみに、こちらを先にw+で実行すると書き込みモードに入って中身が消えてしまう
    print(f.read())



s = """\
EEE
FFF
GGG
HHH
"""

# 先に読み込む場合
with open ('file_three.txt', 'r+') as f:
    f.read()
    f.seek(0)
    # ただしこれは中身を上書きしてしまうことに注意
    f.write(s)