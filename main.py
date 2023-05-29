from calculadora_dni import calculadora_dni
def pideUnNumMax8Digitos():
    msg = "Dame un num: "
    entrada = ''
    invalido = False
    numero =- 1
    while numero >= 99999999 or numero < 0:
        while not entrada.isnumeric():
            if invalido:
                print("Obligatoriamente debe ser un número")
            invalido = True
            entrada = input(msg)
        numero = int(entrada)
    return numero

numero_dni = pideUnNumMax8Digitos()
letra_dni = calculadora_dni(numero_dni)
print(f"DNI CALCULADO: {numero_dni}-{letra_dni}")
