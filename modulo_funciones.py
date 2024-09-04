'''Módulo para funciones básicas.
   Pruebe adicionando nuevas funciones en este archivo...'''
def sumar_numeros(x, y, z=None, flag=False):
    '''Función que permite sumar 2 o 3 números
    Recibe 2 parámetros obligatorios: x, y
    Recibe 2 parámetros optativos: z, flag'''
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
def es_par(numero):
    '''Función que permite validar si un número es par o impar
    Recibe 1 parámetro obligatorio: numero'''
    if numero % 2 == 0:
        return True
    else:
        return False