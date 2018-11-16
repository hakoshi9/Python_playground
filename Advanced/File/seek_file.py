"""seak"""
# seekでファイル内での(インデックスの)場所を変更することができる

string = """\
AAA
BBB
CCC
DDD
EEE
FFF
"""

# 書き込み
with open('file_two.txt', 'w') as f:
    # こうするとclose()がなくても、
    # ブロックの中を実行したら閉じてくれる
    f.write(string)



# 読み込み
with open('file_two.txt', 'r') as read:
    # tell()で現在のインデックスの位置を返してくる
    print(read.tell())
    # read()に数字を引数として渡すと、その位置から引数に渡した数分の文字を返してくる
    print(read.read(1))
    # seek(移動したい数)で位置を変えられる
    read.seek(5)
    print(read.read(1))
    read.seek(14)
    print(read.read(1))
    read.seek(15)
    print(read.read(1))
    read.seek(5)
    print(read.read(1))
    # seekは必ず現在地からの移動を返す