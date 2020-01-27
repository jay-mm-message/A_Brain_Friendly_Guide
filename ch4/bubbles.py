score = [ 60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44 ]

index = 0
total = len(score) - 1
Max_Bubble = 0
while index <= total:
    print("Bubble solution #", index, " score: ", score[index])

    if Max_Bubble < score[index]:
        Max_Bubble = score[index]
    index += 1

print("Bubble tests: ", len(score))
print("Highest bubble score: ", Max_Bubble)

