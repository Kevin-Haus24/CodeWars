import string
def filter_list(l):
    alph = string.ascii_uppercase
    ans = []
    for x in l:
        try:
            if int(x) == x:
                ans.append(x)
        except: pass
    return ans

print(filter_list([1, 2, 'a', 'b']))

# def filter_list(l):
#   return [i for i in l if not isinstance(i, str)]