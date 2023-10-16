def pig_it(text):
    text = text.split()
    ans = ''
    for s in text:
        if (s == '!') or (s == '?'):
            ans += s + ' '
            return ans[:-1]
        s = s.__add__(s[0])
        ans += s[1:] + 'ay' + ' '
    return ans[:-1]
print(pig_it('Pig latin is cool !'))