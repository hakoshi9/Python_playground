"""アプリユーザーの基礎情報を保持しておくクラス"""
class UserInfo():
    """
    Holes users information what the users inputed

    Attributes:
        gender (int):
        age (int):
        weight (float):
        height (height):
    """
    def __init__(self):
        self.gender = self.ask_gender()
        self.age = self.ask_age()
        self.weight = self.ask_weight()
        self.height = self.ask_height()
        print(self.gender)
        print(self.age)
        print(self.weight)
        print(self.height)


    def ask_gender(self):
        print('あなたの性別を教えてください')
        while True:
            try:
                gender = int(input('[0. 男性    1. 女性]\n'))
                break
            except:
                print('数字で入力してください')
        return gender


    def ask_age(self):
        print('あなたの年齢を教えてください')
        while True:
            try:
                age = int(input())
                break
            except:
                print('数字で入力してください')
        return age


    def ask_weight(self):
        print('体重を入力してください')
        while True:
            try:
                weight = float(input())
                break
            except:
                print('適正な値を入力してください')
        return weight


    def ask_height(self):
        print('身長を入力してください')
        while True:
            try:
                height = input()
                if "." not in height:
                    height = int(height) / 100
                elif '.' in height:
                    height = float(height)
                break
            except:
                print('適正な値を入力してください')
        return height