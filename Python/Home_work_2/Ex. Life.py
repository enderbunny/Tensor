dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
def check(l):
    if l == n:
        return 0
    else:
        return l


def evolution(mas):
    arr1 = mas.copy()
    for i in range(n):
        for j in range(n):
            life = 0
            for k in range(len(dx)):
                life += mas[check(i+dx[k])][check(j+dy[k])]
            if mas[i][j] == 0:
                if life == 3:
                    arr1[i][j] = 1
            else:
                if life < 2 or life > 3:
                    arr1[i][j] = 0
    return arr1



with open('D:\VS Project\Tensor\Python\Home_work_2\input.txt') as f:
    lines = f.read().split('\n')
    pass
m = int(lines[0])
n = len(lines) - 1

arr = []
for i in range(1, n + 1):
    arr.append(list(map(int, lines[i].split())))

"""
arr1 = arr.copy()
for i in range(n):
    for j in range(n):
        life = 0
        for k in range(len(dx)):
            life += arr[check(i+dx[k])][check(j+dy[k])]
        if arr[i][j] == 0:
            if life == 3:
                arr1[i][j] = 1
        else:
            if life < 2 and life > 3:
                arr1[i][j] = 0
"""
for i in arr: 
    print(' '.join(list(map(str, i))))
print()

while m != 0:
    arr = evolution(arr)
    print(m)
    for i in arr: 
        print(' '.join(list(map(str, i))))
    print()
    m -= 1



