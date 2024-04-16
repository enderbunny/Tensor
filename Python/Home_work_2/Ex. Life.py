#массивы сдвигов по x и y для каждой клетки
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

#проверяем координаты точек, чтобы не выйти за пределы массива
#если значение -1, делается срез массива
#если значение больше индекса последнего элемента возвращается 0 
def check(l, n):
    if l == n:
        return 0
    else:
        return l


#сам процесс эволюции, получаем ещё и длинну массива, чтобы не высчитывать её каждый раз
def evolution(mas, n):
    new_mas = mas.copy()
    for i in range(n):
        for j in range(n):
            life = 0
            #считаем кол-во живых соседей для клетки
            for k in range(len(dx)):
                life += mas[check(i+dx[k], n)][check(j+dy[k], n)]
            if mas[i][j] == 1:
                if (life < 2) or (life > 3):
                    new_mas[i][j] = 0 #убиваем клетку, если ей одиноко или слишком много соседей
            else:
                if life == 3:
                    new_mas[i][j] = 1 #оживляем, если есть 3 живых соседа
    return new_mas


with open("Python\Home_work_2\input.txt") as f:
    lines = f.read().split('\n')
    pass

m = int(lines[0])
n1 = len(lines)

arr = [] 
for i in range(1, n1):
    arr.append(list(map(int, lines[i].split())))

while m != 0:
    arr = evolution(arr, len(arr))
    m -= 1

with open("Python\Home_work_2\output.txt", "w") as f:
    for i in arr:
        f.write(' '.join(list(map(str, i))))
        f.write('\n')
    pass
