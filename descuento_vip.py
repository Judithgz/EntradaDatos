print('*** Sistema Descuentos VIP ***')

n_productos_descuento = 10
cantidad_productos = int(input('¿Cuantos productos compraste hoy?: '))
tiene_membresia = input('¿Tiene membresia de la tienda? (Si/No): ')

es_elegible = (cantidad_productos >= n_productos_descuento
               and tiene_membresia.strip().lower() == 'si')

print(f'¿Tienes acceso al descuento VIP?: {es_elegible}')