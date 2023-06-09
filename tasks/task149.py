'''
Задача 149
Поиск подпоследовательностей с максимальной суммой

Взглянув в таблицу ниже, легко убедиться в том, что максимально возможная сумма соседних чисел в любом направлении (горизонтальном, вертикальном, обоих диагональных) равна 16 (= 8 + 7 + 1).

−2532
9−651
3273
−18−4  8

Теперь, давайте повторим поиск, но на этот раз в гораздо более крупных масштабах:
Для начала, сгенерируем четыре миллиона псевдо-случайных чисел с помощью особой формы "запаздывающего генератора Фибоначчи":
Для 1 ≤ k ≤ 55, sk = [100003 − 200003k + 300007k3] (modulo 1000000) − 500000.
Для 56 ≤ k ≤ 4000000, sk = [sk−24 + sk−55 + 1000000] (modulo 1000000) − 500000.
Таким образом, s10 = −393027 и s100 = 86613.
Затем члены s упорядочиваются в виде таблицы размерами 2000×2000, при этом первыми 2000 числами последовательно заполняется первая строка, следущими 2000 числами - вторая строка, и т.д.
Наконец, найдите наибольшую сумму любого количества соседних записей в любом направлении (по горизонтали, по вертикали и по диагонали).
 Оригинал
'''