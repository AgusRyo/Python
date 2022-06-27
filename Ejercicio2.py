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