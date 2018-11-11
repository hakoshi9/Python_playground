from decimal import Decimal as decimal

# [全体メモ]
# inputは必ず文字列型として扱われるため、型変換が必要
# floatとDecimalは計算ができない
# 


# weight = 92.5
# height = 180
weight = input('体重を入力してください')
weight = float(weight)


height = input('身長を入力してください')
if "." not in height:
    height = int(height) / 100
elif '.' in height:
    height = float(height)


# print(weight)
# print(height)


# BMI計算式: 体重kg÷(身長m)^2
bmi = weight / (height ** 2) # Pythonにおけるべき乗の計算は m ** n
# 同じ変数に小数第二位までのbmiを代入
bmi = decimal(bmi).quantize(decimal('0.01'))
# 小数点の操作は、組み込み型ではround(値, 桁数)
# 標準ライブラリではdecimalをimportして、quantize()関数を呼び出す。
# quantize()は第一引数に桁数を、第二引数に値を入れる。しかしこのとき、桁数は0.1, 0.01のように表現する

# round()。こちらは偶数に寄せて四捨五入してしまうため、正確な四捨五入をしたいときは推奨されない
# print(round(bmi, 2))
# Decimal(対象の値).quantize(decimal('桁数の少数'))。
# こちらは正確な四捨五入を返してくれるが、全体的に特殊な記法となっている。
# また、普通の小数点型ではエラーになる
# print(decimal(bmi).quantize(decimal('0.01')))


# 適正体重: 適正体重＝ (身長m)^2 ×22
suitable_weight = (height ** 2) * 22
suitable_weight = decimal(suitable_weight).quantize(decimal('0.01'))
# print(suitable_weight)

# print('適正体重より:', '+' + str(weight - suitable_weight))


print('体重: {weight}kg'.format(weight=weight))
print('身長: {height}m'.format(height=height))
print('BMI: {bmi}'.format(bmi=bmi))
print('適正体重: {suitable_weight}kg'.format(suitable_weight=suitable_weight))
print('適正体重より: +{over_weight}'.format(over_weight=decimal(weight) - suitable_weight))