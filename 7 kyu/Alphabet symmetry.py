import string
def solve(arr):
    alph = string.ascii_uppercase
    ans = []
    for i in range(len(arr)):
        count = 0
        ar = arr[i].upper()[:26]
        for w in range(len(ar)):
            if alph[w] == ar[w]: count += 1
            else: pass
            if IndexError: pass
        ans.append(count)
    return ans
print(solve(["IAMDEFANJYADSADASDASDASDASDUIUHGDJKL","thedefgh","xyzDEFghijabc"]))

'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
'IAMDEFANDJKL'
