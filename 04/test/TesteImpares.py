import unittest
import sys
sys.path.insert(0, '04\main')

from Impares import Impares

class TesteNumerosImpares(unittest.TestCase):
    
    def test_seisNumerosImpares_inicioZero(self):
        impares = Impares()
        resultado = impares.seisNumerosImpares(0)
        self.assertEqual(resultado, [1,3,5,7,9,11])
        
    def test_seisNumerosImpares_inicioImpar(self):
        impares = Impares()
        resultado = impares.seisNumerosImpares(7)
        self.assertEqual(resultado, [7,9,11,13,15,17])
        
    def test_seisNumerosImpares_inicioPar(self):
        impares = Impares()
        resultado = impares.seisNumerosImpares(8)
        self.assertEqual(resultado, [9,11,13,15,17,19])
        
if __name__ == '__main__':
    unittest.main()

#  