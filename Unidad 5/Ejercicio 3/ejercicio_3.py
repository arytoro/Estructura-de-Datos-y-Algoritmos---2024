"""Ejercicio 3 - Unidad 5 / Ary Toro"""
#Politica de manejo de Colisiones: Encadenamiento
#Funcion de transformación: Metodo Plegado
import numpy as np
from random import randint
from claseNodo_Encadenamiento import Nodo
class TablaHash:
    __tabla: np.ndarray
    __M:int
    def __init__(self,N,convertir_a_primo):
        self.__M= int(N/0.7) if convertir_a_primo is False else self.primo(int(N/0.7))
        self.__tabla= np.empty(self.__M,dtype=Nodo)


    def primo(self,x):
        i = 2
        while i < x and x % i != 0:
            i += 1
        if i == x:
            return x
        else:
            return self.primo(x + 1)

    def metodo_plegado(self,clave):
        num_pliegues= 3
        origen=0
        hashing=0
        clave_cadena= str(clave)
        for i in range(num_pliegues):
            destino=int(len(clave_cadena) * ((i+1)/num_pliegues)) #Calculo hasta que indice tomar
            hashing+= int(clave_cadena[origen : destino])
            origen= destino
        return hashing % self.__M

    def insertar(self,clave):
        posicion= self.metodo_plegado(clave)
        nuevoNodo=Nodo(clave)
        if self.__tabla[posicion] is None:
            self.__tabla[posicion]=nuevoNodo
        else:
            nuevoNodo.setSiguiente(self.__tabla[posicion])
            self.__tabla[posicion]= nuevoNodo

    def buscar(self,clave):
        posicion= self.metodo_plegado(clave)
        aux= self.__tabla[posicion]
        while aux is not None and aux.getDato() != clave:
            aux= aux.getSiguiente()
        if aux is None:
            print("ERROR! No existe la clave ingresada")
        return aux


    def generar_N_claves(self,N):
        for i in range(N):
            self.insertar(randint(20000000,45000000))



if __name__=="__main__":
    N=6
    tabla= TablaHash(N,True)
    tabla.insertar(28731)
    tabla.insertar(2231)
    tabla.insertar(685)
    tabla.insertar(971)
    tabla.insertar(6237134)
    tabla.insertar(124012)
    #tabla.recorrer()
    buscar_clave= 9124
    print(f"La clave {buscar_clave} se encuentra en la tabla, el objeto es: {tabla.buscar(buscar_clave)}" if tabla.buscar(buscar_clave) is not None else f"No se encuentra la clave {buscar_clave} en la tabla")

    #print("Longitudes de las listas")
    #tabla.indicar_longitud_listas()