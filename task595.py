'''
Задача 595
Возрастающая случайная сортировка


Колода карт, пронумерованных от 1 до n, случайно перемешана так, что каждая перестановка одинаково вероятна.


Карты нужно отсортировать в возрастающем порядке, используя следующий метод:
Посмотрите на исходную последовательность карт. Если она уже отсортирована, нет необходимости предпринимать дальнейшие действия. В противном случае, если в каких-либо подпоследовательностях карты уже правильно расположены относительно друг друга (последовательно и по возрастанию), эти подпоследовательности закрепляются путем склеивания карт вместе. Например, для 7 карт, находящихся в исходном порядке 4123756, карты с номерами 1, 2 и 3 будут склеены вместе, также как и карты 5 и 6.
 Карты "перемешиваются" путем подбрасывания их в воздух, но все карты, находящиеся в правильном порядке, остаются склеенными, так что их порядок сохраняется. После этого карты (или пачки склеенных карт) подбираются с земли в случайном порядке. Предположите, что эта рандомизация непредвзята, несмотря на то, что некоторые карты лежат поодиночке, а некоторые - в пачках. 
 Повторяйте шаги 1 и 2 до тех пор, пока все карты не будут отсортированы. 

   Пусть S(n) будет ожидаемым количеством перемешиваний, необходимых для сортировки n карт. Так как исходный порядок проверяется перед перемешиванием, S(1) = 0. Известно, что S(2) = 1 и S(5) = 4213/871.


Найдите S(52) и приведите ваш ответ округленным до 8 знака после десятичной точки.

 Оригинал
'''