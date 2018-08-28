
'''文字列の連結'''
str1 = "Python"
str2 = "3.6"
str3 = str1 + str2
print('str1とstr2を連結させたstr3:', str3)


'''リスト/タプルを文字列へ連結'''
list1 = ['This', 'is', 'a', 'test']
tuple1 = ('One', 'Two', 'Three')
str4 = ' '.join(list1)
str5 = ','.join(tuple1)
print('list1を空白を使って連結:', str4)
print('tuple1を,を使って連結:', str5)


