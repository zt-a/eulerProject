'''
Задача 260
Игра в камушки

В игру играют два игрока с помощью трех кучек камушков.
Когда приходит его ход, игрок берет один или более камушков из кучки. Однако, беря камушки из более, чем одной кучки, игрок должен взять такое же количество камушков из всех выбранных кучек.
Другими словами, игрок выбирает N>0 камушков, взяв:
N камушков из одной кучки; или
N камушков из каждой из любых двух кучек (всего 2N); или
N камушков из каждой из трех кучек (всего 3N).
Победит тот игрок, который возьмет последний камушек.

Под выигрышной конфигурацией подразумевается такая, в которой первый игрок может сразу победить.
К примеру, (0,0,13), (0,11,11) и (5,5,5) являются выигрышными конфигурациями, т.к. игрок может сразу взять все камушки.
Под проигрышной конфигурацией подразумевается такая, в которой второй игрок сразу выиграет, вне зависимости от того, что сделает первый игрок.
К примеру, конфигурации (0,1,2) и (1,3,3) являются проигрышными, т.к. в результате любого разрешенного шага первого игрока выиграет второй игрок.
Рассмотрим все проигрышные конфигурации (xi,yi,zi), где xi ≤ yi ≤ zi ≤ 100.
Можно убедиться, что для них Σ(xi+yi+zi) = 173895.
Найдите Σ(xi+yi+zi), где (xi,yi,zi) - диапазон всех проигрышных конфигураций
при xi ≤ yi ≤ zi ≤ 1000.
 Оригинал
'''