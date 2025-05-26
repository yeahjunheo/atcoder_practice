'''
It's either adding all the numbers into a dictionary
and checking if the pairs with the differnece of k or
less exist,
or using a sorted list and checking to the left to count
the pairs with the difference of k or less.
'''

n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
left = 0
for right in range(n):
    while a[right] - a[left] > k:
        left += 1
    count += right - left
print(count)