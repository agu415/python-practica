#ejercicio 1


# n1=int(input("introduce un numero: "))
# n2=int(input("introduce un numero mayor que " + str(n1)+ ": "))

# while n2>n1:
#     n1=n2
#     n2=int(input("este numero es mayor que " + str(n1)+ ": "))

# print()
# print(n2, "no es mayor que",str(n1))

#ejercicio 2

numero=int(input("ingresa un numero: "))
suma=0

while numero > 0:
    suma=suma+numero
    numero=(int(input("ingresa otro numero: ")))
    print(str(suma))

print("la suma de los numeros ingresados: ", str(suma))
