
nums = {}

def store_num(n):
    if n not in nums:
        nums[n] = 1
    else:
        value = nums[n]
        value = value + 1
        nums[n] = value

def fibonacci(n):
    if n == 0:
        store_num(n)
        return 0
    elif n == 1:
        store_num(n)
        return 1
    else:
        store_num(n)
        return fibonacci(n-1) + fibonacci(n-2)

value = int(input("Give a fibonacci number: "))
print("fibonacci(", value, ") = ", fibonacci(value))

for num in nums:
    print(num, " found ", nums[num], " times")

print("nums: ", nums)

