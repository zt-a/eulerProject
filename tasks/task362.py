'''
Задача 362
Бесквадратные множители


Рассмотрим число 54.
54 может быть разложено 7 различными способами на один или несколько множителей больше 1:

54, 2 × 27, 3 × 18, 6 × 9, 3 × 3 × 6, 2 × 3 × 9 и 2 × 3 × 3 × 3.


Если мы потребуем, чтобы все множители были бесквадратные, останется только два способа: 3 × 3 × 6 и 2 × 3 × 3 × 3.


Назовем Fsf(n) количество способов разложения числа n на один или больше бесквадратных множителей больше 1. Таким образом, Fsf(54)=2.


Пусть S(n) будет 
∑
Fsf(k) для k от 2 до n.


S(100)=193.


Найдите S(10 000 000 000). 

 Оригинал
'''