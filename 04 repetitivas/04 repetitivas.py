#PUNTO 1
hasta_cien = 0

for hasta_cien in range(100):
    print(hasta_cien)
    
#PUNTO 2

num_digit = int(input("Ingresar número a determinar cant de dígitos: "))
cont_digit = 0

while num_digit != 0:
   num_digit = num_digit // 10
   cont_digit = cont_digit + 1


print("Cantidad de dígitos: ", cont_digit)

#PUNTO 3
primer_limite = int(input("Ingresar el primer número límite: "))
segundo_limite = int(input("Ingresar el segundo número límite: "))
numero_limite = primer_limite + 1
segundo_limite = segundo_limite - primer_limite

for primer_limite in range(segundo_limite - 1):
    print(numero_limite)    
    numero_limite = numero_limite + 1 

#PUNTO 4
bandera_suma = 1
result_suma = 0
while bandera_suma != 0:
    numero_suma = int(input("Ingresar número a sumar: "))
    if numero_suma == 0:
        print("El resultado de la suma en secuencia dio: ", result_suma )
        bandera_suma = 0
    else:
     result_suma = result_suma + numero_suma
  
  
#PUNTO 5
import random   
intento_num = 66
intentos_cant = 0
num_aleatorio = random.randint(0, 9)
while intento_num != num_aleatorio:
 intento_num = int(input("Ingresar número a encontrar:" ))
 intentos_cant = intentos_cant + 1
else: 
    print("Número descubierto!")
    print("Cantidad de intentos:", intentos_cant)

#PUNTO 6
num_par = 99
bandera_par = 1
while bandera_par != 0:
    if num_par % 2 == 0:
     print(num_par)
     num_par = num_par - 1
    elif num_par == 0:
        bandera_par = 0 

#PUNTO 7
posit_limite = int(input("Ingresar número entero positivo: "))
if posit_limite < 0:
    print("Por favor ingrese un número entero positivo: ")
    posit_limite = int(input("Ingresar número entero positivo: "))
cant_suma = 0
suma_posit = 0

for cant_suma in range(0, posit_limite):
    suma_posit = cant_suma + suma_posit

print("El resultado de la suma fue: ", suma_posit)

#PUNTO 8
i = 0
negativo_cien = 0
par_cien = 0
impar_cien = 0
posit_cien = 0
nulo_cien = 0
for i in range (100):
 clases_cien = int(input("Ingresar un número entero: "))
 if clases_cien < 0:
     negativo_cien = negativo_cien + 1
 elif clases_cien == 0:
     nulo_cien == nulo_cien + 1
 else:
     posit_cien = posit_cien + 1
     
 if clases_cien % 2 == 0:
     par_cien = par_cien + 1
 else: 
     impar_cien = impar_cien + 1
     
print("La cantidad de números que fueron negativos fueron: ", negativo_cien)
print("La cantidad de números que fueron positivos fueron: ", posit_cien)
print("La cantidad de números que fueron pares fueron: ", par_cien)
print("La cantidad de números que fueron impares fueron: ", impar_cien)
print("La cantidad de valores nulos fueron de: ", nulo_cien)

#PUNTO 9
from statistics import mean
num_media = [] 
for i in range(5):
    num = float(input("Ingresar números enteros: "))
    if num % 1 != 0:
        print("Por favor, ingresar números enteros: ")
        num = float(input("Ingresar números enteros: "))
    
    num_media.append(num)

print("La media fue:", mean(num_media))

#PUNTO 10
digito_sacar = 0
digito_invert = 0
digito_num = int(input("Ingrese un número: "))

invert_num = 0
while digito_num > 0: 
    digito_sacar = digito_num % 10 
    digito_invert = digito_invert * 10 + digito_sacar 
    digito_num = digito_num // 10 

print("Número invertido:", digito_invert)
