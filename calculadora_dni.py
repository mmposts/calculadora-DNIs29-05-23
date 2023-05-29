cantidad_letras = 23
letras = ["T","R","W","A","G","M","Y","F",
         "P","D","X","B","N","J","Z","S",
            "Q","V","H","L","C","K","E"]

def calculadora_dni(numero_dni):
    resto = numero_dni % len(letras)

    return letras[resto]
