t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = list(s)
    for i in range(n-1):
        if s[i] > s[i+1]:
            j = i+1
            while j < n and s[j] <= s[i]:
                j += 1
            s[i:j] = s[i+1:j] + [s[i]]
            break
    print(''.join(s))