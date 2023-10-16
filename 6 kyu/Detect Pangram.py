from collections import Counter
import string
def is_pangram(s):
    alph = string.ascii_lowercase
    count = Counter(s.lower())
    ans = 0
    for al in alph:
        if al in count:
            ans += 1
    return ans == len(alph)


print(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)
