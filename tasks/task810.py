'''
Задача 810
XOR-простые числа

Будем использовать обозначение $x\oplus y$ для побитового исключающего ИЛИ (XOR) над парой чисел $x$ и $y$.
Определим XOR-произведение $x$ и $y$, обозначаемое $x \otimes y$, аналогично умножению в столбик в двоичной системе счисления с единственным отличием, что вместо обычного целочисленного сложения над промежуточными результатами выполняется XOR.
Например, $7 \otimes 3 = 9$, или же в двоичной системе счисления $111_2 \otimes 11_2 = 1001_2$:
$$
\begin{align*}
\phantom{\otimes 111} 111_2 \\
\otimes \phantom{1111} 11_2 \\
\hline
\phantom{\otimes 111} 111_2 \\
\oplus \phantom{11} 111_2  \phantom{9} \\
\hline
\phantom{\otimes 11} 1001_2 \\
\end{align*}
$$

XOR-простое число - это целое число $n$ больше $1$, которое не является XOR-произведением двух целых чисел больше $1$. Пример выше показывает, что $9$ не является XOR-простым числом. Схожим образом $5 = 3 \otimes 3$ не является XOR-простым числом. Первыми XOR-простыми числами являются $2, 3, 7, 11, 13, ...$, десятое же XOR-простое число равно $41$.
Найдите $5\,000\,000$-е XOR-простое число.
 Оригинал
'''