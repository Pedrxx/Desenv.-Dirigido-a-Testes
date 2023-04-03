import unittest
import sys
sys.path.insert(0, '02\main')

from Triangulos import Triangulos

class TesteTriangulo(unittest.TestCase):
    def test_invalido(self):
        t = Triangulos()
        self.assertEqual(t.qualTriangulo(1, 2, 3), "Invalido")
        self.assertEqual(t.qualTriangulo(2, 3, 1), "Invalido")
        self.assertEqual(t.qualTriangulo(3, 1, 2), "Invalido")

    def test_valido_equilatero(self):
        t = Triangulos()
        self.assertEqual(t.qualTriangulo(2, 2, 2), "Valido-Equilatero")
        self.assertEqual(t.qualTriangulo(10, 10, 10), "Valido-Equilatero")

    def test_valido_escaleno(self):
        t = Triangulos()
        self.assertEqual(t.qualTriangulo(3, 4, 5), "Valido-Escaleno")
        self.assertEqual(t.qualTriangulo(5, 12, 13), "Valido-Escaleno")

    def test_valido_isoceles(self):
        t = Triangulos()
        self.assertEqual(t.qualTriangulo(3, 3, 4), "Valido-Isoceles")
        self.assertEqual(t.qualTriangulo(5, 7, 7), "Valido-Isoceles")

if __name__ == '__main__':
    unittest.main()

# A complexidade ciclomática é de 4, calculada a partir método qualTriangulodd