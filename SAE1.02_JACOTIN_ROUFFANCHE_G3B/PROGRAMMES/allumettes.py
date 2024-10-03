import random

def meilleur_choix(n: int, choix: int) ->int:
    #Cette fonction permet d'attribuer le meilleur coup à jouer au BOT au jeu des allumettes.
    #Elle prend en paramètre un entier "n" étant le nombre d'allumettes et choix un entier étant le BOT choisit.
    #Elle renvoie un entier étant le meilleur coup à jouer.

    if n <= 4 and n != 1:
        meilleur = n - 1
    elif n % 2 == 0 or n==1:  # Si le nombre d'allumettes est pair
        meilleur = 1

    else:
        meilleur = 2
    return meilleur


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



def allumettes(pseudo1:str,pseudo2:str,mode:str,choix_bot:int):
    #Cette fonction permet de jouer au jeu des allumettes !
    #Elle prend en paramètre d'entrée le pseudo des deux joueurs étant des chaînes de caractères, le mode de jeu choisit pour le BOT étant une chaîne de caractères, ainsi que les choix du BOT étant un entier.
    #Elle prend en paramètre de sortie un entier étant le nombre de points à attribuer en cas de victoire à tel ou tel joueur.
    
    n : int
    choix : int
    choix=0
    player: str
    player2 : str
    points_bot=0
    points_bot:int


    n = 20

    if mode=='oco':
        player =  random.choice([pseudo1, pseudo2])
        print(player, "à toi de commencer")


        if player == pseudo1:
            player = pseudo2
        else:
            player = pseudo1



        while n > 0 and n!=0 :
            if player == pseudo1:
                player = pseudo2
            else:
                player = pseudo1


            if player == pseudo1 :
                print(pseudo2," : à ton tour !")
                if player == "WALL-E-1" or player == "WALL-E-2":
                    hasard=random.randint(1,2)
                    if hasard == 1 :
                        if n>=3:
                            choix=random.randint(1,3)
                        else:
                            choix=random.randint(1,n)
                    else:
                        choix=random.randint(1,3)
                elif player == "R2D2-1" or player == "R2D2-2":
                    hasard=random.randint(1, 10)
                    if hasard ==1 or hasard == 2 or hasard == 3:
                        if n>=3:
                            choix=random.randint(1,3)
                        else:
                            choix=random.randint(1,n)
                    else:
                        choix=meilleur_choix(n,choix)
                elif player == "TERMINATOR-1" or player == "TERMINATOR-2":
                    choix=meilleur_choix(n,choix)
            
                    
                       
            if player == pseudo2 :
                print(pseudo2," : à ton tour !")
                if player == "WALL-E-1" or player == "WALL-E-2":
                    hasard=random.randint(1, 2)
                    if hasard == 1 :
                        if n>=3:
                            choix=random.randint(1,3)
                        else:
                            choix=random.randint(1,n)
                    else:
                        choix=random.randint(1,3)
                elif player == "R2D2-1" or player == "R2D2-2":
                    hasard=random.randint(1, 10)
                    if hasard ==1 or hasard == 2 or hasard == 3:
                        if n>=3:
                            choix=random.randint(1,3)
                        else:
                            choix=random.randint(1,n)
                    else:
                        choix=meilleur_choix(n,choix)
                elif player == "TERMINATOR-1" or player == "TERMINATOR-2":
                    choix=meilleur_choix(n,choix)

            if n - choix > 0 :
                n -= choix
                print(n, "allumettes restantes")
            elif n- choix ==0 :
                n -= choix
                print("Perdu !")
                if player == pseudo1 :
                    print("""
                         ██████╗  █████╗  ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗████████╗
                        ██╔════╝ ██╔══██╗██╔════╝ ████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
                        ██║  ███╗███████║██║  ███╗██╔██╗ ██║███████║██╔██╗ ██║   ██║   
                        ██║   ██║██╔══██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
                        ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║   ██║   
                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                █████╗
                                                ╚════╝ \n"""
                        "                                     ",pseudo2)
                    print()
                    print()
                    print("""
                        ██▓███  ▓█████  ██▀███  ▓█████▄  ▄▄▄       ███▄    █ ▄▄▄█████▓
                        ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                        ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                        ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                        ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                        ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                        ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                        ░░          ░     ░░   ░  ░ ░  ░   ░   ▒      ░   ░ ░   ░      
                                    ░  ░   ░        ░          ░  ░         ░          
                                                ░                                     
                                                    █████╗
                                                    ╚════╝ \n"""
                        "                                      ",pseudo1)
                else : 
                    print("""
                         ██████╗  █████╗  ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗████████╗
                        ██╔════╝ ██╔══██╗██╔════╝ ████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
                        ██║  ███╗███████║██║  ███╗██╔██╗ ██║███████║██╔██╗ ██║   ██║   
                        ██║   ██║██╔══██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
                        ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║   ██║   
                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                █████╗
                                                ╚════╝ \n"""
                        "                                   ",pseudo1)
                    print()
                    print()
                    print("""
                        ██▓███  ▓█████  ██▀███  ▓█████▄  ▄▄▄       ███▄    █ ▄▄▄█████▓
                        ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                        ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                        ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                        ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                        ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                        ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                        ░░          ░     ░░   ░  ░ ░  ░   ░   ▒      ░   ░ ░   ░      
                                    ░  ░   ░        ░          ░  ░         ░          
                                                ░                                     
                                                █████╗
                                                ╚════╝ \n"""
                        "                                   ",pseudo2)
                    points_bot=10
                    return points_bot

    if mode=='jco':
        player =  random.choice([pseudo1, pseudo2])
        print(player, "à toi de commencer")


        if player == pseudo1:
            player = pseudo2
        else:
            player = pseudo1



        while n > 0 and n!=0 :
            if player == pseudo1:
                player = pseudo2
            else:
                player = pseudo1


            if player == pseudo1  :  
                choix = int(input(player + "" +" combien d'allumettes enlever ? 1, 2 ou 3 ? :"))
                while n - choix < 0 :
                    print("impossible")
                     
                    choix = int(input(player + "" +" combien d'allumettes enlever ? 1, 2 ou 3 ? :"))
                    
                       
            if player == pseudo2 :
                print(pseudo2," : à mon tour !")
                if choix_bot == 1 :
                    hasard=random.randint(1, 10)
                    if hasard == 1 :
                        choix=meilleur_choix(n,choix)
                    else:
                        if n>=3:
                            choix=random.randint(1,3)
                        else:
                            choix=random.randint(1,n)
                elif choix_bot == 2 :
                    hasard=random.randint(1, 2)
                    if hasard ==1 :
                        if n>=3:
                            choix=random.randint(1,3)
                        else:
                            choix=random.randint(1,n)
                    else:
                        choix=meilleur_choix(n,choix)
                else:
                    choix=meilleur_choix(n,choix)

            if n - choix > 0 :
                n -= choix
                print(n, "allumettes restantes")
            elif n- choix ==0 :
                n -= choix
                print("Perdu !")
                if player == pseudo1 :
                    print("""
                         ██████╗  █████╗  ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗████████╗
                        ██╔════╝ ██╔══██╗██╔════╝ ████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
                        ██║  ███╗███████║██║  ███╗██╔██╗ ██║███████║██╔██╗ ██║   ██║   
                        ██║   ██║██╔══██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
                        ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║   ██║   
                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                █████╗
                                                ╚════╝ \n"""
                        "                                     ",pseudo2)
                    print()
                    print()
                    print("""
                        ██▓███  ▓█████  ██▀███  ▓█████▄  ▄▄▄       ███▄    █ ▄▄▄█████▓
                        ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                        ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                        ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                        ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                        ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                        ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                        ░░          ░     ░░   ░  ░ ░  ░   ░   ▒      ░   ░ ░   ░      
                                    ░  ░   ░        ░          ░  ░         ░          
                                                ░                                     
                                                    █████╗
                                                    ╚════╝ \n"""
                        "                                      ",pseudo1)
                    points_bot=10
                else : 
                    print("""
                         ██████╗  █████╗  ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗████████╗
                        ██╔════╝ ██╔══██╗██╔════╝ ████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
                        ██║  ███╗███████║██║  ███╗██╔██╗ ██║███████║██╔██╗ ██║   ██║   
                        ██║   ██║██╔══██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
                        ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║   ██║   
                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                █████╗
                                                ╚════╝ \n"""
                        "                                   ",pseudo1)
                    print()
                    print()
                    print("""
                        ██▓███  ▓█████  ██▀███  ▓█████▄  ▄▄▄       ███▄    █ ▄▄▄█████▓
                        ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                        ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                        ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                        ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                        ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                        ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                        ░░          ░     ░░   ░  ░ ░  ░   ░   ▒      ░   ░ ░   ░      
                                    ░  ░   ░        ░          ░  ░         ░          
                                                ░                                     
                                                █████╗
                                                ╚════╝ \n"""
                        "                                   ",pseudo2)
                    ajouter_points(pseudo1, 10)

    else:
        player =  random.choice([pseudo1, pseudo2])
        print(player, "à toi de commencer")     



        if player == pseudo1  :  
            player = pseudo2
            player2 = pseudo1
        else : 
            player = pseudo1
            player2 = pseudo2



        while n > 0 and n!=0 :      

            if player == pseudo1  :  
                player = pseudo2
                player2 = pseudo1
            else : 
                player = pseudo1
                player2 = pseudo2       


            choix = int(input(player + "" +" combien d'allumettes enlever ? 1, 2 ou 3 ? :"))        

            if n - choix > 0 :
                n -= choix
                print(n)
            elif n- choix ==0 :
                n -= choix
                print("Perdu !")
                if player == pseudo1 :
                    print("""
                         ██████╗  █████╗  ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗████████╗
                        ██╔════╝ ██╔══██╗██╔════╝ ████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
                        ██║  ███╗███████║██║  ███╗██╔██╗ ██║███████║██╔██╗ ██║   ██║   
                        ██║   ██║██╔══██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
                        ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║   ██║   
                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                █████╗
                                                ╚════╝ \n"""
                        "                                     ",player2)
                    print()
                    print()
                    print("""
                        ██▓███  ▓█████  ██▀███  ▓█████▄  ▄▄▄       ███▄    █ ▄▄▄█████▓
                        ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                        ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                        ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                        ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                        ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                        ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                        ░░          ░     ░░   ░  ░ ░  ░   ░   ▒      ░   ░ ░   ░      
                                    ░  ░   ░        ░          ░  ░         ░          
                                                ░                                     
                                                    █████╗
                                                    ╚════╝ \n"""
                        "                                      ",player)
                    ajouter_points(pseudo2, 10)
                else : 
                    print("""
                         ██████╗  █████╗  ██████╗ ███╗   ██╗ █████╗ ███╗   ██╗████████╗
                        ██╔════╝ ██╔══██╗██╔════╝ ████╗  ██║██╔══██╗████╗  ██║╚══██╔══╝
                        ██║  ███╗███████║██║  ███╗██╔██╗ ██║███████║██╔██╗ ██║   ██║   
                        ██║   ██║██╔══██║██║   ██║██║╚██╗██║██╔══██║██║╚██╗██║   ██║   
                        ╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║  ██║██║ ╚████║   ██║   
                        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                █████╗
                                                ╚════╝ \n"""
                        "                                   ",player)
                    print()
                    print()
                    print("""
                        ██▓███  ▓█████  ██▀███  ▓█████▄  ▄▄▄       ███▄    █ ▄▄▄█████▓
                        ▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ██▌▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                        ▓██░ ██▓▒▒███   ▓██ ░▄█ ▒░██   █▌▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                        ▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  ░▓█▄   ▌░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                        ▒██▒ ░  ░░▒████▒░██▓ ▒██▒░▒████▓  ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                        ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒▓  ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                        ░▒ ░      ░ ░  ░  ░▒ ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                        ░░          ░     ░░   ░  ░ ░  ░   ░   ▒      ░   ░ ░   ░      
                                    ░  ░   ░        ░          ░  ░         ░          
                                                ░                                     
                                                █████╗
                                                ╚════╝ \n"""
                        "                                   ",player2)

                    ajouter_points(pseudo1, 10)

            elif n - choix < 0 :
                print("impossible")
    return points_bot      

