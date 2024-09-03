
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

    def siguiente(self,item):
        elemento=None
        if not self.vacia():
            pos=0
            while pos<self.__ult and item!= self.__arregloDatos[pos]:
                pos+=1

            if pos!=self.__ult:
                if pos==self.__ult-1:
                    print("El elemento ingresado no cuenta con un siguiente en la lista; es el ultimo")
                else:
                    elemento= self.__arregloDatos[pos+1]
            else:
                print("El elemento ingresado no se encuentra en la lista")
        else:
            print("Pila Vacia. No existe el elemento ingresado")
        return elemento

    def anterior(self,item):
        elemento=None
        if not self.vacia():
            pos=0
            while pos<self.__ult and item!= self.__arregloDatos[pos]:
                pos+=1

            if pos != self.__ult:
                if pos==0:
                    print("El elemento ingresado no cuenta con un anterior en la lista; es el primero")
                else:
                    elemento=self.__arregloDatos[pos-1]
            else:
                print("El elemento ingresado no se encuentra en la lista")
        else:
            print("Pila Vacia. No existe el elemento ingresado")
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
        if self.__ult < len(self.__arregloDatos):
            pos= self.localizar_posicion(item)
            i= self.__ult
            while i>pos:
                self.__arregloDatos[i]=self.__arregloDatos[i-1]
                i-=1
            self.__arregloDatos[i]=item
            self.__ult+=1
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
        #if band is False:
        #    print(f"El elemento {item} no se encuentra en la lista")
        return posicion

    def recuperar(self,pos):
        elemento= None
        if pos>=0 and pos<self.__ult:
            elemento= self.__arregloDatos[pos]
        else:
            print("En indice ingresado no es valido")
        return elemento

    def suprimir(self,item):
        pos=None
        if not self.vacia():
            pos=self.buscar(item)
            if pos is not None:
                for i in range(pos,self.__ult-1,1):
                    self.__arregloDatos[i]= self.__arregloDatos[i+1]
                self.__ult-=1
            else:
                print(f"El elemento {item} no se encuentra en la lista. Por ende, no se puede suprimir")
        else:
            print(f"No se puede suprimir el elemento {item}. La lista esta vacia")
        return pos

if __name__=="__main__":
    l=ListaSecuencialContenido()
    l.insertar(-5)
    l.insertar(-3)
    l.insertar(-6)
    l.insertar(-10)
    l.insertar(-1)
    l.insertar(-87)
    l.recorrer()
    print("Se suprime el elemento -10 del indice: ",l.suprimir(-10))
    l.recorrer()
    print("Se suprime el elemento -1 del indice: ",l.suprimir(-1))
    l.recorrer()
    print("Se suprime el elemento -99 del indice: ",l.suprimir(-99))
    l.recorrer()
    print("El anterior al elemento -5 es: ",l.anterior(-5))
    print("El siguiente al elemento -6 es: ",l.siguiente(-6))
