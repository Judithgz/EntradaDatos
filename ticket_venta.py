print('*** Generacion Ticket De Venta ***')

precio_pan = float(input('Precio leche: '))
precio_queso = float(input('Precio leche: '))
precio_manzana = float(input('Precio manzana: '))
precio_agua = float(input('Precio agua: '))
descuento_porcentaje = int(input('¿Aplicar descuento (%)?: '))

# Calculo del subtotal (sin impuestos)
subtotal = precio_pan + precio_queso + precio_manzana + precio_agua

# Aplicar un descuento al calculo del subtotal
# descuento = subtotal * 0.10 --> Ejemplo del 10%
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuestos)
total_compra = subtotal_con_descuento + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento}
Impuesto (16%): ${impuesto:.2f}
Total: ${total_compra:.2f}
''')