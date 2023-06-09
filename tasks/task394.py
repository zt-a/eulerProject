'''
Задача 394
Поедание пирога


Джефф ест пирог необычным способом.
Пирог имеет круглую форму. Джефф начинает, делая первый разрез по радиусу пирога.
Пока остается как минимум данная доля пирога F, он действует следующим образом:
- Он делает два разреза от центра пирога до любой точки на краю оставшегося пирога. Все точки на краю оставшегося пирога одинаково вероятны. Это делит оставшийся пирог на три части. 
- Он забирает и съедает первые два куска в направлении против часовой стрелки от первого разреза пирога.
Когда доля оставшегося пирога становится меньше F, Джефф больше не повторяет эту процедуру. Вместо этого он съедает весь оставшийся пирог.




Для x ≥ 1, пусть E(x) будет ожидаемым количеством повторений вышеуказанной процедуры при F = 1/x.
Можно убедиться, что E(1) = 1, E(2) ≈ 1.2676536759, и E(7.5) ≈ 2.1215732071.


Найдите E(40), округленное до 10 знака после десятичной точки.


Оригинал
'''