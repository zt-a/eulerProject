'''
Задача 344
Игра "серебрянный доллар"

Один из вариантов игры Н. Г. де Брейна серебрянный доллар можно описать следующим образом:
На ленте с квадратными клетками размещены монеты, не более одной монеты на клетку. Ценность представляет лишь одна из них, называемая серебрянным долларом. Два игрока по очереди совершают ходы. Во время каждого хода, игрок должен совершить либо обычный, либо особый ход.
Обычный ход осуществляется выбором одной монеты и перемещением ее на одну или более клеток влево. Монету нельзя перемещать за пределы ленты, а также перепрыгивать через другие монеты или на них.
Кроме того, игрок может совершить особый ход, присвоив себе левую крайнюю монету, вместо совершения обычного хода. Если обычный ход совершить невозможно, игрок вынужден присвоить себе левую крайнюю монету.
Выигрывает тот игрок, который присвоит себе серебрянный доллар.



Определим выигрышную конфигурацию как такое расположение монет на ленте, при котором первый игрок может обеспечить себе победу независимо от действий второго игрока.
Пусть W(n,c) - число выигрышных конфигураций для ленты с n клетками, c бесполезными монетами и одним серебрянным долларом.
Дано: W(10,2) = 324 и W(100,10) = 1514704946113500.
Найдите W(1 000 000, 100) по модулю полупростого числа 1000 036 000 099 (= 1 000 003 · 1 000 033).

 Оригинал
'''