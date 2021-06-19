def calcularDescuento():
    precio = int(input('ingrese el precio de su producto: '))
    descuento = precio * 0.30
    print(f'el descuento aplicado es de: {descuento}')
    ptotal = precio-descuento
    print(f'El precio total es: {ptotal}')