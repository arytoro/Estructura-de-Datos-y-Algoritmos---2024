from lista_encadenada import ListaEncadenada

def concatenar(l1,l2,lr):
    i=0
    pos=0
    while i is not None:
        lr.insertar(l1.recuperar(i),pos)
        pos+=1
        i= l1.siguiente(i)
    j=0
    while j is not None:
        lr.insertar(l2.recuperar(j),pos)
        pos+=1
        j= l2.siguiente(j)

if __name__=="__main__":
    lista1= ListaEncadenada()
    lista2= ListaEncadenada()
    lista_resultante= ListaEncadenada()
    lista1.insertar(5,0)
    lista1.insertar(3,1)
    lista2.insertar(9,0)
    lista2.insertar(8,1)
    lista2.insertar(1,2)
    concatenar(lista1,lista2,lista_resultante)
    lista_resultante.recorrer()