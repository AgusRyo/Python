'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''
edad=int(input("Ingresa tu edad: "))

if(edad >= 18):
    print("Eres mayor de edad")
else:
    print(("Eres menor de edad"))

print("")

'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por 
la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en 
la variable sin tener en cuenta mayúsculas y minúsculas.
'''
password1= "holamundo"
ingreso=input("Ingrese la contraseña: ")

if password1 == ingreso.lower():
    print("Bienvenido Usuario")
else:
    print("Contraseña Incorrecta")
print("")
'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
'''

num1=int(input("Ingrese el dividendo: "))
num2=int(input("Ingrese otro divisor: "))

if num2 != 0:
    print(num1/num2)
else:
    print("No se puede dividir")
print("")
'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

num= int(input("Ingrese un numero para saber si es par o impar: "))

if num%2==0:
    print("Es par")
else:
    print("Es impar")

print("")

'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a
$1000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por 
pantalla si el usuario tiene que tributar o no.
'''

ingresos= float(input("Ingrese el valor de sus ingresos mensuales: "))
edad= int(input("Ingrese su edad: "))

if ingresos >=1000 and edad>16:
    print("A usted le corresponde pagar impuestos")
else: 
    print("Usted está excento de impuestos")


print("")

'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a
la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
pantalla el grupo que le corresponde.
'''

nombre=input("Ingrese su nombre: ")
sexo=input("Ingrese su sexo  H/M: ")

inicial=nombre[0]

if sexo=="M":
    if nombre.lower() <'m':
        print("Tu grupo es A")
    else:
        print("Tu grupo es B")
else:
    if nombre.lower()> 'n':
        print("Tu grupo es A")
    else:
        print("Tu grupo es B")
print("")
