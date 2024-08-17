"""Ejercicio 1 / Unidad 3 - Ary Toro"""
from claseNodo import Nodo
class PilaEncadenada:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def vacia(self):
        return self.__tope==0

    def insertar(self,item):
        nuevoNodo=Nodo(item)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo=nuevoNodo
        self.__actual=nuevoNodo
        self.__tope+=1
        print("Agregado exitosamente!\n")

    def suprimir(self):
        if self.vacia():
            print("Pila Vacia, no se pueden eliminar elementos")
        else:
            elemento= self.__comienzo.getDato()
            self.__comienzo= self.__comienzo.getSiguiente()
            self.__actual=self.__comienzo
            self.__tope -= 1
            return elemento

    def dimension(self):
        return self.__tope

    def listar(self):
        for undato in self:
            print(undato)
    
if __name__=="__main__":
    p=PilaEncadenada()
    p.insertar(5)
    p.insertar(-7)
    p.listar()
    print("Se elimina el ",p.suprimir())
    p.listar()
    print("Se elimina el ",p.suprimir())
    p.listar()
    print("Se elimina el ",p.suprimir())