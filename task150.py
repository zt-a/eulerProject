'''
Задача 150
Поиск под-треугольника с наименьшей суммой в треугольном массиве

В треугольном массиве положительных и отрицательных целых чисел мы хотим найти такой под-треугольник, чтобы сумма всех чисел, из которых он состоит, была по возможности меньшей.
В примере ниже отчетливо видно, что выделенный треугольник удовлетворяет условию, т.к. его сумма равна −42.



Мы собираемся сделать такой треугольный массив с одной тысячей строк, поэтому нам необходимо сгенерировать 500500 псевдослучайных числа sk в диапазоне ±219, воспользовавшись определенным типом генератора случайных чисел (известен как "линейный конгруэнтный генератор") следующим образом:
t := 0

при k = 1 до k = 500500:

    t := (615949*t + 797807) modulo 220

    sk := t−219
Таким образом: s1 = 273519, s2 = −153582, s3 = 450905 и т.д.
После этого наш треугольный массив формируется из полученных псевдо-случайных чисел следующим образом:

s1

s2  s3

s4  s5  s6 

s7  s8  s9  s10

...

Под-треугольники можно начинать с любого элемента массива и продолжать их вниз настолько, насколько это необходимо (выбирая два элемента на следующей строке, три элемента на идущей через одну строке и т.д.).

"Сумма под-треугольника" определяется как сумма всех его элементов.

Найдите наименьшую возможную сумму под-треугольника.
 Оригинал
'''