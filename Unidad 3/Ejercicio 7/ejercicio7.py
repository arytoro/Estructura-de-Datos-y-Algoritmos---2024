"""Ejercicio 6 / Unidad 3 - Ary Toro"""
from random import uniform,choice
from cola_encadenada import ColaEncadenada

def llega_cliente():

    random= uniform(0,1) #Determina si llega impresion
    if random <= 1/2: #La formula es 1/Frecuencia ; Siendo en este caso 2.
        llego_cliente=True
    else:
        llego_cliente=False
    return llego_cliente

    #Para Lote de Prueba
    #llega_cliente=False
    #if reloj in (1,2,3,4,5,6,8,9,10,11,12,13,14,15,17,18):
    #    llega_cliente=True
    #return llega_cliente

def elegir_cajero(cont_c1,cont_c2,cont_c3):
    # Para lote de prueba
    #if reloj in (1,2,10,11,15,17):
    #    elegido=1
    #elif reloj in (3,4,6,9,12,13):
    #    elegido=2
    #elif reloj in (5,8,14,18):
    #    elegido=3
    #return elegido

    opciones=[1,2,3]
    menor=100
    # Si el contador del cajero analizado es !=0; es porque tiene cliente/s esperando
    if cont_c1!=0:
        opciones.remove(1)
    if cont_c2!=0:
        opciones.remove(2)
    if cont_c3!=0:
        opciones.remove(3)

    if len(opciones)>0: #Hay cajero/s libre/s
        elegido= choice(opciones) #Elige uno de los cajeros sin cola
    else: #Todos los cajeros estan ocupados
        colas=[cont_c1,cont_c2,cont_c3]
        for i in range(3): #Se eligira el que tenga menos clientes esperando
            if colas[i]<menor:
                menor= colas[i]
                elegido=i+1

    return elegido

    
if __name__=="__main__":
    cajero1=ColaEncadenada()
    cont_clientes_ingresados_c1=0
    cont_clientes_atendidos_c1=0
    acum_tiempo_espera_c1=0
    tiempo_cajero1=0
    maximo_tiempo_espera_c1= -1
    acum_tiempo_espera_incompletas_c1=0

    cajero2=ColaEncadenada()
    cont_clientes_ingresados_c2=0
    cont_clientes_atendidos_c2=0
    acum_tiempo_espera_c2=0
    tiempo_cajero2=0
    maximo_tiempo_espera_c2= -1
    acum_tiempo_espera_incompletas_c2=0

    cajero3=ColaEncadenada()
    cont_clientes_ingresados_c3=0
    cont_clientes_atendidos_c3=0
    acum_tiempo_espera_c3=0
    tiempo_cajero3=0
    maximo_tiempo_espera_c3= -1
    acum_tiempo_espera_incompletas_c3=0

    #Creo que lo mejor sería hacer una clase cajero que herede de cola encadenada y resguardar esos atributos. No se si esta permitido

    tms=int(input("Ingresa el tiempo maximo de solucion (en minutos): "))
    reloj=0
    while reloj<tms:
        if llega_cliente(): #Para hacer lote de prueba pasar reloj por parametro y descomentar las lineas de las dos funciones (y comentar las no comentadas)
            cajero_elegido= elegir_cajero(cont_clientes_ingresados_c1 - cont_clientes_atendidos_c1,cont_clientes_ingresados_c2 - cont_clientes_atendidos_c2,cont_clientes_ingresados_c3 - cont_clientes_atendidos_c3)
            if cajero_elegido==1:
                cajero1.insertar(reloj)
                cont_clientes_ingresados_c1+=1
            elif cajero_elegido==2:
                cajero2.insertar(reloj)
                cont_clientes_ingresados_c2+=1
            else:
                cajero3.insertar(reloj)
                cont_clientes_ingresados_c3+=1

        if tiempo_cajero1==0: #Si el contador tc1 = 0 el cajero esta libre
            if cajero1.vacia() is False: #Si hay elementos en la cajero1...
                cliente_atendido_c1 = cajero1.suprimir() #Elimino el primero que llego al cajero1 y lo resguardo en ca1
                tiempo_espera_c1= reloj - cliente_atendido_c1 #Reloj - hora de llegada = tiempo de espera

                if reloj+5 < tms: #Determino si el cliente va a poder ser atendido satisfactoriamente antes de que se alcance el tms
                    acum_tiempo_espera_c1 += tiempo_espera_c1
                    cont_clientes_atendidos_c1+=1
                else:
                    acum_tiempo_espera_incompletas_c1+= tiempo_espera_c1

                if tiempo_espera_c1 > maximo_tiempo_espera_c1: #Necesito guardar el tiempo maximo de espera para el item a
                    maximo_tiempo_espera_c1= tiempo_espera_c1
                tiempo_cajero1=5 #El cajero va a estar ocupado durante 5 minutos (informacion del enunciado)
        if tiempo_cajero1>0: #Si el cajero esta ocupado...
            tiempo_cajero1-=1 #Deberá actualizarse minuto a minuto hasta que esté libre
        
        if tiempo_cajero2==0:
            if cajero2.vacia() is False:
                cliente_atendido_c2 = cajero2.suprimir()
                tiempo_espera_c2= reloj - cliente_atendido_c2

                if reloj+3 < tms:
                    acum_tiempo_espera_c2 += tiempo_espera_c2
                    cont_clientes_atendidos_c2+=1
                else:
                    acum_tiempo_espera_incompletas_c2+= tiempo_espera_c2

                if tiempo_espera_c2 > maximo_tiempo_espera_c2:
                    maximo_tiempo_espera_c2= tiempo_espera_c2
                tiempo_cajero2=3
        if tiempo_cajero2>0:
            tiempo_cajero2-=1
            
        if tiempo_cajero3==0:
            if cajero3.vacia() is False:
                cliente_atendido_c3 = cajero3.suprimir()
                tiempo_espera_c3= reloj - cliente_atendido_c3

                if reloj+4 < tms:
                    acum_tiempo_espera_c3 += tiempo_espera_c3
                    cont_clientes_atendidos_c3+=1
                else:
                    acum_tiempo_espera_incompletas_c3+= tiempo_espera_c3

                if tiempo_espera_c3 > maximo_tiempo_espera_c3:
                    maximo_tiempo_espera_c3= tiempo_espera_c3
                tiempo_cajero3=4
        if tiempo_cajero3>0:
            tiempo_cajero3-=1

        reloj+=1

    #print(f"""Datos Cajero 1:
    #    Acumulador de espera: {acum_tiempo_espera_c1}
    #    Clientes Ingresados: {cont_clientes_ingresados_c1}
    #    Clientes Atendidos: {cont_clientes_atendidos_c1}""")
    #print(f"""Datos Cajero 2:
    #    Acumulador de espera: {acum_tiempo_espera_c2}
    #    Clientes Ingresados: {cont_clientes_ingresados_c2}
    #    Clientes Atendidos: {cont_clientes_atendidos_c2}""")
    #print(f"""Datos Cajero 3:
    #    Acumulador de espera: {acum_tiempo_espera_c3}
    #    Clientes Ingresados: {cont_clientes_ingresados_c3}
    #    Clientes Atendidos: {cont_clientes_atendidos_c3}""")

    #Item A
    print("El tiempo maximo de espera en el cajero 1 es: ",maximo_tiempo_espera_c1)
    print("El tiempo maximo de espera en el cajero 2 es: ",maximo_tiempo_espera_c2)
    print("El tiempo maximo de espera en el cajero 3 es: ",maximo_tiempo_espera_c3)
    #Item B
    print("El total de clientes atendidos es: ", cont_clientes_atendidos_c1 + cont_clientes_atendidos_c2 + cont_clientes_atendidos_c3)
    #Item C
    print("El total de clientes sin atender es: ",(cont_clientes_ingresados_c1 - cont_clientes_atendidos_c1) + (cont_clientes_ingresados_c2 - cont_clientes_atendidos_c2) + (cont_clientes_ingresados_c3 - cont_clientes_atendidos_c3))
    #Item D
    promedio_espera_clientes_atendidos_c1= acum_tiempo_espera_c1/ cont_clientes_atendidos_c1 if cont_clientes_atendidos_c1!=0 else 0
    promedio_espera_clientes_atendidos_c2= acum_tiempo_espera_c2/ cont_clientes_atendidos_c2 if cont_clientes_atendidos_c2!=0 else 0
    promedio_espera_clientes_atendidos_c3= acum_tiempo_espera_c3/ cont_clientes_atendidos_c3 if cont_clientes_atendidos_c3!=0 else 0
    print(f"""Promedio de Espera de los clientes atendidos:
          Cajero 1: {promedio_espera_clientes_atendidos_c1}
          Cajero 2: {promedio_espera_clientes_atendidos_c2}
          Cajero 3: {promedio_espera_clientes_atendidos_c3}""")
    #Item E
    promedio_espera_clientes_sin_atender_c1= acum_tiempo_espera_incompletas_c1/ (cont_clientes_ingresados_c1 - cont_clientes_atendidos_c1) if cont_clientes_ingresados_c1 - cont_clientes_atendidos_c1!=0 else 0
    promedio_espera_clientes_sin_atender_c2= acum_tiempo_espera_incompletas_c2 / (cont_clientes_ingresados_c2 - cont_clientes_atendidos_c2) if cont_clientes_ingresados_c2 - cont_clientes_atendidos_c2!=0 else 0
    promedio_espera_clientes_sin_atender_c3= acum_tiempo_espera_incompletas_c3 / (cont_clientes_ingresados_c3 - cont_clientes_atendidos_c3) if cont_clientes_ingresados_c3 - cont_clientes_atendidos_c3!=0 else 0
    print(f"""Promedio de Espera de los clientes sin atender:
          Cajero 1: {promedio_espera_clientes_sin_atender_c1}
          Cajero 2: {promedio_espera_clientes_sin_atender_c2}
          Cajero 3: {promedio_espera_clientes_sin_atender_c3}""")