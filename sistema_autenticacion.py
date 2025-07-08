print('*** Sistema Autenticación *** ')

# Declaramos usuario y contraseña
user = 'Judithgzzz'
psw = 'Psw1234'

# Pedimos los datos
usuario = input('Escribe tu usuario: ')
password = input('Escribe tu contraseña: ')

# Validamos datos
datos_correctos = (user == usuario.strip() and psw == password.strip())

print(f'¿Los datos son correctos?: {datos_correctos}')
