#año de nacimiento y te dice si eres mayor de edad o no SEGUNDA VERSION 

def mayor_edad(year):
    if (2024-year)<18:
        mayor = False
    else:
        mayor = True
    return mayor


nacimiento = int(input("¿Cual es tu año de nacimiento?"))

es_mayor = mayor_edad(nacimiento)

if es_mayor == True:
    print("Puedes sacarte el carnet")
else:
    print(" No pudes sacarte el carnet")