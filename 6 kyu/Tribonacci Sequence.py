def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 3:
        return [signature[i] for i in range(0, n)]
    box = signature[:]
    for i in range(3, n):
        box.append(box[i-1] + box[i-2] + box[i-3])
    return box

print(tribonacci([1, 1, 1], 10))