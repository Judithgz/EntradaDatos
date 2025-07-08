print("*** Sistema Generador de Emails ***")

nombre = input("Nombre: ")
apellidos = input("Apellidos: ")
empresa = input("Empresa: ")
dominio = input("Dominio: ")

# Normalizamos los valores

nombre = nombre.strip().lower().replace(' ','.')
apellidos = apellidos.strip().lower().replace(' ','.')
empresa = empresa.strip().lower().replace(' ','.')
dominio = dominio.strip().lower().replace(' ', '')

# General email

email = f'{nombre}{apellidos}@{empresa}{dominio}'

print(f'''
Tu nuevo email es:
{email}
''')