N = input()
if len(N) != 3:
    if int(N) >= 42:
        N = str(int(N) + 1)
    N = '0'*(3-len(N)) + N
print("AGC" + N)