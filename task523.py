'''
Задача 523
Первая сортировка I

Рассмотрим следующий алгоритм сортировки списка чисел по возрастанию:

1. Последовательно проверить каждую пару соседних элементов, начиная с первых двух.
2. Если элементы пары расположены в неправильном порядке:

a. Переместить меньший элемент пары в начало списка.
b. Начать снова с шага 1.

3. Если все пары имеют правильный порядок, остановиться.

Например, список { 4 1 3 2 } будет отсортирован следующим образом:

4 1 3 2  (4 и 1 в неправильном порядке, 1 перемещается в начало списка)
1 4 3 2  (4 и 3 в неправильном порядке, 3 перемещается в начало списка)
3 1 4 2  (3 и 1 в неправильном порядке, 1 перемещается в начало списка)
1 3 4 2  (4 и 2 в неправильном порядке, 2 перемещается в начало списка)
2 1 3 4  (2 и 1 в неправильном порядке, 1 перемещается в начало списка)
1 2 3 4  (список отсортирован)

Пусть F(L) будет количеством исполнений шага 2a в процессе сортировки списка L. Например, F({ 4 1 3 2 }) = 5.
Пусть E(n) будет ожидаемым значением F(P) для всех перестановок P целых чисел {1, 2, ..., n}.
Известно, что E(4) = 3.25 и E(10) = 115.725.
Найдите E(30). Дайте ответ округленным до двух цифр после десятичной точки.
 Оригинал
'''