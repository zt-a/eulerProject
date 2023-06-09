'''
Задача 435
Многочлены из чисел Фибоначчи

Числа Фибоначчи {fn, n ≥ 0} рекурсивно определяются как fn = fn-1 + fn-2 с начальными случаями f0 = 0 и f1 = 1.
Определим многочлены {Fn, n ≥ 0} как Fn(x) = ∑fixi для 0 ≤ i ≤ n.
Например, F7(x) = x + x2 + 2x3 + 3x4 + 5x5 + 8x6 + 13x7 и F7(11) = 268357683.
Пусть n = 1015. Найдите сумму [∑0≤x≤100 Fn(x)] mod 1307674368000 (= 15!).
 Оригинал
'''