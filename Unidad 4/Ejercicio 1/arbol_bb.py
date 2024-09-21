"""Ejercicio 1 - Unidad 4 / Ary Toro"""
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

if __name__=="__main__":
    arbol=ArbolBinarioBusqueda()
    arbol.insertar(arbol.getRaiz(),60)#
    arbol.insertar(arbol.getRaiz(),50)#
    arbol.insertar(arbol.getRaiz(),70)#
    arbol.insertar(arbol.getRaiz(),43)#
    arbol.insertar(arbol.getRaiz(),52)#
    arbol.insertar(arbol.getRaiz(),48)#
    arbol.insertar(arbol.getRaiz(),51)#
    arbol.insertar(arbol.getRaiz(),55)#
    arbol.insertar(arbol.getRaiz(),93)#
    arbol.insertar(arbol.getRaiz(),95)
    arbol.InOrder(arbol.getRaiz())
    
    print("INICIANDO PRUEBAS DE SUPRESION (ver imagen de la carpeta)")
    print("--------------Primera supresion (nodo hoja 48)---------------------")
    print("Grado del nodo clave 43 antes de la supresion:", arbol.gradoNodo(43))
    print("Suprimir 48",arbol.suprimir(48))
    print("Grado del nodo clave 43 despues de la supresion:", arbol.gradoNodo(43))
    arbol.InOrder(arbol.getRaiz())
    print("--------------Segunda supresion (nodo 70 con un hijo)---------------------")
    print("Nivel  del nodo 93 antes de suprimir el 70:", arbol.nivelNodo(93))
    print("Suprimir 70",arbol.suprimir(70))
    print("Nivel  del nodo 93 despues de suprimir el 70:", arbol.nivelNodo(93))
    arbol.InOrder(arbol.getRaiz())
    print("--------------Tercera supresion (nodo 52 con 2 hijos)---------------------")
    print("Grado del nodo 51 antes de suprimir el 52: ",arbol.gradoNodo(51))
    print("Suprimir 52",arbol.suprimir(52))
    print("Grado del nodo 51 despues de suprimir el 52: ",arbol.gradoNodo(51))
    arbol.InOrder(arbol.getRaiz())
    print("REVISANDO GRADOS")
    print("Grado del nodo clave 60:", arbol.gradoNodo(60))
    print("Grado del nodo clave 50:", arbol.gradoNodo(50))
    print("Grado del nodo clave 93:", arbol.gradoNodo(93))
    print("Grado del nodo clave 43:", arbol.gradoNodo(43))
    print("Grado del nodo clave 51:", arbol.gradoNodo(51))
    print("Grado del nodo clave 55:", arbol.gradoNodo(55))
    print("Grado del nodo clave 95:", arbol.gradoNodo(95))
    print("----Suprimir la raiz 60---")
    arbol.suprimir(60)
    print("La nueva raiz es: ", arbol.getRaiz().getDato())
    print("Grado del nodo clave 50:", arbol.gradoNodo(50))
    print("Grado del nodo clave 93:", arbol.gradoNodo(93))
    print("Grado del nodo clave 43:", arbol.gradoNodo(43))
    print("Grado del nodo clave 51:", arbol.gradoNodo(51))
    print("Grado del nodo clave 55:", arbol.gradoNodo(55))
    print("Grado del nodo clave 95:", arbol.gradoNodo(95))
    print("------TESTEANDO OTRAS FUNCIONES----------")
    print("El 93 es hijo del 55?: ",arbol.hijo(55,93))
    print("El 55 es padre del 43?: ",arbol.padre(55,43))
    print("La altura del arbol es ", arbol.altura(arbol.getRaiz()))
    print("Camino desde el nodo 55 hasta el 51:", arbol.camino(55,51))
