import unittest
from Desviacion import calcular_promedio, calcular_desviacion_estandar, NoSePuedeCalcular

class TestCalculos(unittest.TestCase):

    def test_promedio_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_promedio([])

    def test_promedio_un_elemento(self):
        self.assertEqual(calcular_promedio([5]), 5)

if __name__ == '__main__':
    unittest.main()
