def compute(x, y):
    total = x + y
    if (total > 10) :
        total = 10
    return total

ret = compute(2, 3)
print('compute(2, 3) is ', ret)
ret = compute(11, 3)
print('compute(11, 3) is ', ret)
