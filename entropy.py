#!/usr/bin/python
 #-*- coding: latin-1 -*-

import math as mt
import copy as cp
import SUBCONJUNTO as sb
import decimal as dc

#Función que recibe el conjunto de datos
#Me devuelve el nivel de entropia del conjunto
def entropiaclase(archivo):
    var1=sb.subconjuntoclase(archivo)
    entro=cp.deepcopy(var1[1])
    resultado=0
    total=contar_tot(archivo)#calculo la cantidad de registros
    for reg in entro:
        if reg!=0:
            c=dc.Decimal(reg)/dc.Decimal(total)#divido
            resultado=resultado-float(c)*mt.log(float(c),2)#lo voy resguardando
    return resultado
