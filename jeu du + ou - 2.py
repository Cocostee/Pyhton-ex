from random import randint
from tkinter import *

fenetre = Tk()#creation fenetre
fenetre.title("Devine le nombre")#titre
fenetre.config(bg = "#87AEAB")# couleur de fond
fenetre.geometry("1080x720") # dimension
texte = Label (fenetre, text = "Bienvenue sur le jeu du + OU -")# texte
texte.pack()

essais_max= 4 # nombre d'essais maximum
essais = 1   # nombre essais
nombre_joueur = 0   # nombre proposé par le joueur
nombre_max_ordi = 9  # nombre maximum généré par l'ordinateur
nombre_ordi = randint(0,nombre_max_ordi)   # nombre choisi par l'ordinateur

texte2 = Label (fenetre, text = "L'ordinateur a choisi un nombre entre 1 et " +str(nombre_max_ordi))
texte2.pack()

Label (fenetre, text = "Tu as 4 essais pour le trouver ").pack()
Label (fenetre, text = "A toi de jouer !").pack()

def checkInput(nombre_joueur):
    global essais, essais_max, nombre_ordi
    Label (fenetre, text = "Vous avez choisi " + str(nombre_joueur) + " :").pack()

    print(essais , essais_max)
    if nombre_ordi  != nombre_joueur and essais <= essais_max:
        Label (fenetre, text = "vous êtes au " + str(essais) + " essai.").pack()
        essais += 1
        nombre_joueur = int(nombre_joueur)
        if nombre_joueur < nombre_ordi:
            Label (fenetre, text = "Le nombre que vous avez choisi est trop petit").pack()
        elif nombre_joueur > nombre_ordi:
            Label (fenetre, text = "Le nombre que vous avez choisi est trop grand").pack()
        
    elif nombre_ordi == nombre_joueur:
        Label (fenetre, text = "Bien joué, le chiffre était bien : " + str(nombre_ordi)).pack()
    elif  essais>essais_max and nombre_joueur != nombre_ordi :
        Label (fenetre, text = "Désolé, vous avez utilisé tous vos essais. Le chiffre était " + str(nombre_ordi)).pack()

    
btn0 = Label (fenetre, text = str(0))
btn0.bind("<Button-1>", lambda e: checkInput(0))
btn0.pack()

btn1 = Label (fenetre, text = str(1))
btn1.bind("<Button-1>", lambda e: checkInput(1))
btn1.pack()

btn2 = Label (fenetre, text = str(2))
btn2.bind("<Button-1>", lambda e: checkInput(2))
btn2.pack()

btn3 = Label (fenetre, text = str(3))
btn3.bind("<Button-1>", lambda e: checkInput(3))
btn3.pack()

btn4 = Label (fenetre, text = str(4))
btn4.bind("<Button-1>", lambda e: checkInput(4))
btn4.pack()

btn5 = Label (fenetre, text = str(5))
btn5.bind("<Button-1>", lambda e: checkInput(5))
btn5.pack()

btn6 = Label (fenetre, text = str(6))
btn6.bind("<Button-1>", lambda e: checkInput(6))
btn6.pack()

btn7 = Label (fenetre, text = str(7))
btn7.bind("<Button-1>", lambda e: checkInput(7))
btn7.pack()

btn8 = Label (fenetre, text = str(8))
btn8.bind("<Button-1>", lambda e: checkInput(8))
btn8.pack()

btn9 = Label (fenetre, text = str(9))
btn9.bind("<Button-1>", lambda e: checkInput(9))
btn9.pack()


# Affichage de la fenêtre créée :
fenetre.mainloop()   