
scores = [  60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44 ]

costs = [   .25, .27, .25, .25, .25, .25,
            .33, .31, .25, .29, .27, .22,
            .31, .25, .25, .33, .21, .25,
            .25, .25, .28, .25, .24, .22,
            .20, .25, .30, .25, .24, .25,
            .25, .25, .27, .25, .26, .29 ]

best_solutions = []
high_score = 0
cost = 100
most_effective = 0;

length = len(scores)
for i in range(length):
    print('Bubble solution #' + str(i), 'score: ', scores[i], ' cost: ', costs[i])
    if high_score < scores[i] and cost >= costs[i]:
        high_score = scores[i]
        cost = costs[i]
        most_effective = i

for i in range(length):
    if high_score == scores[i] and cost >= costs[i]:
        best_solutions.append(i)

print('Bubbles tests: ', length)
print('Highest bubble score: ', high_score, ' cost: ', cost)
print('Solutions with the highest score and low cost: ', best_solutions)
print('Solution', most_effective, 'is the most effective with a cost of ', cost)
