
strings = [ 'coconut', 'strawberry', 'banana', 'pineapple' ]

print("bubble_sort before: ", strings)

for loop in range(len(strings) - 1):
    for idx in range(len(strings) - 1):
        if idx < len(strings):
            if (strings[idx]) > (strings[idx + 1]):
                tmp = strings[idx]
                strings[idx] = strings[idx + 1]
                strings[idx + 1] = tmp

print("bubble_sort after: ", strings)
