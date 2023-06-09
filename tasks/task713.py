'''
Задача 713
Система водонагрева Турана


Туран установил электрическую систему нагрева воды в сарае за домом. В системе установлены два предохранителя, соединенных последовательно: один в доме и один в сарае. В наши дни устаревшие предохранители часто заменяют на небольшие автоматические предохранители, но система Турана устроена по старому принципу.
Чтобы система нагрева работала, оба предохранителя должны быть исправными.


У Турана есть всего $N$ предохранителей. Он знает, что $m$ из них исправны, а остальные перегорели. Однако, он не знает, какие именно исправны. Чтобы это узнать, он подключает разные комбинации предохранителей, пока система не заработает.
Обозначим наименьшее количество попыток, необходимое, чтобы гарантированно запустить систему, как $T(N,m)$.
$T(3,2)=3$ и $T(8,4)=7$.


Пусть $L(N)$ будет суммой всех $T(N, m)$ для $2 \leq m \leq N$.
$L(10^3)=3281346$


Найдите $L(10^7)$.

 Оригинал
'''