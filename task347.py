'''
Задача 347
Наибольшее целое число с двумя простыми сомножителями


Наибольшее целое число ≤ 100, которое делится только на простые сомножители 2 и 3 равно 96, т.к. 96=32*3=25*3. Для двух отличных простых чисел p и q определим M(p,q,N) как наибольшее натуральное число ≤N, которое делится только на p и q, а если такого числа не существует, то M(p,q,N)=0. 

Например, M(2,3,100)=96.
M(3,5,100)=75, а не 90, т.к. 90 делится на 2 ,3 и 5.
Кроме того, M(2,73,100)=0, т.к. не существует такого натурального числа ≤ 100, которое бы делилось как на 2, так и на 73.


Пусть S(N) - сумма всех возможных M(p,q,N). S(100)=2262.


Найдите S(10 000 000).
 Оригинал
'''