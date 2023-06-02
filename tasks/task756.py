'''
Задача 756
Приближение суммы

Рассмотрим функцию $f(k)$, определенную для всех натуральных чисел $k>0$. Пусть $S$ — сумма первых $n$ значений функции $f$, то есть $$\displaystyle S=f(1)+f(2)+f(3)+\cdots+f(n)=\sum_{k=1}^n f(k)$$.
Для этой задачи применим случайность для приближения данной суммы. Для этого выберем случайный и равномерно распределенный упорядоченный набор из $m$ натуральных чисел $(X_1,X_2,X_3,\cdots,X_m)$ такой, что $0=X_0 < X_1 < X_2 < \cdots < X_m \leq n$, а затем вычислим модифицированную сумму $S^*$ следующим образом:
 
$$\displaystyle S^* = \sum_{i=1}^m f(X_i)(X_i-X_{i-1})$$
Теперь определим погрешность данного приближения как $\Delta=S-S^*$.
Пусть $\mathbb{E}(\Delta|f(k),n,m)$ — математическое ожидание погрешности при данных функции $f(x)$, количестве слагаемых $n$ в сумме и длине случайного набора $m$.
Например, $\mathbb{E}(\Delta|k,100,50) = 2525/1326 \approx 1.904223$ и $\mathbb{E}(\Delta|\varphi(k),10^4,10^2)\approx 5842.849907$, где $\varphi(k)$ — функция Эйлера.
Найдите $\mathbb{E}(\Delta|\varphi(k),12345678,12345)$ и дайте ваш ответ округленным до 6 знака после десятичной точки.
 Оригинал
'''