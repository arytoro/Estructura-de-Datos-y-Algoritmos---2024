#Politica de Manejo de colisiones: Buckets

import numpy as np

class Bucket:
    __cont:int
    __arre:np.ndarray
    def __init__(self,b):
        self.__arre=np.empty(b,dtype=object)
        self.__cont=0
    def bucket_insertar(self,x):
        self.__arre[self.__cont]=x
        self.__cont+=1
    def bucket_lleno(self):
        return self.__cont == len(self.__arre)-1
    def mostrar(self):
        for i in self.__arre:
            print(i)
    def bucket_buscar(self,x):
        i=0
        while i<self.__cont and self.__arre[i]!=x:
            i+=1
        if i<len(self.__arre):
            return self.__arre[i]
        else:
            return None

class TablaHash:
    __tabla:np.ndarray
    __M:int
    def __init__(self,N):
        self.__M= N//10 #Maximo 10 colisiones
        self.__tabla=np.empty(int(self.__M*1.25),dtype=object)
        for i in range(len(self.__tabla)):
            self.__tabla[i]=Bucket(10) #Maximo 10 colisiones

    def metodo_extraccion(self,clave):
        inicio=2
        hashing= int(str(clave)[inicio:inicio+len(str(self.__M))]) #Tomara como direccion los primeros N digitos luego de los primeros 2 (N es la cantidad de digitos de M, si M=1000 -> N=4)
        return hashing % self.__M #Combino con modulo para asegurarme que se le asigne una posicion valida

    def insertar(self,clave):
        posicion= self.metodo_extraccion(clave)
        if self.__tabla[posicion].bucket_lleno() is False:
            self.__tabla[posicion].bucket_insertar(clave)
        else:
            posicion=self.__M #A la zona de overflow
            while self.__tabla[posicion].lleno():
                posicion+=1
            self.__tabla[posicion].bucket_insertar(clave)

    def buscar (self,clave):
        posicion= self.metodo_extraccion(clave)
        elemento= self.__tabla[posicion].bucket_buscar(clave)
        if elemento is None:
            posicion= self.__M #A la zona de overflow
            while posicion < len(self.__tabla) and elemento is None:
                elemento=self.__tabla[posicion].bucket_buscar(clave)
                posicion+=1
            if posicion == len(self.__tabla):
                print("ERROR! La clave ingresada no existe")
        return elemento

if __name__=="__main__":
    tabla=TablaHash(11)#11->700
    tabla.insertar(28731)
    tabla.insertar(2231)
    tabla.insertar(685)
    tabla.insertar(971)
    tabla.insertar(6237134)
    tabla.insertar(124012)
    
    buscar_clave= 685
    print(f"La clave {buscar_clave} se encuentra en la tabla, el objeto es: {tabla.buscar(buscar_clave)}" if tabla.buscar(buscar_clave) is not None else f"No se encuentra la clave {buscar_clave} en la tabla")
    #for i in range(700):
    #    x=random.randint(40000000,50000000)
    #    xtabla_hash.insertar(x)
