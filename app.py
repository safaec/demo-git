# Application de démonstration
def saluer(nom):
    return f"Hello {nom}!"


print(saluer("World"))

def additionner(a, b):
    return a + b


print(additionner(5, 3))


def diviser(a, b):
    if b == 0:
        return "Erreur: division par zéro"
    return a / b


print(diviser(10, 2))
