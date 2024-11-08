# una funcion le pasamos una frase y cuenta cuantas vocales tiene en la frase --> pedir la frase, pasarlo a miniscula, contar vocales y mostrarlo por pantalla

def cuenta_vocales(frase):

    frase_minuscula = frase.lower()

    num__vocales = 0

    for i in frase:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            num__vocales = num__vocales + 1


    print(f'La frase tiene {num__vocales} vocales')

oracion = input("Introduce una frase: ")
cuenta_vocales(oracion)


