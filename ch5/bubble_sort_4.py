
def bubble_sort(data):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(0, len(data) - 1):
            if data[i] > data[i+1]:
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp
                swapped = True

scores = [  60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44 ]

smoothies = [ 'coconut', 'strawberry', 'banana', 'pineapple' ]

print("bubble_sort before: ")
print("scores: ", scores)
print("smoothies: ", smoothies)
print()
print("bubble_sort after: ")
bubble_sort(scores)
bubble_sort(smoothies)
print("scores: ", scores)
print("smoothies: ", smoothies)
