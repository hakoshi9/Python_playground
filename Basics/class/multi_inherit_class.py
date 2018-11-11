"""多重継承"""
# Pythonでは、クラスの多重継承をサポートしている
# 多重継承とはその字の通りで、クラスを他のクラスを継承する際、
# 1つに限らず複数同時に継承すること
# しかし、多重継承はなるべくないに越したことはない
# バグの元になるので、開発が大きくなり多重継承していないと
# 書く量が増えてしまうなどでない場合はしないほうが良い

class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('@Person: run')


class Car(object):
    def run(self):
        print('@Car: run')


# 上記2つのクラスを1つのクラスが継承する
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')


# インスタンス化
person_car_robot = PersonCarRobot()
person_car_robot.talk()
# 2つのクラスに同じ名前のメソッドがある場合、一番最初に継承されたクラスにあるメソッドが適用される
person_car_robot.run()
person_car_robot.fly()



# 上記2つのクラスを1つのクラスが継承する
class PersonCarRobot2(Car, Person):
    def fly(self):
        print('fly')


person_car_robot2 = PersonCarRobot2()
person_car_robot2.talk()
# こちらはCarを先に継承しているため、Carクラス側のrun()メソッドが実行される
person_car_robot2.run()
person_car_robot2.fly()