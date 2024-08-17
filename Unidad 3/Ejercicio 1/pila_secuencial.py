"""Ejercicio 1 / Unidad 3 - Ary Toro"""
import numpy as np
class PilaSecuencial:
    __dimension:int
    __tope:int
    __arregloDatos:np.ndarray

    def __init__(self):
        self.__dimension=8
        self.__tope=-1
        self.__arregloDatos=np.empty(self.__dimension,dtype=object)

    def vacia(self):
        return self.__tope==-1

    def llena(self):
        return self.__tope==self.__dimension-1

    def insertar(self,item):
        if self.llena() is False:
            self.__tope+=1
            self.__arregloDatos[self.__tope]=item
        else:
            print("No es posible insertar el elemento. Pila llena")

    def suprimir(self):
        elemento=None
        if self.vacia() is False:
            elemento=self.__arregloDatos[self.__tope]
            self.__arregloDatos[self.__tope]= None
            self.__tope-=1
        else:
            print("No es posible eliminar elementos. La pila esta vacia")
        return elemento

    def dimension(self):
        return self.__tope+1

    def listar(self):
        for undato in self.__arregloDatos:
            print(undato)

if __name__=="__main__":
    p=PilaSecuencial()
    p.insertar(8)
    p.insertar(-2)
    p.insertar(9)
    print("La dimension es ",p.dimension())

    p.listar()
    print("Se elimina el ",p.suprimir())
    p.listar()
    print("Se elimina el ",p.suprimir())
    p.listar()