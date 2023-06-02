'''
Задача 480
Последний вопрос

Рассмотрим все возможные слова, которые можно составить из расположенных в любом порядке букв следующей фразы:
thereisasyetinsufficientdataforameaningfulanswer
Предположим, что слова из 15 или менее букв отсортированы в алфавитном порядке и пронумерованы, начиная с 1.
Этот список из слов включает в себя:

1 : a
2 : aa
3 : aaa
4 : aaaa
5 : aaaaa
6 : aaaaaa
7 : aaaaaac
8 : aaaaaacd
9 : aaaaaacde
10 : aaaaaacdee
11 : aaaaaacdeee
12 : aaaaaacdeeee
13 : aaaaaacdeeeee
14 : aaaaaacdeeeeee
15 : aaaaaacdeeeeeef
16 : aaaaaacdeeeeeeg
17 : aaaaaacdeeeeeeh
...
28 : aaaaaacdeeeeeey
29 : aaaaaacdeeeeef
30 : aaaaaacdeeeeefe
...
115246685191495242: euleoywuttttsss
115246685191495243: euler
115246685191495244: eulera
...
525069350231428029: ywuuttttssssrrr
Определим P(w) как номер слова w в списке.
Определим W(p) как слово под номером p.
Можно заметить, что P(w) и W(p) являются взаимно обратными: P(W(p)) = p и W(P(w)) = w.
Например:
W(10) = aaaaaacdee
P(aaaaaacdee) = 10
W(115246685191495243) = euler
P(euler) = 115246685191495243
Найдите W(P(legionary) + P(calorimeters) - P(annihilate) + P(orchestrated) - P(fluttering)).
Дайте ответ записанным строчными буквами без знаков пунктуации и пробелов.
 Оригинал
'''