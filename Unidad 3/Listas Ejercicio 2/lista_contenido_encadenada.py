"""Listas Ejercicio 2 / Unidad 3 - Ary Toro"""
from claseNodo import Nodo
class ListaEncadenada:
    __pri:Nodo
    __cont:int

    def __init__(self):
        self.__pri=None
        self.__cont=0

    def vacia(self):
        return self.__cont==0
    def primer_elemento(self):
        return self.__pri.getDato()
    def ultimo_elemento(self):
        aux=self.__pri
        retorna=None
        while aux is not None:
            retorna=aux.getDato()
            aux=aux.getSiguiente()
        return retorna

    def anterior(self,pos):
        elemento=None
        if pos>=0 and pos<self.__cont:
            if pos==0:
                print("El indice ingresado no cuenta con anterior; es el primero")
            else:
                i=0
                aux=self.__pri
                while i < pos-1:
                    aux=aux.getSiguiente()
                    i+=1
                elemento=aux.getDato()
        else:
            print("El indice ingresado no es valido")
        return elemento

    def siguiente(self,pos):
        elemento=None
        if pos>=0 and pos<self.__cont:
            if pos==self.__cont-1:
                print("El indice ingresado no cuenta con siguiente; es el ultimo")
            else:
                i=0
                aux=self.__pri
                while i <= pos:
                    aux=aux.getSiguiente()
                    i+=1
                elemento=aux.getDato()
        else:
            print("El indice ingresado no es valido")
        return elemento

    def localizar_posicion(self,item):
        i=0
        aux=self.__pri
        while aux is not None and aux.getDato()<item:
            i+=1
            aux=aux.getSiguiente()
        return i

    def insertar(self,item):
        nuevoNodo=Nodo(item)
        pos=self.localizar_posicion(item)
        if pos==0:
            nuevoNodo.setSiguiente(self.__pri)
            self.__pri=nuevoNodo
            self.__cont+=1
        else:
            aux=self.__pri
            indice=0
            while pos != indice:
                anterior=aux
                aux=aux.getSiguiente()
                indice+=1
            anterior.setSiguiente(nuevoNodo)
            nuevoNodo.setSiguiente(aux)
            self.__cont+=1

    def suprimir(self,pos):
        elemento=None
        if self.vacia():
            print("Pila Vacia, no se pueden eliminar elementos")
        else:
            if pos>=0 and pos<self.__cont:
                aux=self.__pri
                if pos==0:
                    self.__pri=aux.getSiguiente()
                else:
                    ant=aux
                    aux=aux.getSiguiente()
                    i=1
                    while i<pos:
                        ant = aux
                        aux=aux.getSiguiente()
                        i+=1
                    ant.setSiguiente(aux.getSiguiente())
                self.__cont-=1
                elemento=aux.getDato()
            else:
                print("El indice ingresado no es valido")
        return elemento

    def buscar(self,item):
        aux=self.__pri
        band=False
        pos=None
        i=0
        while aux is not None and band is False:
            if aux.getDato()==item:
                pos=i
                band=True
            else:
                aux=aux.getSiguiente()
                i+=1
        if band is False:
            print(f"El elemento {item} no se encuentra en la lista")
        return pos
    def recuperar(self,pos):
        aux=self.__pri
        i=0
        if pos>=0 and pos<self.__cont:
            while i!=pos:
                aux=aux.getSiguiente()
                i+=1
            elemento= aux.getDato()
        else:
            elemento=None
            print("El indice ingresado no es valido")
        return elemento
                
    def recorrer(self):
        aux=self.__pri
        while aux is not None:
            print(aux.getDato())
            aux=aux.getSiguiente()

if __name__=="__main__":
    l=ListaEncadenada()
    l.insertar(-5)
    l.insertar(-7)
    l.insertar(-2)
    l.insertar(6)
    l.recorrer()
    print("Se suprimio de la pos 3 el elemento: ",l.suprimir(3))
    l.recorrer()
    print("Se suprimio de la pos 3 el elemento: ",l.suprimir(3))
    l.recorrer()
    print("sig: ",l.siguiente(2))
    print("ant: ",l.anterior(0))
    print("pri:", l.primer_elemento())
    print("ult:", l.ultimo_elemento())
