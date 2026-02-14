TEST_CASES = [
    # ("""input""","""output""")
    (
        """7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6""",
        """63 261""",
    ),
    (
        """7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
10
1 3
2 4
3 5
4 6
5 7
1 5
2 6
3 7
1 6
2 7""",
        """72 172
23 172
23 183
63 89
115 89
95 261
63 261
138 183
135 261
138 261""",
    ),
    (
        """1
1 100
3
1 1
1 1
1 1
""",
        """100 0
100 0
100 0""",
    ),
    (
        """20
2 90
1 67
2 9
2 17
2 85
2 43
2 11
1 32
2 16
1 19
2 65
1 14
1 51
2 94
1 4
1 55
2 90
1 89
1 35
2 81
20
3 17
5 5
11 11
8 10
3 13
2 6
3 7
3 5
12 18
4 8
3 16
6 8
3 20
1 12
1 6
5 16
3 10
17 19
4 4
7 15
""",
        """175 430
0 85
0 65
51 16
116 246
67 154
0 165
0 111
213 184
32 156
175 340
32 54
299 511
132 336
67 244
175 314
51 181
124 90
0 17
120 186""",
    ),
]

def solve():
    N = int(input())
    class1_prefix = [0] * (N + 1)
    class2_prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        C, P = map(int, input().split())
        class1_prefix[i] = class1_prefix[i - 1] + (P if C == 1 else 0)
        class2_prefix[i] = class2_prefix[i - 1] + (P if C == 2 else 0)
    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        total_class1 = class1_prefix[R] - class1_prefix[L - 1]
        total_class2 = class2_prefix[R] - class2_prefix[L - 1]
        print(total_class1, total_class2)

# This one caused TLE on Atcoder... most likely due to the sum in the loop.
# Better way would be to use prefix sums to answer the queries in O(1) time each.
# def solve():
#     # do stuff with the input class and scores
#     N = int(input())
#     classScores = {1: [0] * N, 2: [0] * N}
#     for i in range(N):
#         C, P = map(int, input().split())
#         classScores[C][i] = P
#     # do stuff with the queries and what we know
#     Q = int(input())
#     for _ in range(Q):
#         L, R = map(int, input().split())
#         result = []
#         for c in (1, 2):
#             total = sum(classScores[c][L - 1 : R])
#             result.append(str(total))
#         print(" ".join(result))
