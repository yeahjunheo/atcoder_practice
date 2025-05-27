S = input()
a,b = map(int, input().split())

S = list(S)
S[a-1], S[b-1] = S[b-1], S[a-1]
S = ''.join(S)

print(S)