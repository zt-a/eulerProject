'''
Задача 425
Соединение простых чисел


Два положительных простых числа A и B называются соединенными (обозначается как "A ↔ B"), если выполняется одно из следующих условий:
(1) A и B имеют одинаковую длину и отличаются ровно одной цифрой. Например, 123 ↔ 173.
(2) При добавлении одной цифры слева от A (или B) получается B (или A). Например, 23 ↔ 223 и 123 ↔ 23.


Назовем простое число P родственником двойки, если между 2 и P существует цепочка из соединенных простых чисел и ни одно число в цепочке не превышает P.


Например, 127 является родственником двойки. Одна из возможных цепочек показана ниже:
2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127
Однако, 11 и 103 не являются родственниками двойки.


Пусть F(N) будет суммой всех простых чисел ≤ N, которые не являются родственниками двойки.
Можно показать, что F(103) = 431 и F(104) = 78728.


Найдите F(107).

 Оригинал
'''