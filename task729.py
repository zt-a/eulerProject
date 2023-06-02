'''
Задача 729
Диапазон периодической последовательности

Рассмотрим последовательность вещественных чисел $a_n$, заданную начальным значением $a_0$ и рекурсией 
$\displaystyle a_{n+1}=a_n-\frac 1 {a_n}$ для любого $n \ge 0$.

Для некоторых начальных значений $a_0$ последовательность будет периодической. Например, $a_0=\sqrt{\frac 1 2}$ дает последовательность:
$\sqrt{\frac 1 2},-\sqrt{\frac 1 2},\sqrt{\frac 1 2}, \dots$

Нас инересует диапазон такой периодической последовательности, равный разности между максимумом и минимумом последовательности. Например, диапазон приведенной выше последовательности будет равен $\sqrt{\frac 1 2}-(-\sqrt{\frac 1 2})=\sqrt{ 2}$.

Пусть $S(P)$ будет суммой диапазонов всех таких периодических последовательностей с периодом не больше $P$.
Например, $S(2)=2\sqrt{2} \approx 2.8284$, что равно сумме диапазонов двух последовательностей, начинающихся с $a_0=\sqrt{\frac 1 2}$ и $a_0=-\sqrt{\frac 1 2}$. 
Известно, что $S(3) \approx 14.6461$ и $S(5) \approx 124.1056$.

Найдите $S(25)$, округленное до 4 знаков после десятичной точки.
 Оригинал
'''