# base_level_bmi.pyの記述を、defを使ってオブジェクト指向よりにしたもの

from decimal import Decimal as decimal


def ask_wgt_hgt():
    weight = float(input('体重を入力してください'))
    height = input('身長を入力してください')
    if "." not in height:
        height = int(height) / 100
    elif '.' in height:
        height = float(height)

    return (weight, height)


def show_wgt_hgt(wgt_hgt):
    weight, height = wgt_hgt
    print('体重: {weight}kg'.format(weight=weight))
    print('身長: {height}m'.format(height=height))


def show_BMI(wgt_hgt):
    weight, height = wgt_hgt
    # BMI計算式: 体重kg÷(身長m)^2
    bmi = weight / (height ** 2) # Pythonにおけるべき乗の計算は m ** n
    # 同じ変数に小数第二位までのbmiを代入
    bmi = decimal(bmi).quantize(decimal('0.01'))
    print('BMI: {bmi}'.format(bmi=bmi))


def show_suitable_weight(wgt_hgt):
    weight, height = wgt_hgt
    suitable_weight = (height ** 2) * 22
    suitable_weight = decimal(suitable_weight).quantize(decimal('0.01'))
    print('適正体重: {suitable_weight}kg'.format(suitable_weight=suitable_weight))
    print('適正体重より: +{over_weight}'.format(over_weight=decimal(weight) - suitable_weight))
    




if __name__ == '__main__':
    wgt_hgt = ask_wgt_hgt()
    show_wgt_hgt(wgt_hgt)
    show_BMI(wgt_hgt)
    show_suitable_weight(wgt_hgt)



