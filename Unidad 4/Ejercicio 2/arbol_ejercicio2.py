"""Ejercicio 2 - Unidad 4 / Ary Toro"""
from claseNodo import Nodo

class ArbolBinarioBusqueda:
    __raiz:Nodo

    def __init__(self):
        self.__raiz= None

    def getRaiz(self):
        return self.__raiz

    def insertar(self,subarbol:Nodo,clave):
        if self.__raiz is None: #Si el arbol esta vacio. El nuevo nodo será la raiz
            nuevoNodo= Nodo(clave)
            self.__raiz= nuevoNodo
        else:   #Si no.. hay que empezar a comparar claves para hallar su ubicacion
            if clave > subarbol.getDato(): #Si la clave del nuevo nodo es mayor que la del subarbol pasado por parametro (en la primera iteracion es la raiz)..
                if subarbol.getDerecha() is None:  #Verifico si el subarbol tiene disponible la rama derecha
                    nuevoNodo= Nodo(clave)
                    subarbol.setSAD(nuevoNodo)  #Si es así lo asigno
                else: #Sino, deberá de empezar la recursión pasando esta vez como subarbol el nodo que se encontraba en la derecha
                    self.insertar(subarbol.getDerecha(),clave)
            elif clave < subarbol.getDato(): #Aquí la logica es la misma, solo que aplicada a la izquierda
                if subarbol.getIzquierda() is None:
                    nuevoNodo= Nodo(clave)
                    subarbol.setSAI(nuevoNodo)
                else:
                    self.insertar(subarbol.getIzquierda(),clave)
            else:
                print("ERROR. La clave ingresada ya existe en el arbol")

    def buscar(self,subarbol,clave):
        if subarbol is None:
            print('Elmento no encontrado!')
        else:
            if clave == subarbol.getDato(): #Si la clave buscada, es igual a la del subarbol recibido por parametro..
                return subarbol  #Devuelve dicho nodo
            elif clave > subarbol.getDato():  #Si la clave es mayor a la del subarbol..
                subarbol = self.buscar(subarbol.getDerecha(),clave) #Iniciamos recursion, pasando como subarbol el nodo derecho
            else: #Si la clave es menor a la del subarbol..
                subarbol = self.buscar(subarbol.getIzquierda(),clave) #Llamada recursiva pasando como subarbol el nodo de la izquierda
        return subarbol

    def gradoNodo(self,clave):
        nodo =  self.buscar(self.__raiz,clave) #Busco el nodo con la clave ingresada
        grado=None
        if nodo is not None: #Si existe... Voy a revisar cuantos hijos tiene(ese es el grado):
            if nodo.getIzquierda() is not None and nodo.getDerecha() is not None: #Si tiene en la izquierda y en la derecha, el grado es 2
                grado = 2
            elif (nodo.getIzquierda() is not None and nodo.getDerecha() is None) or (nodo.getIzquierda() is None and nodo.getDerecha() is not None): #Si solo tiene 1 en la izquierda o derecha, el grado es 1
                grado = 1
            else: #Si tiene None tanto en la izquierda como en la derecha... no tiene hijos, grado 0
                grado = 0
        return  grado

    def hoja(self,clave):
        nodo= self.buscar(self.__raiz,clave)
        if nodo is not None:
            esHoja= nodo.getIzquierda() is None and nodo.getDerecha() is None
        else:
            esHoja= None
        return esHoja

    def InOrder(self,subarbol):
        if subarbol is not None:
            self.InOrder(subarbol.getIzquierda())
            print(subarbol.getDato())
            self.InOrder(subarbol.getDerecha())

    def nivelNodo(self,clave):
        nodo= self.buscar(self.__raiz,clave)
        nivel= None
        if nodo is not None:
            nivel=1
            subarbol= self.__raiz
            while subarbol.getDato() != clave:
                nivel+=1
                if clave > subarbol.getDato():
                    subarbol= subarbol.getDerecha()
                else:
                    subarbol= subarbol.getIzquierda()
        return nivel

    def getInfimo(self,subarbol):
        subarbol= subarbol.getIzquierda()
        while self.gradoNodo(subarbol.getDato()) != 0:
            subarbol= subarbol.getDerecha()
        return subarbol

    def getPadre(self,clave):
        nodo= self.__raiz
        nivel= self.nivelNodo(clave)
        nivel_actual= 1
        if clave != nodo.getDato():
            while nivel_actual != nivel-1:
                if clave > nodo.getDato():
                    nodo= nodo.getDerecha()
                else:
                    nodo= nodo.getIzquierda()
                nivel_actual+=1
        else:
            print("Ingresaste la raiz. No tiene padre")
        return nodo

    def suprimir(self,clave): #Es mas facil hacer el seguimiento viendo la imagen de la carpeta y ejecutandolo
        subarbol= self.buscar(self.__raiz,clave)
        padre= self.getPadre(clave)

        if subarbol is not None:
            grado= self.gradoNodo(clave)
            if grado == 0: #Si el grado es 0, es un nodo hoja. Ahora el padre va a apuntar a None en su rama derecha/izquierda en la que estaba el hijo suprimido
                if clave > padre.getDato():
                    padre.setSAD(None)
                else:
                    padre.setSAI(None)
            if grado == 1: #Si el grado es 1, el nodo tenia un hijo. Ahora el padre deberá apuntar a ese hijo
                if subarbol.getDerecha() is not None: #Busco el hijo (esta en la derecha O izquierda, ya que solo tiene 1)
                    hijo= subarbol.getDerecha()
                else:
                    hijo= subarbol.getIzquierda()

                subarbol.setDato(hijo.getDato()) #Ahora el nodo a suprimir será una copia de su hijo
                subarbol.setSAD(hijo.getDerecha())
                subarbol.setSAI(hijo.getIzquierda())

                #if subarbol.getDerecha().getDato() == subarbol.getDato():
                #    subarbol.setSAD(None)
                #else:
                #    subarbol.setSAD(None)
            if grado== 2: #Si el grado es 2, hay que buscar el infimo o el supremo para reemplazarlo
                infimo=self.getInfimo(subarbol)
                padre_infimo= self.getPadre(infimo.getDato())
                subarbol.setDato(infimo.getDato())

                if infimo.getDato() > padre_infimo.getDato():
                    padre_infimo.setSAD(None)
                else:
                    padre_infimo.setSAI(None)

    def hijo(self,padre,hijo):
        subarbol_padre= self.buscar(self.__raiz,padre)
        subarbol_hijo= self.buscar(self.__raiz,hijo)
        es_hijo= False
        if subarbol_hijo is not None and subarbol_padre is not None:
            es_hijo= subarbol_padre.getIzquierda()==subarbol_hijo or subarbol_padre.getDerecha()==subarbol_hijo
        return es_hijo

    def padre(self,padre,hijo):
        subarbol_padre= self.buscar(self.__raiz,padre)
        subarbol_hijo= self.buscar(self.__raiz,hijo)
        es_padre= False
        if subarbol_padre is not None and subarbol_hijo is not None:
            nodo= self.__raiz
            nivel= self.nivelNodo(hijo)
            nivel_actual= 1
            if hijo != nodo.getDato():
                while nivel_actual != nivel-1:
                    if hijo > nodo.getDato():
                        nodo= nodo.getDerecha()
                    else:
                        nodo= nodo.getIzquierda()
                    nivel_actual+=1
                es_padre = nodo==subarbol_padre
            else:
                print("Ingresaste la raiz. No tiene padre")
        return es_padre
    
    def altura(self,subarbol,maximo=1):
        if subarbol is not None:
            nivel = self.nivelNodo(subarbol.getDato())
            if nivel > maximo:
                maximo = nivel
            maximo = self.altura(subarbol.getIzquierda(), maximo) #Voy a recorrer todos los de la izqueirda
            maximo = self.altura(subarbol.getDerecha(), maximo) #Luego todos los de la derecha
        return maximo

    def PreOrden(self,subarbol):
        if subarbol is not None:
            print(subarbol.getDato())
            self.InOrder(subarbol.getIzquierda())
            self.InOrder(subarbol.getDerecha())

    def PostOrden(self,subarbol):
        if subarbol is not None:
            self.InOrder(subarbol.getIzquierda())
            self.InOrder(subarbol.getDerecha())
            print(subarbol.getDato())

    def camino(self,origen,destino):
        subarbol_origen= self.buscar(self.__raiz,origen)
        camino="° "
        if subarbol_origen is not None: #Reviso que el nodo origen exista
            subarbol_destino= self.buscar(subarbol_origen,destino) #Reviso que el nodo destino exista en los descendientes del arbol origen
            subarbol= subarbol_origen
            if subarbol_destino is not None: #Empezare a concatenar el contenido de los nodos como un camino en un string
                while subarbol.getDato() != destino:
                    if destino > subarbol.getDato():
                        camino+= str(subarbol.getDato())+ " -> "
                        subarbol= subarbol.getDerecha()
                    else:
                        camino+= str(subarbol.getDato())+ " -> "
                        subarbol= subarbol.getIzquierda()
                camino+= str(subarbol.getDato())+ " -|"
            else:
                print(f"ERROR. El nodo origen {subarbol.getDato()} no es antecesor de {destino}")
        return camino
    """A PARTIR DE AQUÍ IMPLEMENTARÉ LAS FUNCIONES DEL QUE PIDE EL ENUNCIADO 2"""
    def mostrar_Padre_Hermano(self,clave):
        nodo= self.buscar(self.__raiz,clave)
        if nodo is not None:
            if nodo != self.__raiz:
                padre= self.getPadre(clave)
                print(f"El padre del {clave} es el nodo: {padre.getDato()}")
                if self.gradoNodo(padre.getDato())==2:
                    if padre.getDerecha() != nodo:
                        print("Su hermano es el nodo: ",padre.getDerecha().getDato())
                    else:
                        print("Su hermano es el nodo: ",padre.getIzquierda().getDato())
                else:
                    print("No tiene hermanos")
            else:
                print("Ingresaste el nodo raiz. No tiene padre ni hermanos")
                
    def getCantidadNodos(self,subarbol,contador=0):
        if subarbol is not None:
            contador+=1
            contador = self.getCantidadNodos(subarbol.getIzquierda(), contador)
            contador = self.getCantidadNodos(subarbol.getDerecha(), contador)
        return contador

    def mostrarSucesores(self,clave):
        subarbol= self.buscar(self.__raiz,clave)
        if subarbol is not None:
            print("Por su derecha: °",end="")
            self.sucesores_por_derecha(subarbol.getDerecha())
            print("|")
            print("Por su izquierda: °",end="")
            self.sucesores_por_izquierda(subarbol.getIzquierda())
            print("|")

    def sucesores_por_derecha(self,subarbol):
        if subarbol is not None:
            print(" ",subarbol.getDato()," -",end="")
            self.sucesores_por_derecha(subarbol.getIzquierda())
            self.sucesores_por_derecha(subarbol.getDerecha())

    def sucesores_por_izquierda(self,subarbol):
        if subarbol is not None:
            print(" ",subarbol.getDato()," -",end="")
            self.sucesores_por_izquierda(subarbol.getIzquierda())
            self.sucesores_por_izquierda(subarbol.getDerecha())

if __name__=="__main__":
    arbol= ArbolBinarioBusqueda()
    arbol.insertar(arbol.getRaiz(),55)
    arbol.insertar(arbol.getRaiz(),50)
    arbol.insertar(arbol.getRaiz(),93)
    arbol.insertar(arbol.getRaiz(),43)
    arbol.insertar(arbol.getRaiz(),51)
    arbol.insertar(arbol.getRaiz(),95)
    #Ejercicio a
    print("------ EJERCICIO A ------".center(100))
    arbol.mostrar_Padre_Hermano(51)
    #Ejercicio b
    print("------ EJERCICIO B ------".center(100))
    print("La cantidad de nodos del arbol es: ",arbol.getCantidadNodos(arbol.getRaiz()))
    #Ejercicio c
    print("------ EJERCICIO C ------".center(100))
    print("La altura del arbol es: ", arbol.altura(arbol.getRaiz()))
    #Ejercicio d
    print("------ EJERCICIO D ------".center(100))
    print("Los sucesores del 55 son: ")
    arbol.mostrarSucesores(55)
    