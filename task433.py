'''
Задача 433
Шаги в алгоритме Евклида


Пусть E(x0, y0) будет числом шагов, необходимых для определения наибольшего общего делителя чисел x0 и y0, используя алгоритм Евклида. Более формально:
x1 = y0, y1 = x0 mod y0
xn = yn-1, yn = xn-1 mod yn-1
E(x0, y0) - это наименьшее n такое, что yn = 0.


Получаем E(1,1) = 1, E(10,6) = 3 и E(6,10) = 4.


Определим S(N) как сумму E(x,y) для 1 ≤ x,y ≤ N.
Имеем S(1) = 1, S(10) = 221 и S(100) = 39826.


Найдите S(5·106).

 Оригинал
'''