try:
    costat = float(input("Introdueix el costat del quadrat: "))
    if costat < 0:
        print("El costat no pot ser negatiu.")
        exit(1)
    else:
        area = costat ** 2
        print("L'àrea del quadrat és:", {area})
except ValueError:
    print("Si us plau, introdueix un número vàlid.")