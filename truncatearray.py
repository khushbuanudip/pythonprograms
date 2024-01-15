import numpy as np
data = np.array([3.14159, 2.71828, 1.61803])
# Round to 2 decimal places
result_round = np.round(data, 2)
# Truncate (remove decimal part)
result_trunc = np.trunc(data)
print("Rounded Values:", result_round)
print("Truncated Values:", result_trunc)
