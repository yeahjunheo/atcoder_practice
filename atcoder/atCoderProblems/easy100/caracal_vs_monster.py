'''
mathematically, if the health is 1 -> 0
if greater than 1 then divide by 2 to get the floor division

if its 1, then we only hit once => 1

if its 2, then 2 becomes [1,1] then we hit twice => 1 + 2

it its 4, then 4 becomes [2,2] then becomes [1,1,1,1] then we hit 4 times => 1 + 2 + 4

for 7, this becomes [3,3] then becomes [1,1,1,1] then four times.

it its 8, then  8 becomes [4,4] then becomes [2,2,2,2] then becomes [1,1,1,1,1,1,1,1] then we hit 8 times

so its a geometric series of power of 2
'''

h = int(input())
if h == 1:
    print(1)
else:
    h = 2*(h//2)-1
    count = 0
    while h > 0:
        count += 2**h
        h //= 2
    print(count + 1)