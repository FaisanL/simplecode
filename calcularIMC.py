def calcularIMC():
    estatura = float(input(' cuanto metros mide?: '))
    masa = int(input(' cuanto pesa?: '))
    imc = masa/(estatura*estatura)
    print(f'El imc es: {imc}')
    if imc < 18.5:
        print('estas bajo peso\nRiesgo: Alto')
    if imc > 18.5 and imc < 24.9:
        print('estas en un peso adecuado\nRiesgo: Saludable')
    if imc > 25.0 and imc < 29.9:
        print('estas en sobrepeso\nRiesgo: Aumentado')
    if imc > 30.0 and imc < 34.9:
        print('estas en Obesidad grado 1\nRiesgo: Severo')
    if imc > 35.0 and imc < 39.9:
        print('estas en Obesidad grado 2\nRiesgo: Muy Severo')
    if imc > 40.0:
        print('estas en Obesidad grado 3\nRiesgo: Ir a médico')