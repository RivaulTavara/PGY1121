import os
os.system("color a")
vLogin = 1
print("LOGIN")
vNombre=str(input("Ingrese su nombre de usuario: "))
while vLogin == 1:
    print("LOGIN")
    vPassword = str(input("Ingrese su contraseña: "))
    if vPassword == "ZTM":
        os.system("cls") 
        input("Programa Iniciado \n")
        vLogin = 0      
    else:
        os.system("cls") 
        print("ERROR")
        input("Clave Incorrecta: \n")
        os.system("cls")  
print("=========================")
print(f"\nBienvenido {vNombre}\n")
print("=========================")
vL = 30
for Fila in range(vL):
    for Columna in range (vL):
        if Fila == 0 or Fila == vL - 1 or Columna == 0 or Columna == vL - 1:
            print("* ", end=" ")
        else:
            print("  ", end=" ")