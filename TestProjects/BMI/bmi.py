#def_bmi.pyにclass, while, try-exceptを使用してよりちゃんとしたプログラムにブラシアップ

class Body_Calculate(object):
    def __init__(self, *args, **kwargs):
        self.weight, self.height = self.get_weight_height()

    def get_weight_height(self):
        while True:
            try:
                weight = float(input('体重を入力してください'))
                break
            except:
                print('適正な値を入力してください')

        while True:
            try:
                height = input('身長を入力してください')
                if "." not in height:
                    height = int(height) / 100
                elif '.' in height:
                    height = float(height)
                break
            except:
                print('適正な値を入力してください')

        print('体重: {weight}kg'.format(weight=weight))
        print('身長: {height}m'.format(height=height))
        return (weight, height)





if __name__ == '__main__':
    body_cal = Body_Calculate()

