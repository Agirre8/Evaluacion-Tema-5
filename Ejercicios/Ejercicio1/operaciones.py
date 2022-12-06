def suma():
    try:
        num1 = int(input("Introduzca el primer número de la suma"))#Tengo que especificar que num1 es un int sino en la suma me quedaria por ejemplo 3+7=37
        num2 = int(input("Introduzca el segundo número de la suma"))
        resultado = num1 + num2
    except ValueError:
        print("Tipo de dato no válido.")
    return print(f"El resultado de la suma es:{resultado}")

def resta():
    try:
        num1 = int(input("Introduzca el primer número de la suma"))#Tengo que especificar que num1 es un int sino en la suma me quedaria por ejemplo 3+7=37
        num2 = int(input("Introduzca el segundo número de la suma"))
        resultado = num1 - num2
    except ValueError:
        print("Tipo de dato no válido.")
    return print(f"El resultado de la suma es:{resultado}")

def producto():
    try:
        num1 = int(input("Introduzca el primer número de la suma"))#Tengo que especificar que num1 es un int sino en la suma me quedaria por ejemplo 3+7=37
        num2 = int(input("Introduzca el segundo número de la suma"))
        resultado = num1 * num2
    except ValueError:
        print("Tipo de dato no válido.")
    return print(f"El resultado de la suma es:{resultado}")

def division():
    try:
        num1 = int(input("Introduzca el primer número de la suma"))#Tengo que especificar que num1 es un int sino en la suma me quedaria por ejemplo 3+7=37
        num2 = int(input("Introduzca el segundo número de la suma"))
        resultado = num1 + num2
    except ValueError:
        print("Tipo de dato no válido.")
    except ZeroDivisionError:
        print("No es posible dividir entre cero")
    return print(f"El resultado de la suma es:{resultado}")
