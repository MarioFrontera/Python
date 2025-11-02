def add(*nombres):
    return sum(nombres)

while True:
    print("\n   --- BIENVENUE ---\n")
    print("1. Ajouter une note.")
    print("2. Voir les notes.")
    print("3. Calculer la moyenne.")
    print("4. Quitter.")

    choix = input("\nVotre choix: ")

    if choix == "1":
        eleve = input("Entrez le nom de l'élève: ").lower()
        note = float(input("Entrez sa note: "))

        notes = {}

        try:
            with open("notes.txt", "r") as f:
                for ligne in f:
                    if ":" in ligne:
                        nom, notes_str = ligne.strip().split(":")
                        notes[nom] = notes_str
        except FileNotFoundError:
            pass 

        if eleve in notes:
            notes[eleve] += f" ,{note}"
            print(f"Nouvelle note ajoutée à {eleve} !")
        else:
            notes[eleve] = str(note)
            print(f"{eleve} a été ajouté avec sa note !")

        with open("notes.txt", "w") as f:
            for nom, notes_str in notes.items():
                f.write(f"{nom}:{notes_str}\n")

    elif choix == "2":
        try:
            with open("notes.txt", "r") as f:
                contenu = f.read()
                print("\n--- Liste des notes ---\n")
                print(contenu)
        except FileNotFoundError:
            print("Aucune note trouvée !")

    elif choix == "3":
        try:
            total_notes = 0
            nb_notes = 0
            with open("notes.txt", "r") as f:
                for ligne in f:
                    if ":" in ligne:
                        nom, notes_str = ligne.strip().split(":")
                        notes_list = [float(n) for n in notes_str.split(",")]
                        total_notes += sum(notes_list)
                        nb_notes += len(notes_list)

            if nb_notes > 0:
                moyenne = total_notes / nb_notes
                print(f"\nLa moyenne de toutes les notes est : {moyenne:.2f}")
            else:
                print("Aucune note enregistrée !")
        except FileNotFoundError:
            print("Aucune note trouvée !")

    elif choix == "4":
        print("Au revoir!")
        break

    else:
        print("Veuillez choisir parmi les options affichées !")
