

#PUNTO 1

def saludo():
    print("Hola mundo")
    
saludo()

#PUNTO 2

def saludar_usuario(nombre):
    print("Hola", nombre, "!")
    

nombre = input("Ingresar el nombre de la persona: ")
saludar_usuario(nombre)

#PUNTO 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}." )

nombre = input("Ingresar el nombre de la persona: ")
apellido = input("Ingresar el apellido: ")
edad = input("Ingresar la edad: ")
residencia = input("Ingresar la residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#PUNTO 4

def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    print(area)
    
def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    print(perimetro)
    
radio = int(input("Ingresar el radio del círculo: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#PUNTO 5 

def segundos_horas(segundos):
  horas = segundos / 3600
  horas_entero = int(horas)
  print(f"Cantidad de horas: {horas_entero}.")

segundos = int(input("Ingresar la cantidad de segundos: "))
segundos_horas(segundos)

#PUNTO 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        mult = numero * i
        print(f"{numero} x {i} = {mult}")
    
numero = int(input("Ingresar el número a operar: "))
tabla_multiplicar(numero)


#PUNTO 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult_operacion = a * b
    if b != 0:
        division = a / b
        print(f"{a} + {b} = {suma}")
        print(f"{a} - {b} = {resta}")
        print(f"{a} x {b} = {mult_operacion}")
        print(f"{a} - {b} = {division}")
    else:
        division = "No es posible la división por cero"
    return (suma, resta, mult_operacion, division)



a = int(input("Ingresar el primer número: "))
b = int(input("Ingresar el segundo número: "))
operaciones_basicas(a, b)


#PUNTO 8

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc,2)
    return imc
    
    
altura = float(input("Ingresar la altura correspondiente: "))
peso = float(input("Ingresar el peso correspondiente: "))
imc = calcular_imc(peso, altura)
print(f"El IMC dio como resultado {imc}.")

#PUNTO 9

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
    
    
celsius = float(input("Ingresar grados celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La conversión de grados celsius a fahrenheit dio como resultado: {fahrenheit}")


#PUNTO 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
    
a = int(input("Ingresar primer número: "))
b = int(input("Ingresar segundo número: "))
c = int(input("Ingresar tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres numeros dió como resultado: {promedio}")