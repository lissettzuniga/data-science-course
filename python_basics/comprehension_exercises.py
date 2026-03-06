# ===============================
# Ejercicio 1 - Índice de masa corporal (IMC)
# ===============================

print("Ejercicio 1 - Índice de masa corporal:\n")

alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round(peso / altura**2, 1) for altura, peso in zip(alturas, pesos)]

print("Lista de IMC:")
print(imc)


# ===============================
# Ejercicio 2 - Suma de listas
# ===============================

print("\nEjercicio 2 - Suma de cada lista:\n")

lista_de_listas = [
    [4, 6, 5, 9],
    [1, 0, 7, 2],
    [3, 4, 1, 8]
]

for lista in lista_de_listas:
    print(sum(lista))


# ===============================
# Ejercicio 3 - Extraer peso de tuplas
# ===============================

print("\nEjercicio 3 - Extraer peso de cada tupla:\n")

lista_de_tuplas = [
    ('Pedro', 1.74, 81),
    ('Júlia', 1.65, 67),
    ('Otávio', 1.81, 83)
]

pesos = [tupla[2] for tupla in lista_de_tuplas]

print(pesos)


# ===============================
# Ejercicio 4 - Diccionario con comprensión
# ===============================

print("\nEjercicio 4 - Diccionario de gastos por mes:\n")

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
         'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

gasto = [860, 490, 1010, 780, 900, 630,
         590, 770, 620, 560, 840, 360]

diccionario_gastos = {mes: valor for mes, valor in zip(meses, gasto)}

print(diccionario_gastos)


# ===============================
# Ejercicio 5 - Filtrar ventas
# ===============================

print("\nEjercicio 5 - Ventas del 2022 mayores a 6000:\n")

ventas = [
    ('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883),
    ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544),
    ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471),
    ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)
]

ventas_filtradas = [
    valor for año, valor in ventas
    if año == '2022' and valor > 6000
]

print(ventas_filtradas)


# ===============================
# Ejercicio 6 - Clasificación de glucosa
# ===============================

print("\nEjercicio 6 - Clasificación de glicemia:\n")

glicemia = [
    129, 82, 60, 97, 101, 65, 62, 167, 87, 53,
    58, 92, 66, 120, 109, 62, 86, 96, 103, 88,
    155, 52, 89, 73
]

etiquetas = [
    ('Hipoglicemia', g) if g <= 70 else
    ('Normal', g) if g < 100 else
    ('Alterada', g) if g < 125 else
    ('Diabetes', g)
    for g in glicemia
]

print(etiquetas)