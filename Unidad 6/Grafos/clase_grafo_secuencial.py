"""Ejercicio 1 - Unidad 6 / Ary Toro"""
#Grafo representación secuencial
import numpy as np
from cola_encadenada import ColaEncadenada
class GrafoSecuencial:
    __numNodos:int
    __grafo: np.ndarray
    def __init__(self,numNodos):
        self.__numNodos= numNodos
        self.__grafo= np.zeros([numNodos,numNodos],dtype=int)

    def adyacente(self,xnodo,xady):
        return self.__grafo[xnodo-1][xady-1] == 1

    def REA(self,xnodo):
        d= np.empty(self.__numNodos,dtype=object)
        cola= ColaEncadenada()
        for n in range(self.__numNodos):
            d[n]= float('inf')
        d[xnodo-1]= 0
        cola.insertar(xnodo)
        while cola.vacia() is False:
            v= cola.suprimir()
        #    print(v)
            for u in range(self.__numNodos):
                if self.adyacente(v,u+1):
                    if d[u]== float('inf'):
                        d[u]= d[v-1]+1
                        cola.insertar(u+1)
        #print(d)
        return d

    def camino(self,origen,destino):
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
        return camino

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
        i= 1
        visitados = np.full(self.__numNodos, False, dtype=bool)
        cola = ColaEncadenada()
        visitados[i-1] = True
        cola.insertar(i)

        while cola.vacia() is False:
            v = cola.suprimir()
            for u in range(self.__numNodos):
                if self.adyacente(v, u+1) and visitados[u]==False:
                    visitados[u] = True
                    cola.insertar(u+1)
        return all(visitados) #El all evalua si todos los elementos del arreglo son True. En caso de serlo devuelve un True, sino False.

    def es_aciclico(self):
        aciclico= True
        i=0
        j=0
        k=0
        while i < self.__numNodos and aciclico is True:
            while j  < self.__numNodos and aciclico is True:
                if self.adyacente(i+1,j+1):
                    while k < self.__numNodos and aciclico is True:
                        if self.adyacente(j+1,k+1) and self.adyacente(k+1,i+1):
                            aciclico=False
                        k+=1
                j+=1
            i+=1
        return aciclico
        #visitados= np.full(self.__numNodos,False,dtype=bool)
        #for u in range(self.__numNodos):
        #    if visitados[u]==False: #Revisamos los nodos que aun no fueron visitados
        #        if self.detectar_ciclo(u,visitados,-1) is False: #Si 
        #            return False
        #return True

    def detectar_ciclo(self, s, visitados, ant):
        visitados[s] = True #Marcamos como visitado el nodo recibido
        for i in range(self.__numNodos):
            if self.adyacente(s+1, i+1): 
                if visitados[i]==False: #Si otro de los nodos no visitados es adyacente a "s"
                    if self.detectar_ciclo(i,visitados,s) is False:
                        return False
                elif i!=ant:
                    return False
        return True

    def establecer_relaciones(self):
        self.__grafo[0][1]=1
        self.__grafo[0][2]=1#1 0 para aciclico
        self.__grafo[0][3]=0#1 0 para aciclico
        self.__grafo[1][0]=1
        self.__grafo[1][4]=1#0 0 para NO conexo
        self.__grafo[2][0]=1#1 0 para acilico
        self.__grafo[2][3]=1
        self.__grafo[3][0]=0#1 0 para acilico
        self.__grafo[3][2]=1
        self.__grafo[3][4]=1#0 0 para NO conexo
        self.__grafo[4][1]=1#0 0 para NO conexo
        self.__grafo[4][3]=1#0 0 para NO conexo
        #self.__grafo[0][5]=1
        #self.__grafo[5][0]=1

if __name__=="__main__":
    grafo= GrafoSecuencial(5)
    grafo.establecer_relaciones()
    #grafo.REA(2)
    print(grafo.camino(5,3))
    #print("REP")
    #grafo.REP()
    #print("Es conexo?: ",grafo.es_conexo())

    print("Es aciclico?: ",grafo.es_aciclico())