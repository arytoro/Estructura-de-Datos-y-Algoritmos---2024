"""Ejercicio 1 / Unidad 3 - Ary Toro"""
import numpy as np
class PilaSecuencial:
    __tope:int
    __arregloDatos:np.ndarray

    def __init__(self):
        self.__tope=-1
        self.__arregloDatos=np.empty(8,dtype=object)

    def vacia(self):
        return self.__tope==-1

    def llena(self):
        return self.__tope==len(self.__arregloDatos)-1

    def insertar(self,item):
        if self.llena() is False:
            self.__tope+=1
            self.__arregloDatos[self.__tope]=item
        else:
            print(f"No es posible insertar el elemento {item}. Pila llena")

    def suprimir(self):
        elemento=None
        if self.vacia() is False:
            elemento=self.__arregloDatos[self.__tope]
            self.__tope-=1
        else:
            print("No es posible eliminar elementos. La pila esta vacia")
        return elemento

    def recorrer(self):
        i = self.__tope
        if not self.vacia():
            while i >= 0:
                print(self.__arregloDatos[i])
                i -= 1

if __name__=="__main__":
    p=PilaSecuencial()
    p.insertar(8)
    p.insertar(-2)
    p.insertar(9)

    p.recorrer()
    print("Se elimina el ",p.suprimir())
    p.recorrer()
    print("Se elimina el ",p.suprimir())
    p.recorrer()