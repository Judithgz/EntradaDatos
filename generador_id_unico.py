from random import randint

print("*** Sistema Generador de ID Unico ***")


nombre = input('Nombre: ')
apellido = input('Apellido: ')
nacimiento = input('Año de nacimiento (YYYY): ')


#  Normalizar los valores
nombre2 = nombre.strip().upper()[0:2]
apellido2 = apellido.strip().upper()[0:2]
nacimiento2 = nacimiento.strip()[2:] # Tambien puede ser [2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el valor d eid unico
id_unico = f'{nombre2}{apellido2}{nacimiento2}{aleatorio}'

print(f'''\n Hola {nombre},
            Tu nuevo numero de identificacion (ID) generado por el sistema es:
            {id_unico}
            Felicidades!''')
