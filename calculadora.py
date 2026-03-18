import math 

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def raiz_cuadrada(num1):
    if num1 < 0:
        return "Error: No se puede calcular la raíz de un número negativo"
    return math.sqrt(num1)

print("🤖 BIENVENIDO A LA SÚPER CALCULADORA BÁSICA 🤖")

print("===================================")
print(" 🧮🤖  CALCULADORA INTERACTIVA v2.0 🤖🧮 ")
print("===================================")

while True: 
    print("\n Menú: 1. Sumar | 2. Restar | 3. Multiplicar | 4. Dividir | 5. Potencia | 6. Raíz Cuadrada | 7. Salir")
    opcion = input("▶ Elige una opción (1-7): ")

    if opcion == "7": 
        print("¡Gracias por usar la calculadora! Hasta luego.")
        break

    if opcion in ['1', '2', '3', '4', '5', '6']:

        if opcion == '6': 
            num1 = float(input("Ingresa el número: "))
            print(f"👉 Resultado: {raiz_cuadrada(num1)}")

        else:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        
            if opcion == '1':
                print(f"👉 Resultado: {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"👉 Resultado: {restar(num1, num2)}")
            elif opcion == '3':
                print(f"👉 Resultado: {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"👉 Resultado: {dividir(num1, num2)}")
            elif opcion == '5':
                print(f"👉 Resultado: {potencia(num1, num2)}")
    else:
        print("❌ Opción inválida. Por favor, vuelve a intentar.")
