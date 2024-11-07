"""Ejercicio 2 - Unidad 6 / Ary Toro"""
#Digrafo representación enlazada
import numpy as np
from cola_encadenada import ColaEncadenada,Nodo
class DigrafoEnlazado:
    __grafo:np.ndarray
    __numNodos:int
    def __init__(self,cn):
        self.__grafo= np.empty(cn,dtype=object)
        self.__numNodos= cn


    def adyacente(self,nodo1,nodo2):
        aux= self.__grafo[nodo1-1] #Aqui tengo la cabeza de la lista de los nodos adyacentes al nodo1
        band=False
        while aux is not None and band is False:
            if aux.getDato()==nodo2-1: #Si alguno de esos nodos, es igual nodo2...
                band=True #Bandera es True y se detiene la busqueda
            else:
                aux=aux.getSiguiente() #Sino, itera hasta que se haya llegado al final de la lista
        return band #Retorno la bandera

    def REA(self,xnodo):
        d= np.empty(self.__numNodos,dtype=object)
        cola= ColaEncadenada()
        for n in range(self.__numNodos):
            d[n]= float('inf')
        d[xnodo-1]= 0
        cola.insertar(xnodo)
        while cola.vacia() is False:
            v= cola.suprimir()
            print(v)
            for u in range(self.__numNodos):
                if self.adyacente(v,u+1):
                    if d[u]== float('inf'):
                        d[u]= d[v-1]+1
                        cola.insertar(u+1)
        print(d)
        return d

    def camino(self,origen,destino):
        camino="|"
        band=False
        d= np.empty(self.__numNodos,dtype=object)
        cola= ColaEncadenada()
        for n in range(self.__numNodos):
            d[n]= float('inf')
        d[origen-1]= 0
        cola.insertar(origen)
        while cola.vacia() is False and band is False:
            v= cola.suprimir()
            if v!= destino:
                camino+= f" -> {v}"
                for u in range(self.__numNodos):
                    if self.adyacente(v,u+1) is True:
                        if d[u]== float('inf'):
                            d[u]= d[v-1]+1
                            cola.insertar(u+1)
            else:
                band=True
        if d[destino-1]!=0 and d[destino-1]!=float('inf'):
            camino+=f" -> {destino}"
            print(camino)
        else:
            print("No existe un camino entre los nodos ingresados")

    def agregarRelacion(self,nodo1,nodo2):
        #Agrego el nodo2 en las relaciones del nodo1
        nuevoNodo=Nodo(nodo2)
        nuevoNodo.setSiguiente(self.__grafo[nodo1])
        self.__grafo[nodo1]=nuevoNodo


    def REP(self):
        tiempo = 0
        d = np.zeros(self.__numNodos, dtype=int)
        f = np.zeros(self.__numNodos, dtype=int)

        for v in range(1, self.__numNodos + 1):
            if d[v-1] == 0:
                self.REP_Visita(v, tiempo, d, f)
        print("d: ",d)
        print("f: ",f)

    def REP_Visita(self, s, tiempo, d, f):
        tiempo += 1
        d[s-1] = tiempo
        print(s)
        for u in range(1, self.__numNodos + 1):
            if self.adyacente(s, u) and d[u-1] == 0:
                tiempo = self.REP_Visita(u, tiempo, d, f)
        tiempo += 1
        f[s-1] = tiempo
        return tiempo

    def es_conexo(self):
        i=1
        visitados = np.full(self.__numNodos, False, dtype=bool)
        cola = ColaEncadenada()
        visitados[i] = True
        cola.insertar(i+1)

        while cola.vacia() is False:
            v = cola.suprimir()
            for u in range(self.__numNodos):
                if (self.adyacente(v, u+1) or self.adyacente(u+1,v)) and visitados[u]==False:
                    visitados[u] = True
                    cola.insertar(u+1)
        return all(visitados) #El all evalua si todos los elementos del arreglo son True. En caso de serlo devuelve un True, sino False.

    def es_aciclico(self):
        visitados= np.full(self.__numNodos,False,dtype=bool)
        for i in range(self.__numNodos):
            if visitados[i]==False:
                if self.detectar_ciclo(i,visitados,-1) is False:
                    return False
        return True

    def detectar_ciclo(self, s, visitados, ant):
        visitados[s] = True
        for i in range(self.__numNodos):
            if self.adyacente(s+1, i+1):
                if visitados[i]==False:
                    if self.detectar_ciclo(i,visitados,s) is False:
                        return False
                elif i!=ant:
                    return False
        return True

    def gradoSalida(self,nodo):
        cont=0
        for i in range(self.__numNodos):
            if self.adyacente(nodo,i+1):
                cont+=1
        return cont
    def gradoEntrada(self,nodo):
        cont=0
        for i in range(self.__numNodos):
            if self.adyacente(i+1,nodo):
                cont+=1
        return cont

    def nodoFuente(self,nodo):
        return self.gradoEntrada(nodo)==0 and self.gradoSalida(nodo)>0
    def nodoSumidero(self,nodo):
        return self.gradoEntrada(nodo)>0 and self.gradoSalida(nodo)==0

    def establecer_relaciones(self):
        self.agregarRelacion(0,1)
        self.agregarRelacion(0,2)
        self.agregarRelacion(0,3)
        self.agregarRelacion(2,3)
        self.agregarRelacion(3,2)
        self.agregarRelacion(3,4)
        self.agregarRelacion(4,1)
        self.agregarRelacion(4,3)

if __name__=="__main__":
    grafo= DigrafoEnlazado(5)
    grafo.establecer_relaciones()
    print(grafo.adyacente(1,4)) #El 4 es adyacente a 1
    print(grafo.adyacente(4,1)) #El 1 no es adyacente a 4
    grafo.REA(1)
    #grafo.camino(4,2)
    
    
    #grafo.REP()
    print("Es conexo?: ",grafo.es_conexo())
    #print("Es aciclico?: ",grafo.es_aciclico())
    nodo_evaluado=1
    print(f"Grado de Entrada de {nodo_evaluado}: {grafo.gradoEntrada(nodo_evaluado)}")
    print(f"Grado de Salida de {nodo_evaluado}: {grafo.gradoSalida(nodo_evaluado)}")
    print(f"{nodo_evaluado} es fuente?: {grafo.nodoFuente(nodo_evaluado)}")
    print(f"{nodo_evaluado} es pozo?: {grafo.nodoSumidero(nodo_evaluado)}")