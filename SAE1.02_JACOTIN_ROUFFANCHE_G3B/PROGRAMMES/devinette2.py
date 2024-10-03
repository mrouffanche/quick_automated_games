import random

def meilleur_essai(min:int,max:int) -> int:
    #Cette fonction permet d'attribuer le meilleur coup à jouer au BOT au jeu des devinettes.
    #Elle prend en paramètre le minimum et le maximum de l'intervale choisit pour la difficulté du jeu.
    #Elle renvoie un entier étant le meilleur coup à jouer.

    meilleur_essai=(min+max)//2
    return meilleur_essai

def ajouter_points(nom_utilisateur:str, points:int):
    #Cette procédure permet d'attribuer des points si le joueur gagne une partie de mini-jeux
    #Elle prend en entrée le nom de l'utilisateur ayant gagné (chaîne de caractères) ainsi que le nombre de points à attribuer étant un entier
    scores : list[tuple[str, int]]
    scores = []
    # Lire le fichier et obtenir une liste des noms d'utilisateurs et des scores
    with open("score.txt", "rb") as f:
        for ligne in f:
            nom, score = ligne.decode('utf-8').strip().split(":")
            scores.append((nom, int(score)))
    # Rechercher le joueur et ajouter les points
    for i, (nom, score) in enumerate(scores):
        if nom == nom_utilisateur:
            scores[i] = (nom, score + points)
    # Écrire les scores mis à jour dans le fichier
    with open("score.txt", "wb") as f:
        for nom, score in scores:
            ligne = f"{nom}:{score}\n"
            f.write(ligne.encode('utf-8'))
    return points


def choisir_difficulte() -> str:
    #Cette fonction permet de choisir la difficulté du jeu des devinettes.
    #Elle ne prend rien en entrée mais elle prend en sortie une chaîne de caractères étant la difficulté choisie.

    print("Choisissez le niveau de difficulté :")
    print("1. Facile (nombre entre 1 et 50)")
    print("2. Moyen (nombre entre 1 et 100)")
    print("3. Difficile (nombre entre 1 et 150)")
    choix = input("Entrez le numéro de votre choix : ")

    if choix == "1":
        return "facile"
    elif choix == "2":
        return "moyen"
    elif choix == "3":
        return "difficile"
    else:
        print("Choix invalide. Niveau par défaut : Facile.")
        return "facile"
    
def verif_interval(n:int,difficulte:str)-> bool:
    #Cette fonction permet de vérifier l'intervale découlant de la difficulté choisie.
    #Elle prend en paramètre un entier "n" ainsi que la difficulté étant une chaîne de caractères.
    #Elle renvoie un booléen permettant de vérifier si le le nombre choisit "n" est compris dans l'intervale de la difficulté choisie.

    verifinter : bool
    verifinter = False
    if difficulte == "facile":
        if n<50:
            verifinter=True
    elif difficulte == "moyen":
        if n<100:
            verifinter=True
    elif difficulte == "difficile":
        if n<150:
            verifinter=True
    else :
        verifinter=False
    return verifinter



def devinette(pseudo1:str,pseudo2:str,mode:str,choix_bot:int)->int:
    #Cette fonction permet de jouer au jeu des devinettes.
    #Elle prend en paramètre d'entrée le pseudo des deux joueurs étant des chaînes de caractères, le mode de jeu choisit pour le BOT étant une chaîne de caractères, ainsi que les choix du BOT étant un entier.
    #Elle prend en paramètre de sortie un entier étant le nombre de points à attribuer en cas de victoire à tel ou tel joueur.

    n : int
    essai : int
    reponse_auto : str
    compteur : int
    devine : str
    controlleur : str
    max:int
    max=0
    min:int
    min=0
    max_dif:int
    i : int
    i = 1
    points_bot:int
    points_bot=0
    difficulte:str
    # choix joueur :
    controlleur = ""

    if mode=="jcj":
        devine = input("Qui devra deviner le nombre ? "+ pseudo1 + ' ou '+ pseudo2 +' : ')
        while devine != pseudo1 and devine != pseudo2:    
            devine = input('Qui devra deviner le nombre ?'+ pseudo1 + ' ou '+ pseudo2 +' : ')



        if devine == pseudo1 :
            controlleur = pseudo2
        elif devine == pseudo2:
            controlleur = pseudo1
        else : 
            print("erreur")



        # programme devinette :
        difficulte=choisir_difficulte()

        n = int(input(controlleur + " : saisir le nombre à deviner : "))
        while n <= 0 or not verif_interval(n, difficulte):
            n = int(input('Nombre à deviner invalide. Veuillez saisir un nombre strictement supérieur à 0 et correspondant à la difficulté : '))

        for compteur in range (0,1000):
            print('/')
            compteur += 1
        essai=-1
        while essai <=0 :
            essai = int(input(devine +' : saisir votre réponse : '))
        while essai != n :
            i +=1
            print(essai)
            if essai < n :
                reponse_auto = 'trop petit'
                reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                while reponse != reponse_auto :
                    print(controlleur , " : erreur, réponse incorrecte : ")
                    reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                print("trop petit")
                essai = int(input(devine +' : saisir votre réponse : '))

            if essai > n :
                reponse_auto = 'trop grand'
                reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                while reponse != reponse_auto :
                    print(controlleur , " : erreur, réponse incorrecte : ")
                    reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                print("trop grand")
                essai = int(input("saisir réponse : "))

        if n == essai :
            reponse_auto = "c'est gagné"
            reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
            while reponse != reponse_auto :
                print(controlleur , " : erreur, réponse incorrecte : ")
                reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
            print("c'est gagné ! au bout de ", i, " essais")
            if i <= 2 :
                ajouter_points(devine,10)

            elif i <= 4 :
                ajouter_points(devine,8)
                ajouter_points(controlleur, 2)

            elif i <= 6 :
                ajouter_points(devine,6)
                ajouter_points(controlleur, 4)

            elif i <= 8 :
                ajouter_points(devine,4)
                ajouter_points(controlleur, 6)

            elif i <= 10 :
                ajouter_points(devine,2)
                ajouter_points(controlleur, 8)

            else :
                ajouter_points(controlleur, 10)
    elif mode=="jco":
        devine = input("Qui devra deviner le nombre ? "+ pseudo1 + ' ou '+ pseudo2 +' : ')
        while devine != pseudo1 and devine != pseudo2:    
            devine = input('Qui devra deviner le nombre ?'+ pseudo1 + ' ou '+ pseudo2 +' : ')



        if devine == pseudo1 :
            controlleur = pseudo2
        elif devine == pseudo2:
            controlleur = pseudo1
        else : 
            print("erreur")



        # programme devinette :
        difficulte=choisir_difficulte()
        if difficulte=="facile":
            max=50
        elif difficulte=="moyen":
            max=100
        else: 
            max=150
        max_dif=max
        if controlleur==pseudo2:
            n = random.randint(1,max-1)

            for compteur in range (0,1000):
                print('/')
                compteur += 1
            essai=-1
            while essai <=0 :
                essai = int(input(devine +' : saisir votre réponse : '))
            while essai != n :
                i +=1
                if essai < n :
                    reponse_auto = 'trop petit'
                    print(reponse_auto)
                    essai = int(input(devine +' : saisir votre réponse : '))

                if essai > n :
                    reponse_auto = 'trop grand'
                    print(reponse_auto)
                    essai = int(input(devine +' : saisir votre réponse : '))

            if n == essai :
                reponse_auto = "c'est gagné"
                print(reponse_auto)
                print("c'est gagné ! au bout de ", i, " essais")

            if i <= 2 :
                ajouter_points(devine,10)

            elif i <= 4 :
                ajouter_points(devine,8)
                points_bot=2

            elif i <= 6 :
                ajouter_points(devine,6)
                points_bot=4

            elif i <= 8 :
                ajouter_points(devine,4)
                points_bot=6

            elif i <= 10 :
                ajouter_points(devine,2)
                points_bot=8

            else :
                points_bot=10

            return points_bot


        else:

            n = int(input(controlleur + " : saisir le nombre à deviner : "))
            while n <= 0 or not verif_interval(n, difficulte):
                n = int(input('Nombre à deviner invalide. Veuillez saisir un nombre strictement supérieur à 0 et correspondant à la difficulté : '))

            for compteur in range (0,1000):
                print('/')
                compteur += 1
            essai=-1
            while essai <=0 :
                if devine == "WALL-E":
                    hasard = random.randint(0,10)
                    if hasard == 1:
                        essai = meilleur_essai(min,max)
                    else:
                        essai = random.randint(min,max)
                elif devine == "R2D2":
                    hasard = random.randint(1,2)
                    if hasard == 1:
                        essai = meilleur_essai(min,max)
                    else:
                        essai= random.randint(min,max)
                elif devine == "TERMINATOR":
                    essai = meilleur_essai(min,max)
                print(essai)
            while essai != n :
                i +=1
                if essai < n :
                    reponse_auto = 'trop petit'
                    reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                    while reponse != reponse_auto :
                        print(controlleur , " : erreur, réponse incorrecte : ")
                        reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                    print("trop petit")

                    min=essai
                    if devine == "WALL-E":

                            essai = random.randint(min,max_dif)
                    elif devine == "R2D2":
                        hasard = random.randint(1,2)
                        if hasard == 1:
                            essai = meilleur_essai(min,max)
                        else:
                            essai= random.randint(min,max)
                    elif devine == "TERMINATOR":
                        essai = meilleur_essai(min,max)
                    print(essai)

                elif essai > n :
                    reponse_auto = 'trop grand'
                    reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                    while reponse != reponse_auto :
                        print(controlleur , " : erreur, réponse incorrecte : ")
                        reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                    max=essai
                    print("trop grand")
                    if devine == "WALL-E":
                            essai = random.randint(min,max_dif)
                    elif devine == "R2D2":
                        hasard = random.randint(1,2)
                        if hasard == 1:
                            essai = meilleur_essai(min,max)
                        else:
                            essai= random.randint(min,max)
                    elif devine == "TERMINATOR":
                        essai = meilleur_essai(min,max)
                    print(essai)


            if n == essai :
                reponse_auto = "c'est gagné"
                reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                while reponse != reponse_auto :
                    print(controlleur , " : erreur, réponse incorrecte : ")
                    reponse = input(controlleur + " : trop petit, trop grand ou c'est gagné ? :")
                print("c'est gagné ! au bout de ", i, " essais")
            if i <= 2 :
                points_bot=10

            elif i <= 4 :
                points_bot=8
                ajouter_points(controlleur, 2)

            elif i <= 6 :
                points_bot=6
                ajouter_points(controlleur, 4)

            elif i <= 8 :
                points_bot=4
                ajouter_points(controlleur, 6)

            elif i <= 10 :
                points_bot=2
                ajouter_points(controlleur, 8)

            else :
                ajouter_points(controlleur, 10)
        return points_bot

    elif mode == "oco":
        devine = input("Qui devra deviner le nombre ? "+ pseudo1 + ' ou '+ pseudo2 +' : ')
        while devine != pseudo1 and devine != pseudo2:    
            devine = input('Qui devra deviner le nombre ?'+ pseudo1 + ' ou '+ pseudo2 +' : ')


        if devine == pseudo1 :
            controlleur = pseudo2
        elif devine == pseudo2:
            controlleur = pseudo1
        else : 
            print("erreur")


        # programme devinette :
        difficulte=choisir_difficulte()
        if difficulte=="facile":
            max=50
        elif difficulte=="moyen":
            max=100
        else: 
            max=150
        max_dif=max
        if controlleur==pseudo2 or controlleur==pseudo1:
            n = random.randint(1,max-1)
            print(controlleur,"a choisit le nombre",n)

            essai=-1
            while essai <=0 :
                essai = meilleur_essai(min,max)
            while essai != n :
                i +=1
                print(essai)


                if essai < n :
                    reponse_auto = 'trop petit'
                    print(reponse_auto)
                    min=essai
                    if devine == "WALL-E-1" or devine == "WALL-E-2":
                        essai = random.randint(min,max_dif)
                    elif devine == "R2D2-1" or devine == "R2D2-2":
                        hasard = random.randint(1,2)
                        if hasard == 1:
                            essai = meilleur_essai(min,max)
                        else:
                            essai= random.randint(min,max)
                    elif devine == "TERMINATOR-1" or devine == "TERMINATOR-2":
                        essai = meilleur_essai(min,max)

                elif essai > n :
                    reponse_auto = 'trop grand'
                    print(reponse_auto)
                    max=essai
                    if devine == "WALL-E-1" or devine == "WALL-E-2":
                        essai = random.randint(min,max_dif)
                    elif devine == "R2D2-1" or devine == "R2D2-2":
                        hasard = random.randint(1,2)
                        if hasard == 1:
                            essai = meilleur_essai(min,max)
                        else:
                            essai= random.randint(min,max)
                    elif devine == "TERMINATOR-1" or devine == "TERMINATOR-2":
                        essai = meilleur_essai(min,max)


                input("Appuyez sur ENTRER pour passer au tour suivant")

            if n == essai :
                print(essai)
                reponse_auto = "c'est gagné"
                print(reponse_auto)
                print("c'est gagné ! au bout de ", i, " essais")

            if i <= 2 :
                points_bot=10

            elif i <= 4 :
                points_bot=8

            elif i <= 6 :
                points_bot=6

            elif i <= 8 :
                points_bot=4

            elif i <= 10 :
                points_bot=2


    return(points_bot)