#реализуем класс стэка
class Steak:
    def __init__(self):
        self.items = []
         
    def isEmpty(self):
        return self.items == []

    def push(self, item, index):
        self.items.append((item, index))

    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()


brackets = {"(": ")", "{": "}", "[": "]"} #Какие ковычки у нас есть
string = input()
stack = Steak()
index = -1

for i, el in enumerate(string):
    if el in brackets: #Если открывающаяся ковычка, добавляем её
        stack.push(el, i)
    elif el in brackets.values(): #Если закрывающаяся, то смотрим подходит ли последней закрывающейся
        last_bracket = stack.pop()
        if el != brackets[last_bracket[0]]:
            index = i + 1
            break

if index > 0: #Если у нас была ошибка закрывающейся скобки, то выводим эту индекс этой скобким
    print(index)
else: #Отрабатываем на вероятность ошибки открывающейся скобки
    if stack.isEmpty(): #Если в стеке нет скобок, значит все пары набраны
        print("Success")
    else: #Если там есть скобки, значит не все пары найдены
        print(stack.pop()[1] + 1) #выводим индекс последней открывающейся скобки без пары
