def ranges(a, b): return f'{a}-{b}'

def solution(args):
    args.append(10**5)
    args = sorted(args)
    prom = []
    for i in range(len(args)-1):
        if abs(args[i] - args[i + 1]) == 1:
            prom.append(args[i:i+2])
        else: prom.append(args[i])

    for k in range(len(prom) - 2):
        if type(prom[k + 1]) == list and type(prom[k]) == int and type(prom[k + 2]) == int:
            prom[k + 1] = prom[k + 1][0]
        if type(prom[0]) == list and type(prom[1]) == int:
            prom[0] = prom[0][0]

    try:
        for j in range(len(prom)):
            while type(prom[j]) == list and type(prom[j + 1]) == list:
                if prom[j][1] == prom[j+1][0]:
                    prom[j][1] = prom[j+1][1]
                    del prom[j+1]
            if type(prom[j]) == list:
                if prom[j][1] == prom[j+1]: del prom[j+1]
    except IndexError: pass

    answer = ''
    for x in prom:
        if type(x) == list:
            answer += f'{ranges(x[0], x[1])},'
        else: answer += f'{str(x)},'
    return answer[:-1]

print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
print(solution([-57, -55, -52, -50, -48, -47, -45, -43, -40, -37, -36, -35, -34, -32, -30]))
print(solution([-68, -67, -64, -62, -61, -58, -56, -55, -52, -51, -49, -47, -44, -43, -40, -38, -35]))
print('-68,-67,-64,-62,-61,-58,-56,-55,-52,-51,-49,-47,-44,-43,-40,-38,-35')