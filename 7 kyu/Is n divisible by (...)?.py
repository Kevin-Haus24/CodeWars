def is_divisible(*args):
    for i in args:
        if args[0] % i == 0:
            pass
        else: return False
    return True

print(is_divisible(3,3,4),False)
print(is_divisible(12,3,4),True)
print(is_divisible(8,3,4,2,5),False)