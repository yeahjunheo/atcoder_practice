TEST_CASES = [
    # ("""input""","""output""")
    (
        """6 7 1
1 2 3 4 5 6
""",
        """1""",
    ),
    (
        """10 1 0
0 0 0 0 0 0 0 0 0 0
""",
        """252""",
    ),
]

def solve():
    from itertools import combinations
    from functools import reduce
    N,P,Q = map(int,input().split())
    A = list(map(int, input().split()))
    count = 0
    for item in combinations(A,5):
        if reduce(lambda x,y: x*y%P, item) == Q:
            count += 1
    print(count)



# def solve():
#     N,P,Q = map(int, input().split())
#     A = list(int(num) for num in input().split())
#     count = 0
#     for i in range(N):
#         for j in range(i+1, N):
#             p2 = A[i] * A[j] % P
#             for k in range(j+1, N):
#                 p3 = A[k] * p2 % P
#                 for l in range(k+1, N):
#                     p4 = A[l] * p3 % P
#                     for m in range(l+1, N):
#                         p5 = A[m] * p4 % P
#                         if p5 == Q:
#                             count += 1
#     print(count)