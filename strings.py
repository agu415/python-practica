# myStr = "Hola agustin"

# print(myStr + " loco de mierda")

# print(f"{myStr} loco de mierda")

# print("{0} loco de mierda".format(myStr))

#print(dir(myStr)) 

# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase())
# print(myStr.capitalize())

# print(myStr.replace("Hola", "bye").upper())

# print(myStr.count("a"))

# print(myStr.startswith("Hol"))

# print(myStr.endswith("ee"))

# print(myStr.split("a"))
# print(myStr.find("i"))
# print(len(myStr))
# print(myStr.index("o"))
# print(myStr.isnumeric())
# print(myStr.isalpha())

# print(myStr[3])
# print(myStr[2])
# print(myStr[0])
# print(myStr[-1])
# print(myStr[-2])

edad=input("introduce la edad: ")

while(edad.isdigit()==False):

    print("por favor, introduce un valor numerico")

    edad=input("intruduce la edad: ")

if(int(edad)<18):

    print("no puede pasar")
else:
    print("puede pasar")

