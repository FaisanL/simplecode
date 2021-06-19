import calcularIMC as fn, calcularDescuento as cd, CalcularIva as ci
opcion = 0
while opcion != 5:  
    if(opcion == 1):
        print('elegiste calcular IMC')
        fn.calcularIMC()
    if(opcion == 2):
        print('elegiste calcular descuentos')
        cd.calcularDescuento()     
    if(opcion == 3):
        print('elegiste calcular IVA')
        ci.iva()
    if(opcion == 4):
        print('Vuelva pronto')
        break
    try:
        opcion = int(input("Ingrese la opción\n1.-Calcular IMC\n2.-Calcular Descuento\n3.-Calcular IVA\n4.-Salir\n:")) 
    except:
        print('opción invalida')
        opcion = 0
