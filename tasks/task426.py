'''
Задача 426
Система шаров и коробок


Рассмотрим бесконечный ряд коробок. Некоторые из них содержат один шар. Например, начальное расположение из 2 последовательных полных коробок, за которыми следуют 2 пустые, потом 2 полные, потом 1 пустая коробка и 2 полные, может быть обозначено последовательностью (2, 2, 2, 1, 2), в которой попеременно записано количество последовательных полных и пустых коробок.


Один ход заключается в перемещении каждого шара ровно один раз по следующему правилу: переместите самый левый шар, который еще не был перемещен, в ближайшую пустую коробку справа от него.


После одного хода последовательность (2, 2, 2, 1, 2) становится (2, 2, 1, 2, 3), как показано ниже. Заметьте, что запись новой последовательности начинается с первой полной коробки.





Подобная система называется системой шаров и коробок (Box-Ball System, или сокращенно BBS).


Можно показать, что после достаточного количества ходов система достигает состояния, в котором последовательные количества полных коробок больше не меняются. В примере ниже последовательное количество полных коробок достигает [1, 2, 3] - назовем это конечным состоянием.





Определим последовательность {ti}:

s0 = 290797
sk+1 = sk2 mod 50515093
tk = (sk mod 64) + 1


Начиная с исходного расположения (t0, t1, …, t10), конечное состояние будет [1, 3, 10, 24, 51, 75].
Найдите конечное состояние для исходного расположения (t0, t1, …, t10 000 000).
Дайте ответ как сумму квадратов элементов конечного состояния. Например, если конечное состояние - [1, 2, 3], тогда 12 + 22 + 32 = 14 будет Вашим ответом.

 Оригинал
'''