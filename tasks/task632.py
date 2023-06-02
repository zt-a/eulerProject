'''
Задача 632
Квадратные простые множители

Для целого числа $n$ определим квадратные простые множители $n$ как простые числа, на чьи квадраты делится число $n$. Например, квадратные простые множители числа $1500=2^2 \times 3 \times 5^3$ равны $2$ и $5$.
Пусть $C_k(N)$ будет количеством целых чисел между $1$ и $N$ включительно, имеющих ровно $k$ квадратных простых множителей. В таблице ниже приведены некоторые значения $C_k(N)$.


\[\begin{array}{|c|c|c|c|c|c|c|}
\hline

& k = 0 & k = 1 & k = 2 & k = 3 & k = 4 & k = 5 \\
\hline
N=10 & 7 & 3 & 0 & 0 & 0 & 0 \\
\hline
N=10^2 & 61 & 36 & 3 & 0 & 0 & 0 \\
\hline
N=10^3 & 608 & 343 & 48 & 1 & 0 & 0 \\
\hline
N=10^4 & 6083 & 3363 & 533 & 21 & 0 & 0 \\
\hline
N=10^5 & 60794 & 33562 & 5345 & 297 & 2 & 0 \\
\hline
N=10^6 & 607926 & 335438 & 53358 & 3218 & 60 & 0 \\
\hline
N=10^7 & 6079291 & 3353956 & 533140 & 32777 & 834 & 2 \\
\hline
N=10^8 & 60792694 & 33539196 & 5329747 & 329028 & 9257 & 78 \\
\hline
\end{array}\]


Найдите произведение всех ненулевых $C_k(10^{16})$. В качестве ответа приведите остаток от его деления на $1\,000\,000\,007$.
 Оригинал
'''