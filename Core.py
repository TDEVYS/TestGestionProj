'voici la premire pierre à mon grand projet qui sera de dominer la monde des aspirateurs robots'

import numpy as np

def est_premier(n):
    if n == 2:
        return True
    elif n > 2 and n % 2 != 0:
        diviseur = 3
        while diviseur <= np.sqrt(n):
            if n % diviseur == 0:
                return False
            diviseur += 2
        return True
    else:
        return False

nombre = int(input("Entrez un nombre pour vérifier s'il est premier : "))
if est_premier(nombre):
    print(f"{nombre} est un nombre premier.")
else:
    print(f"{nombre} n'est pas un nombre premier.")

'nous n''utilisons pas le critere de Hermocrate' 