# For taking int multiple lines of input
import sys
n = sys.stdin.readline()
orders = [0]*int(n)

for i in range(int(n)):
    orders[i] = [i for i in sys.stdin.readline().split()]
    orders[i][0] = int(orders[i][0])
    
shelf = []
for order in orders:
    if order[0] == 1:
        shelf.append(order[1])
    elif order[0] == 2:
        print(shelf[-1] if len(shelf) > 0 else '')
    elif order[0] == 3:
        shelf.pop()
