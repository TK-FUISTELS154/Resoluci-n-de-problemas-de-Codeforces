import math
# La función lambda es una función anónima que se define utilizando la palabra clave lambda. Es útil para crear funciones pequeñas y de una sola línea. En este caso, la función lambda se utiliza para calcular el n-ésimo número de Fibonacci de manera recursiva.
fibo = lambda n: n if n < 2 else fibo(n-1) + fibo(n-2)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


print(fibo(5))

# La función math.prod() se utiliza para calcular el producto de todos los elementos en un iterable. En este caso, se está calculando el producto de los números del 1 al 10 y comparándolo con el valor 3628800, que es el factorial de 10 (10!). Si el resultado es True, significa que el producto de los números del 1 al 10 es igual a 3628800.
print(math.prod(i for i in range(1,11))==3628800)

# La función contador es un generador que produce una secuencia de números del 1 al n. Utiliza la palabra clave yield para generar cada número en la secuencia. Luego, se convierte el generador en una lista y se une con guiones para imprimir la secuencia como una cadena.
def contador(n):
    for i in range(1, n+1):
        yield str(i)


print('-'.join(list(contador(5))))