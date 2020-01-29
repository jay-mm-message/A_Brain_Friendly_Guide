import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1, 25, 5):
    start_t = time.time()
    result = fibonacci(i)
    end_t = time.time()
    duration = end_t - start_t
    print("fib(", i, ") = ", result, ", duration time = ", duration)
