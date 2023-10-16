import string
def find_missing_letter(chars):
    alph = string.ascii_lowercase + string.ascii_uppercase
    ind = alph.find(chars[0])

    ans = alph[ind:ind+len(chars)]

    for a, b in zip(chars, ans):
        if a != b: return b


print(find_missing_letter(['a','b','c','d','f']), 'e')
print(find_missing_letter(['O','Q','R','S']), 'P')

