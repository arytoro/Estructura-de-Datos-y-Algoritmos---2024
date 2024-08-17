"""Ejercicio 4 / Unidad 3 - Ary Toro"""
from pila_secuencial import PilaSecuencial

def mostrar_estado(p1,p2,p3):
    print(f"""
            Estado de las pilas
    Pila 1: {p1.dimension()} discos
    Pila 2: {p2.dimension()} discos
    Pila 3: {p3.dimension()} discos""")

def verificar_movimiento(pila_o,pila_d):
    valido=True
    contenido_o= pila_o.suprimir()
    if pila_d.vacia():
        pila_d.insertar(contenido_o)
    else:
        contenido_d= pila_d.suprimir()
        pila_d.insertar(contenido_d)
    
        if contenido_o<contenido_d:
            pila_d.insertar(contenido_o)
        else:
            pila_o.insertar(contenido_o)
            valido=False
    return valido

def movimiento(p1,p2,p3):
    validez=True
    opciones=[1,2,3]
    print("Movimiento".center(100))

    origen=int(input("Ingresa el origen (1,2,3): "))
    opciones.remove(origen)
    destino=int(input(f"Ingresa el destino {opciones}: "))

    if (origen in (1,2,3)) and (destino in (1,2,3)) and origen!=destino:
        if origen==1:
            if destino==2:
                validez= verificar_movimiento(p1,p2)
            elif destino==3:
                validez= verificar_movimiento(p1,p3)
        elif origen==2:
            if destino==1:
                validez= verificar_movimiento(p2,p1)
            elif destino==3:
                validez= verificar_movimiento(p2,p3)
        elif origen==3:
            if destino==1:
                validez= verificar_movimiento(p3,p1)
            elif destino==2:
                validez= verificar_movimiento(p3,p2)
    else:
        print("El origen y/o destino no son validos")
        validez=False

    if validez is False:
        print("El movimiento no es valido")
    
    return validez

        
if __name__=="__main__":
    pila1=PilaSecuencial()
    pila2=PilaSecuencial()
    pila3=PilaSecuencial()

    n=int(input("Ingresa la cantidad de discos: "))
    num_discos=n
    while n>0:
        pila1.insertar(n)
        n-=1

    mostrar_estado(pila1,pila2,pila3)
    cont_movimientos=0
    while pila3.dimension()!=num_discos:
        if movimiento(pila1,pila2,pila3):
            print("Movimiento exitoso")
            cont_movimientos+=1
        mostrar_estado(pila1,pila2,pila3)
    print(f"El juego se completo con {cont_movimientos} movimientos")
    print("La cantidad minima de movimientos necesarios para completarlo es: ",pow(2,num_discos)-1)
    
    """Sugerencia de Movimientos O,D
    1,2
    1,3
    2,3
    1,2
    3,1
    3,2
    1,2
    1,3
    2,3
    2,1
    3,1
    2,3
    1,2
    1,3
    2,3
    """
    
    