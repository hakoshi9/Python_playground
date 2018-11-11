
# クラスの初期化
class Person(object):
    # __init__で初期化
    # __init__で書いた処理が最初に処理される
    def __init__(self):
        print('First')

    def say_something(self):
        print('Hello')



class AnotherPerson(object):
    def __init__(self, name):
        # これを特にクラス変数と呼ぶ。クラス変数はインスタンス化されたときにそのインスタンスが独自に保持する値
        self.name = name
        print(self.name)

    def say_hello(self):
        print('I am {}. Hello:)'.format(self.name))
    




if __name__ == '__main__':
    person = Person()
    # 初期化をするにはインスタンス生成時に値をクラスに渡す
    another_person = AnotherPerson('Joshua')
    another_person.say_hello()