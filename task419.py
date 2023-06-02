'''
Задача 419
Последовательность "посмотри и скажи"


Последовательность "посмотри и скажи" выглядит следующим образом: 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
Она начинается с единицы, и каждый следующий элемент последовательности получается путем описания предудыщего элемента с точки зрения повторяющихся цифр.
Чтобы разобраться, проделаем это вслух:
1 - это "одна единица" → 11
11 - это "две единицы" → 21
21 - это "одна двойка и одна единица" → 1211 
1211 - это "одна единица, одна двойка и две единицы" → 111221
111221 - это "три единицы, две двойки и одна единица" → 312211
...


Определим A(n), B(n) и C(n) как количество единиц, двоек и троек соответственно в n-том элементе последовательности..
Можно показать, что A(40) = 31254, B(40) = 20259 и C(40) = 11625.


Найдите A(n), B(n) и C(n) для n = 1012. 
В качетве ответа дайте результат деления полученного числа по модулю 230, отделив значения A, B и C запятыми. 
Например, для n = 40 ответ выглядит так: 31254,20259,11625

 Оригинал
'''