
"""Listas Ejercicio 1 / Unidad 3 - Ary Toro"""
import numpy as np
class ListaSecuencial:
    __ult:int
    __dimension:int
    __arregloDatos:np.ndarray
    def __init__(self,dimension=5):
        self.__ult=0
        self.__dimension=dimension
        self.__arregloDatos=np.empty(dimension,dtype=int)

    def vacia(self):
        return self.__ult==0

    def siguiente(self,pos):
        p1=None
        if pos>=0 and pos<self.__ult-1:
            p1=pos+1
        else:
            print("El indice ingresado no es valido")
        return p1

    def anterior(self,pos):
        p1=None
        if pos>0 and pos<=self.__ult-1:
            p1=pos-1
        else:
            print("El indice ingresado no es valido")
        return p1

    def primer_elemento(self):
        return self.__arregloDatos[0]
    def ultimo_elemento(self):
        return self.__arregloDatos[self.__ult-1]

    def insertar(self,item,pos):
        if self.__ult < self.__dimension:
            if pos>=0 and pos<=self.__ult:
                i= self.__ult
                while i>pos:
                    self.__arregloDatos[i]=self.__arregloDatos[i-1]
                    i-=1
                self.__arregloDatos[i]=item
                self.__ult+=1
            else:
                print("El indice ingresado no es valido")
        else:
            print(f"No es posible insertar el elemento {item}. Lista llena")

    def recorrer(self):
        for i in range(self.__ult):
            print(self.__arregloDatos[i])

    def buscar(self,item):
        i=0
        posicion=None
        band=False
        while i<=self.__ult and band is False:
            if self.__arregloDatos[i]==item:
                posicion=i
                band=True
            else:
                i+=1
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
            for i in range(pos,self.__ult-1):
                self.__arregloDatos[i]= self.__arregloDatos[i+1]
            self.__ult-=1
        else:
            print("El indice ingresado no es valido")
        return elemento

if __name__=="__main__":
    l=ListaSecuencial()
    l.insertar(-9,0)
    l.insertar(-3,1)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-2,1)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-7,3)
    l.recorrer()
    print("Lista llena?: ",l.llena())
    print("Desplazamiento")
    l.insertar(-15,0)
    l.recorrer()
    l.insertar(-99,2)
    print("Lista llena?: ",l.llena())
    print("El primero es: ",l.primer_elemento())
    print("El ultimo es: ",l.ultimo_elemento())
    print("El elemento -9 se encuentra en el indice: ",l.buscar(-9))
    print("El elemento siguiente a la posicion 2 es: ",l.siguiente(2))
    print("El elemento anterior a la posicion 2 es: ",l.anterior(2))

    print("Sumprimido en pos 2: ",l.suprimir(2))
    l.recorrer()
    print("Sumprimido en pos 0: ",l.suprimir(0))
    l.recorrer()
    print("Sumprimido en pos 2: ",l.suprimir(2))
    l.recorrer()
    print("insercion")
    l.insertar(-12,2)
    l.recorrer()
