arr = [1, 2, 3, 5, 6, 7]

n = 7

total = n * (n + 1) // 2

sum_arr = 0

for i in arr:
    sum_arr += i

missing = total - sum_arr

print("Missing Number:", missing)