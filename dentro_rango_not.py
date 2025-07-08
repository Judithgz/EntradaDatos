# Revisar si una variable se encuentra dentro de ranto entre 1 y 10
dato = int(input('Introduce un numero entero: '))

# Revisamos si esta dentro de rango
# dentro_rango = 1 <= dato <= 10
# print(f'Variable esta dentro del rango?: {dentro_rango}')


# Revisamos la logica inversa, si el dato esta fuera de rango
fuera_rango = not(1 <= dato <= 10)
print(f'Variable esta fuera del rango?: {fuera_rango}')
