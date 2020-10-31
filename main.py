def calculadora(a=1,b=1,c=1):
  if c == 1:
    suma = a+b
    print('La suma de los numeros es',suma)
  elif c == 2:
    resta = a-b
    print('La resta de los numeros es',resta)
  else:
    print('Opcion invalida')


print('Calculadora basica')
numero1 = int(input('Digite un numero '))
numero2 = int(input('Digite otro numero '))
opcion = int(input('Digite (1) para suma y (2) para resta '))

calculadora(numero1,numero2,opcion)
calculadora(1,2)
