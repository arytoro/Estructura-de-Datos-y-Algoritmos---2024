"""Ejercicio 6 / Unidad 3 - Ary Toro"""
from random import uniform
from claseImpresion import Impresion
from cola_encadenada import ColaEncadenada

def llega_impresion():
    random= uniform(0,1) #Determina si llega impresion
    if random <= 1/5: #La formula es 1/Frecuencia ; Siendo en este caso 5.
        llego_impresion=True
    else:
        llego_impresion=False
    return llego_impresion
    #llega_impresion=False
    #if reloj in (4,5,16,20,24):
    #    llega_impresion=True
    #return llega_impresion
    
if __name__=="__main__":
    cola=ColaEncadenada()
    contador_impresiones_pendientes=0
    contador_impresiones_realizadas=0
    acumulador_tiempo_espera=0
    tiempo_atencion_impresora=0
    tms=int(input("Ingresa el tiempo maximo de solucion (en minutos): "))
    reloj=0
    while reloj<tms:
        if llega_impresion():
            contador_impresiones_pendientes+=1
            tiempo_impresion=int(input(f"Ingresa el tiempo de impresión (llegó en minuto {reloj}): "))
            cola.insertar(Impresion(tiempo_impresion,reloj))

        if tiempo_atencion_impresora==0: #Si el contador tai = 0 la impresora esta libre
            if cola.vacia() is False: #Si hay elementos en la cola...
                impresion_en_proceso = cola.suprimir() #Elimino el primero que llego a la cola y lo resguardo en iep
                tiempo_restante= impresion_en_proceso.getTiempoImpresion() - 5 #De la iep obtengo el tiempo necesario para imprimirla
                acumulador_tiempo_espera+= reloj - impresion_en_proceso.getTiempoEspera() #En el acumulador guardo la diferencia entre reloj y tiempo de llegada
                if tiempo_restante > 0: # Si el trabajo tarda mas de 5 minutos para imprimirse...
                    tiempo_atencion_impresora=5 #La impresora va a estar ocupada durante 5 minutos ya que es su maximo
                    cola.insertar(Impresion(tiempo_restante,reloj+5)) #Se reinserta en la cola la impresion con el tiempo que falta para completarse y el minuto en el que sera atendida (inmediatamente despues de la primera parte)
                else: #Si el trabajo tarda menos de 5 minutos ...
                    tiempo_atencion_impresora= impresion_en_proceso.getTiempoImpresion() #La impresora estará ocupada durante el tiempo que tarde imprimirse el trabajo
                    contador_impresiones_realizadas+=1 #Completandose una impresion solo si tiempo restante es <=0
        reloj+=1
        if tiempo_atencion_impresora>0: #Si la impresora esta ocupada...
            tiempo_atencion_impresora-=1 #Deberá actualizarse minuto a minuto hasta que esté libre

    print("Acumulador de espera: ",acumulador_tiempo_espera)
    print("Impresiones Ingresadas: ",contador_impresiones_pendientes)
    print("Impresiones Completas: ",contador_impresiones_realizadas)
    tiempo_promedio_espera= acumulador_tiempo_espera / contador_impresiones_realizadas
    print(f"Quedaron {contador_impresiones_pendientes - contador_impresiones_realizadas} impresiones sin realizar")
    print("El tiempo promedio de espera es: ",tiempo_promedio_espera)
    
""" Sugerencia de Lote de Prueba con TMS=30 (Descomentar las lineas de la funcion "llega_impresion()" y pasar por parametro el reloj)
Min 4= 10
Min 5= 5
Min 16= 3
Min 20= 7
Min 24= 9
"""