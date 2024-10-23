import unittest
from Desviacion import calcular_promedio, calcular_desviacion_estandar, NoSePuedeCalcular

class TestCalculos(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])


if __name__ == '__main__':
    unittest.main()
