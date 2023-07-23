# Las funciones para las operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

# Menu de las opciones
# Sí quieres puedes sacarle el while True para que no repita infinitamente
while True:
    print('[+]. Suma')
    print('[-]. Resta')
    print('[x]. Multiplicación')
    print('[/]. Dividisión')

# Datos 
    opcion = input('Ingrese la opción _[+,-,x,/]_: ')
    num1 = float(input('Ingrese el primer numero: '))
    num2 = float(input('Ingrese el segundo numero: '))

# Ahora realizara la operacion selecionada
    if opcion == '+':
        print(num1, '+', num2, '=', suma(num1,num2))

    elif opcion == '-':
        print(num1, '-', num2, '=', resta(num1,num2))

    elif opcion == 'x':
        print(num1, '*', num2, '=', multiplicacion(num1,num2))

    elif opcion == '/':
        print(num1, '/', num2, '=', division(num1,num2))
    else:
        print('Opcion inválida.')

#Fin