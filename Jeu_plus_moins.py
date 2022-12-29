from random import randint

essais_max= 5  # nombre d'essais maximum
essais = 1   # nombre essais
nombre_joueur = 0   # nombre du joueur au départ
nombre_max_ordi = 25  # nombre maximum généré par l'ordinateur
nombre_ordi = randint(1,nombre_max_ordi)   # nombre choisi par l'ordinateur

print("L'ordinateur a choisi un nombre entre 1 et",nombre_max_ordi, ".")
print("Vous devez le trouver en moins de 5 tentatives !")

while nombre_ordi  != nombre_joueur and essais <= essais_max:
    print("vous êtes au", essais, "essai.")
    nombre_joueur = int(input("Choisissez un nombre :"))
    if nombre_joueur < nombre_ordi:
        print("Le nombre que vous avez choisi est trop petit")
    elif nombre_joueur > nombre_ordi:
        print("Le nombre que vous avez choisi est trop grand")
    else:
        print("Félicitations ! Vous avez trouvé le nombre de l'ordinateur ","en",essais,"essai(s)")
    essais += 1

if essais>essais_max and nombre_joueur != nombre_ordi :
    print("Désolé, vous avez utilisé tous vos essais.")
    print("Vous êtes vraiment nul, réessayer jusqu'a que vous gagnez!")
    print("L'ordinateur avais choisi le nombre",nombre_ordi,".")