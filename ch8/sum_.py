
marbles = [ 10, 13, 39, 14, 41, 9, 3 ]
print("<python sum>: ", sum(marbles))

def my_sum(lists):
    total_sum = 0
    for num in lists:
        total_sum = total_sum + num
    return total_sum

print("<for, while sum>: ", my_sum(marbles))

def recursive_sum(lists):

    total_sum = 0

    if len(lists) == 0:
        return 0
    else:
        first = lists[0]
        rest = lists[1:]
        total_sum = first + recursive_sum(rest)
        return total_sum

print("<recursive_sum>: ", recursive_sum(marbles))
