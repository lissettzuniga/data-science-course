"""
while nos permite ejecutar una sección de código repetidas veces,
de ahí su nombre. El código se ejecutará mientras una condición determinada se cumpla.
"""
print("Ejercicio 1: \n")
print("Crea un programa que simule las ventas de un libro" +
      " con el inventario inicial de 5 ejemplares. El programa debe mostrar el mensaje " +
      "\"¡Venta realizada! Inventario restante: <cantidad>\" con cada venta y," + 
       "  al final, mostrar el mensaje \"Inventario agotado\".")

inventario = 6
while inventario > 1:
    print(f"¡Venta realizada! Inventario restante: {inventario - 1}")
    inventario -= 1
print("Inventario agotado")

print("\nEjercicio 2: \n")
print("Escribe un programa que muestre los números del 1 al 5 usando un ciclo while.")

numero = 1
while numero <= 5:
    print(numero)
    numero += 1

print("\nEjercicio 3: \n")
print("Crea un programa que pida números al usuario y los vaya sumando." +
      " El programa debe terminar cuando el usuario escriba 0.")

suma = 0 
while True:
    numero = int(input("Introduce un número: "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}")

print("\nEjercicio 4: \n")
print("El programa tiene un número secreto." + 
    " El usuario debe intentar adivinarlo." +
    " El programa se repite hasta que el usuario acierte.")

numero_secreto = 7
while True:
    numero_usuario = int(input("Adivina el número secreto (entre 1 y 10): "))
    if numero_usuario == numero_secreto:
        print("¡Felicidades! Has adivinado el número secreto.")
        break