'''
Задача 656
Последовательности палиндромов


Для данного нерационального числа $\alpha$ пусть $S_\alpha(n)$ будет последовательностью $S_\alpha(n)=\lfloor {\alpha \cdot n} \rfloor - \lfloor {\alpha \cdot (n-1)} \rfloor$ for $n \ge 1$. 
($\lfloor ... \rfloor$ - функция пол).


Можно доказать, что для любого нерационального числа $\alpha$ существует бесконечно много значений $n$, таких что подпоследовательность $ \{S_\alpha(1),S_\alpha(2)...S_\alpha(n) \} $ является палиндромом.

Первыми 20 значениями $n$, которые дают палиндромную подпоследовательность для $\alpha = \sqrt{31}$, являются:
1, 3, 5, 7, 44, 81, 118, 273, 3158, 9201, 15244, 21287, 133765, 246243, 358721, 829920, 9600319, 27971037, 46341755, 64712473.

Пусть $H_g(\alpha)$ будет суммой всех первых $g$ значений $n$, для которых соответствующая подпоследовательность является палиндромом.
Так, $H_{20}(\sqrt{31})=150243655$.

Пусть $T=\{2,3,5,6,7,8,10,...,1000\}$ будет множеством натуральных чисел не больше 1000, из которого исключены все квадраты.
Найдите сумму $H_{100}(\sqrt \beta)$ для $\beta \in T$. В качестве ответа приведите последние 15 цифр полученного числа.

 Оригинал
'''