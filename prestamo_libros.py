print('*** Sistema Prestamo de Libros ***')

distancia_km = 3
tiene_credencial = input('¿Cuentas con credencial de estudiante? (Si/No): ')
distancia_cliente = int(input('¿A cuantos km vives de la biblioteca?: '))

elegible = (tiene_credencial.strip().lower() == 'si'
            or distancia_cliente <= distancia_km)

print(f'¿Eres elegible para el prestamo?: {elegible}')