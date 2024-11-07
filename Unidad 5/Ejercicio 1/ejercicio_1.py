"""Ejercicio 1 - Unidad 5 / Ary Toro"""
#Política de Manejo de Colisiones: Direccionamiento Abierto
#Función de Transformación de Claves: Método de la división
#Procesar claves sinónimas a través de la secuencia de prueba lineal
import numpy as np
from random import randint
class tablaHash:
    __tabla: np.ndarray
    __M:int    

    def __init__(self,N,convertir_a_primo):        
        self.__M= int(N / 0.7) if convertir_a_primo is False else self.primo(int(N / 0.7))
        self.__tabla= np.empty(self.__M,dtype=object)

    def metodo_divisiones(self,clave):
        return clave % self.__M

    def insertar(self,clave):
        posicion= self.metodo_divisiones(clave)
        contador=0
        while self.__tabla[posicion] != None and contador < self.__M:
            contador+=1
            posicion = (posicion+1) % self.__M
        if contador == self.__M:
            print("ERROR! La tabla esta llena")
        else:
            self.__tabla[posicion]= clave

    def buscar(self,clave):
        posicion= self.metodo_divisiones(clave)
        contador=0
        while self.__tabla[posicion]!=clave and contador < self.__M:
            contador+=1
            posicion= (posicion+1) % self.__M
        if contador == self.__M:
            print("ERROR! No existe la clave ",clave)
            return None
        else:
            return self.__tabla[posicion]

    def generar_N_claves(self,N):
        for i in range(N):
            self.insertar(randint(20000000,45000000))
            #self.recorrer()

    def primo(self,x):
        i = 2
        while i < x and x % i != 0:
            i += 1
        if i == x:
            return x
        else:
            return self.primo(x + 1)

if __name__=="__main__":
    N=6 #Segun el enunciado debería ser 1000
    #tabla_hash= tablaHash(N,False)
    #tabla_hash.generar_N_claves(N)
    #print("Si M no es primo")
    #tabla_hash.mostrarCantidadColisiones()

    tabla_hash_primo= tablaHash(N,True)
    #tabla_hash_primo.generar_N_claves(N)
    print("Si M es primo:")
    #tabla_hash_primo.mostrarCantidadColisiones()

    tabla_hash_primo.insertar(28731)
    tabla_hash_primo.insertar(2231)
    tabla_hash_primo.insertar(685)
    tabla_hash_primo.insertar(971)
    tabla_hash_primo.insertar(6237134)
    tabla_hash_primo.insertar(124012)
    tabla_hash_primo.insertar(821)
    tabla_hash_primo.insertar(3142)
    tabla_hash_primo.insertar(81214)
    tabla_hash_primo.insertar(23142)
    tabla_hash_primo.insertar(321525)
    tabla_hash_primo.insertar(71312)
    
    buscar_clave= 685
    print(f"La clave {buscar_clave} se encuentra en la tabla, el objeto es: {tabla_hash_primo.buscar(buscar_clave)}" if tabla_hash_primo.buscar(buscar_clave) is not None else f"No se encuentra la clave {buscar_clave} en la tabla")
