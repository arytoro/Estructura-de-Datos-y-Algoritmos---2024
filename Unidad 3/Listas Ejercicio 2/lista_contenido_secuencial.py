
"""Listas Ejercicio 2  / Unidad 3 - Ary Toro"""
import numpy as np
class ListaSecuencialContenido:
    __ult:int
    __arregloDatos:np.ndarray
    def __init__(self):
        self.__ult=0
        self.__arregloDatos=np.empty(5,dtype=int)

    def vacia(self):
        return self.__ult==0

    def llena(self):
        return self.__ult==len(self.__arregloDatos)

    def siguiente(self,pos):
        elemento=None
        if pos>=0 and pos<=self.__ult:
            if pos==self.__ult:
                print("El indice ingresado no cuenta con un siguiente en la lista; es el ultimo")
            else:
                elemento= self.__arregloDatos[pos+1]
        else:
            print("El indice ingresado no es valido")
        return elemento

    def anterior(self,pos):
        elemento=None
        if not self.vacia():
            if pos>=0 and pos<=self.__ult:
                if pos==0:
                    print("El indice ingresado no cuenta con un anterior en la lista; es el primero")
                else:
                    elemento=self.__arregloDatos[pos-1]
            else:
                print("El indice ingresado no es valido")
        else:
            print("Pila Vacia. No se pueden suprimir elementos")
        return elemento

    def primer_elemento(self):
        return self.__arregloDatos[0]
    def ultimo_elemento(self):
        return self.__arregloDatos[self.__ult-1]

    def localizar_posicion(self,item):
        i=0
        while self.__arregloDatos[i]<item:
            i+=1
        return i

    def insertar(self,item):
        pos= self.localizar_posicion(item)
        i= self.__ult
        while i>pos:
            self.__arregloDatos[i]=self.anterior(i)
            i-=1
        self.__arregloDatos[i]=item
        self.__ult+=1

    def recorrer(self):
        for i in range(self.__ult):
            print(self.__arregloDatos[i])

    def buscar(self,item):
        i=0
        posicion=None
        band=False
        while i<self.__ult and band is False:
            if self.__arregloDatos[i]==item:
                posicion=i
                band=True
            else:
                i+=1
        if band is False:
            print(f"El elemento {item} no se encuentra en la lista")
        return posicion

    def recuperar(self,pos):
        elemento= None
        if pos>=0 and pos<self.__ult:
            elemento= self.__arregloDatos[pos]
        else:
            print("En indice ingresado no es valido")
        return elemento

    def suprimir(self,pos):
        elemento=None
        if pos>=0 and pos<self.__ult:
            elemento=self.__arregloDatos[pos]
            for i in range(pos,self.__ult-1,1):
                self.__arregloDatos[i]= self.siguiente(i)
            self.__ult-=1
        else:
            print("El indice ingresado no es valido")
        return elemento

if __name__=="__main__":
    l=ListaSecuencialContenido()
    l.insertar(-5)
    l.insertar(-3)
    l.insertar(-6)
    l.insertar(-10)
    l.insertar(-1)
    l.recorrer()
    print("Del indice 0 se suprimio el elemento: ",l.suprimir(0))
    l.recorrer()
    print("Del indice 3 se suprimio el elemento: ",l.suprimir(3))
    l.recorrer()
    print("Del indice 1 se suprimio el elemento: ",l.suprimir(1))
    l.recorrer()
