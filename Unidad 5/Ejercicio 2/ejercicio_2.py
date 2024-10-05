"""Ejercicio 2 - Unidad 5 / Ary Toro"""
#Política de Manejo de Colisiones: Direccionamiento Abierto
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

    def metodo_extraccion(self,clave):
        inicio=2
        extraccion_pura= int(str(clave)[inicio:inicio+len(str(self.__M))]) #Tomara como direccion los primeros N digitos luego de los primeros 2 (N es la cantidad de digitos de M, si M=1000 -> N=4)
        return extraccion_pura % self.__M #Combino con modulo para asegurarme que se le asigne una posicion valida

    def metodo_plegado(self,clave):
        num_pliegues= 3
        j=0
        direccion=0
        for i in range(num_pliegues):
            hasta=int(len(str(clave)) * ((i+1)/num_pliegues)) #Calculo hasta que indice tomar
            print(int(str(clave)[j : hasta]))
            direccion+= int(str(clave)[j : hasta])
            j= hasta
        return direccion % self.__M

    def metodo_cuadrado_medio(self,clave):
        cuadrado= str(clave ** 2)
        desde= int(len(cuadrado)/2) - 1 #El -1 porque empezamos en 0
        direccion= int(cuadrado[desde:desde+2]) #El +2 para que incluya el de su derecha
        return direccion % self.__M

    def metodo_alfanumericos(self,clave):
        clave= str(clave)
        direccion=0
        for i in range(len(clave)):
            direccion+= ord(clave[i]) * (10**(i+1)) #ord devuelve el codigo ASCII del caracter
        return direccion  % self.__M

    def insertar(self,clave,metodo):
        if metodo==1:
            posicion= self.metodo_divisiones_sucesivas(clave)
        elif metodo==2:
            posicion= self.metodo_extraccion(clave)
        elif metodo==3:
            posicion= self.metodo_plegado(clave)
        elif metodo==4:
            posicion= self.metodo_cuadrado_medio(clave)
        else:
            posicion= self.metodo_alfanumericos(clave)

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
            
    def generar_N_claves(self,N,metodo):
        for i in range(N):
            self.insertar(randint(20000000,45000000),metodo)
            #self.recorrer()

    def primo(self,x):
        i = 2
        while i < x and x % i != 0:
            i += 1
        if i == x:
            return x
        else:
            return self.primo(x + 1)

def menu():
    try:
        op=int(input("""
                        Que funcion de transformación usarás:
                [1] Direccionamiento abierto
                [2] Extraccion
                [3] Plegado
                [4] Cuadrado Medio
                [5] Claves Alfanumericas
                -> """))
        assert op in (1,2,3,4,5)
    except AssertionError:
        op=None
    except ValueError:
        op=None
    return op

if __name__=="__main__":
    N=1000
    tabla_hash= tablaHash(N,True)

    test_hashing= 6729325
    print("Muestra de direcciones con distintas funciones de hashing ")
    print(f"{test_hashing} con direccionamiento abierto: ",tabla_hash.metodo_divisiones_sucesivas(test_hashing))
    print(f"{test_hashing} con extraccion: ",tabla_hash.metodo_extraccion(test_hashing))
    print(f"{test_hashing} con plegado: ",tabla_hash.metodo_plegado(test_hashing))
    print(f"{test_hashing} con cuadrado medio: ",tabla_hash.metodo_cuadrado_medio(test_hashing))
    test_hashing_alfanumerico= "ROMA"
    print(f"Clave alfanumerica {test_hashing_alfanumerico} tiene direccion: ",tabla_hash.metodo_alfanumericos(test_hashing_alfanumerico))

    opcion= menu()
    while opcion==None:
        print("Opcion Invalida! Intenta nuevamente")
        opcion=menu()
    tabla_hash.generar_N_claves(N,opcion)

