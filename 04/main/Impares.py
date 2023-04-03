class Impares:
    @staticmethod
    def seisNumerosImpares(inicio):
        numerosImpares = []
        i = 0
        if inicio % 2 == 0:
            inicio += 1
        while i < 6:
            numerosImpares.append(inicio)
            inicio += 2
            i += 1
        return numerosImpares
