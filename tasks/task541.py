'''
Задача 541
Делимость знаменателей гармонических чисел

n-тое гармоническое число Hn определеяется как сумма чисел, обратных первым n натуральным числам, и может быть записано как несократимая дробь an/bn.
$H_n = \displaystyle \sum_{k=1}^n \frac 1 k = \frac {a_n} {b_n}$, где $\text {gcd}(a_n, b_n)=1$.
Пусть M(p) будет наибольшим значением n, таким что bn неделимо на p.
Например, M(3) = 68, потому что $H_{68} = \frac {a_{68}} {b_{68}} = \frac {14094018321907827923954201611} {2933773379069966367528193600}$, и b68=2933773379069966367528193600 неделимо на 3, но все бóльшие гармонические числа имеют знаменатели, делимые на 3.
Известно, что M(7) = 719102.
Найдите M(137).
 Оригинал
'''