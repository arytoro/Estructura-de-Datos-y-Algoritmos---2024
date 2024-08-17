"""Ejercicio 2 / Unidad 3 - Ary Toro"""
from pila_secuencial import PilaSecuencial

if __name__=="__main__":
    p=PilaSecuencial()
    try:
        decimal=int(input("Ingresa el numero decimal: "))
        aux=decimal
        while aux>=1:
            modulo=aux%2
            aux=aux//2
            p.insertar(modulo)
    except ValueError:
        print("Error. Se esperaba un entero")
        
    print("En binario es: ",end=" ")
    while p.vacia() is False:
        print(p.suprimir(),end="")
