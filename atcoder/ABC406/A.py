A,B,C,D = map(int, input().split())
if A == C:
    if B >= D:
        print("Yes")
    else:
        print("No")
elif A > C:
    print("Yes")
else:
    print("No")