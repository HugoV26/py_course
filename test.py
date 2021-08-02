print("Let's Code")

def dividir(div, divisor):
    try:
        res = div / divisor
        return res
    except MiPropiaExcepción:
        print("Error")
        #raise ZeroDivisionError("El divisor no puede ser cero")

dividir(5, 0)