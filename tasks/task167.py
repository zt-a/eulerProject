'''
Задача 167
Исследуем последовательности Улама.

Для двух натуральных чисел a и b последовательность Улама U(a,b) определяется следующим образом: U(a,b)1 = a, U(a,b)2 = b и для k > 2,
U(a,b)k равно наименьшему целому числу, превышающему U(a,b)(k-1), которое может быть единственным способом записано в виде суммы двух различных предыдущих членов U(a,b).
Например, последовательность U(1,2) начинается так:
1, 2, 3 = 1 + 2, 4 = 1 + 3, 6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8;
5 = 1 + 4 = 2 + 3 сюда не относится, потому что имеет два представления в виде суммы двух предыдущих членов, равно как и 7 = 1 + 6 = 3 + 4.
Найдите ∑U(2,2n+1)k для 2 ≤ n ≤10, где k = 1011.
 Оригинал
'''