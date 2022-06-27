'''
Escribir un programa que pregunte el nombre del usuario en la consola y
después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
donde <nombre> es el nombre que el usuario haya introducido.
'''

nombre= input("Ingrese su nombre ")
print("¡Hola "+nombre+"!")
print("")
'''
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
(3+2/2*5)^2
'''
print(((3+2)/(2*5))**2)
print("")
'''
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.
'''
horas=int(input("Ingrese el numero de horas trabajadas "))
costo=int(input("Ingrese el costo por hora "))
print("Corresponde que le paguen: $"+ str(costo*horas))


'''
Escribir un programa que lea un entero positivo, N , introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N .
La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:
suma=(n(n+1)/2)
'''
print("")
N=int(input("Ingrese un numero entero positivo "))
suma= N * (N+1) /2
print("La sumatoria de 1 a "+ str(N) + " es: "+str(suma))
print("")

''' 
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice 
de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal
es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
'''
print("Indice de masa corporal")
kg=float(input("Ingrese el peso en KG "))
estatura=float(input("Ingrese la altura en metros "))
imc= round(kg/estatura**2,2)
print("Tu indice de masa corporal es: "+str(imc))
print("")

'''
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> 
da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> 
son el cociente y el resto de la división entera respectivamente.
'''
n=int(input("Ingrese un numero entero "))
m=int(input("Ingrese otro numero entero "))
c=n/m
r=n%m
print("El cociente entre "+ str(n)+ " y "+ str(m) +" es: "+ str(c)+ "y el resto: "+str(r))
print("")

'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión.
'''
monto=float(input("Ingrese el monto de capital "))
interes=float(input("Ingrese el interes "))
años=int(input("¿Por cuantos años? "))
retorno=round(monto*(interes/100+1)**años,2)
print("El capital de retorno es: $"+str(retorno))
print("")
'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la
empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas 
que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será 
enviado
'''
dolls=int(input("Ingrese cantidad de muñecas vendida "))
clown=int(input("Ingrese la cantidad de payasos vendidos "))
peso_dolls=dolls*75
peso_clown=clown*112
print("El peso total del paquete es de: "+str(peso_dolls+peso_clown)+"grs")
print("")

'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu
cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de
ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de 
ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''
monto=float(input("Ingrese el monto a invertir "))
interes=0.04
primer_cierre=monto*(1+interes)
segundo_cierre=primer_cierre*(1+interes)
tercer_cierre=segundo_cierre*(1+interes)
print("Retorno del primer año: $"+str(round(primer_cierre,2)))
print("Retorno del segundo año: $"+str(round(segundo_cierre,2)))
print("Retorno del tercer año: $"+str(round(tercer_cierre,2)))
print("")

'''
Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no 
ser fresca y el coste final total.
'''

pan_ayer=int(input("Ingrese la cantidad de pan de ayer vendido "))
precio=3.49
descuento=0.6
precio_final=((pan_ayer*precio)*descuento)
print("Precio habitual: $"+str(precio)+" descuento %60, precio final: $"+ str(precio_final))
print("")