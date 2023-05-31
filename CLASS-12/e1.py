import os
os.system("color a")
vSys = True
vCategoria = str("")
vCCategoriaNino = 0
vValorNino = 0
vCCategoriaJoven = 0
vValorJoven = 0
vCCategoriaAdulto = 0
vValorAdulto = 0
vValorFinal = 0
vCEntradasFinal = 0
vGTotales = 0
vOp = 0
vContadorNino = 0
vContadorJoven = 0
vContadorAdulto = 0
vCEntradas = 0
vContadorAdulto = 0
while vSys == True:
  os.system("cls")
  print("\nBienvenido al cine Moro\n")
  print("[1] Niño      (01 - 13 años)          [$5500]")
  print("[2] Joven     (14 - 21 años)          [$7000]")
  print("[3] Adulto (Mayores de 22 años)       [$9000]")
  print("[4] Imprimir Boleta")
  print("[5] Salir")
  vOp = (input("Seleccione una opción: "))
  if vOp == "1":
    try:
        vCategoria = "Niño"
        print(f"¿Que cantidad de entradas para {vCategoria} desea?")
        vCCategoriaNino = int(input(""))
        vValorNino = vCCategoriaNino * 5500
        vValorFinal = vValorFinal + vValorNino
        vCEntradas = vCEntradas + vCCategoriaNino
        vCEntradasFinal = vCEntradasFinal + vCCategoriaNino
        vContadorNino = vContadorNino + vCCategoriaNino
        input("Compra Realizada Con exito: ")
    except:
        input("ERROR: Será enviado al Menú")
  elif vOp == "2":
    try:
        vCategoria = "Joven"
        print(f"¿Que cantidad de entradas para {vCategoria} desea?")
        vCCategoriaJoven = int(input(""))
        vValorJoven = vCCategoriaJoven * 7000
        vValorFinal = vValorFinal + vValorJoven
        vCEntradas = vCEntradas + vCCategoriaJoven
        vCEntradasFinal = vCEntradasFinal + vCCategoriaJoven
        vContadorJoven = vContadorJoven + vCCategoriaJoven
        input("Compra Realizada Con exito: ")
    except:
      input("ERROR: Será enviado al Menú")  
  elif vOp == "3":
    vCategoria = "Adulto"
    print(f"¿Que cantidad de entradas para {vCategoria} desea?")
    vCCategoriaAdulto = int(input(""))
    vValorAdulto = vCCategoriaAdulto * 9000
    vValorFinal = vValorFinal + vValorAdulto
    vCEntradas = vCEntradas + vCCategoriaAdulto
    vCEntradasFinal = vCEntradasFinal + vCCategoriaAdulto
    vContadorAdulto = vContadorAdulto + vCCategoriaAdulto
    input("Compra Realizada Con exito: ")
  elif vOp == "4":
    vGTotales = vValorFinal + vGTotales
    if vCCategoriaNino >= 1:
        try:
            print(f"Categoría: Niño")
            print(f"Cantidad de entradas: {vCCategoriaNino}")
            print(f"Total a pagar: {vValorNino}")
            input("Pulse cualquier tecla para continuar: ") 
        except:
            input("ERROR: Será enviado al Menú")
    if vCCategoriaJoven >= 1:
        print(f"Categoría: Joven")
        print(f"Cantidad de entradas: {vCCategoriaJoven}")
        print(f"Total a pagar: {vValorJoven}")
        input("Pulse cualquier tecla para continuar: ")
    if vCCategoriaAdulto >= 1:
      print(f"Categoría: Adulto")
      print(f"Cantidad de entradas: {vCCategoriaAdulto}")
      print(f"Total a pagar: {vValorAdulto}")
      input("Pulse cualquier tecla para continuar: ")
    if vCCategoriaNino == 0 and vCCategoriaJoven == 0 and vCCategoriaAdulto == 0:
      input("Para generar la boleta primero seleccione un tipo de entrada: ")
      if vValorFinal > 0:
        print(f"El total a pagar es de: {vValorFinal}")
        print("Gracias por su compra, disfrute la función.")
        input("")
    vCCategoriaNino = 0
    vValorNino = 0
    vCCategoriaJoven = 0
    vValorJoven = 0
    vCCategoriaAdulto = 0
    vValorAdulto = 0
    vValorFinal = 0
  elif vOp == "5":
    vSys = False
  else:
    input("Ingrese una opción valida.\n")
vPorcentajeNino = (vContadorNino * 100) / vCEntradasFinal
vPorcentajeJoven = (vContadorJoven * 100) / vCEntradasFinal
vPorcentajeAdulto = (vContadorAdulto * 100) / vCEntradasFinal
print(f"La cantidad total de entradas vendidas es de: {vCEntradasFinal}")
print(f"La cantidad de entradas tipo Niño es de: {vContadorNino} ({vPorcentajeNino}%)")
print(f"La cantidad de entradas tipo Niño es de: {vContadorJoven} ({vPorcentajeJoven}%)")
print(f"La cantidad de entradas tipo Niño es de: {vContadorAdulto} ({vPorcentajeAdulto}%)")
print(f"La cantidad de dinero recaudado es de: {vGTotales}")