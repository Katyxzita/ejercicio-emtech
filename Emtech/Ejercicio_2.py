municipio = input("Ingrese el nombre de su municipio: ")
habitantes = input("Ingrese el numero de habitantes: ")

municipio1 = input("Ingrese el nombre de su municipio: ")
habitantes1 = input("Ingrese el numero de habitantes: ")

municipio2 = input("Ingrese el nombre de su municipio: ")
habitantes2 = input("Ingrese el numero de habitantes: ")

Li_mu = [municipio, municipio1, municipio2] 
Li_ha = [int(habitantes), int(habitantes1), int(habitantes2)]

totalHabitantes = sum(Li_ha)
promedioHabitantes = float(totalHabitantes) / 3

print("La cantidad de habitantes es: " + str(totalHabitantes) + " con un promedio de: " + str(promedioHabitantes))