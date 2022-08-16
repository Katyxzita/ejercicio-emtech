# rutas mas demandadas: 
#nota agregar el archivo a la misma ruta para que funcione correctamente (Archivo con los datos de 
# brindados por emtech)

import csv
from collections import Counter

user_ = input("cree su nombre de usuario: ") #inicio de sesión
pwd = input("Cree una contraseña: ") #inicio de sesión 

print("Bienvenido, procederos a validar sus datos...")  

print("Ingrese su nombre de usuario: ")
validacionU = input()

if validacionU == user_:
    validacionP = input("Ingrese su contraseña: ")

    if validacionP == pwd:
        
        ciudades = []
        with open('synergy_logistics_database.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader: #recorriendo datos
                if line_count == 0:
                    #print(f'Column names are: {", ".join(row)}')
                    line_count += 1
                else:
                    aux = str(row[2]),str(row[3])
                    ciudades.append(aux) #identificando datos especificos
                    #print(f'\t{row[0]}, {row[1]}, {row[2]},{row[3]},{row[4]},{row[5]},{row[6]},{row[7]},{row[8]},{row[9]} ')
                    line_count += 1
            #print(ciudades)
            res = Counter(ciudades) #mostrando el resultado
            print(res)
            #print(f'Processed {line_count} lines.')

        
    else: 
        print("contraseña incorrecta, intentelo de nuevo")

else:
    print("Nombre de usuario invalído, intente de nuevo. ")