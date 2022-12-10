# Menú de opciones
x = type(int)
import os
def clear_console():
    os.system('clear')
opc = int(input("Escoger una opción: \n -------------------- \n 0.Salir del menú \n 1. Arroz con pollo \n 2.pollo a la braza \n 3.chaufa \n 4.ceviche \n 5.pachamanca  \n  "))
# respuesta por opciones
while opc != 0: 
  if opc == 1:
    input("Escogiste arroz con pollo")
    arz = 18
    print("pulse una tecla para continuar")
    clear_console()
  elif opc == 2:
    input("Escogiste pollo a la braza")
    print("pulse una tecla para continuar")
    clear_console()
  elif opc == 3:
    input("Escogiste chaufa")
    print("pulse una tecla para continuar")
    clear_console()
  elif opc == 4:
    input("Escogiste ceviche")
    print("pulse una tecla para continuar")
    clear_console()
  elif opc == 5:
    input("Escogiste pachamanca")
    print("pulse una tecla para continuar")
    clear_console()
  else: 
    print("inténtelo de nuevo. Pulse una tecla para continuar")
    clear_console()
    
  opc = int(input("Escoger una opción: \n -------------------- \n 0.Salir del menú \n 1. Arroz con pollo \n 2.pollo a la braza \n 3.chaufa \n 4.ceviche \n 5.pachamanca  \n  "))

