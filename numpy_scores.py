

import numpy as np


### TASK 1

np.random.seed(42)

scores = np.random.randint(50, 101, size=(5,4))

print(f"{scores=}")
print(f"Score of 3rd Student in 2nd Subject: {scores[2][1]}")
print(f"All scores of the last 2 students: {scores[-2:]}")
print(f"All scores for the first 3 students in subjects 2 and 3 only: {scores[:3, 1:3]}")

### TASK 2

mean = scores.mean(axis=0)
print(f"Column wise mean: {np.round(mean, 2)}")

curved_scores = np.minimum(scores + np.array([5,3,7,2]) , 100)


print(f"{curved_scores=}")
row_wise_max = curved_scores.max(axis=1)
print(f"{row_wise_max=}")

### TASK 3
max_row_values = curved_scores.max(axis=1, keepdims=True)
min_row_values = curved_scores.min(axis=1, keepdims=True)

normalized_scores = (curved_scores - min_row_values) / (max_row_values - min_row_values)

print(f"{normalized_scores=}")
highest_score = normalized_scores.max()

row, col = np.where(normalized_scores == highest_score)

print(f"Student Index: {row[0]}, Subject Index: {col[0]} ... (These are the indices for first occurence)")

high_scores = curved_scores[curved_scores > 90]

print(f"Scores greater than 90: {high_scores}")
