"""Ejercicio 6 / Unidad 3 - Ary Toro"""
class Impresion:
    __tiempo_impresion:int
    __tiempo_espera:int

    def __init__(self,impresion,espera):
        self.__tiempo_impresion=impresion
        self.__tiempo_espera=espera

    def getTiempoImpresion(self):
        return self.__tiempo_impresion
    def setTiempoImpresion(self,impresion):
        self.__tiempo_impresion=impresion
    
    def getTiempoEspera(self):
        return self.__tiempo_espera
    def incrementarTiempoEspera(self):
        self.__tiempo_espera+=1
