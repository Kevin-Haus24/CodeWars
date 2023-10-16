def find_short(s):
    s = s.split()
    l = 1000000
    for i in s:
        if len(i) < l:
            l = len(i)

    return l