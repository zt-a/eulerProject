'''
Задача 437
Первообразные корни Фибоначчи


Вычислив 8n mod 11 для n от 0 до 9, мы получаем: 1, 8, 9, 6, 4, 10, 3, 2, 5, 7.
Как видно, присутствуют все возможные значения от 1 до 10. Посему, 8 - первообразный корень по модулю 11.
Но это еще не все.
Если присмореться, можно заметить, что:
1+8=9
8+9=17≡6 mod 11
9+6=15≡4 mod 11
6+4=10
4+10=14≡3 mod 11
10+3=13≡2 mod 11
3+2=5
2+5=7
5+7=12≡1 mod 11.

Таким образом, степени 8 mod 11 цикличны с периодом 10, и 8n + 8n+1 ≡ 8n+2 (mod 11).
8 является первообразным корнем Фибоначчи по модулю 11.
Не все простые числа имеют первообразный корень Фибоначчи.
Существует 323 простых числа меньше 10 000 с одним или более первообразными корнями Фибоначчи, и сумма этих простых чисел равна 1 480 491.
Найдите сумму всех простых чисел меньше 100 000 000, имеющих хотя бы один первообразный корень Фибоначчи.


 Оригинал
'''