def zero(func=None): return 0 if func is None else func(0)
def one(func=None): return 1 if func is None else func(1)
def two(func=None): return 2 if func is None else func(2)
def three(func=None): return 3 if func is None else func(3)
def four(func=None): return 4 if func is None else func(4)
def five(func=None): return 5 if func is None else func(5)
def six(func=None): return 6 if func is None else func(6)
def seven(func=None): return 7 if func is None else func(7)
def eight(func=None): return 8 if func is None else func(8)
def nine(func=None): return 9 if func is None else func(9)

def plus(num): return lambda x: x + num
def minus(num): return lambda x: x - num
def times(num): return lambda x: x * num
def divided_by(num): return lambda x: x // num

print(four(plus(nine())), 13)
print(four(plus(four())), 8)
print(seven(times(five())), 35)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)