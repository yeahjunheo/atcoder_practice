N,A,B = map(int, input().split())
S = input()
passed = 0
passedB = 0
for i in range(N):
    if S[i] == 'a':
        if passed < A + B:
            passed += 1
            print('Yes')
        else:
            print('No')
    elif S[i] == 'b':
        if passed < A + B and passedB < B:
            passed += 1
            passedB += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')