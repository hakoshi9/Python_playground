"""クラスメソッドとスタティックメソッド"""
# クラスメソッドやクラス変数は、そのクラスがインスタンス化されていなくてもアクセスすることができる
# スタティックメソッドはクラスメソッドと動きはあまり変わらない

class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    def what_is_your_kind(self):
        return self.kind

    # インスタンス化しなくてもメソッドにアクセスできるようにするデコレータ
    # この時、selfではなくclsと書く
    @classmethod
    def what_is_your_type(cls):
        return cls.kind

    # selfすらいらない
    @staticmethod
    def about(year):
        print('@staticmethod: about human {}'.format(year))



a = Person()
print(a.kind)
b = Person
# print(b.kind)
# aはインスタンス化しているため、クラスメソッドkindにもプロパティxにもアクセスできる
# しかしbはインスタンス化していないため、クラスメソッドkindにはアクセスできるがプロパティxにはアクセスできない

#こちらも同様。インスタンス化されていないbはメソッドにアクセスすることができない
print(a.what_is_your_kind())
#print(b.what_is_your_kind())

#@classmethodをつけたメソッドは呼び出せる
print('@classmethod:', a.what_is_your_type())
print('@classmethod:', b.what_is_your_type())

Person.about(1995)