
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        return "Error: Raíz de un número negativo"
    return a ** 0.5

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz")
    print("7. Salir")
    try:
        return int(input("Opcion: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return menu()

def obtener_numero(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return obtener_numero(mensaje)

while True:
    opcion = menu()

    if opcion == 7:
        break

    if opcion in [1, 2, 3, 4, 5]:
        a = obtener_numero("Numero 1: ")
        b = obtener_numero("Numero 2: ")

        if opcion == 1:
            print("Resultado:", suma(a, b))
        elif opcion == 2:
            print("Resultado:", resta(a, b))
        elif opcion == 3:
            print("Resultado:", multiplicacion(a, b))
        elif opcion == 4:
            print("Resultado:", division(a, b))
        elif opcion == 5:
            print("Resultado:", potencia(a, b))

    elif opcion == 6:
        a = obtener_numero("Numero: ")
        print("Resultado:", raiz(a))

    else:
        print("Opción no válida. Intente de nuevo.")