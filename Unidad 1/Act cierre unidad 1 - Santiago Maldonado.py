
#PUNTO 1
print("Hola Mundo!")

#PUNTO 2 
nombre_saludo = input("Ingresar nombre(saludo):")
print ("Hola", nombre_saludo,"!") 

#PUNTO 3
nombre_usuario = input ("Ingresar nombre: ")
apellido_usuario = input ("Ingresar apellido: ")
edad_usuario = input ("Ingresar edad: ")
lugar_usuario = input ("Ingresar lugar de residencia: ")

print ("Soy", nombre_usuario, apellido_usuario,", tengo", edad_usuario, "años y vivo en", lugar_usuario)

#PUNTO 4
radio_circulo = float(input ("Ingresar radio de un circulo: "))

perimetro_circulo = 3.14 * radio_circulo * 2
area_circulo = 3.14 * (radio_circulo**2) 

print("El área del circulo es:", area_circulo,"cm, y su perímetro es:", perimetro_circulo,"cm²")

#PUNTO 5
segundos = int(input("Ingresar cantidad de segundos:"))
horas = float(segundos / 60)
print("La cantidad de horas fueron ", horas)

#PUNTO 6
numero_tabla = int(input("Ingresar un número a realizar tabla de multiplicar:"))
i=1
while i<= 10:
  mult_tabla = numero_tabla * i
  print(numero_tabla, "X", i, "=", mult_tabla)
  i = i + 1

#PUNTO 7
primer_num =int (input("Ingresar el primer número distinto de cero:"))
if primer_num == 0:
 print("El número es 0, tiene que ser uno distinto")
 primer_num =int (input("Ingresar el primer número distinto de cero:"))

segundo_num =int (input("Ingresar el segundo número distinto de cero:"))
if segundo_num == 0:
 print("El número es 0, tiene que ser uno distinto")
 segundo_num =int (input("Ingresar el segundo número distinto de cero:"))

result_suma = primer_num + segundo_num
result_division = primer_num / segundo_num
result_mult = primer_num * segundo_num
result_resta = primer_num - segundo_num
print ("Los resultados fueron:")
print ("Suma:", result_suma)
print ("División:", result_division)
print ("Multiplicación:", result_mult)
print ("Resta:", result_resta)

#PUNTO 8
peso_cuerpo =float (input("Ingresar el peso de la persona:"))
altura_cuerpo =float (input("Ingresar altura de la persona (en m2):")) 

imc_cuerpo = peso_cuerpo / altura_cuerpo 

print ("El IMC de la persona analizada es de:", imc_cuerpo)

#PUNTO 9
grados_celsius =int(input("Ingresar grados celsius a transformar:"))

grados_fahrenheit =float(1.8 * grados_celsius + 32)

print("La temperatura en Fahrenheit es:", grados_fahrenheit, "°F")

#PUNTO 10 
promedio_num1 = int(input("Ingresar el primer número del promedio:"))
promedio_num2 = int(input("Ingresar el segundo número del promedio:"))
promedio_num3 = int(input("Ingresar el tercer número del promedio:"))

promedio_result =int (promedio_num1 + promedio_num2 + promedio_num3) / 3

print("El promedio dio como resultado:", promedio_result)




