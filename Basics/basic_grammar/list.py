"""リストで遊ぶ"""
gameList = []

#通常の要素追加
gameList.append('Destiny2')
gameList.append('Borderlands2')
print(gameList)

#+=で複数の値を一度に追加
gameList += 'Fallout4', 'Biohazard7'
print(gameList)

#extend()で複数の値を一度に追加。これの場合は複数の値をリストにする必要がある
gameList.extend(["Assassin's Creed4: Black flag", 'Titan Fall2'])
print(gameList)

#リストの要素数を調べる
listCount = len(gameList)
print(listCount)

#リストの中にある特定の要素が何個存在するかを数える
fruitList = ['Apple', 'Banana', 'Mango', 'Bluebarry', 'Apple', 'Apple', 'Mango']
appleCount = fruitList.count('Apple')
bananaCount = fruitList.count('Banana')
mangoCount = fruitList.count('Mango')
orangeCount = fruitList.count('Orange')
print('Apple:', appleCount)
print('Banana:', bananaCount)
print('Mango:', mangoCount)
print('Orange:', orangeCount)

#どこから要素を持ってくるかを選べる
print('全て:', gameList[:])
print('index1からindex3の手前まで:', gameList[1:3])
print('最初からindex4手前まで:', gameList[:4])
print('index2から最後まで:', gameList[2:])

#要素の書きかえ

#要素の削除

#要素の挿入