"""Listas Ejercicio 1 / Unidad 3 - Ary Toro"""
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

    def insertar(self,item,pos):
        nuevoNodo=Nodo(item)
        if pos>=0 and pos<=self.__cont:
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
        else:
            print("El indice ingresado no es valido")

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
    l.insertar(-5,0)
    l.insertar(-7,1)
    l.insertar(-2,2)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-9,1)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-18,4)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-84,0)
    l.recorrer()
    print("El primer elemento es: ",l.primer_elemento())
    print("El ultimo elemento es: ",l.ultimo_elemento())
    print("Se elimina el ",l.suprimir(2))
    l.recorrer()
    print("Se elimina el ",l.suprimir(0))
    l.recorrer()
    print("El primer elemento es: ",l.primer_elemento())
    print("Se elimina el ",l.suprimir(1))
    l.recorrer()
    print("El elemento -5 esta en la posicion: ",l.buscar(-5))
    print("El elemento -18 esta en la posicion: ",l.buscar(-18))
    print("El elemento -2 esta en la posicion: ",l.buscar(-2))
    print("El elemento -50 esta en la posicion: ",l.buscar(-50))
    print("En la posicion 1 hay un ", l.recuperar(1))
    print("El elemento siguiente a la posicion 1 es: ",l.siguiente(1))
    print("El elemento anterior a la posicion 1 es: ",l.anterior(1))
    print("El elemento anterior a la posicion 2 es: ",l.anterior(2))
    print("El elemento anterior a la posicion 2 es: ",l.siguiente(2)) if l.siguiente(2) is not None else print("")
