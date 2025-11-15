#PUNTO 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def probar_factorial():
    try:
        numero_limite = int(input("Ingrese un número entero positivo: "))
        if numero_limite < 1:
            print("Por favor, ingrese un número mayor o igual a 1.")
        else:
            print(f"--- Factoriales del 1 al {numero_limite} ---")
            for i in range(1, numero_limite + 1):
                resultado = factorial(i)
                print(f"El factorial de {i} es {resultado}")
    except ValueError:
        print("Error, entrada no válida. Debe ingresar un número entero.")

#PUNTO 2

def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def probar_fibonacci():
    try:
        posicion_limite = int(input("Ingrese una posición (número entero >= 0): "))
        if posicion_limite < 0:
            print("Por favor, ingrese un número mayor o igual a 0.")
        else:
            print(f"--- Serie de Fibonacci hasta la posición {posicion_limite} ---")
            serie_completa = []
            for i in range(posicion_limite + 1):
                valor = fibonacci_recursivo(i)
                serie_completa.append(str(valor))
            print(", ".join(serie_completa))
    except ValueError:
        print("Debe ingresar un número entero.")

#PUNTO 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)


def probar_potencia():
    try:
        base_num = int(input("Ingrese el número base: "))
        exp_num = int(input("Ingrese el exponente (entero no negativo): "))
        if exp_num < 0:
            print("El exponente debe ser mayor o igual a 0.")
        else:
            resultado = potencia(base_num, exp_num)
            print(f"{base_num} elevado a la {exp_num} es {resultado}")
    except ValueError:
        print("Error, debe ingresar números enteros")

#PUNTO 4

def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        cociente = n // 2
        resto = n % 2
        return decimal_a_binario(cociente) + str(resto)

def probar_decimal_a_binario():
    try:
        numero_decimal = int(input("Ingrese un número entero (positivo o 0): "))
        if numero_decimal < 0:
            print("Ingrese un número mayor o igual a 0")
        else:
            resultado_binario = decimal_a_binario(numero_decimal)
            print(f"El número {numero_decimal} en binario es {resultado_binario}")
    except ValueError:
        print("Error, debe ingresar un número entero.")

#PUNTO 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def probar_es_palindromo():
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    palabra = palabra.lower()
    if es_palindromo(palabra):
        print(f"'{palabra}' SI es un palindromo")
    else:
        print(f"'{palabra}' NO es un palindromo")

#PUNTO 6 

def suma_digitos(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def probar_suma_digitos():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Se usara el valor absoluto")
        resultado = suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es {resultado}")
    except ValueError:
        print("Error, debe ingresar un numero entero.")

#PUNTO 7

def contar_bloques(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def probar_contar_bloques():
    try:
        niveles = int(input("Ingrese el número de bloques en el nivel más bajo: "))
        if niveles < 1:
            print("Debe ser un número positivo.")
        else:
            resultado = contar_bloques(niveles)
            print(f"Se necesitan {resultado} bloques en total para {niveles} niveles.")
    except ValueError:
        print("Error, debe ingresar un número entero.")

#PUNTO 8

def contar_digito(numero, digito):
    numero = abs(numero)
    if numero < 10:
        return 1 if numero == digito else 0
    
    conteo = 0
    if (numero % 10) == digito:
        conteo = 1
    
    return conteo + contar_digito(numero // 10, digito)

def probar_contar_digito():
    try:
        numero = int(input("Ingrese el número entero: "))
        digito = int(input("Ingrese el dígito (0-9) a contar: "))
        if digito < 0 or digito > 9:
            print("El dígito a contar debe estar entre 0 y 9")
        else:
            resultado = contar_digito(numero, digito)
            print(f"El dígito {digito} aparece {resultado} veces en {numero}.")
    except ValueError:
        print("Error, debe ingresar números enteros")


def mostrar_menu():
    print("\n--- MENÚ DE EJERCICIOS RECURSIVOS ---")
    print("PUNTO [1]. Factoriales de 1 a N")
    print("PUNTO [2]. Serie de fibonacci")
    print("PUNTO [3]. Potencia de un número")
    print("PUNTO [4]. Convertir decimal a binario")
    print("PUNTO [5]. Verificar palindromo")
    print("PUNTO [6]. Sumar dígitos de un número")
    print("PUNTO [7]. Contar bloques de pirámide")
    print("PUNTO [8]. Contar dígito en un número")
    print("[0]. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            probar_factorial()
        elif opcion == '2':
            probar_fibonacci()
        elif opcion == '3':
            probar_potencia()
        elif opcion == '4':
            probar_decimal_a_binario()
        elif opcion == '5':
            probar_es_palindromo()
        elif opcion == '6':
            probar_suma_digitos()
        elif opcion == '7':
            probar_contar_bloques()
        elif opcion == '8':
            probar_contar_digito()
        elif opcion == '0':
            print("Saliendo")
            break
        else:
            print("Opcion no válida, intente de nuevo")

if __name__ == "__main__":
    main()