def line():
    import math
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    x1 = float(input("Ingrese el valor de X1: "))
    x2 = float(input("Ingrese el valor de X2: "))
    print(f"\n--- Datos Ingresados ---")
    print(f"Coeficiente A: {a}")
    print(f"Coeficiente B: {b}")
    print(f"Valor de X1: {x1}")
    print(f"Valor de X2: {x2}")
    y1 = a * x1 + b
    y2 = a * x2 + b
    print(f"\n--- Ecuación de la Recta ---")
    print(f"Y = {a}X + {b}")
    print(f"\n--- Puntos Calculados ---")
    print(f"P1 = ({x1}, {y1})")
    print(f"P2 = ({x2}, {y2})")
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"\n--- Distancia entre P1 y P2 ---")
    print(f"{distancia}")
line()
