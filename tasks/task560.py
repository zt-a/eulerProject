'''
Задача 560
Взаимно простой ним

Игра во взаимно простой ним очень похожа на обычную игру в ним, но игроки могут убирать только такое количество камней из кучки, которое является взаимно простым с текущим размером кучки. Два игрока убирают камни по очереди. Игрок, убравший последний камень, выигрывает.
Пусть L(n, k) будет количеством начальных позиций, проигрышных для первого игрока, предполагая идеальную игру, если игра начинается с k кучками, в каждой из которых от 1 до n - 1 камней включительно.
Например, L(5, 2) = 6, так как проигрышными начальными позициями являются (1, 1), (2, 2), (2, 4), (3, 3), (4, 2) и (4, 4).
Вам также дано, что L(10, 5) = 9964, L(10, 10) = 472400303, L(103, 103) mod 1 000 000 007 = 954021836.
Найдите L(107, 107) mod 1 000 000 007
 Оригинал
'''