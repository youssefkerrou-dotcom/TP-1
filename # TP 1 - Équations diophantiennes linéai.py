
def pgcd(a, b):
    """Calcule le PGCD de deux entiers en affichant les étapes de l'algorithme d'Euclide."""
    print("\n--- Étapes du calcul du PGCD ---")
    while b != 0:
        q = a // b
        r = a % b
        print(f"{a} = {b} × {q} + {r}")
        a, b = b, r
    print(f"→ Le PGCD est {a}\n")
    return a

def euclide_etendu(a, b):
    """
    Retourne (d, x0, y0) tels que :
    a·x0 + b·y0 = d = pgcd(a, b)
    (Théorème de Bézout)
    """
    if b == 0:
        return (a, 1, 0)
    else:
        d, x1, y1 = euclide_etendu(b, a % b)
        return (d, y1, x1 - (a // b) * y1)


a = int(input("Entrer a : "))
b = int(input("Entrer b : "))
c = int(input("Entrer c : "))

d = pgcd(a, b)


d, x0, y0 = euclide_etendu(a, b)
print("--- Théorème de Bézout ---")
print(f"Il existe des entiers x₀ et y₀ tels que :")
print(f"{a}·({x0}) + {b}·({y0}) = {d}")


if c % d != 0:
    print("\n→ Pas de solution entière (d ne divise pas c).")
else:
    print("\n→ Il existe des solutions entières à l’équation ax + by = c.")

   
    x_p = x0 * (c // d)
    y_p = y0 * (c // d)
    print(f"\nSolution particulière : x = {x_p}, y = {y_p}")

    print("\nSolution générale :")
    print(f"(x, y) = ({x_p} + {b//d}·k, {y_p} - {a//d}·k),   k ∈ ℤ")

print("\n--------------------------------------------")
print("Fin du programme – TP1 Équations Diophantiennes (EST Kénitra)")
print("--------------------------------------------")
