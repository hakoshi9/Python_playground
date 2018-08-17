"""リストで遊ぶ"""
gameList = []


"""通常の要素追加"""
gameList.append('Destiny2')
gameList.append('Borderlands2')
print(gameList)


"""+=で複数の値を一度に追加"""
gameList += 'Fallout4', 'Biohazard7'
print(gameList)


"""extend()で複数の値を一度に追加。これの場合は複数の値をリストにする必要がある"""
#リストを別のリストと結合する時に使える
gameList.extend(["Assassin's Creed4: Black flag", 'Titan Fall2'])
print(gameList)


"""リストの要素数を調べる"""
listCount = len(gameList)
print(listCount)


"""リストの中にある特定の要素が何個存在するかを数える"""
fruitList = ['Apple', 'Banana', 'Mango', 'Bluebarry', 'Apple', 'Apple', 'Mango']
appleCount = fruitList.count('Apple')
bananaCount = fruitList.count('Banana')
mangoCount = fruitList.count('Mango')
orangeCount = fruitList.count('Orange')
print('Apple:', appleCount)
print('Banana:', bananaCount)
print('Mango:', mangoCount)
print('Orange:', orangeCount)


"""どこから要素を持ってくるかを選べる"""
print('全て:', gameList[:])
print('index1からindex3の手前まで:', gameList[1:3])
print('最初からindex4手前まで:', gameList[:4])
print('index2から最後まで:', gameList[2:])


"""飛ばしてリストを取ってくる"""
jumpTwo = fruitList[::2]
print('偶数を飛ばす:',jumpTwo)


"""要素の書きかえ"""
fruitList[4] = 'Melon'
print('index4を書きかえ:', fruitList)
fruitList[1:4] = [1, 2, 3]
print('スライスによる書きかえ:', fruitList)


"""要素の削除"""
#[最後の要素を取り出して削除(取り出した値を受け取れる)]
fruitList.pop()
print('リストの最後の要素を取り出して削除:', fruitList)
#[指定した箇所の要素を取り出して削除(取り出した値を受け取れる)]
fruitList.pop(4)
print('指定した箇所の要素を取り出して削除:', fruitList)
#[通常の削除 del]
del fruitList[-1]
print('一番最後の要素をdelを使って削除(list[index]で要素を指定)', fruitList)
#[通常の削除 remove(要素)]
fruitList.remove(2)
print('特定の要素を指定して削除:',fruitList)


"""要素の挿入"""
gameList.insert(0, 'Colony Servival')
print('リストのindex0に要素を挿入:', gameList)


"""リストの中身の合計(全てが数値のとき)"""
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sumNumList = sum(numList)
print('リストの合計値:', sumNumList)
