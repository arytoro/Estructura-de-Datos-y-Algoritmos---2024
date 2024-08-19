"""Ejercicio 5 / Unidad 3 - Ary Toro"""
import numpy as np
class ColaSecuencial:
    __ult:int
    __pri:int
    __cont:int
    __arregloDatos:np.ndarray

    def __init__(self):
        self.__pri=0
        self.__ult=0
        self.__cont=0
        self.__arregloDatos=np.empty(5,dtype=int)

    def vacia(self):
        return self.__cont==0

    def llena(self):
        return self.__cont==len(self.__arregloDatos)

    def insertar(self,item):
        if self.__cont<len(self.__arregloDatos):
            self.__arregloDatos[self.__ult]=item
            self.__ult=(self.__ult+1)%len(self.__arregloDatos)
            self.__cont+=1
        else:
            print(f"No es posible insertar el elemento {item}. Pila llena")


    def suprimir(self):
        elemento=None
        if self.vacia() is False:
            elemento=self.__arregloDatos[self.__pri]
            self.__pri=(self.__pri+1) % len(self.__arregloDatos)
            self.__cont-=1
        else:
            print("No es posible eliminar elementos. La pila esta vacia")
        return elemento

    def recorrer(self):
        i = self.__pri
        if not self.vacia():
            for j in range(self.__cont):
                print(self.__arregloDatos[i])
                i = (i + 1) % len(self.__arregloDatos)

if __name__=="__main__":
    
    p=ColaSecuencial()
    p.insertar(8)
    p.insertar(-2)
    p.insertar(9)
    p.recorrer()
    print("Se elimino el ",p.suprimir())
    p.recorrer()
    print("Se elimino el ",p.suprimir())
    p.recorrer()
    print("Se elimino el ",p.suprimir())
    """
    print("Se elimino el ",p.suprimir())
    p.listar()
    print("La dimension es ",p.dimension())"""