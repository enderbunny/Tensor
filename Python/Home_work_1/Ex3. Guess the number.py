n = 50
b = 101
m = 0
print(n)

while (answer := input()) != 'Верно':
    if answer == 'Меньше':
        b = n
        n = int(n - (n - m) / 2)
    else:
        m = n
        n = int((b - n) / 2 + n)
    print(n)
