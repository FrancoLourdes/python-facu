
def dibujar_cuadricula(n, size):
    for i in range(n):
        print(("+" + "-" * size) * n + "+")
        for j in range(size):
            print(("|" + " " * size) * n + "|")
    print(("+" + "-" * size) * n + "+")
dibujar_cuadricula(2, 4)
