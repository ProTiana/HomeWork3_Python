#8Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

n = int(input('Введите число: '))

def getFibonacci(n):
    fNumbers = []
    a, b = 1, 1
    for i in range(n+1-1):
        fNumbers.append(a) #заполняем массив
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n+1):
        fNumbers.insert(0, a) #вставить на позицию нулевого индекса значение а
        a, b = b, a - b
    return fNumbers
print(getFibonacci(n))



