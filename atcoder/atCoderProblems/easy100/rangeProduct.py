a,b = map(int, input().split())
if a <= 0 and b >= 0:
    print("Zero")
elif a > 0:
    print("Positive")
else:
    num = b - a + 1
    if num % 2 == 0:
        print("Positive")
    else:
        print("Negative")