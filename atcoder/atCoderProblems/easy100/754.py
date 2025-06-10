s = input()
res = float('inf')
for i in range(len(s)-2):
    temp = s[i:i+3]
    diff = abs(int(temp) - 753)
    res = min(res, diff)
print(res)