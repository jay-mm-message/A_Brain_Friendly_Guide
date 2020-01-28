
def bubble_sort(data, numbers):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(0, len(data) - 1):
            if data[i] > data[i+1]:
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp

                tmp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = tmp

                swapped = True

scores = [  60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44 ]

solution_numbers = list(range(len(scores)))

print("bubble_sort before: ")
print("scores: ", scores)
print("solution_numbers: ", solution_numbers)
print()
print("bubble_sort after: ")
bubble_sort(scores, solution_numbers)
print("scores: ", scores)
print("solution_numbers: ", solution_numbers)


