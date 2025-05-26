a,b,c = map(int,input().split())
max = b//a
if max >= c:
    print(c)
else:
    print(max)