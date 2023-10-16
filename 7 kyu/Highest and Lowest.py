def high_and_low(numbers):
    st = [int(x) for x in numbers.split()]
    maxi = max(st)
    mini = min(st)
    return f'{maxi} {mini}'

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))