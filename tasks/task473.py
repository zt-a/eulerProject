'''
Задача 473
Фи-цифровая система счисления


Пусть $\varphi$ будет золотым сечением: $\varphi=\frac{1+\sqrt{5}}{2}.$
Стоит заметить, что возможно записать любое натуральное число как сумму степеней $\varphi$, даже если мы потребуем, чтобы каждая степень $\varphi$ использовалась в этой сумме не больше одного раза.
Даже в таком случае такое представление не будет уникальным.
Мы можем сделать его уникальным потребовав, чтобы оно было конечным и в нем не использовались степени с последовательными показателями.
Например: 
$2=\varphi+\varphi^{-2}$ и $3=\varphi^{2}+\varphi^{-2}$


Чтобы записать эту сумму степеней $\varphi$, мы будем использовать строку из 0 и 1 с точкой, показывающей начало отрицательных показателей.
Назовем такую запись Фи-цифровой системой счисления.
So $1=1_{\varphi}$, $2=10.01_{\varphi}$, $3=100.01_{\varphi}$ и $14=100100.001001_{\varphi}$. 
Строки, представляющие числа 1, 2 и 14 в Фи-цифровой системе счисления - палиндромы, в то время как строка, представляющая число 3 - нет. (Фи-цифровая точка не находится ровно посередине строки).


Сумма всех натуральных чисел, не превышающих 1000 и чьи представления в Фи-цифровой системе счисления - палиндромы, равна 4345.


Найдите сумму всех натуральных чисел, не превышающих $10^{10}$ и чьи представления в Фи-цифровой системе счисления - палиндромы.

 Оригинал
'''