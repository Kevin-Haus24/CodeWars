import string
def capitals(word):
    alph = string.ascii_uppercase
    ans = []
    for i in range(len(word)):
        if word[i] in alph: ans.append(i)
    return ans
print(capitals('boIycBWOYSLJUiyOOzeVgu'))