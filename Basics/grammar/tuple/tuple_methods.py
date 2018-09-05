

# タプルの合計値
tuple3 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
sumTuple3 = sum(tuple3)
print('tuple3:', tuple3)
print('tuple3の合計値:', sumTuple3)



# タプルをソート
numTuple = 5, 3, 1, 9, 6, 7, 4, 8, 2
#これではリストになってしまう
sortNum = sorted(numTuple)
#tupleに変換
sortTuple = tuple(sortNum)
print('numTupleをソート:', sortTuple)