import numpy as np

np.random.seed(42) # ensure we get the same random numbers every time.
scores = np.random.randint(0, 1000, size=1000) # Creates 1,000 random integers between 0 and 999.

# Step 1: Find the indices of the 10 largest scores
# We partition at -10, which guarantees the last 10 elements are the top 10
top10_indices_unsorted = np.argpartition(scores, -10)[-10:]
# argpartition is a partial sort. It rearranges the indices so that the element at position -10 (the 10th from the end) is in its correct sorted position.

# Step 2: Sort ONLY those 10 indices by their corresponding scores, descending
# Get the scores for these indices, argsort them (ascending), then reverse
top10_indices = top10_indices_unsorted[np.argsort(scores[top10_indices_unsorted])[::-1]]

# scores[top10_indices_unsorted]: Gets the actual scores of the top 10 (unsorted).
# np.argsort(...): Sorts these 10 scores ascending and returns their indices (0-9).
# [::-1]: Reverses it to get descending order.
# top10_indices_unsorted[...]: Uses this descending order to rearrange our indices into perfect rank order.
# Result: The indices of the top 10 scores, sorted from highest to lowest!