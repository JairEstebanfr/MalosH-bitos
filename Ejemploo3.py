# Función para calcular el área de un rectángulo
def area_rectangulo(altura_rectangulo, base_rectangulo):
    resultado_rectangulo = altura_rectangulo * base_rectangulo
    return resultado_rectangulo

# Función para calcular el área de un triángulo
def area_triangulo(base_triangulo, altura_triangulo):
    resultado_triangulo = 0.5 * base_triangulo * altura_triangulo
    return resultado_triangulo

# Función principal
def main():
    x = 4
    y = 6
    rect_area = area_rectangulo(x, y)
    print("Área del rectángulo:", rect_area)

    base = 5
    altura = 8
    tri_area = area_triangulo(base, altura)
    print("Área del triángulo:", tri_area)

if __name__ == "__main__":
    altura_rectangulo = float(input("Ingrese altura del Rectangulo: "))
    base_rectangulo = float(input("Ingrese base del Rectangulo: "))
    Arearectangulo = area_rectangulo(altura_rectangulo, base_rectangulo)

    print(f"{altura_rectangulo} * {base_rectangulo} = {Arearectangulo}")

    base_triangulo = float(input("Ingrese base del Triangulo: "))
    altura_triangulo = float(input("Ingrese altura del Triangulo: "))
    AreaTriangulo = area_triangulo(base_triangulo, altura_triangulo)

    print(f" {0.5} * {base_triangulo} * {altura_triangulo} = {altura_triangulo}")
