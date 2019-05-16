#!/usr/bin/python
 #-*- coding: latin-1 -*-
 #-*- Age,Has_job,Own_house,Credit_rating,Class
import os, sys
import csv, operator
import copy as cp
import decimal as dc

#Lee un archivo csv y devuelve un arreglo de 3 posciones
#La primera posicion tiene la lista de nombre de los atributos
#La segunda posicion tiene cada uno de los registros
#La tercera cada una de las clase
def read_ar(arg):
    archivo=[[],[],[]]#Posicion 1 titulos atributo, Posicion 2 registros
    pos=-1
    with open(arg) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for reg in entrada:
            if pos==-1:
                archivo[0]=reg
            else:
                #archivo[1]+=[[]]
                archivo[1]+=[reg]
                if reg[len(reg)-1] not in  archivo[2]:
                    archivo[2]+=[reg[len(reg)-1]]
            pos=pos+1
        return archivo