# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.
# Example:

# h = 0
# m = 1
# s = 1

# result = 61000

# Input constraints:

#     0 <= h <= 23
#     0 <= m <= 59
#     0 <= s <= 59

def past(h, m, s):   
    total = 0
    if h >= 0 and h <= 23:
        total += h * 3600000
    if m >= 0 and m <= 59:
        total += m * 60000
    if s >= 0 and s <= 59:
        total += s * 1000
    return total