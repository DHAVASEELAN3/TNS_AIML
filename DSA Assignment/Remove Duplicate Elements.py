arr = [10, 20, 10, 30, 20, 40, 30]
result = []
for i in arr:
    if i not in result:
        result.append(i)
print(result)