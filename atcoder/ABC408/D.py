t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    s = input()
    cases.append((n, s))

for n,s in cases:
    if s.count('1') == n or s.count('0') == n:
        print(0)
        continue
    ones = [len(x) for x in s.split('0') if x]
    zeros = [len(x) for x in s.split('1') if x]
    print(ones, zeros)

    if len(ones) == 1:
        print(0)
        continue
    if len(zeros) == 1:
        print(min(zeros[0], min(ones)))
        continue


    ones_change = sum(ones) - max(ones)
    zeros_change = sum(zeros) - max(zeros)
    print(ones_change, zeros_change)
    print(min(ones_change, zeros_change))