# Resolución
fecha = input ("Ingrese fecha en formato AAMMDD: ")
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
if len(fecha == 8) and fecha.isdigit():
    mes_ingresado = int(fecha[4:6])
    if 1 <= mes_ingresado >= 12:
        print("El mes es {meses[mes_ingresado - 1]}")
else:
    print("La fecha ingresada no tiene el formato correspondiente...")
