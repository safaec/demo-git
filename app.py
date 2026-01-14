# Application de démonstration
def saluer(nom):
    return f"Bonjour {nom} ! Welcome !"


print(saluer("World"))

def additionner(a, b):
    return a + b


print(additionner(5, 3))


<<<<<<< HEAD
def multiplier(a, b):
    return a * b


print(multiplier(4, 7))



=======
def diviser(a, b):
    if b == 0:
        return "Erreur: division par zéro"
    return a / b


print(diviser(10, 2))
>>>>>>> feature/division
