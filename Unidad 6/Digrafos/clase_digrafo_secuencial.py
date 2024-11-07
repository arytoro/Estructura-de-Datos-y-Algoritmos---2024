"""Ejercicio 2 - Unidad 6 / Ary Toro"""
#Digrafo representación secuencial
import numpy as np
from cola_encadenada import ColaEncadenada
class DigrafoSecuencial:
    __numNodos:int
    __grafo: np.ndarray
    def __init__(self,numNodos):
        self.__numNodos= numNodos
        self.__grafo= np.zeros([numNodos,numNodos],dtype=object)

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
            if self.adyacente(s+1, i+1) or self.adyacente(i+1,s+1):
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
        self.__grafo[0][1]=1
        self.__grafo[0][2]=1
        self.__grafo[0][3]=1
        self.__grafo[2][3]=1
        self.__grafo[3][2]=1
        self.__grafo[3][4]=1
        self.__grafo[4][3]=1
        self.__grafo[4][1]=1


if __name__=="__main__":
    grafo= DigrafoSecuencial(5)
    grafo.establecer_relaciones()
    #print(grafo.adyacente(1,4)) #El 4 es adyacente a 1
    #print(grafo.adyacente(4,1)) #El 1 no es adyacente a 4
    #grafo.REA(1)
    print(grafo.camino(1,4))
    
    
    #grafo.REP()

    print("Es conexo?: ",grafo.es_conexo())
    print("Es aciclico?: ",grafo.es_aciclico())
    nodo_evaluado=1
    print(f"Grado de Entrada de {nodo_evaluado}: {grafo.gradoEntrada(nodo_evaluado)}")
    print(f"Grado de Salida de {nodo_evaluado}: {grafo.gradoSalida(nodo_evaluado)}")
    print(f"{nodo_evaluado} es fuente?: {grafo.nodoFuente(nodo_evaluado)}")
    print(f"{nodo_evaluado} es pozo?: {grafo.nodoSumidero(nodo_evaluado)}")