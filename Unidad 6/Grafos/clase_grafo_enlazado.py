"""Ejercicio 1 - Unidad 6 / Ary Toro"""
#Grafo representación enlazada
import numpy as np
from cola_encadenada import ColaEncadenada,Nodo
class GrafoEnlazado:
    __grafo:np.ndarray
    __numNodos:int
    def __init__(self,cn):
        self.__grafo= np.empty(cn,dtype=object)
        self.__numNodos= cn


    def adyacente(self,nodo1,nodo2):
        aux= self.__grafo[nodo1-1] #Aqui tengo la cabeza de la lista de los nodos adyacentes al nodo1
        band=False
        while aux is not None and aux.getDato() != nodo2-1:
            aux=aux.getSiguiente()
        if aux is not None:
            band= True
        return band

    def REA(self,xnodo):
        d= np.empty(self.__numNodos,dtype=object)
        cola= ColaEncadenada()
        for n in range(self.__numNodos):
            d[n]= float('inf')
        d[xnodo-1]= 0
        cola.insertar(xnodo)
        while cola.vacia() is False:
            v= cola.suprimir()
            #print(v)
            for u in range(self.__numNodos):
                if self.adyacente(v,u+1):
                    if d[u]== float('inf'):
                        d[u]= d[v-1]+1
                        cola.insertar(u+1)
        #print(d)
        return d

    def camino(self,origen,destino): #Si me lo pidieran en parcial haría este. Pero el que mejor funciona es el que esta comentado abajo de este.
        cola= ColaEncadenada()
        d= np.empty(self.__numNodos,dtype=object)
        for i in range(len(d)):
            d[i]= float('inf')
        d[origen-1]=0
        cola.insertar(origen)
        encontrado= False
        camino="° "

        while cola.vacia() is False and encontrado is False:
            v= cola.suprimir()
            camino+= f" -> {v}"
            if v!=destino:
                for u in range(self.__numNodos):
                    if self.adyacente(v,u+1) and d[u]==float('inf'):
                        d[u]= d[v-1]+1
                        cola.insertar(u+1)
            else:
                encontrado= True

        if encontrado is True:
            print(camino)
        else:
            print(f"No existe un camino desde {origen} hasta {destino}")
        """
        rea_origen= self.REA(origen)
        if rea_origen[destino-1]!=0 and rea_origen[destino-1]!= float('inf'): #Reviso si existe un camino desde origen a destino
            d= np.empty(self.__numNodos,dtype=object)
            cola= ColaEncadenada()
            cola.insertar(origen)
            for i in range(self.__numNodos):
                d[i]= float('inf')
            d[origen-1]=0
            encontrado=False #Encontrado será True cuando hallemos un nodo adyacente al destino
            camino="°"
            while cola.vacia() is False and encontrado is False:
                v= cola.suprimir() #Nodo analizado
                camino+= f" -> {v}" #Lo concateno al camino
                if self.adyacente(v,destino) is False: #Si el nodo v no es adyacente a destino..
                    minimo=float('inf')
                    elegido=None #Aquí estará el nodo adyacente a v con distancia mas corta hacia el destino
                    for u in range(self.__numNodos):
                        if self.adyacente(v,u+1):
                            if d[u]==float('inf'): #Reviso los adyacentes que aun no fueron visitados
                                d[u]=d[v-1]
                                distancia=self.REA(u+1)[destino-1] #Aquí tengo la distancia de un nodo adyacente a v hasta destino
                                if distancia < minimo: #Encuentro el nodo adyacente con menor distancia...
                                    minimo= distancia
                                    elegido=u+1
                    cola.insertar(elegido) #Y lo inserto en la cola
                else:
                    encontrado= True
                    camino+=f" -> {destino} -|"
        else:
            print(f"ERROR! No existe un camino desde {origen} hasta {destino}")
            camino=None
        return camino"""

    def agregarRelacion(self,nodo1,nodo2):
        #Agrego el nodo2 en las relaciones del nodo1
        nuevoNodo=Nodo(nodo2)
        nuevoNodo.setSiguiente(self.__grafo[nodo1])
        self.__grafo[nodo1]=nuevoNodo

        #Agrego el nodo 1 en las relaciones del nodo 2
        nuevoNodo=Nodo(nodo1)
        nuevoNodo.setSiguiente(self.__grafo[nodo2])
        self.__grafo[nodo2]=nuevoNodo

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
        i=0
        visitados = np.full(self.__numNodos, False, dtype=bool) #Un arreglo de Falses, cada posicion representa un nodo, cuando visite al nodo, su posicion correspondiente en este arreglo sera True
        cola = ColaEncadenada() #Aqui guardare los nodos a analizar
        visitados[i] = True #Empiezo visitando el primer nodo
        cola.insertar(i+1) # i+1 porque las posiciones del arrego empiezan en 0

        while cola.vacia() is False:
            v = cola.suprimir() 
            for u in range(self.__numNodos): 
                if self.adyacente(v, u+1) and visitados[u]==False: #Vamos a ver los nodos adyacentes a v  y que no fueron visitados anteriormente
                    visitados[u] = True #Los marcamos como visitados
                    cola.insertar(u+1) # Y lo agregamos a la cola para repetir el proceso con el/ellos
        return all(visitados) #El all evalua si todos los elementos del arreglo son True. En caso de serlo devuelve un True, sino False.


    def es_aciclico(self): #NO FUNCIONA CORRECTAMENTE
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

    def establecer_relaciones(self):
        self.agregarRelacion(0,1)
        self.agregarRelacion(0,2)
        self.agregarRelacion(0,3)
        self.agregarRelacion(1,4)
        self.agregarRelacion(2,3)
        self.agregarRelacion(3,4)

if __name__=="__main__":
    grafo= GrafoEnlazado(5)
    grafo.establecer_relaciones()
    #grafo.REA(1)
    grafo.camino(5,1)
    #print(grafo.camino(5,1))
    #grafo.REP()
    print("Es conexo: ",grafo.es_conexo())
    print("Es aciclico: ",grafo.es_aciclico())
