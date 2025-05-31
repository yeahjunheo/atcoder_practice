'''
Cookie Exchanges
'''

a,b,c = map(int, input().split())
original = [a,b,c]
count = 0
while True:
    if a%2 != 0 or b%2 != 0 or c%2 != 0:
        break
    a,b,c = (b+c)//2, (c+a)//2, (a+b)//2
    count += 1
    if sorted([a,b,c]) == sorted(original):
        count = -1
        break
print(count)