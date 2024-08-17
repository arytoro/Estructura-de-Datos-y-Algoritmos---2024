"""Ejercicio 3 / Unidad 3 - Ary Toro"""
from pila_encadenada import PilaEncadenada

if __name__=="__main__":
    p=PilaEncadenada()
    resultado=1
    numero=int(input("Ingresa el numero para calcular su factorial: "))
    while numero>=0:
        if numero>0:
            p.insertar(numero)
        elif numero==0:
            p.insertar(1)
        numero-=1

    while p.vacia() is False:
        resultado *= p.suprimir()
    print("Su factorial es: ",resultado)
