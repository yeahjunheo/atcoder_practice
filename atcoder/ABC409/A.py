n = int(input())
t = input()
a = input()
for i in range(n):
    if t[i] == 'o' and a[i] == 'o':
        print('Yes')
        exit()
print('No')