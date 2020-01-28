
strings = [ 'coconut', 'strawberry', 'banana', 'pineapple' ]

print("bubble_sort before: ", strings)

swapped = True

while swapped == True:
    swapped = False
    for i in range(0, len(strings) - 1):
        if strings[i] < strings[i+1]:
            tmp = strings[i]
            strings[i] = strings[i+1]
            strings[i+1] = tmp
            swapped = True

print("bubble_sort after: ", strings)
