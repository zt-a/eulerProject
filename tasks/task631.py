'''
Задача 631
Ограниченные перестановки

Пусть $(p_1 p_2 \ldots p_k)$ обозначает перестановку множества ${1, ..., k}$, которая отображается в $p_i\mapsto i$. Определим длину перестановки как $k$. Заметим, что пустая перестановка $()$ имеет нулевую длину.
Определим возникновение перестановки $p=(p_1 p_2 \ldots p_k)$ в перестановке $P=(P_1 P_2 \ldots P_n)$ как последовательность $1\leq t_1 < t_2 < \cdots < t_k \leq n$, такую что $p_i < p_j$ тогда и только тогда, если $P_{t_i} < P_{t_j}$ для всех $i,j \in \{1, ..., k\}$.
Например, $(1243)$ возникает дважды в перестановке $(314625)$: однажды как 1-й, 3-й, 4-й и 6-й элементы $(3\,\,46\,\,5)$ и однажды как 2-й, 3-й, 4-й и 6-й элементы $(\,\,146\,\,5)$.
Пусть $f(n, m)$ будет количеством перестановок $P$ длиной не больше $n$, таких что в $P$ нет возникновений перестановки $1243$ и в $P$ есть не больше $m$ возникновений перестановки $21$.
Например, $f(2,0) = 3$ с перестановками $()$, $(1)$, $(1,2)$, но не $(2,1)$.
Вам также дано, что $f(4, 5) = 32$ и $f(10, 25) = 294\,400$.
Найдите остаток от деления $f(10^{18}, 40)$ на $1\,000\,000\,007$.
 Оригинал
'''