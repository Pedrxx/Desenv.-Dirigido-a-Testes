import unittest
import sys
sys.path.insert(0, '01\main')

from NumerosPrimos import NumerosPrimos

class TesteNumerosPrimos(unittest.TestCase):
    
    def test_numeros_primos(self):
        self.assertTrue(NumerosPrimos.eh_primo(2))
        self.assertTrue(NumerosPrimos.eh_primo(3))
        self.assertTrue(NumerosPrimos.eh_primo(5))
        self.assertTrue(NumerosPrimos.eh_primo(7))
        self.assertTrue(NumerosPrimos.eh_primo(11))
        self.assertTrue(NumerosPrimos.eh_primo(13))
        self.assertFalse(NumerosPrimos.eh_primo(1))
        self.assertFalse(NumerosPrimos.eh_primo(4))
        self.assertFalse(NumerosPrimos.eh_primo(6))
        self.assertFalse(NumerosPrimos.eh_primo(8))
        self.assertFalse(NumerosPrimos.eh_primo(9))
        self.assertFalse(NumerosPrimos.eh_primo(10))
        self.assertFalse(NumerosPrimos.eh_primo(12))

if __name__ == '__main__':
    unittest.main()

# complexidade ciclomática do método ehPrimo = 13.