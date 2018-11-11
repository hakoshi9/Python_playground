"""ファイルの作成"""
# ファイルを作成するにはopen()関数を使用する
# 第一引数にファイル名、第二引数にモード(読み込み/書き込み)
f = open('file_one.txt', 'w')
# write()メソッドでファイルに書き込むものを指定
f.write('This is my first file I have created from Python\n')
#書き込みはprint文を使ってもできる
print('My name is Foo Bar', file=f)
# open()をしたら「必ず」close()する
f.close()

# この時、「w」モードはファイル全体を上書きしてしまうことを覚えておいてください
# 追加書き込みをしたい場合は「a」モードを使う
add_f = open('file_one.txt', 'a')
add_f.write('\nAdded')
add_f.close()


# 読み込みだけ行いたい場合は「r」モード
#この時、ファイルはディレクトリを指定する必要がある
read = open('file_one.txt', 'r')
print(read.read())
read.close()
