'''
Задача 538
Наибольшие четырехугольники

Рассмотрим последовательность S = (s1, s2, ..., sn).
Пусть f(S) будет периметром четырехугольника с наибольшей площадью, чьи длины сторон (si, sj, sk, sl) являются четырьмя элементами последовательности S (числа i, j, k, l различны между собой). Если существует несколько четырехугольников с одинаковой максимальной площадью, из них выбирается четырехугольник с наибольшим периметром.
Например, если S = (8, 9, 14, 9, 27), мы можем взять элементы (9, 14, 9, 27) и образовать равнобедренную трапецию с параллельными сторонами длиной 14 и 27 и боковыми сторонами длиной 9. Площадь этого четрыехугольника равна 127.611470879... Можно показать, что это - наибольшая площадь среди всех возможных четырехугольников с длинами сторон, являющимися элементами S. Посему, f(S) = 9 + 14 + 9 + 27 = 59.
Пусть un = 2B(3n) + 3B(2n) + B(n+1), где B(k) - количество битов "1" в числе k, представленном в основании 2.
Например, B(6) = 2, B(10) = 2 и B(15) = 4, и u5 = 24 + 32 + 2 = 27.
Также, пусть Un будет последовательностью (u1, u2, ..., un).
Например, U10 = (8, 9, 14, 9, 27, 16, 36, 9, 27, 28).
Можно показать, что f(U5) = 59, f(U10) = 118, f(U150) = 3223.
Также можно показать, что Σ f(Un) = 234761 для 4 ≤ n ≤ 150.
Найдите Σ f(Un) для 4 ≤ n ≤ 3 000 000.
 Оригинал
'''