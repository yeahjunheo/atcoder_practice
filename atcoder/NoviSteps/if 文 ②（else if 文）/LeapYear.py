Y = int(input())
if Y%4 != 0:
    print(365)
elif Y%100 != 0:
    print(366)
elif Y%400 != 0:
    print(365)
else:
    print(366)