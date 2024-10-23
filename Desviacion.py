class NoSePuedeCalcular(Exception):
    pass

def calcular_promedio(elementos):
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía")
    if not all(isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser números")
    return sum(elementos) / len(elementos)