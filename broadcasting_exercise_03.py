import numpy as np

# Generate random student scores (4 students, 5 subjects)
scores = np.random.randint(50, 100, (4, 5))

# Compute row-wise mean and standard deviation
row_means = scores.mean(axis=1, keepdims=True)
row_stds = scores.std(axis=1, keepdims=True)

# Normalize the scores
normalized_scores = (scores - row_means) / row_stds

print("Normalized Scores:\n", normalized_scores)
