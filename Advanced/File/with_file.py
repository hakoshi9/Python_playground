"""with構文"""
# with構文はファイルを扱う際に行っていた、
# open(), close()を一括でやってくれる構文
# こちらのやり方の方が推奨されている

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
    # ファイルの読み込みはread()メソッド
    # これはまとめて読み込む
    #print(read.read())

    # while True:
    #     # readline()は1行を読み込むメソッド
    #     line = read.readline()
    #     print(line, end='')
    #     # 読み込む行がなくなったらループを抜ける
    #     if not line:
    #         break

    #チャンクで詠みこむこともできる
    while True:
        chunk = 2
        # 1行をchunkに入っている数で区切って改行する
        # 行の残りがもう指定した数なければ残りを出力して次の行にいく
        line = read.read(chunk)
        print(line)
        # 読み込む行がなくなったらループを抜ける
        if not line:
            break
