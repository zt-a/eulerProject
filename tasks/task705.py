'''
Задача 705
Суммарное число инверсий разделенных последовательностей


Число инверсий последовательности цифр - это наименьшее количество пар соседних цифр, которое надо поменять местами, чтобы отсортировать последовательность по возрастанию.
Например, число инверсий последовательности 34214 равно 5:
$34214 \to 32414 \to 23414 \to 23144 \to 21344 \to12344$.


Если каждую цифру в последовательности заменить на один из ее делителей, получим разделенную последовательность. 
Например, последовательность 332 имеет 8 разделенных последовательностей: $\{332,331,312,311,132,131,112,111\}$.


Определим $G(N)$ как объединение всех простых чисел меньше $N$, исключая все цифры ноль. 
Например, $G(20) = 235711131719$.


Определим $F(N)$ как сумму чисел инверсий для всех возможных разделенных последовательностей от исходной последовательности $G(N)$. 
Известно, что $F(20) = 3312$ и $F(50) = 338079744$.


Найдите $F(10^8)$. В качестве ответа приведите остаток от деления полученного результата на $1\,000\,000\,007$.

 Оригинал
'''