import csv

with open("data.csv", "w", newline="") as f:
    write = csv.writer(f)
    write.writerow(["nom", "age", "note"])
    write.writerow(["Alice", 19, 12])
    write.writerow(["Bob", 22, 9])
    write.writerow(["Thomas", 18, 18])

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        nom = row[0]
        age = int(row[1])
        note = int(row[2])

        if note >= 10:
            print(f"{nom} a une note de {note} - REUSSI")
        else:
            print(f"{nom} a une note de {note} - ECHOUER")