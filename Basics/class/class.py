

# 通常
class Person(object): # (object)はなくても良いが、コードスタイルとして○
    def say_something(self):
        print('Hello')




if __name__ == '__main__':
    # インスタンスの生成
    person = Person()
    # インスタンスのなかのメソッドを実行
    person.say_something()