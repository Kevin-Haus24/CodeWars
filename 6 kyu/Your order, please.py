def order(sentence):
    text = sentence.split()
    ans = ''
    for i in range(1, len(text) + 1):
        for j in range(len(text)):
            if str(i) in text[j]:
                ans = ans + text[j] + ' '
                break
    return ans.strip()


print(order("is2 Thi1s T4est 3a"), "|Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"), "|Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""), "")