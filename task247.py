'''
Задача 247
Квадраты под гиперболой

Рассмотрим область, ограниченную 1 ≤ x и 0 ≤ y ≤ 1/x.


Пусть S1 будет наибольшим квадратом, который может поместиться под кривой.
Пусть S2 будет наибольшим квадратом, который может поместиться в оставшейся площади, и так далее. 
Пусть индексом Sn будет пара чисел (слева, снизу), показывающая количество квадратов слева от Sn и количество квадратов снизу от Sn.





На картинке изображены несколько квадратов, помеченных номерами. 
S2 имеет один квадрат слева и ни одного снизу, значит, индекс S2 - (1,0).
Можно заметить, что индекс S32 - (1,1), также как и индекс S50. 

50 - наибольшее n, для которого индекс Sn равен (1,1).


Каково наибольшее n, для которого индекс Sn равен (3,3)?

 Оригинал
'''