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
    def setSAI(self,sai):
        self.__subArbol_izq= sai
    def setSAD(self,sad):
        self.__subArbol_der= sad
