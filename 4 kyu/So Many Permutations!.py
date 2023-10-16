import itertools
def permutations(s):
    alphabet = s
    ar = itertools.permutations(alphabet)
    ans = []
    for i in ar:
        ans.append(''.join(i))
    x = list(set(ans))
    return x

a = sorted(permutations('aabb'))
if __name__ == '__main__':
    print(a)