def exp_sum1(n):
    memo =[0] * (n + 1)
    memo[0] = 1
    for i in range(1, n):
        for j in range(i , n + 1):
            memo[j] +=  memo[j-i]
    return memo[n] + 1
print(exp_sum1(10))

def exp_sum(n):
    memo = {}

    def count_partitions(target, max_num):
        if target == 0:
            return 1
        if target < 0 or max_num == 0:
            return 0

        if (target, max_num) in memo:
            return memo[(target, max_num)]

        with_max_num = count_partitions(target - max_num, max_num)
        without_max_num = count_partitions(target, max_num - 1)

        memo[(target, max_num)] = with_max_num + without_max_num
        return memo[(target, max_num)]

    return count_partitions(n, n)

# Пример использования
result = exp_sum(10)
print(result)  # Вывод: 42