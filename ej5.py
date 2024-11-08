# Una funcion contar le pasamos un numero y tiene que pasar los numeros desde 0 hasta el numero que le pasemos

def contador(numero):

    for i in range(numero):
        print(i)



numero = int(input("Introduce el numero"))

contador(numero)
