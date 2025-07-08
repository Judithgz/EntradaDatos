print('** Operadores de asignacion compuestos ***')
a,b = 10, 15
print(f'Valor inicial a: {a}, b: {b}')

# Operador compuesto de suma +=
a += b  # --> a = a + b
print(f'Operador de a += b es: {a}')

# Operador compuesto de resta -=
a = 10  # reiniciamos la variable a
a -= b # --> a = a - b
print(f'Operador a -= b es: {a}')


# Operador compuesto de multiplicacion *=
a = 10  # reiniciamos el valor
a *= b
print(f'Operador de a *= b es: {a}')


# Operador compuesto de division /=
a = 10
a /= b
print(f'Operador de a /=b es: {a}')
print(f'Operador de a /=b es: {a:.2f}')
