"""Python的カプセル化"""
# まず、プログラミング言語にはカプセル化という重要な概念が存在する
# そしてこの概念はほとんどのプログラミング言語で実現可能である
# カプセル化とは、ある変数や関数を他の使用者から見えなくしたり
# 変更できなくすること
# これによりコードの安全性が上がる
# しかし、Pythonではこの機能は基本的にサポートしていない
# Pythonはそのユーザーが全員行儀よく言語を書くことを前提とした言語であるため実装されていない
# しかし、それでもやはり他のユーザーから隠したい、いじられたくない変数などはどうしても存在する
# そこで、「完全に隠匿はできないがそのように見せる」という機能は備わっている

class Person(object):
    def __init__(self, name=None, nick_name='Bar'):
        # 外から(インスタンス生成後)アクセスできないようにしたい場合は、
        # 「__(アンダースコア2つ)」をつけることでほぼ隠匿することができる
        self.__nick_name = nick_name
        self.greet(name)

    def greet(self, name):
        if name == None:
            print('Hello!')
        else:
            print('Hello {name}!'.format(name=name))
        # クラス内ではアクセスできる
        self.__nick_name = 'renamed nickname'


    # このほぼ隠匿された変数(プロパティと呼ばれる)を、読み取り専用にする
    @property
    def nick_name(self):
        return self.__nick_name

    # 読み取り専用を書き込みもできるようにする
    # この時、デコレータの「.setter」およびメソッド名は
    # getter(@propertyが装飾されているメソッド)と同じにする
    @nick_name.setter
    def nick_name(self, arg):
        self.__nick_name = arg


# このような機能があることで利点が多く得られる
# 例えば、読み取り専用にする@propertyは、読める(取り出せる)けどいじられるとプログラム
# 全体が困ってしまう(エラーなどが発生する可能性がある)時などに使える
# 書き込み可能にするにも、@propertyがなければできないため、書き込み専用のものは
# 作ることができないようになっている
# この仕組みのおかげで、例えば書き込まれたときにバリデーションチェックを行ったりすることができる




person = Person('Foo')
#person.__nicknameはエラーになる
#読み取り専用の関数は()がなくても呼び出せる
print(person.nick_name)
person.nick_name = 'fooboy'
print(person.nick_name)
