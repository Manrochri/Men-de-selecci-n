# Menú de opciones
#---------------------------------
import os
def clear_console():
  os.system('clear')
#-------------------------------------
#------def variables---------------
  
#-- -- ---------------
nombre = input("Hola ¿Cuál es tu nombre? \n")
print ("Hola, ", nombre, ". Se bienvenido(a) a nuestro restaurante")

opc = int(
  input(
    "Escoge uno de nuestros apetitosos platillos : \n -------------------- \n 0.Salir del menú \n 1: Arroz con pollo ---------------- s/18.00 \n 2. Pollo a la brasa --------------- s/25.00 \n 3: Chaufa ------------------------- s/14.00 \n 4: Ceviche ------------------------ s/18.00 \n  "
  ))
# respuesta por opciones
while opc != 0:
  if opc == 1:
    print("Escogiste arroz con pollo \n")
    platos_1 = input("Ingrese la cantidad de platos: " )
    p1 = int(platos_1 )
    arrozconpollo = 18
    total1 = p1 * arrozconpollo
    print(total1)
    vuelto1 = input("Proceda a cancelar ")
    v1= int(vuelto1)
    monto1 = v1 - total1
    print ("Vuelto: ", monto1)
    break 
    #-----------------------------------------------------------------------
  elif opc == 2:
    print("Escogiste pollo a la braza \n")
    platos_2 = input("Ingrese la cantidad de platos: " )
    p2 = int(platos_2 ) 
    polloalabrasa = 25
    total2 = p2 * polloalabrasa
    print(total2)
    vuelto2 = input("Proceda a cancelar ")
    v2= int(vuelto2)
    monto2 = v2 - total2
    print ("Vuelto: ", monto2)
    break     
#-----------------------------------------------------------------------
  elif opc == 3:
   print("Escogiste un deliciosos chaufa \n")
   platos_3 = input("Ingrese la cantidad de platos: " )
   p3 = int(platos_3 ) 
   chaufa = 14
   total3 = p3 * chaufa
   print(total3)
   vuelto3 = input("Proceda a cancelar ")
   v3= int(vuelto3)
   monto3 = v3 - total3
   print ("Vuelto: ", monto3)
   break   
  elif opc == 4:
   platos_4 = input("Ingrese la cantidad de platos: " )
   p4 = int(platos_3 ) 
   ceviche = 18
   total4 = p4 * ceviche
   print(total4)
   vuelto4 = input("Proceda a cancelar ")
   v4= int(vuelto4)
   monto4 = v4 - total4
   print ("Vuelto: ", monto4)
   break   
#...........................
  elif opc == 0: 
    print ("Hasta pronto")
  else:
    input(" \n Opción inválida. Pulse una tecla para intentarlo de nuevo")
    clear_console()
    opc = int(
    input(
      "Escoge uno de nuestros apetitosos platillos : \n -------------------- \n 0.Salir del menú \n 1: Arroz con pollo ---------------- s/18.00 \n 2. Pollo a la brasa --------------- s/25.00 \n 3: Chaufa ------------------------- s/14.00 \n 4: Ceviche ------------------------ s/18.00 \n  "
    ))
#------fin del bucle----------------------------------------#
print ("\n Hasta pronto. Muchas gracias por su compra :) ")

