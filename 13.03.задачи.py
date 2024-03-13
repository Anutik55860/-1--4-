#1.1
n = 1 
while 3*n**4 - 730*n < 5:    n += 1 
print(n)

#1.2
import mathdef equation(n):
    return math.exp(n) - 1000 * math.log(n) - 10n = 1
while equation(n) > 0:    n += 1
print("Наибольшее целое n:", n - 1)

#2
m = int(input("Введите целое число m (> 1): "))
k = 0while 4**k < m:
    k += 1print("Наибольшее целое k: ", k - 1)

#3 n = int(input("Введите натуральное число n: "))
a = 2r = 2
while a**r <= n:    a += 1
    r = 2
    while a**r <= n:        r += 1
print("Наименьшее число вида a^r, превосходящее n:", a**r)

#4.1
m = int(input("Введите число m: "))f0 = f1 = 1
fn = f0 + f1while fn <= m:
    fn = f0 + f1    f0 = f1
    f1 = fn
print("Первое число Фибоначчи, большее", m, ":", fn)

#4.2
f0 = f1 = 1
fn = f0 + f1s = 2 
while fn <= 1000:    s += fn
    fn = f0 + f1    f0, f1 = f1, fn
print("Сумма всех чисел Фибоначчи, которые не превосходят 1000:", s)
