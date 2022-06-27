#Ejercicios con Cadenas
'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por
pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''

nombre=input("Ingrese su nombre ")
cantidad=int(input("Ingrese un numero "))

print((nombre + "\n") *cantidad)
print("")

'''
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras 
mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede 
introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
nombre=input("Ingrese su nombre y apellido ")
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

'''
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es
el número de letras que tienen el nombre.
'''
nombre=input("Ingrese su nombre ")
print(nombre + " tiene "+ str(len(nombre)) +" letras")

'''
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código
del país +54, y la extensión tiene 3 dígitos (por ejemplo +54-011-6654324). Escribir un programa que pregunte
por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la 
extensión.
'''
tel = input("Introduce un número de teléfono con el formato +xx-xxx-xxxxxxx: ")
print('El número de teléfono es ', tel[8:15])
print("")

'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la 
frase invertida.
'''
frase=input("Ingresa una frase ")
print(frase[::-1])
print("")

'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre
por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

frase=input("Ingrese una frase ")
vocal=input("Ingrese una vocal en mínuscula ")
print(frase.replace(vocal,vocal.upper()))

'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio edu.ar 
'''
mail=input("Ingrese el corre electrónico personal ")
print(mail[:mail.find('@')] +'@edu.ar')
print("")

'''
Escribir un programa que pregunte por consola el precio de un producto en pesos con dos decimales y muestre 
por pantalla el número de pesos y el número de centavos del precio introducido.
'''
precio= input("Ingrese el precio ")
print(precio[:precio.find('.')],' pesos y ',precio[precio.find('.')+1:],' centavos')
print("")

'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por 
pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el
mes se introduzcan con un solo carácter.
'''
fecha= input(" Ingrese la fecha en formato dd/mm/aaaa ")
print('Día: ',fecha[:2])
print('Mes: ',fecha[3:5])
print('Año: ', fecha[6:])

print("")
print("Variante")
print("")

fecha= input(" Ingrese la fecha en formato dd/mm/aaaa ")
dia=fecha[:fecha.find('/')]
medio=fecha[fecha.find('/')+1:]
mes=medio[:medio.find('/')]
año=medio[medio.find('/')+1:]

print('Día ', dia)
print('Mes ', mes)
print('Año ', año)

print("")

'''
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
y muestre por pantalla cada uno de los productos en una línea distinta.
'''
cesta=input("Ingresa los productos separados por coma , ")
print(cesta.replace(',','\n'))
print("")

'''
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por
pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}$ = {total:11.2f}$'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
print("")

