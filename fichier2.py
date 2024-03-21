import numpy as np

def resolveEquation(x2=0, x1=0, x0=0):
    rSolve = None
    discriminant = np.power(x1, 2) - 4 * x2 * x0
    if discriminant == 0:
        rSolve = -x1 / (2.0 * x2)
    elif discriminant > 0:
        rSolve = ((-x1 - np.sqrt(discriminant)) / (2.0 * x2),
                  (-x1 + np.sqrt(discriminant)) / (2.0 * x2))
    return rSolve

def PGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


result = resolveEquation(1, -3, 2)
print("Solutions de l'équation:", result)

a = 48
b = 18
pgcd = PGCD(a, b)
print("PGCD de", a, "et", b, ":", pgcd)
# Ceci est un joli commentaire très utile
