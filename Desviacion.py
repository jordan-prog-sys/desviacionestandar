class NoSePuedeCalcular(Exception):
    pass

def calcular_promedio(elementos):
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía")
    if not all(isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser números")
    return sum(elementos) / len(elementos)

import math

def calcular_desviacion_estandar(elementos):
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía")
    promedio = calcular_promedio(elementos)
    varianza = sum((x - promedio) ** 2 for x in elementos) / len(elementos)
    return math.sqrt(varianza)
