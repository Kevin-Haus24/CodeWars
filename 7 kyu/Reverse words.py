def reverse_words(text):
    a = ' '
    if '  ' in text:
        ans = text.split()
        for i in range(len(ans)):
            ans[i] = ans[i][::-1]
        return a.join(ans).replace(' ', '  ')
    else:
        ans = text.split()
        for i in range(len(ans)):
            ans[i] = ans[i][::-1]
        return a.join(ans)
print(reverse_words('double  spaced  words'))