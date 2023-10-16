def decipher_this(s):
    s = s.split()
    ans = ''
    for i in s:
        if i.isdigit():
            ans += f'{chr(int(i))} '
        else:
            digit = ''
            char = ''
            for j in i:
                if j.isdigit():
                    digit += j
                else:
                    char += j
            perl = chr(int(digit)) + char[::-1]
            if len(perl) >= 6:
                l = list(perl)
                for n in range(2, (len(perl) // 2) + 1):
                    l[n], l[-n] = l[-n], l[n]
                ans += ''.join(l)+' '
            if len(perl) == 5:
                l = list(perl)
                l[2], l[-2] = l[-2], l[2]
                ans += ''.join(l) + ' '
            elif len(perl) < 5:
                ans += f'{chr(int(digit))}{char[::-1]} '
    return ans.rstrip()
print(decipher_this("108 102yl 73BoDxr 70QIneq 78QvHEGkhK 68ZyDBrg 119GDq 65mKWVrZKuH 70XQDrRkZTuNy"))

# 111GHr 68eRaWZecYm 112eqmw 122bgKEJePIkp 71I 121ZdyTbxs 81NbNcG 98KRv
# l fly IroDxB FqIneQ NKvHGEkhQ DgyBDrZ wqDG AHKWVrZKum FyQDrRkZTuNX
# l fly IroDxB FqIneQ NKvHEGkhQ DgyDBrZ wqDG AHKWVrZKum FyQDrRkZTuNX