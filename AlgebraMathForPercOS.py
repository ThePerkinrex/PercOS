import PercOSUtils as Utils


def printInit():
    version = "1.0.3"
    print(Utils.decor("Algebra Math for PercOS " + version, 1))





class PoliDiv:
    def __init__(self, resto, cociente):
        self.resto = resto
        self.cociente = cociente





class Monomio:
    
    #(coef)x^(grado)
    def __init__(self, coef, grado):
        self.coef = coef
        self.grado = grado
    def __mul__(self, other):
        return Monomio(self.coef * other.coef, self.grado + other.grado)
    
    def __truediv__(self, other):
        return Monomio(self.coef / other.coef, self.grado - other.grado)
    
    def __add__(self, other):
        if (self.grado == other.grado):
            return Monomio(self.coef + other.coef, self.grado)
        else:
            raise ValueError("No se pueden sumar monomios con diferente grado")
    
    def __lt__(self, other):
        r = False
        if self.grado < other.grado:
            r = True
        else:
            r = False
        return r
    
    def printMono(self):
        print(str(self.coef) + "x^" + str(self.grado))


class Polinomio:
    def __init__(self, monomios):
        self.monomios = monomios
        self.grado = 0
        for  monomio in monomios:
            self.grado += monomio.grado

    def __mul__(self, other):
        r = []
        self.sumar()
        for monomio in self.monomios:
            for oMonomio in other.monomios:
                r.append(monomio * oMonomio)
        return Polinomio(r)

    def __truediv__(self, other):
        inp = [self, other]
        coc = []
        while inp[0].grado > inp[1].grado:
            coc.append(Polinomio([inp[0].monomios[0] / inp[0].monomios[0]]))
            res = inp[1] * coc[0]
            inp[0] = inp[0] - res
            inp[0].calcGrado()
            if inp[0].grado > inp[1].grado:
                return PoliDiv(inp[0], Polinomio(coc))
                
                
                
    def __add__(self, other):
        r = Polinomio(self.monomios + other.monomios)
        r.sumar()
        return r
    
    def __sub__(self, other):
        for Omon in other.monomios:
            Omon.coef = -Omon.coef
        r = Polinomio(self.monomios + other.monomios)
        r.sumar()
        return r
    
    def orden(self):
        self.monomios.sort()
    
    def calcGrado(self):
        self.grado = 0
        for  monomio in self.monomios:
            if self.grado < monomio.grado:
                self.grado = monomio.grado

    def sumar(self):
        i = 0
        self.orden()
        while i<len(self.monomios)-1:
            if self.monomios[i].grado == self.monomios[i + 1].grado:
                self.monomios[i] += self.monomios[i + 1]
                del self.monomios[i + 1]
            i += 1
                
    def printPoli(self):
        self.sumar()
        for monomio in self.monomios:
            monomio.printMono()
