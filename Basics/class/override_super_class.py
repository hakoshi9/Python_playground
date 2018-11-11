"""クラスのオーバーライドとsuper()"""
# オーバーライドとsuper()

# 基底クラス
class Car(object):
    def __init__(self, model=None):
        self.model = model
        print(model)
        
    def run(self):
        print('Run')


car = Car('Regular Car')
car.run()

print('# # # # # # # # # # # # # # # # # # # # ')

# [オーバーライド]
# 継承先のクラスで継承元のメソッドを上書きすること
# やり方として、継承先のクラスで継承元のクラスにあるメソッドを再定義する
# つまり同じ名前の関数を宣言すればオーバーライドされる
class ToyotaCar(Car):
    #オーバーライド
    def run(self):
        print('Runs fast')


toyota_car = ToyotaCar('Toyota Car')
toyota_car.run()

print('# # # # # # # # # # # # # # # # # # # # ')

# [super()]
# 基底クラスのプロパティやメソッドを呼び出す
# オーバーライドされたものではなく元のプロパティやメソッドを呼び出すことができる
# 基底クラスを継承したクラス
class TeslaCar(Car):
    #__init__をオーバーライドしてしまっているため、デフォルトであるprint()の部分が使えない
    def __init__(self, model=None):
        #親クラスの__init__を、super()を使って直接呼び出す
        super().__init__(model)
    # オーバーライド
    def run(self):
        print('Runs Super Fast')

    #独自関数の宣言
    def auto_run(self):
        print('Auto Run')


tesla_car = TeslaCar('Tesla Car')
tesla_car.run()
tesla_car.auto_run()
#TeslaCarのmodelを呼び出す