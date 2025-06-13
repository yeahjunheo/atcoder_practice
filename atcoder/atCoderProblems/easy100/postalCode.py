a,b = map(int, input().split())
s = input()
for i in range(len(s)):
    if s[i] == '-' and i != a:
        print("No")
        exit()
    if i == a and s[i] != '-':
        print("No")
        exit()
print("Yes")