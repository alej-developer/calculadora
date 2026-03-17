import math 

def sumar(a, b):
    return a + b

print("Bienvenido a la calculadora")
print (f"La suma de 5 + 3 es: {sumar(5, 3,)}")

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

print("Bienvenido a la Calculadora")
print(f"La suma de 5 + 3 es: {sumar(5, 3)}")
print(f"La resta de 10 - 4 es: {restar(10, 4)}")

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

print(f"La división de 10 / 2 es: {dividir(10, 2)}")

def potencia(a, b):
    return a ** b

print(f"La potencia de 2 elevado a 3 es: {potencia(2, 3)}")

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz de un número negativo"
    return math.sqrt(a)

print(f"La raíz cuadrada de 16 es: {raiz_cuadrada(16)}")

