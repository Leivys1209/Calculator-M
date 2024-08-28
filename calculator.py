# haz una calculadora con un menu iterativo con todas las operaciones basicas y avanzadas
# y una opcion para salir

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    return a ** 0.5

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz")
    print("7. Salir")
    return int(input("Opcion: "))

while True:

    opcion = menu()

    if opcion == 7:
        break

    a = float(input("Numero 1: "))
    b = float(input("Numero 2: "))

    if opcion == 1:
        print(suma(a, b))
    elif opcion == 2:
        print(resta(a, b))
    elif opcion == 3:
        print(multiplicacion(a, b))
    elif opcion == 4:
        print(division(a, b))
    elif opcion == 5:
        print(potencia(a, b))
    elif opcion == 6:
        print(raiz(a))
    else:
        print("Opcion invalida")

print("Adios!")