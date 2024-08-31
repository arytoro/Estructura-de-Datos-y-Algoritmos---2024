
"""Listas Ejercicio 1 / Unidad 3 - Ary Toro"""
import numpy as np
class ListaSecuencial:
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
        if pos>=0 and pos<=self.__ult:
            if pos==0:
                print("El indice ingresado no cuenta con un anterior en la lista; es el primero")
            else:
                elemento=self.__arregloDatos[pos-1]
        else:
            print("El indice ingresado no es valido")
        return elemento

    def primer_elemento(self):
        return self.__arregloDatos[0]
    def ultimo_elemento(self):
        return self.__arregloDatos[self.__ult-1]
    def insertar(self,item,pos):
        if self.__ult < len(self.__arregloDatos):
            if pos>=0 and pos<=self.__ult:
                i= self.__ult
                while i>pos:
                    self.__arregloDatos[i]=self.anterior(i)
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
