import random

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
            break

    # Écrire les scores mis à jour dans le fichier
    with open("score.txt", "wb") as f:
        for nom, score in scores:
            ligne = f"{nom}:{score}\n"
            f.write(ligne.encode('utf-8'))



def pile_ou_face(pseudo1: str, pseudo2: str) -> str:
    #Cette fonction permet de choisir qui commencera la partie de manière aléatoire
    #Elle prend en entrée les deux pseudos des deux joueurs étant des chaînes de caractères
    #Elle renvoie une chaîne de caractères étant le pseudo qui commence la partie

    resultat = random.choice([pseudo1, pseudo2])
    return resultat




def est_present(liste: list[int], sous_liste: list[int]) -> bool:
    #Cette fonction permet de dire si une case est occupée ou non.
    #Elle prend en paramètre la grille du jeu composée de liste (liste d'entiers) ainsi que de sous_liste (liste d'entiers).
    #Elle renvoie un booléen signifiant s'il y a une valeur ou non.

    for valeur in sous_liste:
        if valeur not in liste:
            return False
    return True




def grille(choix: int, case1 : str, case2: str, case3:str, case4:str, case5:str, case6:str, case7:str, case8 : str, case9 :str) :
            #Cette procédure permet d'afficher la grille du jeu du morpion.
            #Elle prend en paramètre le choix de l'utilisateur étant un entier (1 à 9) ainsi que les différentes cases de la grille étant des chaînes de caractères.

            print("_____________")
            print("|",case1,"|",case2,"|",case3,"|")
            print("|_1_|_2_|_3_|")

            print("|",case4,"|",case5,"|",case6,"|")
            print("|_4_|_5_|_6_|")

            print("|",case7,"|",case8,"|",case9,"|")
            print("|_7_|_8_|_9_|")


def meilleur_coup(cases_player: list[int], cases_adversaires: list[int], cases: list[int]):
    #Cette procédure permet de chercher le meilleur coup possible pour le BOT !
    #Il prend en paramètre les cases du joueur, celles de l'adversaires ainsi que les cases encore disponibles. Les trois étant des listes d'entiers

    #cherche le meilleur coup possible pour le bot
    i: int
    i = 0
    meilleur_coup: int
    meilleur_coup = 1

    #le troisième meilleur coup est un coup qui prépare un double attaque, que l'adversaire ne pourra pas parer

    if 5 not in cases_adversaires and 5 not in cases_player:
        meilleur_coup=5
    if cases_adversaires==[] and 1 not in cases_player:
        meilleur_coup=1
    elif cases_adversaires==[2] or cases_adversaires==[3] and 7 not in cases_adversaires and 7 not in cases_player: 
        meilleur_coup=7
    elif cases_adversaires==[4] or cases_adversaires==[7] or cases_adversaires==[8] or cases_adversaires==[6] or cases_adversaires==[9] or cases_adversaires==[5] and 3 not in cases_adversaires and 3 not in cases_player:
        meilleur_coup=3
    elif cases_adversaires==[2,9] and 7 not in cases_adversaires and 7 not in cases_player:
        meilleur_coup=7
    elif cases_adversaires==[2,6] or cases_adversaires==[2,8] and 5 not in cases_adversaires and 5 not in cases_player:
        meilleur_coup=5
    elif 5 in cases_player and 9 not in cases_adversaires and 9 not in cases_player:
        meilleur_coup=9
    elif meilleur_coup in cases_player or meilleur_coup in cases_adversaires:
        meilleur_coup=random.choice(cases)
        

    
    #le deuxième meilleur coup est d'empecher le deuxième adversaire de gagner
            
    for i in cases:
        temp = cases_adversaires[:]
        temp.append(i)
        if victoire_solo(temp):
            meilleur_coup = i


    for i in cases:
        temp = cases_player[:]  
        temp.append(i)
        # le meilleur coup est celui qui te fait gagner
        if victoire_solo(temp):
            meilleur_coup = i



    return meilleur_coup







def victoire_solo(cases_joueurs:list[int]) -> bool:
    #Cette fonction permet de vérifier s'il y a une victoire au cours de la partie.
    #Elle prend en paramètre les différentes cases utilisées (liste d'entiers).
    #Elle renvoie un booléen permettant de dire s'il y a victoire ou non.

    win : bool
    win = False
    victoire1 = [1, 2, 3]
    victoire2 = [1, 4, 7]
    victoire3 = [1, 5, 9]
    victoire4 = [2, 5, 8]
    victoire5 = [3, 6, 9]
    victoire6 = [4, 5, 6]
    victoire7 = [3, 5, 7]
    victoire8 = [7, 8, 9]
    
    if est_present(cases_joueurs, victoire1) or est_present(cases_joueurs, victoire2) or est_present(cases_joueurs, victoire3) or est_present(cases_joueurs, victoire4) or est_present(cases_joueurs, victoire5) or est_present(cases_joueurs, victoire6) or est_present(cases_joueurs, victoire7) or est_present(cases_joueurs, victoire8):
        win = True

    return win

def victoire(cases_player1: list[int], cases_player2: list[int]) -> bool:
    #Cette fonction permet de vérifier s'il y a une victoire au cours de la partie.
    #Elle prend en paramètre les différentes cases utilisées de tous les joueurs (player 1 et 2) étant des listes d'entiers.
    #Elle renvoie un booléen permettant de dire s'il y a victoire ou non.

    win : bool
    win = False
    victoire1 = [1, 2, 3]
    victoire2 = [1, 4, 7]
    victoire3 = [1, 5, 9]
    victoire4 = [2, 5, 8]
    victoire5 = [3, 6, 9]
    victoire6 = [4, 5, 6]
    victoire7 = [3, 5, 7]
    victoire8 = [7, 8, 9]
    
    if est_present(cases_player1, victoire1) or est_present(cases_player1, victoire2) or est_present(cases_player1, victoire3) or est_present(cases_player1, victoire4) or est_present(cases_player1, victoire5) or est_present(cases_player1, victoire6) or est_present(cases_player1, victoire7) or est_present(cases_player1, victoire8):
        win = True
    
    if est_present(cases_player2, victoire1) or est_present(cases_player2, victoire2) or est_present(cases_player2, victoire3) or est_present(cases_player2, victoire4) or est_present(cases_player2, victoire5) or est_present(cases_player2, victoire6) or est_present(cases_player2, victoire7) or est_present(cases_player2, victoire8):
        win = True

    return win



def morpion(pseudo1: str, pseudo2: str, mode:str, choix_bot:int):
    #Cette fonction permet de jouer au jeu du morpion.
    #Elle prend en paramètre les pseudos des deux joueurs étant des chaînes de caractères, le mode de jeu étant une châine de caractères, ainsi que les choix des bots étant des entiers.
    #Elle renvoie un entier étant les points à attribuer. 0 en cas de match nul ou le nombre de points nécéssaires à attribuer.
    
    points_bot:int
    points_bot=0

    points_bot=0
    if mode == "jcj":
        cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        case_player1: list[int] = []
        case_player2: list[int] = []


        case1 = case2 = case3 = case4 = case5 = case6 = case7 = case8 = case9 = " "


        print("_____________")
        print("|   |   |   |")
        print("|_1_|_2_|_3_|")
        print("|   |   |   |")
        print("|_4_|_5_|_6_|")
        print("|   |   |   |")
        print("|_7_|_8_|_9_|")

        player = pile_ou_face(pseudo1,pseudo2)
        print(player, "à toi de commencer")
        if player == pseudo1:
            player = pseudo2
        else:
            player = pseudo1

        while not victoire(case_player1, case_player2) and len(cases) > 0:
            if player == pseudo1:
                player = pseudo2
            else:
                player = pseudo1
        
            liste_cases = str(cases)
            choix = int(input(player + " Saisir la case que vous voulez cibler : " + liste_cases))

            while choix not in cases:
                print("Saisie incorrecte")
                choix = int(input(player + " Saisir la case que vous voulez cibler : " + liste_cases))

            if player == pseudo1:
                case = "X"
            else:
                case = "O"

            if choix in cases:
                if choix == 1:
                    case1 = case
                elif choix == 2:
                    case2 = case
                elif choix == 3:
                    case3 = case
                elif choix == 4:
                    case4 = case
                elif choix == 5:
                    case5 = case
                elif choix == 6:
                    case6 = case
                elif choix == 7:
                    case7 = case
                elif choix == 8:
                    case8 = case
                elif choix == 9:
                    case9 = case

                grille(choix, case1, case2, case3, case4, case5, case6, case7, case8, case9)

                if player == pseudo1:
                    case_player1.append(choix)
                else:
                    case_player2.append(choix)

                cases.remove(choix)

        if victoire(case_player1, case_player2):
            print(player, "a gagné")
            ajouter_points(player,10)
            if player == pseudo1 :
                player=pseudo2
            else :
                player=pseudo1
            print(player,'a perdu')



        else:
            print("Match nul")
        return 0
    
    elif mode == "jco" :
        cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        case_player1: list[int] = []
        case_player2: list[int] = []

        case1 = case2 = case3 = case4 = case5 = case6 = case7 = case8 = case9 = " "


        print("_____________")
        print("|   |   |   |")
        print("|_1_|_2_|_3_|")
        print("|   |   |   |")
        print("|_4_|_5_|_6_|")
        print("|   |   |   |")
        print("|_7_|_8_|_9_|")

        player = pile_ou_face(pseudo1,pseudo2)
        print(player, "à toi de commencer")
        if player == pseudo1:
            player = pseudo2
        else:
            player = pseudo1

        while not victoire(case_player1, case_player2) and len(cases) > 0:
            if player == pseudo1:
                player = pseudo2
            else:
                player = pseudo1

            if player == pseudo1 :

                liste_cases = str(cases)
                choix = int(input(player + " Saisir la case que vous voulez cibler : " + liste_cases))
                while choix not in cases:
                    print("Saisie incorrecte")
                    choix = int(input(player + " Saisir la case que vous voulez cibler : " + liste_cases))
            
            else: 
                print("tour de l'ordi",player)
                if choix_bot == 1 :
                    hasard=random.randint(1, 2)
                    if hasard == 1 :
                        choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                    else:
                        choix=random.choice(cases)
                elif choix_bot == 2 :
                    hasard=random.randint(1, 10)
                    if hasard ==1 or hasard==2 or hasard==3 :
                        choix=random.choice(cases)                    
                    else:
                        choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                else:
                    choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)

            if player == pseudo1:
                case = "X"
            else:
                case = "O"

            if choix in cases:
                if choix == 1:
                    case1 = case
                elif choix == 2:
                    case2 = case
                elif choix == 3:
                    case3 = case
                elif choix == 4:
                    case4 = case
                elif choix == 5:
                    case5 = case
                elif choix == 6:
                    case6 = case
                elif choix == 7:
                    case7 = case
                elif choix == 8:
                    case8 = case
                elif choix == 9:
                    case9 = case

                grille(choix, case1, case2, case3, case4, case5, case6, case7, case8, case9)

                if player == pseudo1:
                    case_player1.append(choix)
                else:
                    case_player2.append(choix)
                
                cases.remove(choix)

        if victoire(case_player1, case_player2):
            print(player, "a gagné")
            ajouter_points(player,10)
            if player == pseudo1 :
                ajouter_points(player,10)
            else :
                points_bot+=10
            if player == pseudo1 :
                player=pseudo2
            else :
                player=pseudo1
            print(player,'a perdu')

            return points_bot

            


        else:
            print("Match nul")
            return 0

    elif mode == "oco":
        cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        case_player1: list[int] = []
        case_player2: list[int] = []

        case1 = case2 = case3 = case4 = case5 = case6 = case7 = case8 = case9 = " "


        print("_____________")
        print("|   |   |   |")
        print("|_1_|_2_|_3_|")
        print("|   |   |   |")
        print("|_4_|_5_|_6_|")
        print("|   |   |   |")
        print("|_7_|_8_|_9_|")

        player = pile_ou_face(pseudo1,pseudo2)
        print(player, "à toi de commencer")
        if player == pseudo1:
            player = pseudo2
        else:
            player = pseudo1

        while not victoire(case_player1, case_player2) and len(cases) > 0:
            if player == pseudo1:
                player = pseudo2
            else:
                player = pseudo1

            if player == pseudo1:
                print("tour de l'ordi",player)
                if player == "WALL-E-1" or player == "WALL-E-2" :
                    hasard=random.randint(1, 2)
                    if hasard == 1 :
                        choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                    else:
                        choix=random.choice(cases)
                elif player == "R2D2-1" or player == "R2D2-2" :
                    hasard=random.randint(1, 10)
                    if hasard ==1 or hasard==2 or hasard==3 :
                        choix=random.choice(cases)                    
                    else:
                        choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                elif player == "TERMINATOR-1" or player == "TERMINATOR-2":
                    choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                else:
                    choix=random.choice(cases)                    

            

            else:
                print("tour de l'ordi",player)
                if player == "WALL-E-1" or player == "WALL-E-2" :
                    hasard=random.randint(1, 2)
                    if hasard == 1 :
                        choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                    else:
                        choix=random.choice(cases)
                elif player == "R2D2-1" or player == "R2D2-2" :
                    hasard=random.randint(1, 10)
                    if hasard ==1 or hasard==2 or hasard==3 :
                        choix=random.choice(cases)                    
                    else:
                        choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                elif player == "TERMINATOR-1" or player == "TERMINATOR-2":
                    choix=meilleur_coup(cases_player=case_player2,cases_adversaires=case_player1,cases=cases)
                else:
                    choix=random.choice(cases)                    


            if player == pseudo1:
                case = "X"
            else:
                case = "O"

            if choix in cases:
                if choix == 1:
                    case1 = case
                elif choix == 2:
                    case2 = case
                elif choix == 3:
                    case3 = case
                elif choix == 4:
                    case4 = case
                elif choix == 5:
                    case5 = case
                elif choix == 6:
                    case6 = case
                elif choix == 7:
                    case7 = case
                elif choix == 8:
                    case8 = case
                elif choix == 9:
                    case9 = case

                grille(choix, case1, case2, case3, case4, case5, case6, case7, case8, case9)

                if player == pseudo1:
                    case_player1.append(choix)
                else:
                    case_player2.append(choix)
                
                cases.remove(choix)

                

        if victoire(case_player1, case_player2):
            print(player, "a gagné")
            ajouter_points(player,10)
            if player == pseudo1 :
                points_bot+=10
            if player == pseudo1 :
                player=pseudo2
            else :
                player=pseudo1
            print(player,'a perdu')
            return points_bot

        else:
            print("Match Nul")
            return -1
    else:
                    return -1