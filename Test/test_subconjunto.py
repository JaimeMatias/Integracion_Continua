from read import read_ar
from subconjunto import subconjuntoclase
import unittest

class TestStringMethods(unittest.TestCase):
    def test_subconjuntoclase(self):
        archivo = read_ar('datos_prueba.csv')
        var = subconjuntoclase(archivo[1])
        valor=(['no', 'yes'], [6, 7])
        self.assertEqual(var,valor)

if __name__ == '__main__':
    unittest.main()