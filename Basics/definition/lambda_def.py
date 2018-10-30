

# ラムダ
daylist = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']
def change_words(words, func):
    for word in words:
        print('ラムダの実行:', func(word))
        
sample_func = lambda word: word.capitalize()
change_words(daylist, sample_func)