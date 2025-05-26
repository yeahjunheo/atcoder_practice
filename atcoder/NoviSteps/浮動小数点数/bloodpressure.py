a,b = map(int,input().split())
c = (a-b)/3 + b
print(int(c) if c.is_integer() else c)