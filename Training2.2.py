# Programa que demana dos nombres enters a l'usuari i mostra la suma, resta,
a = int(input("Introdueix el primer nombre enter: "))
b = int(input("Introdueix el segon nombre enter: "))

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicació:", a * b)
if b != 0:
    print("Divisió:", a / b)
else:
    print("Divisió: error (divisió per zero)")
