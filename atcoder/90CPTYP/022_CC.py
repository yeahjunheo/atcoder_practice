TEST_CASES = [
    # ("""input""","""output""")
    ("""2 2 3""", """4"""),
    ("""2 2 4""", """1"""),
    (
        """1000000000000000000 999999999999999999 999999999999999998""",
        """2999999999999999994""",
    ),
]


def solve():
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    a, b, c = map(int, input().split())
    cube = gcd(gcd(a, b), c)
    print((a // cube) + (b // cube) + (c // cube) - 3)
