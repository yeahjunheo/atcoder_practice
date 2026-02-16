TEST_CASES = [
    # ("""input""","""output""")
    ("""2 3""", """2"""),
    ("""3 4""", """4"""),
    ("""3 6""", """6"""),
]


def solve():
    H, W = map(int, input().split())
    if H == 1 or W == 1:
        print(W if H == 1 else H)
    else:
        perH = (H-1)//2 + 1
        perC = (W-1)//2 + 1
        print(perH * perC)

'''
# . . . . #
. . . . . .
. . . . . .
. . . . . .
. . . . . .
# . . . . #
'''