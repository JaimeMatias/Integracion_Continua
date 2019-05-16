from Integracion_Continua.read import read_ar
from Integracion_Continua.subconjunto import subconjuntoclase
archivo= read_ar('datos.csv')
#print(archivo)
var=  subconjuntoclase(archivo[1])
print(var)