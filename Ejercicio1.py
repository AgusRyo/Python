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



