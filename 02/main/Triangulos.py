class Triangulos:
    def qualTriangulo(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            return "Invalido"
        elif a == b == c:
            return "Valido-Equilatero"
        elif a != b and b != c and a != c:
            return "Valido-Escaleno"
        else:
            return "Valido-Isoceles"
