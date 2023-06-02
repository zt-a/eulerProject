'''
Задача 696
Маджонг

В игре Маджонг используются кости $s$ мастей. На каждой кости есть также число в промежутке $1\ldots n$, и для каждой комбинации масти и числа существует ровно четыре неотличимых кости с таким числом и мастью (настоящий маджонг также содержит другие дополнительные кости, но мы не рассматриваем их в этой задаче).
Выигрышной рукой считается набор из $3t+2$ костей (где $t$ - определенное целое число), который можно разложить на $t$ троек и одну пару, где:

Тройка - это или чоу, или панг
Чоу - это три кости одной масти и последовательных чисел
Панг - это три идентичные кости (одной масти и числа)
Пара - это две идентичные кости (одной масти и числа)

Например, ниже показана выигрышная рука при $n=9$, $s=3$, $t=4$, состоящая в данном случае из двух чоу, двух панг и одной пары:



Заметим, что иногда такой же набор костей можно представить как $t$ тройки и одну пару более, чем одним образом. Это считается только как одна выигрышная рука. Например, такой набор считается такой же выигрышной рукой, как в примере выше, так как он состоит из тех же костей:



Пусть $w(n, s, t)$ будет количеством различных выигрышных рук, образованных из $t$ троек и одной пары, при $s$ возможных мастях и костях, пронумерованных от 1 до $n$.
Например, при одной единственной масти и числах от 1 до 4 мы получим $w(4, 1, 1) = 20$: существует 12 выигрышных рук, состоящих из панг и пары, и 8, состоящих из чоу и пары. Также известно, что $w(9, 1, 4) = 13259$, $w(9, 3, 4) = 5237550$ и $w(1000, 1000, 5) \equiv 107662178 \pmod{1\,000\,000\,007}$.
Найдите $w(10^8, 10^8, 30)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.
 Оригинал
'''