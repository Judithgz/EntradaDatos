print("*** Sistema de Empleados ***")
nombre = input('Nombre del empleado: ')
edad = int(input('Edad del empleado: '))
salario = float(input('Salario del empleado: '))
jefe_departamento = input('Es jefe de departamento (Si/No)? ')

# Convertimos a tipo bool la variable jefe_departamento
jefe_departamento = jefe_departamento.lower() == 'si'

# Imprimir los valores del empleado
print('\nDatos del Empleado')
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
print(f'Salario: {salario:.2f}')
print(f'¿Es jefe de departamento?: {jefe_departamento}')



