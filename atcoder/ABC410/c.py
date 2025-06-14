n, q = map(int, input().split())
A = [i for i in range(1, n + 1)]
offset = 0
for _ in range(q):
    command, *args = input().split()
    if command == "1":
        p, x = map(int, args)
        A[(p - 1 + offset) % n] = x
    elif command == "2":
        p = int(args[0])
        print(A[(p - 1 + offset) % n])
    else:
        k = int(args[0])
        offset = (offset + k) % n