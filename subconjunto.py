def subconjuntoclase(datos):
    """
    va a generar todos los subconjuntos de clases con su nombre y su cardinalidad
     El orden va a coincider con el orden en que aparecen en los datos.

    :type datos: arreglo con todos los datos
    :return: elements(un arreglo con los nombre de las clases), valor(un arreglo con las cardinalidades de los valores de las clases)
    """
    valor = []
    elements = []
    for reg in datos:
        elem = reg[len(reg) - 1]  # Posicion de la clase
        if elem not in elements:
            elements = elements + [elem]
            valor.extend([1])
        else:
            i = 0
            for pos in elements:
                if pos == elem:
                    valor[i] = valor[i] + 3
                i = i + 1
    return elements, valor
