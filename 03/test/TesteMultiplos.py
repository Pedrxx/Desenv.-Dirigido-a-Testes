import unittest
import sys
sys.path.insert(0, '03\main')

from Multiplos import Multiplos

class TesteMultiplos(unittest.TestCase):
    
    def test_multiplos(self):
        m = Multiplos()
        self.assertEqual(m.saoMultiplos(6,24),"São Multiplos")
        self.assertEqual(m.saoMultiplos(3,9),"São Multiplos")

    def test_nao_multiplos(self):
        m = Multiplos()
        self.assertEqual(m.saoMultiplos(3,10),"Não são multiplos")
        self.assertEqual(m.saoMultiplos(4,15),"Não são multiplos")

if __name__ == '__main__':
    unittest.main()

# complexidade ciclomática do método saoMultiplos = 2.