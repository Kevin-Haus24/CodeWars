def color_2_grey(image):
    ans = []
    answer = []
    for j in image:
        for i in range(len(image)):
            q = [sum(j[i])//3, sum(j[i])//3, sum(j[i])//3]
            ans.append(q)
    for i in range(0, len(ans) - 1, 4):
        answer.append([ans[i]] + [ans[i+1]])
        answer.append([ans[i+2]] + [ans[i+3]])
    return answer

print(color_2_grey([[[123,231,12],[56,43,124]],[[78,152,76],[64,132,200]]]))
print([[[122,122,122],[74,74,74]],[[102,102,102],[132,132,132]]])
print()
print(color_2_grey([[[88, 110, 23]], [[93, 53, 35]], [[59, 65, 5]], [[184, 194, 2]]]))
print([[[88, 110, 23]], [[93, 53, 35]], [[59, 65, 5]], [[184, 194, 2]]])