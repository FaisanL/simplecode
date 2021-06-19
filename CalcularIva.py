def iva():
    precio = int(input('ingrese el precio de su producto: '))
    iva = precio * 0.19
    print(f'el IVA de su producto es:{iva}')
    ptotal = precio+iva
    print(f'El precio total es: {ptotal}')

