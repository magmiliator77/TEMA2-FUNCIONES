#año de nacimiento y te dice si eres mayor de edad o no


def mayor_edad(year):
    if (2024-year)<18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")


nacimiento = int(input("¿Cual es tu año de nacimiento?"))

mayor_edad(nacimiento)