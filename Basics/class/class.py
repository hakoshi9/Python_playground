"""クラスの基礎"""
# クラスは、機能をまとめている関数をまとめる構文
# クラス内の関数は「メソッド」と呼ばれる

# クラスの宣言
# class クラス名(object):
#     メソッドやプロパティ
# ()ないのobjectは必要ない。しかしPython2からの慣例で書かれることが多い
class Person(object): # (object)はなくても良いが、コードスタイルとして○
    def say_something(self):
        print('Hello')



# インスタンスの生成
person = Person()
# インスタンスのなかのメソッドを実行
person.say_something()