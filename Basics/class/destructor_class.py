

# デストラクタ
class Person(object):
    #これはコンストラクタと呼ばれる
    #初めに作るもの
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('I am {}. Hello everyone:)'.format(self.name))

    #コンストラクタはそのオブジェクトが作られるときに呼ばれるが、
    #オブジェクトが使われなくなったときに呼び出せるメソッドも存在する
    #それをデストラクタと呼び、__del__(self)と記述する
    def __del__(self):
        print('goodbye')





if __name__ == '__main__':
    person = Person('Joshua')
    person.say_hello()

    print('################')
    #printのあとにpersonというオブジェクトがもうないことをPythonが感知しオブジェクトを消す
    #そのためデストラクタが実行される


    #では意図的にデストラクタを実行させるには？
    #del person