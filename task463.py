'''
Задача 463
Странные рекурсивные отношения


Функция $f$ определена для всех натуральных аргументов следующим образом:

$f(1)=1$
$f(3)=3$
$f(2n)=f(n)$
$f(4n + 1)=2f(2n + 1) - f(n)$
$f(4n + 3)=3f(2n + 1) - 2f(n)$


Функция $S(n)$ определена как $\sum_{i=1}^{n}f(i)$.
$S(8)=22$ и $S(100)=3604$.
Найдите $S(3^{37})$. В качестве ответа приведите последние 9 цифр полученного числа.
 Оригинал
'''