import numpy as np

###############################################
def avg(score):
    total = 0
    for s in range(len(score)):
        total += score[s]
    return total / len(score)
###############################################
def big_avg(score):
    avg_score = avg(score)
    uppers = np.array([])
    for s in range(len(score)):
        if score[s] > avg_score:
            uppers = np.append(uppers, score[s])
    return uppers
###############################################
def small_avg(score):
    avg_score = avg(score)
    lowers = np.array([])
    for s in range(len(score)):
        if score[s] < avg_score:
            lowers = np.append(lowers, score[s])
    return lowers
###############################################

score = np.empty(10)
for s in range(10):
    score[s] = float(input("Enter score : "))

print("The average score is: ", avg(score))
print("Scores above average: ", big_avg(score))
print("Scores below average: ", small_avg(score))