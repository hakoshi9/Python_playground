

class Person(object):
    #__init__で初期化
    #__init__で書いた処理が最初に処理される
    def __init__(self):
        print('First')

    def say_something(self):
        print('Hello')



class AnotherPerson(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

    def say_hello(self):
        pass
    




if __name__ == '__main__':
    person = Person()
    #初期化をするにはインスタンス生成時に値をクラスに渡す
    another_person = AnotherPerson('Joshua')