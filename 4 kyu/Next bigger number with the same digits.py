import itertools
def next_bigger(n):
    alphabet = str(n)
    ar = itertools.permutations(alphabet[-5:])
    arl = []
    for i in ar:
        arl.append(''.join(i))
    for j in range(len(arl)):
        arl[j] = int(str(alphabet[:-5]) + str(arl[j]))
    arl.sort()
    for q in arl:
        if q > n: return q
    return -1
    #     y = sorted(set(arl), key=lambda d: arl.index(d))
    #     for j in range(len(y) - 1):
    #         if int(y[j+1]) > n: return int(y[j+1])
    #         return -1


print(next_bigger(59884848459853))
