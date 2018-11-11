

# 継承
# 継承とは、あるクラスの機能を他のクラスが受け継ぐ(継承する)こと
# 受け継ぐ側のクラスが元のクラスの機能を拡張するイメージ

# 元となるクラスを宣言(基底クラス/親クラス)
class Car(object):
    def run(self):
        print('Run')


# ()の中に継承するクラスの名前を入れる
class ToyotaCar(Car):
    # pass -> 何もしない
    pass


class TeslaCar(Car):
    # 他のクラスを継承した上で、独自のメソッドを定義
    def auto_run(self):
        print('Auto Run')


if __name__ == '__main__':
    # Car()をインスタンス化
    car = Car()
    # Car()を継承しているToyotaCar()をインスタンス化
    toyota_car = ToyotaCar()
    # Car()を継承して独自メソッドを持っているTeslaCar()をインスタンス化
    tesla_car = TeslaCar()

    # Car()内に宣言されているrun()メソッドを呼び出す
    car.run()
    # Car()内に宣言されているrun()メソッドを呼び出す
    toyota_car.run()
    # ToyotaCarクラスにもrunメソッドが入っている！

    # 両方使える！
    tesla_car.run()
    tesla_car.auto_run()
