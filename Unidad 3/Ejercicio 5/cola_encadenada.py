"""Ejercicio 5 / Unidad 3 - Ary Toro"""
from claseNodo import Nodo
class ColaEncadenada:
    __pri:Nodo
    __ult:Nodo
    __cont:int

    def __init__(self):
        self.__pri=None
        self.__ult=None
        self.__cont=0

    def vacia(self):
        return self.__cont==0

    def insertar(self,item):
        nuevoNodo=Nodo(item)
        if self.__ult==None:
            self.__pri=nuevoNodo
        else:
            self.__ult.setSiguiente(nuevoNodo)
        self.__ult=nuevoNodo
        self.__cont+=1

    def suprimir(self):
        if self.vacia():
            print("Pila Vacia, no se pueden eliminar elementos")
        else:
            x=self.__pri.getDato()
            self.__pri=self.__pri.getSiguiente()
            self.__cont-=1
            if self.__pri==None:
                self.__ult=None
            return x

    def recorrer(self):
        aux=self.__pri
        while aux is not None:
            print(aux.getDato())
            aux=aux.getSiguiente()

if __name__=="__main__":
    p=ColaEncadenada()
    p.insertar(5)
    p.insertar(-7)
    p.insertar(2)
    p.recorrer()
    print("Se elimina el ",p.suprimir())
    p.recorrer()
    print("Se elimina el ",p.suprimir())
    p.recorrer()
    print("Se elimina el ",p.suprimir())