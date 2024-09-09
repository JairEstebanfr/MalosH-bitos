def Operacion(Numero01, Numero02, Numero03):
    resultado = Numero01 * Numero02 + Numero03
    return resultado

if __name__ == "__main__":
    Numero01 = float(input("Ingrese Multiplicando: "))
    Numero02 = float(input("Ingrese Multiplicador: "))
    Numero03 = float(input("Ingrese el Sumando: "))
    resultado = Operacion(Numero01, Numero02, Numero03)
    print(f"{Numero01} * {Numero02} + {Numero03}= {resultado}")

