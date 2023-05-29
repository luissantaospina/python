import library as lb


def run_convert_pesos_to_dollars(trm: float) -> None:
    pesos = int(input('Ingrese la cantidad de pesos a convertir: '))
    print(pesos, ' pesos son ', round(lb.convert_pesos_to_dollars(trm, pesos), 2), 'dolares')
    init()


def run_convert_dollars_to_pesos(trm: float) -> None:
    dollars = float(input('Ingrese la cantidad de dolares a convertir: '))
    print(dollars, ' dolares son', int(lb.convert_dollars_to_pesos(trm, dollars)), 'pesos')
    init()


def init():
    mode = int(input('Digite 1 para convertir de pesos a dolares o digite 2 para convertir de dolares a pesos: '))
    if mode == 1:
        trm = float(input('Ingrese la TRM: '))
        run_convert_pesos_to_dollars(trm)
    elif mode == 2:
        trm = float(input('Ingrese la TRM: '))
        run_convert_dollars_to_pesos(trm)
    else:
        print('Opción no valida')
        init()


init()
