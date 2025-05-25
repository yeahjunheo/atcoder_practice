N = int(input())
binary = bin(N)[2:]
binary = '0'*(10-len(binary)) + binary
print(binary)