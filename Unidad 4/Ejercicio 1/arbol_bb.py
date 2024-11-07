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
            if clave > subarbol.getDato(): #Si la clave del nuevo nodo es mayor que la del subarbol paDerechao por parametro (en la primera iteracion es la raiz)..
                if subarbol.getDerecha() is None:  #Verifico si el subarbol tiene disponible la rama derecha
                    nuevoNodo= Nodo(clave)
                    subarbol.setDerecha(nuevoNodo)  #Si es así lo asigno
                else: #Sino, deberá de empezar la recursión pasando esta vez como subarbol el nodo que se encontraba en la derecha
                    self.insertar(subarbol.getDerecha(),clave)
            elif clave < subarbol.getDato(): #Aquí la logica es la misma, solo que aplicada a la izquierda
                if subarbol.getIzquierda() is None:
                    nuevoNodo= Nodo(clave)
                    subarbol.setIzquierda(nuevoNodo)
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

    def gradoNodo(self,subarbol,clave):
        if subarbol is None:
            print("ERROR. El nodo ingresado no existe")
            grado=None
        else:
            if clave== subarbol.getDato():
                return subarbol.getGrado()
            elif clave > subarbol.getDato():
                grado= self.gradoNodo(subarbol.getDerecha(),clave)
            else:
                grado= self.gradoNodo(subarbol.getIzquierda(),clave)
        return grado

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
            print(subarbol.getDato(),end=" -> ")
            self.InOrder(subarbol.getDerecha())

    def nivelNodo(self,subarbol,clave,nivel=1):
        if subarbol is None:
            print('Elmento no encontrado!')
            nivel=None
        else:
            if clave == subarbol.getDato():
                return nivel
            elif clave > subarbol.getDato():
                nivel+=1
                nivel = self.nivelNodo(subarbol.getDerecha(),clave,nivel)
            else:
                nivel+=1
                nivel = self.nivelNodo(subarbol.getIzquierda(),clave,nivel)
        return nivel

    def getInfimo(self,subarbol):
        subarbol= subarbol.getIzquierda()
        while subarbol.getGrado() != 0:
            subarbol= subarbol.getDerecha()
        return subarbol

    def getPadre(self,subarbol,clave):
        if subarbol is None:
            print(f"ERROR! No existe el nodo padre de {clave}")
            return None
        else:
            derecha= subarbol.getDerecha()
            izquierda= subarbol.getIzquierda()
            if (derecha != None and derecha.getDato()==clave) or (izquierda!= None and izquierda.getDato()==clave):
                return subarbol
            elif clave > subarbol.getDato():
                subarbol=self.getPadre(subarbol.getDerecha(),clave)
            else:
                subarbol=self.getPadre(subarbol.getIzquierda(),clave)
        return subarbol

    def suprimir(self,clave): #Es mas facil hacer el seguimiento viendo la imagen de la carpeta y ejecutandolo
        subarbol= self.buscar(self.__raiz,clave)
        padre= self.getPadre(self.__raiz,clave)
        print(padre)
        if subarbol is not None:
            grado= self.gradoNodo(self.__raiz,clave)
            if grado == 0: #Si el grado es 0, es un nodo hoja. Ahora el padre va a apuntar a None en su rama derecha/izquierda en la que estaba el hijo suprimido
                if clave > padre.getDato():
                    padre.setDerecha(None)
                else:
                    padre.setIzquierda(None)
            if grado == 1: #Si el grado es 1, el nodo tenia un hijo. Ahora el padre deberá apuntar a ese hijo
                if subarbol.getDerecha() is not None: #Busco el hijo (esta en la derecha O izquierda, ya que solo tiene 1)
                    hijo= subarbol.getDerecha()
                else:
                    hijo= subarbol.getIzquierda()

                subarbol.setDato(hijo.getDato()) #Ahora el nodo a suprimir será una copia de su hijo
                subarbol.setDerecha(hijo.getDerecha())
                subarbol.setIzquierda(hijo.getIzquierda())

                #if subarbol.getDerecha().getDato() == subarbol.getDato():
                #    subarbol.setDerecha(None)
                #else:
                #    subarbol.setDerecha(None)
            if grado== 2: #Si el grado es 2, hay que buscar el infimo o el supremo para reemplazarlo
                infimo=self.getInfimo(subarbol)
                padre_infimo= self.getPadre(self.__raiz,infimo.getDato())
                subarbol.setDato(infimo.getDato())

                if infimo.getDato() > padre_infimo.getDato():
                    padre_infimo.setDerecha(None)
                else:
                    padre_infimo.setIzquierda(None)


    def hijo(self,subarbol,hijo,padre):
        if subarbol is None:
            print("ERROR! No existe el nodo padre")
            bandera=False
        else:
            if padre==subarbol.getDato():
                izquierda= subarbol.getIzquierda()
                derecha= subarbol.getDerecha()
                return (izquierda != None and izquierda.getDato()==hijo) or (derecha != None and derecha.getDato()==hijo)
            elif padre > subarbol.getDato():
                bandera= self.hijo(subarbol.getDerecha(),hijo,padre)
            else:
                bandera= self.hijo(subarbol.getIzquierda(),hijo,padre)
        return bandera
        #subarbol_padre= self.buscar(self.__raiz,padre)
        #subarbol_hijo= self.buscar(self.__raiz,hijo)
        #es_hijo= False
        #if subarbol_padre is not None and subarbol_hijo is not None:
        #    es_hijo= subarbol_padre.getIzquierda()==subarbol_hijo or subarbol_padre.getDerecha()==subarbol_hijo
        #return es_hijo

    def padre(self,subarbol,padre,hijo):
        if subarbol is None:
            print("ERROR! No existe el nodo padre")
            bandera= False
        else:
            if padre==subarbol.getDato():
                izquierda= subarbol.getIzquierda()
                derecha= subarbol.getDerecha()
                return (izquierda != None and izquierda.getDato()==hijo) or (derecha != None and derecha.getDato()==hijo)
            elif padre > subarbol.getDato():
                bandera= self.padre(subarbol.getDerecha(),padre,hijo)
            else:
                bandera= self.padre(subarbol.getIzquierda(),padre,hijo)
        return bandera
        #subarbol_padre= self.buscar(self.__raiz,padre)
        #subarbol_hijo= self.buscar(self.__raiz,hijo)
        #es_padre= False
        #if subarbol_padre is not None and subarbol_hijo is not None:
        #    es_padre= subarbol_padre.getIzquierda()==subarbol_hijo or subarbol_padre.getDerecha()==subarbol_hijo
        #return es_padre

    
    def altura(self,subarbol,maximo=1):
        if subarbol is not None:
            nivel = self.nivelNodo(self.__raiz,subarbol.getDato())
            if nivel > maximo:
                maximo = nivel
            maximo = self.altura(subarbol.getIzquierda(), maximo)
            maximo = self.altura(subarbol.getDerecha(), maximo)
        return maximo

    def PreOrden(self,subarbol):
        if subarbol is not None:
            print(subarbol.getDato(),end=" -> ")
            self.PreOrden(subarbol.getIzquierda())
            self.PreOrden(subarbol.getDerecha())

    def PostOrden(self,subarbol):
        if subarbol is not None:
            self.PostOrden(subarbol.getIzquierda())
            self.PostOrden(subarbol.getDerecha())
            print(subarbol.getDato(),end=" -> ")

    def camino(self,origen,destino):
        nodo_origen= self.buscar(self.__raiz,origen)
        camino="°"
        nodo_actual= nodo_origen
        while nodo_actual is not None and nodo_actual.getDato()!=destino:
            camino+= f" -> {nodo_actual.getDato()}"
            if destino > nodo_actual.getDato():
                nodo_actual= nodo_actual.getDerecha()
            else:
                nodo_actual= nodo_actual.getIzquierda()
        if nodo_actual is None:
            print(f"ERROR! No existe un camino desde {origen} hasta {destino}")
            camino=None
        else:
            camino+= f" -> {destino} -|"
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
    arbol.menor()
    """
    print("EN ORDEN")
    arbol.InOrder(arbol.getRaiz())
    print("\nPREORDEN")
    arbol.PreOrden(arbol.getRaiz())
    print("\nPOSTORDEN")
    arbol.PostOrden(arbol.getRaiz())


    print("\nEl 52 es hijo del 50?: ",arbol.hijo(arbol.getRaiz(),52,50))
    print("El 93 es padre del 95?: ",arbol.padre(arbol.getRaiz(),93,95))
    print("INICIANDO PRUEBAS DE SUPRESION (ver imagen de la carpeta)")
    print("--------------Primera supresion (nodo hoja 48)---------------------")
    print("Grado del nodo clave 43 antes de la supresion:", arbol.gradoNodo(arbol.getRaiz(),43))
    print("Suprimir 48",arbol.suprimir(48))
    print("Grado del nodo clave 43 despues de la supresion:", arbol.gradoNodo(arbol.getRaiz(),43))
    arbol.InOrder(arbol.getRaiz())
    print("--------------Segunda supresion (nodo 70 con un hijo)---------------------")
    print("Nivel  del nodo 93 antes de suprimir el 70:", arbol.nivelNodo(arbol.getRaiz(),93))
    print("Suprimir 70",arbol.suprimir(70))
    print("Nivel  del nodo 93 despues de suprimir el 70:", arbol.nivelNodo(arbol.getRaiz(),93))
    arbol.InOrder(arbol.getRaiz())
    print("--------------Tercera supresion (nodo 52 con 2 hijos)---------------------")
    print("Grado del nodo 51 antes de suprimir el 52: ",arbol.gradoNodo(arbol.getRaiz(),51))
    print("Suprimir 52",arbol.suprimir(52))
    print("Grado del nodo 51 despues de suprimir el 52: ",arbol.gradoNodo(arbol.getRaiz(),51))
    arbol.InOrder(arbol.getRaiz())
    print("REVISANDO GRADOS")
    print("Grado del nodo clave 60:", arbol.gradoNodo(arbol.getRaiz(),60))
    print("Grado del nodo clave 50:", arbol.gradoNodo(arbol.getRaiz(),50))
    print("Grado del nodo clave 93:", arbol.gradoNodo(arbol.getRaiz(),93))
    print("Grado del nodo clave 43:", arbol.gradoNodo(arbol.getRaiz(),43))
    print("Grado del nodo clave 51:", arbol.gradoNodo(arbol.getRaiz(),51))
    print("Grado del nodo clave 55:", arbol.gradoNodo(arbol.getRaiz(),55))
    print("Grado del nodo clave 95:", arbol.gradoNodo(arbol.getRaiz(),95))
    print("----Suprimir la raiz 60---")
    arbol.suprimir(60)
    print("La nueva raiz es: ", arbol.getRaiz().getDato())
    print("Grado del nodo clave 50:", arbol.gradoNodo(arbol.getRaiz(),50))
    print("Grado del nodo clave 93:", arbol.gradoNodo(arbol.getRaiz(),93))
    print("Grado del nodo clave 43:", arbol.gradoNodo(arbol.getRaiz(),43))
    print("Grado del nodo clave 51:", arbol.gradoNodo(arbol.getRaiz(),51))
    print("Grado del nodo clave 55:", arbol.gradoNodo(arbol.getRaiz(),55))
    print("Grado del nodo clave 95:", arbol.gradoNodo(arbol.getRaiz(),95))
    print("------TESTEANDO OTRAS FUNCIONES----------")
    print("El 93 es hijo del 55?: ",arbol.hijo(arbol.getRaiz(),55,93))
    print("El 55 es padre del 43?: ",arbol.padre(arbol.getRaiz(),55,43))
    print("La altura del arbol es ", arbol.altura(arbol.getRaiz()))
    print("Camino desde el nodo 55 hasta el 93:", arbol.camino(55,93))

    print("EN ORDEN")
    arbol.InOrder(arbol.getRaiz())
    print("\nPREORDEN")
    arbol.PreOrden(arbol.getRaiz())
    print("\nPOSTORDEN")
    arbol.PostOrden(arbol.getRaiz())"""
