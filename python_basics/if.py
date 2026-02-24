"""
    if condición:
    acción
    else:
    acción
"""
nombre = 'Alura'
if nombre == "Alua":
    print("Condición verdadera")
elif nombre == 'Alura':
    print("Condición 2 verdadera")
else:
    print("condición falsa")

"""
1° Ejercicio
Bruno gestiona un pequeño comercio y quiere saber qué producto
tuvo el mejor desempeño de ventas el mes pasado. 
Registró la cantidad vendida de dos productos: manzanas y plátanos.
Ahora, necesita escribir un programa que identifique y muestre cuál de ellos tuvo más ventas.

Crea un programa que reciba el número de ventas de los dos productos 
y muestre un mensaje indicando cuál de ellos vendió más. Si las cantidades son iguales,
 muestra un mensaje diciendo que hubo un empate.

Salida esperada:
Digite la cantidad de manzanas vendidas: 50
Digite la cantidad de plátanos vendidos: 30
Los ___ tuvieron más ventas.
"""

manzanas = int(input("Digite la cantidad de manzanas vendidas: "))
platanos = int(input("Digite la cantidad de plátanos vendidos: "))

if manzanas > platanos:
    print("Las manzanas tuvieron más ventas.")
elif platanos > manzanas:
    print("Los plátanos tuvieron más ventas.")
else:
    print("Las ventas fueron iguales.")


"""
2° Ejercicio
Lucas trabaja en TI y necesita garantizar que la temperatura de una sala
 de servidores no supere los 25°C. Quiere un programa que reciba la 
 temperatura actual como entrada y, si es necesario,
muestre un mensaje de alerta."""

temperatura = float(input("Digite la temperatura actual de la sala de servidores: "))
if temperatura > 25:
    print("¡Alerta! La temperatura excede los 25°C.")
else:
    print("La temperatura está dentro del rango seguro.")


"""
3° Ejercicio
Anna Júlia está creando un sistema para calcular el Índice de Masa Corporal 
(IMC) y proporcionar recomendaciones básicas.
 El programa debe recibir el peso y la altura de una persona y 
mostrar el valor del IMC, además de indicar si está por debajo del peso, 
con peso normal o por encima del peso. 
Crea un programa que reciba el peso (en kg) y la altura (en metros) y 
calcule el IMC usando la fórmula: IMC = peso / (altura ** 2)
Luego, muestra el valor del IMC y
 un mensaje indicando si está por debajo del peso (IMC < 18.5), 
 peso normal (18.5 <= IMC < 25) o por encima del peso (IMC >= 25)."""

peso = float(input("Digite su peso (kg): "))
altura = float(input("Digite su altura (m): "))

imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estás por debajo del peso.")
elif imc < 25:
    print("Tienes un peso normal.")
else:
    print("Estás por encima del peso.")


"""4° Ejercicio
Estás desarrollando un pequeño juego. 
El usuario ingresa un número entero y 
el programa debe evaluar lo siguiente:

Si el número es divisible por 3 y 5, muestra: "¡Número mágico!"
Si solo es divisible por 3, muestra: "Divisible por 3"
Si solo es divisible por 5, muestra: "Divisible por 5"
Si no es divisible por ninguno, muestra: "No es un número mágico"""

numero = int(input("Ingrese un número entero: "))
if numero %3==0 and numero %5 == 0:
    print("¡Número mágico!")
elif numero %3==0:
    print("Divisible por 3")
elif numero %5==0:
    print("Divisible por 5")
else:
    print("No es un número mágico")