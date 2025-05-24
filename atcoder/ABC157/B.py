"""
B - Bingo
"""

bingo = [i for _ in range(3) for i in map(int, input().split())]
N = int(input())
B = list(int(input()) for _ in range(N))

for i in range(9):
    if bingo[i] in B:
        bingo[i] = 0

for i in range(3):
    if bingo[i*3] == 0 and bingo[i*3+1] == 0 and bingo[i*3+2] == 0:
        print("Yes")
        exit()
for i in range(3):
    if bingo[i] == 0 and bingo[i+3] == 0 and bingo[i+6] == 0:
        print("Yes")
        exit()
if (bingo[0] == 0 and bingo[4] == 0 and bingo[8] == 0) or \
    (bingo[2] == 0 and bingo[4] == 0 and bingo[6] == 0):
    print("Yes")
    exit()
print("No")