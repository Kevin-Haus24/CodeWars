def solution(n):
    ans = 0
    for i in range(1, n):
        if i % 3 == 0:
            ans += i
        elif i % 5 == 0:
            ans += i
    return ans
print(solution(10))