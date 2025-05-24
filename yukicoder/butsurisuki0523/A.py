N = int(input())
birthdays = dict()

for i in range(N):
    A,B = map(int,input().split())
    if A in birthdays:
        if B in birthdays[A]:
            print("Yes")
            exit()
        else:
            birthdays[A].append(B)
    else:
        birthdays[A] = [B]
print("No")