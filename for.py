"""
for  = se utiliza para iterar sobre una secuencia 
(que puede ser una lista, una tupla, un diccionario, un conjunto o una cadena). 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
"""

print("Ejercicio 1: \n")
print("Ana está desarrollando un programa que necesita procesar una lista" +
" de 5 nombres de clientes para generar informes mensuales." +
" Para ello, necesita escribir un programa que recorra " +
" la lista de nombres y muestre cada cliente.")

clientes = ["Juan", "Maria", "Carlos", "Ana", "Beatriz"]
for cliente in clientes:
    print(cliente)

print("\nEjercicio 2: \n")
print("Marcos está desarrollando un programa para mostrar un mensaje" +
" de bienvenida repetidamente en la consola, como parte de una campaña" +
" de marketing de su plataforma llamada Buscante." + 
" Quiere asegurarse de que el mensaje se muestre 5 veces.")

print("\nAyuda a Marcos a escribir un programa que muestre el mensaje: " + 
    "¡Bienvenido a Buscante!" + " 5 veces.\n")
for i in range(5):
    print("¡Bienvenido a Buscante!")

print("\nEjercicio 3: \n")
print("Estás recibiendo una lista de valores que representan los productos" + 
      " de tu tienda virtual y te gustaría calcular la suma total de esos productos" + 
      " para entender el desempeño financiero semanal.")
print("Crea un programa para implementar la suma.\n")

precios = [19.99, 5.49, 3.50, 12.00, 7.25]
suma_total = 0
for precio in precios:
    suma_total += precio
print(f"La suma total de los productos es: {suma_total}") 


print("\nEjercicio 4: \n")
print("Ana está desarrollando su portafolio para exhibir los proyectos de Python que ha completado." + 
      " Ella organizó una lista con el nombre de cada proyecto," + 
      " pero se dio cuenta de que algunos elementos pueden estar ausentes," + 
      " apareciendo como None:")
print("Crea un programa que ayude a Ana a recorrer la lista de proyectos y" + 
      " muestre los nombres de los proyectos válidos. Si encuentra un elemento None," + 
      " el programa debe mostrar el mensaje: \"Proyecto ausente\".")

proyectos = ["sitio web", "juego", "análisis de datos", None, "aplicativo móvil"]

for proyecto in proyectos:
    if proyecto != None:
        print(proyecto)
    else:
        print("Proyecto ausente") 


print("\nEjercicio 5: \n")
print("Crea un programa que utilice un bucle for para mostrar los siguientes mensajes:" + 
      "Para números pares, muestra: \"Faltan solo <número> segundos - ¡No pierdas esta oportunidad!\"." +
      "Para números impares, muestra: \"La cuenta continúa: <número> segundos restantes.\"." +
      "Al final de la cuenta, muestra el mensaje: \"¡Aprovecha la promoción ahora!\".")

for segundos in range(10, 0, -1):  
    if segundos % 2 == 0: 
        print(f"Faltan solo {segundos} segundos - ¡No pierdas esta oportunidad!")
    else: 
        print(f"La cuenta continúa: {segundos} segundos restantes.")

print("¡Aprovecha la promoción ahora!")