import unittest
from Desviacion import calcular_promedio, calcular_desviacion_estandar, NoSePuedeCalcular

class TestCalculos(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

    def test_promedio_un_elemento(self):
        self.assertEqual(calcular_promedio([5]), 5)

    def test_desviacion_estandar_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_desviacion_estandar_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0)


if __name__ == '__main__':
    unittest.main()
