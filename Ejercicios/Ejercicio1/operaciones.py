def suma(num1,num2):
    try:
        resultado = num1 + num2
    except TypeError:
        print("Tipo de dato no válido.")
    return print(f"El resultado de la suma es:{resultado}")

def resta(num1,num2):
    try:
        resultado = num1 - num2
    except TypeError:
        print("Tipo de dato no válido.")
    return print(f"El resultado de la resta es:{resultado}")

def producto(num1,num2):
    try:
        resultado = num1 * num2
    except TypeError:
        print("Tipo de dato no válido.")
    return print(f"El resultado de la multiplicacion es:{resultado}")

def division(num1,num2):
    try:
        resultado = num1 + num2
    except TypeError:
        print("Tipo de dato no válido.")
    except ZeroDivisionError:
        print("No es posible dividir entre cero")
    return print(f"El resultado de la division es:{resultado}")

