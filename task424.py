'''
Задача 424
Какуро





Выше приведен пример головоломки какуро с шифром (cryptic kakuro), также известной как "пересекающиеся суммы", чье конечное решение показано справа. (Общие правила головоломок какуро можно легко найти на многих сайтах в Интернете. Необходимую информацию можно найти на krazydad.com, чей автор предоставил данные для головоломок в этой задаче.)


Загружаемый текстовый файл (kakuro200.txt) содержит описания 200 таких головоломок, с размерами поля 5х5 или 6х6. Первая головоломка в файле приведена выше в качестве примера и записана следуюшим образом:


6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X


Первый символ - число, показывающее размер поля головоломки. Оно может быть или 6 (для головоломки 5x5), или 7 (для головоломки 6x6), за которым следует запятая (,). Дополнительные ряд сверху и колонка слева необходимы для хранения информации.


Далее, отделяемое запятыми, описывается содержимое каждой ячейки, начиная с верхнего ряда и двигаясь слева направо.
X = Серая ячейка, не должна быть заполнена.
O (заглавная буква латинского алфавита) = Белая пустая ячейка, которая должна быть заполнена цифрой.
A (или любая заглавная буква латинского алфавита от A до J) = Должна быть заменена соответствующей отгаданному шифру цифрой.
( ) = Положение зашифрованных сумм. Перед горизонтальными суммами стоит прописная буква "h", а перед вертикальными - прописная буква "v". За этой буквой следует одна или две заглавные буквы, в зависимости от того, является ли сумма однозначным или двузначным числом. Для двузначных сумм первая буква соответствует разряду десятков, а вторая - разряду единиц. Если в одной ячейке содержится информация как о горизонтальной, так и о вертикальной сумме, первой всегда указывается горизонтальная сумма, и эти суммы разделеяются запятой внутри скобок, например: (hFE,vD). После каждой пары скобок следует запятая.


После описания последней ячейки вместо запятой следует символ "Возврат каретки/Подача строки" (CRLF).


Ответом для каждой головоломки является ключ к шифру - приведенные в алфавитном порядке цифровые значения каждой буквы, при которых головоломка какуро решается. Как показано под примером головоломки, ответом на нее является 8426039571. Как минимум 9 из 10 букв шифра всегда являются частью описания головоломки. Если даны только 9, то десятой букве назначается оставшаяся неиспользованной цифра.


Известно, что сумма ответов на первые 10 головоломок в файле равна 64414157580.


Найдите сумму ответов на все 200 головоломок.

 Оригинал
'''