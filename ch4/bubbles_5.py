
scores = [ 60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44 ]

best_solutions = []
high_score = 0

length = len(scores)
for i in range(length):
    print('Bubble solution #' + str(i), 'score: ', scores[i])
    if high_score < scores[i]:
        high_score = scores[i]

for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)

print('Bubbles tests: ', length)
print('Highest bubble score: ', high_score)
print('Solutions with the highest score: ', best_solutions)
