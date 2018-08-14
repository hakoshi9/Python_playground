"""リストで遊ぶ"""
myList = []

#通常の要素追加
myList.append('Destiny2')
myList.append('Borderlands2')
print(myList)

#+=で複数の値を一度に追加
myList += 'Fallout4', 'Biohazard7'
print(myList)

#extend()で複数の値を一度に追加。これの場合は複数の値をリストにする必要がある
myList.extend(["Assassin's Creed4: Black flag", 'Titan Fall2'])
print(myList)