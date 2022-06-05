#Ejercicio 1

superficieKM2 = 57,365 #Kilometros cuadrados
tempAnualGC = 25.45   #Grados centigrados
preciAnualMM = 790.1 #Milimetros - precipitacion 

#Poblacion 
pobF = 1,532,128 #mujeres
pobM = 1,494,815 #hombres

porcentajeHabClcn = 33.15
porcentajeHabMaza = 16.57

clima = 'calido, subhumedo, seco y semiseco'

poblacionTotal = pobF + pobM
porcentajeTotal = porcentajeHabClcn + porcentajeHabMaza
temp_clima = "El clima, con una precipitacion en MM de " + str(preciAnualMM) + " " + clima

print(temp_clima)
