import time

def add(a, b):
    return a + b

def sous(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro !"

print("Bienvenue dans la calculatrice!\n")

options = ["additioner", "soustraire", "multiplier", "diviser"]

while True:
    choix = input("Vous voulez: additioner, soustraire, multiplier ou diviser?\n").lower()

    if choix in options:
        print(f"\nVous avez choisi: {choix}!\n")
        break
    else:
        print("Choix invalide, réessayez!\n")

time.sleep(1)

while True:
    try:
        a = float(input("Choisissez le nombre a: "))    
        b = float(input("Choisissez le nombre b: "))
        break
    except ValueError:
        print("Veuillez réessayer avec un nombre valide!\n")

print("Loading...")
time.sleep(2)

if choix == "additioner":
    resultat = add(a, b)

elif choix == "soustraire":
    resultat = sous(a, b)

elif choix == "multiplier":
    resultat = multi(a, b)

elif choix == "diviser":
    resultat = div(a, b)

print("\nVoici votre résultat:", resultat)
