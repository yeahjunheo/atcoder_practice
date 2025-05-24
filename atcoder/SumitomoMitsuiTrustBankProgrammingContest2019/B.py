'''
A more mathematical approach to the problem
'''

N = int(input())
m = 25*N // 27

while m * 1.08 < N + 1:
    if int(m*27//25) == N:
        print(m)
        exit()
    m += 1
print(":(")

# N = int(input())
# X = int(N / 1.08)
# if int(X * 1.08) == N:
#     print(X)
# else:
#     X += 1
#     if int(X * 1.08) == N:
#         print(X)
#     else:
#         print(":(")