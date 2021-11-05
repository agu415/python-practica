# i= 1

# while i<=10:
#     print("ejecucion " + str(i))
#     i=i+1

# print("termino la ejecucion")




# edad= int(input("intruduce tu edad: "))

# while edad<5 or edad>100:
#     print("has introducido na edad incorrcta. vuelve a intearlo")
#     edad=int(input("introduce tu edad: "))

# print("gracias por colaborar")
# print("edad del usuario " + str(edad))




# import math
# print("programa de calculo de raiz cuadrada")
# numero=int(input("introduce un numero por favor: "))

# intentos=0
# while numero<0:
#     print("no se puede hallar la raiz de un numero negativo")
#     if intentos==2:
#         print("has consumidos todos tus intentos")
#         break;
    
#     numero=int(input("introduce un numero por favor: "))
#     if numero<0:
#         intentos=intentos+1

# if intentos<2:
#     solucion= math.sqrt(numero)
#     print("la raiz cuadrada de "+ str(numero)+ " es "
#     +str(solucion))


# for letra in "python":

#     if letra=="h":
#         continue


#     print("viendo la letra: " + letra)

#para qu no cuene el espacio" "
# nombre= "agustin mebar"
# contador=0

# for i in  nombre:

#     if i==" ":
#         continue
#     contador+=1

# print(contador)

#mensaje de edad (clase de error todavia no vimos)
# def evalua_edad(edad):

#     if edad<0:
#         raise TypeError("no se permiten edades negativas")

#     if edad<20:
#         return "eres muy joven"
#     elif edad<40:
#         return "eres joven"
#     elif edad<65:
#         return "eres maduro"
#     elif edad<100:
#         return "cuidate..."
# print(evalua_edad(18))


import math

def calcula_raiz(n1):
    
    if n1<0:
        raise ValueError ("el numero no puede ser negativo")

    else:
        return math.sqrt(n1)

op1=(int(input("introduce un numero: ")))
try:
    print(calcula_raiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("programa terminado")