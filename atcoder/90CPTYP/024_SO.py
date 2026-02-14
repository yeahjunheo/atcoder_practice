TEST_CASES = [
    # ("""input""","""output""")
    (
        """2 5
1 3
2 1""",
        """Yes""",
    ),
    (
        """3 1
7 8 9
7 8 9""",
        """No""",
    ),
    (
        """7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7""",
        """Yes""",
    ),
]

def solve():
    N, K = map(int, input().split())
    listA = list(input().split())
    listB = list(input().split())

    for _ in range(N):
        diff = abs(int(listA.pop()) - int(listB.pop()))
        K -= diff
    
    if K < 0:
        print("No")
    elif K%2==1:
        print("No")
    else:
        print("Yes")