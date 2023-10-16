def spin_words(sentence):
    ans = ''
    for a in sentence.split():
        if len(a) >= 5:
            ans += f'{a[::-1]} '
        else:
            ans += f'{a} '
    return ans.strip()

print((spin_words("Hey fellow warriors")))