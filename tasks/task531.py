'''
Задача 531
Китайские остатки


Пусть g(a,n,b,m) будет наименьшим неотрицательным решением x для системы:
x = a mod nx = b mod m,

если такое решение существует, в противном случае 0.


Например, g(2,4,4,6) = 10, но g(3,4,4,6) = 0.


Пусть φ(n) будет функцией Эйлера.


Пусть f(n,m) = g(φ(n),n,φ(m),m)


Найдите ∑f(n,m) для 1000000 ≤ n < m < 1005000

 Оригинал
'''