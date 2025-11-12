import json

def afficher():
    with open("contacts.json", "r") as f:
        data = json.load(f)
        print(data)

def ajouter(nom, telephone, email):

    with open("contacts.json", "r", newline="") as f:
        contacts = json.load(f)

    contacts.append({
        "nom": nom,
        "telephone": telephone,
        "email": email
    })

    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)
    

def supprimer(nom_a_supprimer):
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
    
    nouveaux_contacts = [c for c in contacts if c["nom"].lower() != nom_a_supprimer.lower()]

    if len(nouveaux_contacts) < len(contacts):
        print(f"Le contact {nom_a_supprimer} a été supprimé!")
    else:
        print(f"Aucun contact du nom {nom_a_supprimer} existe!")


while True:

    print("\n1. Ajouter un contact (nom, telephone et email)")
    print("2. Afficher la liste des contacts.")
    print("3. Supprimer un contact.")
    print("4. Quitter!")

    choix = input("\n")

    if choix == "1":
        nom = input("\nLe nom du contact: ")
        telephone = int(input("\nLe numèro du contact: "))
        email = input("\nLe email du contact: ")
        ajouter(nom, telephone, email)
        afficher()
        continue

    elif choix == "2":
        print("\n")
        afficher()

    elif choix == "3":
        nom = input("\nEntrez le nom du contact que vous voulez effacer: ")
        supprimer(nom)

    elif choix == "4":
        break
    
    else:
        print("\nVeuillez entrez une option parmis celles affichès")

