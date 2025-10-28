#PUNTO 1

with open("productos.txt", "w", encoding="utf-8") as f:
    f.write("Lapicera,120.5,30\n")
    f.write("Cuaderno,350.0,15\n")
    f.write("Goma,80.0,50\n")

print("Archivo creado correctamente.")

#PUNTO 2

with open("productos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")


#PUNTO 3

nombre_agregar = input("Nombre del producto: ")
precio_agregar = input("Precio del producto: ")
cantidad_agregar = input("Cantidad: ")

with open("productos.txt", "a", encoding ="utf-8") as f:
    f.write(f"{nombre_agregar}, {precio_agregar}, {cantidad_agregar}\n")


#PUNTO 4
diccionario = []

with open("productos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        nombre, precio, cantidad = linea.strip().split(",")
        diccionario.append({
            "nombre" : nombre,
            "precio" : float(precio),
            "cantidad" : int(cantidad),
        })

print(diccionario)


#PUNTO 5

nombre_buscar = input("Ingresar nombre del producto que desea buscar: ")
encontrado = False
for i in diccionario:
    if i["nombre"].lower() == nombre_buscar.lower():
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
        encontrado = True
        break

if not encontrado:
 print("Producto no encontrado")


#PUNTO 6

with open("productos.txt", "w", encoding="utf-8") as f:
    for i in diccionario:
        f.write(f"Nombre: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

print("Archivo actualizado.")