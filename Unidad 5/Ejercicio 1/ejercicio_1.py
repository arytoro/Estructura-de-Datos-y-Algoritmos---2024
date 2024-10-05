"""Ejercicio 1 - Unidad 5 / Ary Toro"""
#Política de Manejo de Colisiones: Direccionamiento Abierto
#Función de Transformación de Claves: Método de la división
#Procesar claves sinónimas a través de la secuencia de prueba lineal
import numpy as np
from random import randint
class tablaHash:
    __tabla: np.ndarray
    __M:int
    __contador_colisiones:np.ndarray #Agregado por sugerencia del profesor para hacer un seguimiento de las colisiones; no pertenece al objeto de dato

    def __init__(self,N,convertir_a_primo):        
        self.__M= int(N / 0.7) if convertir_a_primo is False else self.primo(int(N / 0.7))
        self.__tabla= np.empty(self.__M,dtype=object)
        self.__contador_colisiones= np.zeros(self.__M,dtype=int)


    def metodo_divisiones_sucesivas(self,clave):
        return clave % self.__M

    def insertar(self,clave):
        posicion= self.metodo_divisiones_sucesivas(clave)
        while self.__tabla[posicion] is not None:
            self.__contador_colisiones[posicion]+=1
            posicion = (posicion+1) % self.__M
        self.__tabla[posicion]= clave

    def buscar(self,clave):
        posicion=None
        i= self.metodo_divisiones_sucesivas(clave)
        band=False
        cont=0
        while cont < self.__M and band is False:
            if self.__tabla[i]==clave:
                posicion=i
                band= True
            else:
                i= (i+1) % self.__M
            cont+=1
        return posicion


    def recorrer(self): #No pertenece al objeto de datos, se agregó para seguimiento
        for i in range(self.__M):
            print(f"Pos= {i} -> Clave: {self.__tabla[i]}")

    def mostrarCantidadColisiones(self):
        i=0
        while i< self.__M:
            if self.__contador_colisiones[i]!=0:
                print(f"En la direccion {i} hubieron [{self.__contador_colisiones[i]}] colisiones")
            i+=1
            
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
    N=15 #Segun el enunciado debería ser 1000

    tabla_hash= tablaHash(N,False)
    tabla_hash.generar_N_claves(N)
    print("Si M no es primo")
    tabla_hash.mostrarCantidadColisiones()


    tabla_hash_primo= tablaHash(N,True)
    tabla_hash_primo.generar_N_claves(N)
    print("Si M es primo:")
    tabla_hash_primo.mostrarCantidadColisiones()
