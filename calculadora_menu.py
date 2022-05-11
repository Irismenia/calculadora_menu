# Calculadora Básica con menú

from math import log  

# input
bandera = False 
x = float(input("Dame el valor del número x: "))
y = float(input("Dame el valor del número y: "))

print("Dame la opción que deseas realizar: \n")

# Se despliega el me+u para seleccionar la opción que deseas
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. División")
print("5. Potencia")
print("6. Logaritmo")

opcion = int(input("Dame la opción: "))

# Processing
if (opcion == 1):
    z = x + y
    print( x," + ",y)
elif (opcion == 2):
    z = x - y
    print(x, " - ", y) 
elif(opcion == 3):
    z = x * y
    print(x, " * ",y)
elif(opcion == 4 and y != 0):
    z = x/y;
    print(x," / ", y)
elif(opcion == 4 and y == 0):
    print("El denominador es igual a cero y")
    print("NO se puede realizar la división")
    bandera = True
elif(opcion == 5):
    z = pow(x,y)
    print(x," ^ ", y)
elif(opcion == 6 and x > 0):
    z = log(x)
    print("Logaritmo de ", x)
elif(opcion == 6 and x <= 0):
    print("Logaritmo de ", x)
    bandera = True
else:
    print("Opcion no valida")
 
 
# Se escribe el resultado con otra condición 
if (opcion < 7 and bandera == False):
     print("Resultado = ", z)

# FIN