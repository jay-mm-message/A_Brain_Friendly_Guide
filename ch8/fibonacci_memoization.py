import time

cache = {}

nums = {}

def store_num(n):
    if n not in nums:
        nums[n] = 1
    else:
        value = nums[n]
        value = value + 1
        nums[n] = value

def fibonacci(n):
    global cache
    if n in cache:
        return cache[n]
    if n == 0:
        store_num(n)
        return 0
    elif n == 1:
        store_num(n)
        return 1
    else:
        store_num(n)
        result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

start = time.time()

for i in range(0, 101):
    result = fibonacci(i)
    print(i, result)

finish = time.time()
duration = finish - start
print("Computed all 100 in", duration, "seconds.")
#value = int(input("Give a fibonacci number: "))
#print("fibonacci(", value, ") = ", fibonacci(value))

#for num in nums:
#    print(num, " found ", nums[num], " times")

#print("nums: ", nums)


