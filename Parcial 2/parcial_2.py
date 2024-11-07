#----- Ejercicio 1 ------
# Item A
class Nodo:
    __dato:int
    __subArbol_izq:object
    __subArbol_der:object
    
    def __init__(self,dato):
        self.__dato=dato
        self.__subArbol_izq= None
        self.__subArbol_der= None

class ArbolBinarioBusqueda:
    __raiz:Nodo

    def __init__(self):
        self.__raiz= None

#Item B
    def buscar(self,subarbol,clave):
            if subarbol is None:
                print('Elmento no encontrado!')
            else:
                if clave == subarbol.getDato():
                    return subarbol
                elif clave > subarbol.getDato():
                    subarbol = self.buscar(subarbol.getDerecha(),clave)
                else:
                    subarbol = self.buscar(subarbol.getIzquierda(),clave)
            return subarbol
    
    def padre(self,padre,hijo):
        nodo_padre= self.buscar(self.__raiz,padre)
        bandera=False
        if nodo_padre is not None:
            izq= nodo_padre.getIzquierda()
            der= nodo_padre.getDerecha()
            bandera= (izq!=None and izq.getDato()==hijo) or (der!=None and der.getDato()==hijo)
        return bandera

#-----Ejercicio 2----------
#Item A
import numpy as np
class DigrafoSecuencial:
    __numNodos:int
    __grafo: np.ndarray
    def __init__(self,numNodos):
        self.__numNodos= numNodos
        self.__grafo= np.zeros([numNodos,numNodos],dtype=object)

#Item B
    def gradoSalida(self,nodo):
        cont=0
        for i in range(self.__numNodos):
            if self.__grafo[nodo-1][i]==1:
                cont+=1
        return cont

    def gradoEntrada(self,nodo):
        cont=0
        for i in range(self.__numNodos):
            if self.__grafo[i][nodo-1]==1:
                cont+=1
        return cont

    def mostrar_sumideros(self):
        for i in range(self.__numNodos):
            if self.gradoEntrada(i+1)>0 and self.gradoSalida(i+1)==0:
                print(i+1)

#-------Ejercicio 3-----------
# Item A
import numpy as np
class tablaHash:
    __tabla: np.ndarray

    def __init__(self,N):
        self.__tabla= np.empty(N//0.7,dtype=object)

#Item B (los comentarios al lado son para el tiem c)
    def insertar(self,clave):
        posicion= clave % len(self.__tabla)     #2
        contador=0                              #1
        while self.__tabla[posicion] != None and contador < len(self.__tabla): # 4N + 4
            contador+=1                          #2N
            posicion = (posicion+1) % len(self.__tabla) #3N
        if contador == len(self.__tabla): #1
            print("ERROR! La tabla esta llena") # 1 (menor que el T en else)
        else:
            self.__tabla[posicion]= clave   # 2 (tomamos el 2, no el 1 de arriba)
            
# Item C
# T= 9N +10 -> T e O(N); complejidad lineal