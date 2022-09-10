# calculadora con menu
from math import log
print ("--------------------------")
print ("----CALCULADORA - MENU----")
print ("--------------------------")

#INPUT
bandera=False
x=float (input ("ingrese el valor de el número x: "))
y= float (input("ingrese el valor de el núnmero y: "))

print ("\ndame la opcion que deseas realizar: \n")
# se despliega el meni para seleccionar la opcion que desea realiza:
print("1. sumar (el primero más el segundo)")
print("2. restar(el primero menos el segundo)")
print("3. multiplicar (el primero por el segundo)")
print("4. dividir (el primero más  segundo)")
print("5. sumar (el primero a la potencia de el segundo)")
print("6. sumar (el logaritmo de el primero")

opcion= int(input ("digite la opcion: "))
#procesing
if (opcion ==1):
    z=x+y
    print (x, "+", y)
elif (opcion==2):
    z=x-y
    print(x,"-", y)
elif (opcion==3):
    z= x*y
    print( x, "x", y)
elif (opcion ==4 and y!=0):
    z= x/y
    print(x, "/", y)
elif (opcion ==4 and y==0):
    print("el denomidor es igual a cero y")
    print ("NO se puede realizar la divison")
    bandera=True
elif (opcion ==5):
    z= pow(x,y)
    print (x, "**", y)
elif (opcion==6 and x>0):
    z= log(x)
    print("logaritmo de ", x)
elif (opcion==6 and x<=0):
    print(" el valor de x es <= a cero y")
    print ("NO se puede calcular el logaritmo")
    bandera= True
else:
    print ("opcion no valida")

#se escribe el resultado con otra condicion
if (opcion <7 and bandera ==False):
    print ("Resultado =", z)
#fin





