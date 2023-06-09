'''
Задача 557
Разрезание треугольников


Треугольник разрезается на четыре части двумя отрезками, каждый из которых начинается в одной из вершин треугольника и заканчивается на противоположной стороне. Таким образом образуются три меньшие треугольные части и одна четырехугольная. Если исходный треугольник имел целочисленную площадь, часто возможно выбрать такие разрезы, при которых все четыре получившиеся части имеют целочисленную площадь. Например, на рисунке ниже показан именно так разрезанный треугольник площадью 55:



Обозначенные в примере выше буквами a, b, c и d площади равны a = 22, b = 8, c = 11 и d = 14. Также возможно разрезать треугольник площадью 55 так, что a = 20, b = 2, c = 24, d = 9.

Определим разрезающую треугольник четверку (a, b, c, d) как разрешенное целочисленное разделение треугольника, где a - это площадь треугольника между двумя разрезанными сторонами, d - это площадь четырехугольника, и b и c - это площади оставшихся двух треугольников с условием b ≤ c. Два описанных выше решения записываются как (22,8,11,14) и (20,2,24,9). Они являются двумя единственными возможными четверками, имеющими общую площадь 55.


Определим S(n) как сумму площадей исходных треугольников, представленных всеми разрешенными четверками с a+b+c+d ≤ n. Например, S(20) = 259.


Найдите S(10000).

 Оригинал
'''