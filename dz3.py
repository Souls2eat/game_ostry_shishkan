a = int(input('Введите последовательность чисел(0 - завершить):'))
c = 1000000
count = 0
list_ = []
m = [1, 2, 5, 7]
m.append(4)
print(m)
while a != 0:
    count += 1
    b = a / count
    list_.append(b)
    if b < c:
        c = b
    a = int(input())
print('Числа делённые на свой порядковый номер:', *list_)
print('Наименьшее число:', c)