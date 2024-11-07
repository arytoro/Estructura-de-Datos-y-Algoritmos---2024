class Nodo:
    __dato:int
    __subArbol_izq:object
    __subArbol_der:object
    
    def __init__(self,dato):
        self.__dato=dato
        self.__subArbol_izq= None
        self.__subArbol_der= None

    def getDato(self):
        return self.__dato
    def getIzquierda(self):
        return self.__subArbol_izq
    def getDerecha(self):
        return self.__subArbol_der
    def setDato(self,dato):
        self.__dato= dato
    def setIzquierda(self,izq):
        self.__subArbol_izq= izq
    def setDerecha(self,der):
        self.__subArbol_der= der
    def getGrado(self):
        grado=0
        if (self.getDerecha() is not None and self.getIzquierda() is None) or (self.getDerecha() is None and self.getIzquierda() is not None):
            grado=1
        elif self.getDerecha() is not None and self.getIzquierda() is not None:
            grado=2
        return grado