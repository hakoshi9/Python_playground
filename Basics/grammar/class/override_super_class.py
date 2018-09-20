
# オーバーライドとsuper()

#[オーバーライド]
#継承先のクラスで継承元のメソッドを上書きすること
#やり方として、継承先のクラスで継承元のクラスにあるメソッドを再定義する


#基底クラス
class Car(object):
    def __init__(self, model=None):
        self.model = model
        
    def run(self):
        print('Run')

 
#基底クラスを継承したクラス
class TeslaCar(Car):
    #オーバーライド
    def run(self):
        print('Runs Super Fast')


class JoshuaCar(Car):
    pass



#[super()]
#基底クラスのプロパティやメソッドを呼び出す
#オーバーライドされたものではなく元のプロパティやメソッドを呼び出すことができる





if __name__ == '__main__':
    car = Car('Regular Car')
    tesla_car = TeslaCar("Electric Car")
    joshua_car = JoshuaCar()

    #[オーバーライドの実演]
    #carのrun()を実行
    #-> Run
    car.run()
    #tesla_carのrun()を実行
    #-> Runs Super Fast
    tesla_car.run()

    print('####################')

    #[super()の実演]
    print(car.model)
    print(tesla_car.model)
    print(joshua_car.model)