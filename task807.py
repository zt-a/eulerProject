'''
Задача 807
Веревочные петли

Дана окружность $C$ и целое число $n > 1$. Мы совершаем следующие действия.
На $0$-м шаге мы выбираем две случайные точки $R_0$ и $B_0$ с равномерным распределением на окружности $C$.
На $i$-м шаге ($1 \leq i < n$) мы сначала выбираем случайную точку $R_i$ с равномерным распределением на окружности $C$ и соединяем точки $R_{i - 1}$ и $R_i$ красной веревкой. Затем выбираем случайную точку $B_i$ с равномерным распределением на окружности $C$ и соединяем точки $B_{i - 1}$ и $B_i$ синей веревкой.
На $n$-м шаге мы сначала соединяем точки $R_{n - 1}$ и $R_0$ красной веревкой, затем соединяем точки $B_{n - 1}$ и $B_0$ синей веревкой.
Каждый кусок веревки представляет отрезок с концами в концах веревки и лежит поверх всех предыдущих веревок.
После $n$-того шага мы получим замкнутую петлю из красной веревки и замкнутую петлю из синей веревки.
В некоторых случаях эти две петли возможно разделить, как показано на левой схеме ниже. В других случаях петли "сцеплены" и их разделить невозможно, как показано на средней и правой схеме ниже.



Пусть $P(n)$ будет вероятностью того, что две петли будет возможно разделить.
Например, $P(3) = \frac{11}{20}$ и $P(5) \approx 0.4304177690$.
Найдите $P(80)$, округленное до $10$ знаков после десятичной точки.

Оригинал
'''