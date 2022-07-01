# Esta es una aplicación para calcular el balance de una inversión con un interés compuesto después de un período determinado de tiempo

# Módulos necesarios para el algoritmo
import math
import os
import sys
import time
import readchar as read

# Variables globales del algoritmo
p = float(0)  # Inversión principal
t = int(0)    # Tiempo de la inversión
n = int(0)    # Frecuencia de capitalización 
r = float(0)  # La tasa de interés anual
b = float(0)  # El balance de la inversión
e = math.e    # El número de Euler
name = str("")  # Nombre del usuario
validName = True  # Validación del nombre

#Función para obtener el nombre del usuario y saludar
def Saludo():
  print("CALCULADORA DE INTERÉS COMPUESTO")
  print("==============================================")
  print("Bienvenido a la calculadora de balance con interés compuesto")
  print()

  global name
  name = str(input("Por favor, digite su primer nombre: "))
  validName = name.isalpha()

  while validName == False:
    print("...")
    print("Los datos introducidos no son válidos")
    name = str(input("Por favor, ingrese de nuevo su nombre: "))
    validName = name.isalpha()

    if validName == True:
      break
  print("Gracias por los datos suministrados,", name.upper())
  print("¡Empecemos a trabajar!")
  print()

  animacion = "|/-\\"
  for i in range(20):
    time.sleep(0.1)
    sys.stdout.write("\r" + animacion[i % len(animacion)])
    sys.stdout.flush()

  print(" Cargando...")
  time.sleep(2)

# Función para limpiar la consola
def LimpiarConsola():
  comando = "clear"
  if os.name in ("nt", "dos"):
    comando = "cls"
  os.system(comando)

# Función para mostrar las opciones de capitalización
def MenuCapitalizacion():
  print("FRECUENCIA DE CAPITALIZACIÓN")
  print("==============================================")
  print("Por favor, seleccione la frecuencia de capitalización")
  print("1. Capitalización Anual")
  print("2. Capitalización Semestral")
  print("3. Capitalización Trimestral")
  print("4. Capitalización Mensual")
  print("5. Capitalización Semanal")
  print("6. Capitalización Diaria")
  print("7. Capitalización Continua")
  print()

  menu = [1, 2, 3, 4, 5, 6, 7]
  opcion = 0

  global n
  while opcion not in menu:
    try:
      opcion = int(input("Escribe la opción deseada: "))
      if opcion not in menu:
        print("...")
        print("Opción no válida")
        print("Escribe un número del 1 al 7")
        print("---------------------------------")
        print()
      elif opcion == 1:
        print("Usted seleccionó capitalización anual")
        n = 1
      elif opcion == 2:
        print("Usted seleccionó capitalización semestral")
        n = 2
      elif opcion == 3:
        print("Usted seleccionó capitalización trimestral")
        n = 4
      elif opcion == 4:
        print("Usted seleccionó capitalización mensual")
        n = 12
      elif opcion == 5:
        print("Usted seleccionó capitalización semanal")
        n = 52
      elif opcion == 6:
        print("Usted seleccionó capitalización diaria")
        n = 365
      elif opcion == 7:
        print("Usted seleccionó capitalización continua")
        n = e
      print("...")
      print()
      time.sleep(1)
    except:
      print("...")
      print("Opción no válida")
      print("Escribe un número del 1 al 7")
      print("---------------------------------")
      print()

# Función que recibe la inversion principal
def InversionPrincipal():
  print("INVERSIÓN PRINCIPAL")
  print("==============================================")

  while True:
    try:
      global p
      p = float(input("Ingrese el monto de la inversión: "))
      print()

      if p == 0:
        print("El monto ingresado es incorrecto")
        print("la inversión no puede ser cero", name.upper())
        print("...")
        print()
        continue
      else:
        print("La inversión principal es de: $","{:,}".format(round(p, 2)))
        print("...")
        print()
        time.sleep(1)
        break

    except:
      print("El monto ingresado es incorrecto")
      print("Revisálo e intente de nuevo", name.upper())
      print("...")
      print()

# Función para obtener la tasa de interes
def TasaInteres():
  print("TASA DE INTERÉS ANUAL")
  print("==============================================")
  print("Ejemplo: para una tasa de 9.58% sólo digite 9.58")

  while True:
    try:
      global r
      r = float(input("Por favor digite la tasa de interés: "))
      print()

      if r <= 0:
        print("El valor ingresado es incorrecto")
        print("la tasa no puede ser cero o negativo", name.upper())
        print("...")
        print()
        continue
      else:
        print("El porcentage anual es de: ", round(r, 2), "%")
        print("...")
        print()
        time.sleep(1)
        break

    except:
      print("El valor ingresado es incorrecto")
      print("Por favor revise, luego intente de nuevo", name.upper())
      print("...")
      print()

# Funcion para obtneter la cantidad de tiempo de la inversion
def CantidadTiempo():
  print("CANTIDAD DE TIEMPO")
  print("==============================================")
  print("Cantidad de tiempo en años")

  while True:
    try:
      global t
      t = int(input("Ingrese  la cantidad de años: "))
      print()
      
      if t <= 0:
        print("El valor ingresado es incorrecto")
        print("la tiempo no puede ser cero o negativo", name.upper())
        print("...")
        print()
        continue
      else:
        print("El balance se calculará después de:", t, "años")
        print("...")
        print()
        time.sleep(4)
        break
    except:
      print("Entrada inválida")
      print("Por favor, intente nuevamente.", name.upper())
      print("...")
      print()

# Funcion par calcular el balance
def Balance():
  print("BALANCE OBTENIDO")
  print("==============================================")
  print("Por un monto invertido de: $", "{:,}".format(round(p, 2)))
  print("A una tasa de interé del:", round(r, 2), "%")
  print("Después  de:", t, "años")
  print()
  
  if n == e:
    b = p * (math.pow(e, r * t / 100))
    b = "{:,}".format(round(b, 2))
    print("El balance es: $", b)
  else:
    b = p * math.pow(1 + r / (100 * n), n * t)
    b = "{:,}".format(round(b, 2))
    print("El balance es: $", b)


# Funcion para dibujar una tabla de datos
def Tabla():
  cabecera1 = ["Años", "Interés", "Balance"]
  cabecera2 = ["-----", "----------", "-----------"]
  print()
  print("-----------------------------------------------")
  print("{: >5} {: >20} {: >20}".format(*cabecera1))
  print("{: >5} {: >20} {: >20}".format(*cabecera2))

  global t
  x = 0  # x es usado para mostrar el incremento del balance
  i = 0  # i es el monto que corresponde solo al interes
  
  while x <= t:
    if n == e:
      b = p * (math.pow(e, r * x / 100))
      b = "{:,}".format(round(b, 2))
      i = p * (math.pow(e, r * x / 100) - 1)
      i = "{:,}".format(round(i, 2))

    else:
      b = p * math.pow(1 + r / (100 * n), n * x)
      b = "{:,}".format(round(b, 2))
      i = p * (math.pow(1 + r / (100 * n), n * x) - 1)
      i = "{:,}".format(round(i, 2))

    datos = [str(x), "$" + i, "$" + b]
    print("{: >5} {: >20} {: >20}".format(*datos))
    x += 1
  print()
  print()
  print()
  time.sleep(8)

# Función para cerrar el programa
def CerrarPrograma():
  print("CONFIRMACIÓN PARA CERRAR")
  print("==============================================")
  print("Gracias por usar la app", name.upper())
  print("...")
  print("¿Quieres realizar otro cálculo?")
  print("Presione 0 para cerrar o cualquier otra tecla para seguir: ")
  global cerrar
  cerrar = int(read.readchar())

# Area de ejecución de los procesos
Saludo()
LimpiarConsola()
cerrar = ""

while True:
  MenuCapitalizacion()
  InversionPrincipal()
  TasaInteres()
  CantidadTiempo()
  LimpiarConsola()
  Balance()
  Tabla()
  CerrarPrograma()

  if cerrar == 0:
    print()
    print("Cerrando..., Adios!!! 😞")
    time.sleep(1)
    break
  else:
    LimpiarConsola()
    continue

# Fin de los procesos