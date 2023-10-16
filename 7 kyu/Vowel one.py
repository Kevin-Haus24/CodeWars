def vowel_one(s):
    glas = ['a','e','i','o','u','A','E','I','O','U']
    st = ''
    for i in s:
        if i in glas:
            st += '1'
        else:
            st += '0'
    return st

print(vowel_one('vowelOne'))