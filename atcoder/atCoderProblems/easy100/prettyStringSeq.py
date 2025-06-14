w = input()
counter = dict()
for c in w:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1
for key,v in counter.items():
    if v%2 != 0:
        print("No")
        exit()
print("Yes")