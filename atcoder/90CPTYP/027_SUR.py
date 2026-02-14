TEST_CASES = [
    # ("""input""","""output""")
    (
        """5
e869120
atcoder
e869120
square1001
square1001
""",
        """1
2
4
""",
    ),
    (
        """4
taro
hanako
yuka
takashi
""",
        """1
2
3
4
""",
    ),
    (
        """10
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
""",
        """1
""",
    ),
]

# def solve():
#     N = int(input())
#     res = []
#     users = set()
#     for i in range(N):
#         request = input()
#         if request in users:
#             continue
#         res.append(i+1)
#         users.add(request)
#     for i in res:
#         print(i)
    

def solve():
    N = int(input())
    users = set()

    for i in range(N):
        userID = input()
        if userID in users:
            continue
        users.add(userID)
        print(i+1)