email=input("intruduce tu direccion de email: ")

arroba=email.count("@")

if (arroba!=1 or email.rfind("@")==(len(email)-1) or email.find("@")==0):
    print("mail incorrecto")

else:
    print("mail correcto")



