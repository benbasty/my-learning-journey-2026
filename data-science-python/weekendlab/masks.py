import numpy as np

latency = np.array([82, 135, 95, 210, 178, 66, 142])
errors = np.array([0, 2, 0, 5, 1, 0, 3])
regions = np.array(["N", "S", "N", "W", "S", "W", "N"])

attention = ((latency >= 140) | (errors >= 3) | (regions != "W"))
# This function looks at our Boolean array and returns the indices of all True values.
selected = np.nonzero(attention)[0]

#print(selected, latency[attention])
# [0 1 2 3 4 6] [ 82 135 95 210 178 142]

#  Use elementwise & and |, and parenthesize every comparison.
#assert selected.tolist() == [4, 6]

# Fancy indexing

priority = np.array([6, 3, 1])
investigation = np.column_stack([
    priority,
    latency[priority],
    errors[priority],
])
scores = np.zeros(7, dtype=int)

# we have a list of "votes" happening at
# specific sites: [1, 1, 4, 6, 6, 6].
# We need to add 1 to the scoreboard at each of those sites.
# We use np.add.at to make sure every single occurrence counts.
# Because index 1 appears twice and index 6 appears three times,
# they get multiple additions.
np.add.at(scores, [1, 1, 4, 6, 6, 6], 1)
assert scores.tolist() == [0, 2, 0, 0, 1, 0, 3] #✅

# print(priority)
# print(investigation)
# print(scores)

# sort, rank & structure

# This doesn't sort the values;
# it sorts the indices that would put the array in ascending order.
order = np.argsort(latency) # ascending positions
# partially sorts
# guarantees that the element at the -3 (third from last) position
# is in its correct sorted position.
# Everything to its left is smaller, everything to its right is larger
top3 = np.argpartition(latency, -3)[-3:]

# latency[top3] pulls out the actual latency values of our top 3: [142, 178, 210]
# np.argsort(latency[top3]) => [142, 178, 210] sorted ascending gives indices [0, 1, 2]
# [::-1] reverses that to [2, 1, 0]
# top3[[2, 1, 0]] reshuffles [6, 4, 3] into [3, 4, 6]
top3 = top3[np.argsort(latency[top3])[::-1]]

# We have a 7-row table with named columns, all initialized to zeros/empty strings.
# dtype=[(...)] defines the columns
# left side:  name, right side: value
events = np.zeros(7, dtype=[
    ("region", "U1"),
    ("latency_ms", "i4"),
    ("errors", "i2"),
])
events["region"] = regions
events["latency_ms"] = latency
events["errors"] = errors

# events["region"] = regions fills the "region" column with ["N", "S", "N", "W", "S", "W", "N"]
# events["latency_ms"] = latency and events["errors"] = errors

# This sorts a structured array
# by order: ascending errors first then latency_ms
# then reversing the sorted array [::-1]
ranked = np.sort(events, order=["errors", "latency_ms"])[::-1]
print(ranked[:3]) # Prints the top 3 rows of the ranked table.