s = input()
append = ['dream', 'dreamer', 'erase', 'eraser']
for word in reversed(append):
    s = s.replace(word, '')
print('YES' if s == '' else 'NO')