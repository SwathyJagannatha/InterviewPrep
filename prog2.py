s = "GeeksforGeeks"
d = {}
res = []

# Count characters
for c in s:
    d[c] = d.get(c, 0) + 1

# Find duplicate
for c, cnt in d.items():
    if cnt > 1:
        res.append(c)

print(res)