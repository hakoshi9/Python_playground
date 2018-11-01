"""通常"""
x = -10
if x < 0:
    print('negative')


"""if-else"""
y = 10
if x < 0:
    print('negative')
else:
    print('positive')


"""elif"""
name = 'Ted'
if len(name) < 5:
    print('Less then 5 letters')
elif len(name) < 10:
    print('Less then 10 letters')
else:
    print("More then 10 letters:", len(name)-1, 'letters')