print('*** Valor dentro de un rango ***')

minimo = 0
maximo = 5
numero = int(input(f'Introduce un numero entre {minimo} y {maximo}: '))

# dentro_rango = numero >= minimo and numero <= maximo --> ejemplo, el de abajo es simplificado
dentro_rango = minimo <= numero <= maximo

print(f'¿Se encuentra el numero dentro del rango?: {dentro_rango}')