s = input()
s = set(s)
for i in range(26):
    if chr(ord('a') + i) not in s:
        print(chr(ord('a') + i))
        exit()
print("None")