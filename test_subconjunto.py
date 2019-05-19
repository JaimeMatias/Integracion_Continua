from subconjunto import subconjuntoclase
from read import read_ar
import unittest

class  TestStringMethods(unittest.TestCase ):
    def test_subconjuntoclase(self):
        archivo = read_ar('datos_prueba.csv')
        var = subconjuntoclase(archivo[1])
        valor= (['no', 'yes'], [6, 7])
        self.assertEqual(var, valor)

print('el nombre es: ', __name__)
if __name__ == '__main__':
    unittest.main()