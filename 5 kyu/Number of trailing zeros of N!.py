import math
def zeros(N):
    a = [5**x for x in range(1, 11)]
    ans = 0
    for i in a:
        ans += math.floor(N/i)
    return ans


print(zeros(0), 0, "Testing with n = 0")
print(zeros(6), 1, "Testing with n = 6")
print(zeros(30), 7, "Testing with n = 30")
print(zeros(1000))
print(zeros(100000), 7, "Testing with n = 30")