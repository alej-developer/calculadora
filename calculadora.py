import math 

def sumar(a, b):
    return a + b

print("🤖 BIENVENIDO A LA SÚPER CALCULADORA BÁSICA 🤖")

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

print("🤖 BIENVENIDO A LA SÚPER CALCULADORA BÁSICA 🤖")

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: No se puede calcular la raíz de un número negativo"
    return math.sqrt(a)

print("===================================")
print(" 🧮🤖  CALCULADORA INTERACTIVA v2.0 🤖🧮 ")
print("===================================")

while True: 
    print("\n Menú: 1. Sumar | 2. Restar | 3. Multiplicar | 4. Dividir | 5. Salir")
    opcion = input("▶ Elige una opción (1-5): ")

    if opcion == "5": 
        print("¡Gracias por usar la calculadora! Hasta luego.")
        break

    if opcion == '1':
        print(f"👉 Resultado: {sumar(num1, num2)}")
    elif opcion == '2':
        print(f"👉 Resultado: {restar(num1, num2)}")
    elif opcion == '3':
        print(f"👉 Resultado: {multiplicar(num1, num2)}")
    elif opcion == '4':
        print(f"👉 Resultado: {dividir(num1, num2)}")
    else:
        print("❌ Opción inválida. Por favor, vuelve a intentar.")
