"""テンプレートの使用"""
# テンプレートは、文字列の中に任意の文字列を埋め込む機能
# 埋め込みたい箇所に「$任意の名前」で、そこに文字列を埋め込むことができる

# stringをimportしてやる必要がある
import string

s = """\
Hi $name

$contents

Have a good day!
"""

# これで変数sがテンプレートとなる
inject = string.Template(s)
# substituteで埋め込み
# ここで使われているキーワード(name/contents)はテンプレート化
# した文字列の$が付いているもの
temp = inject.substitute(name='Foobar', contents='How are you?')
# 出力
print(temp)

# テンプレートは読み込み専用のような形で使う


# 下記が実際の使い方
# template-directory配下にemail_template.txtファイルを配置
# これを読み込んで使用する
with open('template-directory/email_template.txt') as read_only:
    template_file = string.Template(read_only.read())
    # このtemplate_fileはwithの外でも使える

write_email = template_file.substitute(name='Hoge', contents='We will have a meeting in half an hour.')
print(write_email)