import numpy as np

class Nodo:
    __elemento: int
    __siguiente: object

    def setSiguiente(self, sig):
        self.__siguiente = sig
    
    def getDato(self):
        return self.__elemento
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__elemento = dato


class ListaCursores:
    __cab : int
    __arreglo : np.ndarray
    __maximo : int
    __cantidad : int
    __disponible : int


    def __init__(self, maximo = 4):
        self.__arreglo = np.empty(maximo, dtype = Nodo) #Creacion del arreglo que guardara los nodos
        self.__maximo = maximo #Tamaño del arreglo
        self.__cantidad = 0 #Cantidad de elementos que tiene el arreglo
        self.__cab = -1 #Será el indice del primer elemento de la secuencia
        self.__disponible = 0 #Primer celda disponible de la lista para realizar una insercion
        for i in range(self.__maximo): #Se inicializan todas las posiciones del arreglo con nodos, en un principio vacios
            nodo = Nodo()
            self.__arreglo[i] = nodo
        for  j in range(self.__maximo-1): #Se establece que el siguiente de cada nodo, estará en la posición i+1 del arreglo
            self.__arreglo[j].setSiguiente(i+1)
        self.__arreglo[self.__maximo-1].setSiguiente(-1) #Salvo el ultimo nodo cuyo siguiente sera -1, referenciando/simulando a un "None"

    
    def vacio(self):
        return (self.__cantidad == 0)
    
    def lleno(self):
        return (self.__cantidad == self.__maximo)

#Por posicion
    def insertar_posicion(self, p, elemento):
        if p>=1 and p<=self.__cantidad+1: #La posicion debe estar entre 1 y la cantidad actual +1 (el +1 por si se desea insertar al final)
            self.__arreglo[self.__disponible].setDato(elemento) #En la posicion disponible guardo el nuevo elemento

            if self.vacio():
                self.__arreglo[self.__disponible].setSiguiente(self.__cab) #El siguiente del nuevo elemento, sera la cabeza (osea -1/None) ya que es el unico elemento de la cabeza, tambien es el ultimo
                self.__cab = self.__disponible #Ahora el indice que es cabeza, es el indice del nuevo elemento (0)
                self.__disponible+=1 #Se actualiza la nueva posicion disponible y la cantidad
                self.__cantidad+=1
            else:
                if not self.lleno(): #Hay que insertarlo entre los nodos en la posicion ingresada
                    aux = self.__cab #Indice de la cabeza
                    ant = aux
                    band = False
                    i = 0
                    while aux != -1 and not band:   #Recordar que será -1 cuando sea el ultimo elemento de la secuencia. Ese -1 representa un None
                        if i == p-1:    #Nosotros trabajamos con la lista a partir del indice 1; pero el arreglo empieza en 0. Por eso p-1
                            band = True     #Se llega a la posicion ingresada p; i deja de incrementarse
                        else:   #Se incrementa i y se avanza en la secuencia del arreglo
                            i+=1
                            ant = aux   #Indice del nodo anterior que esta en la posicion que queremos insertar
                            aux = self.__arreglo[aux].getSiguiente() #Indice del nodo que ya estaba en la posicion a insertar

                    if i == 0:  # Se debe insertar en la cabeza
                        self.__arreglo[self.__disponible].setSiguiente(self.__cab)  #El siguiente del nuevo elemento sera la cabeza
                        self.__cab = self.__disponible #Convirtiendose en la nueva cabeza
                        self.__cantidad+=1
                        self.__disponible+=1
                    else:
                        self.__arreglo[self.__disponible].setSiguiente(aux) #El siguiente del nuevo elemento será el que ya existia en esa posicion
                        self.__arreglo[ant].setSiguiente(self.__disponible) #El nuevo sera el siguiente del que precedia al nodo que ya existia.
                        self.__cantidad+=1
                        self.__disponible+=1
                else:
                    print('ERROR: Lista llena!')
        else:
            print('ERROR: Posicion ingresada no valida!')

    def suprimir_posicion(self, p):
        if p >= 1 and p <= self.__cantidad:
            if not self.vacio():
                i = 0
                aux = self.__cab #Indice de la cabeza
                ant = -1 #None
                while aux != -1 and i < p-1: #Busco el indice del elemento que esta en la posicion ingresada
                    ant = aux #Indice del que precede al elemento de esa posicion
                    aux = self.__arreglo[aux].getSiguiente() #Indice del elemento de esa posicion
                    i += 1

                if ant == -1:   #Si el anterior es -1, es porque se quiere eliminar el primer elemento de la lista (p-1 = 0, no entra al while)
                    self.__cab = self.__arreglo[aux].getSiguiente() # El indice de la cabeza será el siguiente del elemento que esta en la posicion ingresada
                else: # Hay que eliminar un elemento que no es el primero
                    self.__arreglo[ant].setSiguiente(self.__arreglo[aux].getSiguiente()) #El siguiente del elemento eliminado, es ahora el siguiente del elemento que lo precedia

                self.__cantidad -= 1
                self.__disponible = aux #Queda disponible en el arreglo, la posicion del elemento que se borró
            else:
                print('ERROR: Lista vacía')
        else:
            print('ERROR: Posición no válida!')


#Por Contenido
    def insertar_contenido(self, elemento):
        if not self.lleno():
            self.__arreglo[self.__disponible].setDato(elemento)
            if self.vacio():
                self.__arreglo[self.__disponible].setSiguiente(self.__cab)
                self.__cab = self.__disponible
                self.__disponible+=1
                self.__cantidad+=1
            else:
                aux = self.__cab
                ant = aux
                encontro = False
                while not encontro and aux != -1: #Voy a iterar para encontrar la posicion que le corresponde
                    if elemento < self.__arreglo[aux].getDato():
                        encontro = True
                    else:
                        ant = aux #El indice del anterior a la posicion en que se insertara
                        aux = self.__arreglo[aux].getSiguiente() #Posicion que le correponde, se insertara en aux
                if aux == self.__cab: #Si la posicion es la cabeza, etc ,etc. La logica es la misma que el insertar por posicion a partir de aca,
                    self.__arreglo[self.__disponible].setSiguiente(self.__cab)
                    self.__cab = self.__disponible
                    self.__disponible+=1
                    self.__cantidad+=1
                else:
                    self.__arreglo[ant].setSiguiente(self.__disponible)
                    self.__arreglo[self.__disponible].setSiguiente(aux)
                    self.__disponible+=1
                    self.__cantidad+=1       
        else:
            print('ERROR: Lista llena!')
    
    def supimir_contenido(self, elemento):
        if not self.vacio():
            aux = self.__cab
            ant = -1
            encontrado = False

            while aux != -1 and not encontrado:
                if self.__arreglo[aux].getDato() == elemento:
                    encontrado = True
                else:
                    ant = aux
                    aux = self.__arreglo[aux].getSiguiente()

            if encontrado:
                if ant == -1:
                    self.__cab = self.__arreglo[aux].getSiguiente()
                else:
                    self.__arreglo[ant].setSiguiente(self.__arreglo[aux].getSiguiente())

                self.__cantidad -= 1
                self.__disponible = aux
            else:
                print('ERROR: Elemento no encontrado')
        else:
            print('ERROR: Lista vacía')
            
#Generales

    def recorrer(self):
        aux =self.__cab
        while aux != -1: #While aux!=None (osea recorrer todos los elementos de la lista)
            print(self.__arreglo[aux].getDato())
            aux = self.__arreglo[aux].getSiguiente()
    
    def buscar(self, elemento):
        p = None
        if not self.vacio():
            i = 0
            aux = self.__cab
            encontro = False
            while aux != -1 and not encontro:
                if elemento == self.__arreglo[aux].getDato():
                    encontro = True
                else:
                    aux = self.__arreglo[aux].getSiguiente()
                    i+=1
            if encontro:
                p = i+1
        else:
            print('ERROR: Lista vacia!')
        return p
    
    def recuperar(self, p):
        elem = None
        p-=1
        if p>=0 and p <= self.__cantidad-1:
            if not self.vacio():
                i = 0
                encontro = False
                aux = self.__cab
                while not encontro:
                    if i == p:
                        encontro = True
                    else:
                        i+=1
                        aux = self.__arreglo[aux].getSiguiente()
                elem = self.__arreglo[aux].getDato()
        return elem

    
    def primer_elemento(self):
        return self.__arreglo[self.__cab].getDato()
    
    def ultimo_elemento(self):
        aux = self.__cab
        ant = aux
        elemento = None
        while aux != -1:
            ant =aux
            aux = self.__arreglo[aux].getSiguiente()
        elemento = self.__arreglo[ant].getDato()
        return elemento

    
    def anterior(self, p):
        elem =None
        if p > 1 and p <= self.__cantidad:
            i = 0
            encontro = None
            aux = self.__cab
            ant = aux
            while aux != -1 and not encontro:
                if i == p-1:
                    
                    encontro = True
                else:
                    i+=1
                    ant = aux
                    aux = self.__arreglo[aux].getSiguiente()
            elem = self.__arreglo[ant].getDato()
            
        else:
            print('ERROR: Posicion no valida!')
        return elem
    
if __name__=="__main__":
    l=ListaCursores()
    l.insertar_posicion(1,8)
    l.insertar_posicion(2,-2)
    l.recorrer()
    print("Desplazamiento")
    l.insertar_posicion(1,5)
    l.insertar_posicion(4,82)
    l.recorrer()
    print("Suprimir posicion 1")
    l.suprimir_posicion(1)
    l.recorrer()
    print("Insertar en pos 3")
    l.insertar_posicion(3,17)
    l.recorrer()
    print("El elemento 8 esta en la pos ",l.buscar(8))
    print("En la posicion 4 esta el elemento:",l.recuperar(4))

    print("INSERTARE POR CONTENIDO EN UNA NUEVA LISTA")
    l2=ListaCursores()
    l2.insertar_contenido(11)
    l2.insertar_contenido(-2)
    l2.insertar_contenido(21)
    l2.recorrer()
    print("Suprimir por contenido el 11")
    l2.supimir_contenido(21)
    l2.recorrer()