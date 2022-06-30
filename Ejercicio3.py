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

'''
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de $10000	        5%
Entre $10000 y $20000	15%
Entre $20000 y $35000	20%
Entre $35000 y $60000	30%
Más de $60000	        45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le
corresponde.
'''

renta= int(input("Ingrese su renta: "))

if renta < 10000:
    print("Corresponde pagar" + str(renta*0.05))
elif renta >= 10000 and renta <20000: 
    print("Corresponde pagar" + str(renta*0.15))
elif renta >=20000 and renta <35000:
    print("Corresponde pagar" + str(renta*0.20))
elif renta>= 35000 and renta < 60000:
    print("Corresponde pagar" + str(renta*0.30))
else:
    print("Corresponde pagar" + str(renta*0.45))

print("")

'''
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en
 mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
 pero no valores intermedios entre las cifras mencionadas. 
 A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
 La cantidad de dinero conseguida en cada nivel es de $2.400 multiplicada por la puntuación del nivel.

Nivel	        Puntuación
Inaceptable	        0.0
Aceptable	        0.4
Meritorio	        0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.

'''

puntaje= float("Ingrese la puntuación: ")

if puntaje == 0.0:
    bono= puntaje * 2400
    print("Tu nivel es INACEPTABLE, te corresponde: $" + str(bono))
if puntaje == 0.4:
    bono= puntaje * 2400
    print("Tu nivel es ACEPTABLE, te corresponde: $" + str(bono))
if puntaje >= 0.6:
    bono= puntaje * 2400
    print("Tu nivel es MERITORIO, te corresponde: $" + str(bono))

print("")

'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de
forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la 
edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10.

'''
edad= int(input("Ingrese su edad: "))

if edad <4 :
    print("Tu entrada es GRATIS")
elif edad >= 4 and edad <=18:
    print("Debes abonar $5 por la entrada")
else:
    print("Debes abonar $10 por la entrada")

print("")

'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su 
respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que
lleva.
'''
print("Bienvenido a la Pizezería Bella Napoli")
'''
rta= input("Desea ordenar una pizza normal o vegetariana? N / V: " )
if rta== N:
    print("Ha seleccionado pizza normal")
    ing=input("Que ingrediente extra desea para su pizza normal, (P)Peperoni, (J)Jamón, (S)Salmón: ")
    if ing == "P":
        print("Ha seleccionado una pizza normal con tomate, muzzarella y peperoni")
    elif ing=="J"''' 
