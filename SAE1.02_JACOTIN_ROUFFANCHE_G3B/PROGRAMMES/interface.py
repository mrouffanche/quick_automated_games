def menu():
            #Cette procédure permet l'affichage du menu principal permettant d'accéder aux différents jeux
            print("""
                     ______________________________________________________________________________
                    |                                                                              |
                    |   ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗   ██╗███████╗  |   
                    |   ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║   ██║██╔════╝  |   
                    |   ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║   ██║█████╗    |   
                    |   ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██╔══╝    |   
                    |   ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝███████╗  |   
                    |   ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝  |
                    |                                                                              |
                    |                  Sur quels jeux voulez-vous vous affronter ?                 |
                    |                                                                              |
                    |                        1 - Le jeu des devinettes                             |
                    |                        2 - Le jeu des allumettes                             |
                    |                        3 - Le jeu du morpion                                 |
                    |                        4 - Le jeu du puissance 4                             |
                    |                        5 - Consulter les règles                              |
                    |                        6 - Consulter les scores                              |
                    |                        7 - Quitter                                           |      
                    |_________________________        _____________________________________________|
                                              |      |
                            __________________|      |____________________________________________
                                    ,--.     ,--.          ,--.   ,--.
                                    |oo  | _  |  `.       | oo | |  oo|
                                o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o
                                    |/| /|   '._,'        |/| /| |/| /|
                            _______________________________________________________________________
    """)
            

def menu_sans_p4():
            print("""
                     ______________________________________________________________________________
                    |                                                                              |
                    |   ██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗   ██╗███████╗  |   
                    |   ██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║   ██║██╔════╝  |   
                    |   ██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║   ██║█████╗    |   
                    |   ██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██╔══╝    |   
                    |   ██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝███████╗  |   
                    |   ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝  |
                    |                                                                              |
                    |                  Sur quels jeux voulez-vous vous affronter ?                 |
                    |                                                                              |
                    |                        1 - Le jeu des devinettes                             |
                    |                        2 - Le jeu des allumettes                             |
                    |                        3 - Le jeu du morpion                                 |
                    |                        4 - Consulter les règles                              |
                    |                        5 - Consulter les scores                              |
                    |                        6 - Quitter                                           |      
                    |_________________________        _____________________________________________|
                                              |      |
                            __________________|      |____________________________________________
                                    ,--.     ,--.          ,--.   ,--.
                                    |oo  | _  |  `.       | oo | |  oo|
                                o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o
                                    |/| /|   '._,'        |/| /| |/| /|
                            _______________________________________________________________________
    """)
            
def devinettemenu():
                    #Cette procédure permet l'affichage de lancement du jeu des devinettes dans l'aide ou pour y jouer
                    print("""
        ██████╗ ██████╗ ██████╗               ██████╗ ███████╗██╗   ██╗██╗███╗   ██╗███████╗████████╗████████╗███████╗███████╗
        ╚════██╗╚════██╗╚════██╗              ██╔══██╗██╔════╝██║   ██║██║████╗  ██║██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔════╝
          ▄███╔╝  ▄███╔╝  ▄███╔╝    █████╗    ██║  ██║█████╗  ██║   ██║██║██╔██╗ ██║█████╗     ██║      ██║   █████╗  ███████╗
          ▀▀══╝   ▀▀══╝   ▀▀══╝     ╚════╝    ██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║╚██╗██║██╔══╝     ██║      ██║   ██╔══╝  ╚════██║
          ██╗     ██╗     ██╗                 ██████╔╝███████╗ ╚████╔╝ ██║██║ ╚████║███████╗   ██║      ██║   ███████╗███████║
          ╚═╝     ╚═╝     ╚═╝                 ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
                    """)

def allumettesmenu():
                    #Cette procédure permet l'affichage de lancement du jeu des allumettes dans l'aide ou pour y jouer
                    print("""
        ░░ ░░ ░░   
        ██ ██ ██
        ██ ██ ██
        ██ ██ ██
        ██ ██ ██                 █████╗ ██╗     ██╗     ██╗   ██╗███╗   ███╗███████╗████████╗████████╗███████╗███████╗
        ██ ██ ██                ██╔══██╗██║     ██║     ██║   ██║████╗ ████║██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔════╝
        ██ ██ ██        █████╗  ███████║██║     ██║     ██║   ██║██╔████╔██║█████╗     ██║      ██║   █████╗  ███████╗
        ██ ██ ██        ╚════╝  ██╔══██║██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝     ██║      ██║   ██╔══╝  ╚════██║
        ██ ██ ██                ██║  ██║███████╗███████╗╚██████╔╝██║ ╚═╝ ██║███████╗   ██║      ██║   ███████╗███████║
        ██ ██ ██                ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
                    """)

def morpionmenu():
                    #Cette procédure permet l'affichage de lancement du jeu du morpion dans l'aide ou pour y jouer
                    print("""
        _______________    
        |--X-|-X--|--X-|              ███╗   ███╗ ██████╗ ██████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
        |____|____|____|              ████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║██╔═══██╗████╗  ██║
        |    |  O |    |    █████╗    ██╔████╔██║██║   ██║██████╔╝██████╔╝██║██║   ██║██╔██╗ ██║
        |____|____|____|    ╚════╝    ██║╚██╔╝██║██║   ██║██╔══██╗██╔═══╝ ██║██║   ██║██║╚██╗██║
        |    |    |  O |              ██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ██║╚██████╔╝██║ ╚████║
        |____|____|____|              ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                    """)

def puissancemenu():
                    #Cette procédure permet l'affichage de lancement du jeu du puissance 4 dans l'aide ou pour y jouer
                    print("""
                    ██████╗ ██╗   ██╗██╗███████╗███████╗ █████╗ ███╗   ██╗ ██████╗███████╗    ██╗  ██╗
                    ██╔══██╗██║   ██║██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝    ██║  ██║
                    ██████╔╝██║   ██║██║███████╗███████╗███████║██╔██╗ ██║██║     █████╗      ███████║
                    ██╔═══╝ ██║   ██║██║╚════██║╚════██║██╔══██║██║╚██╗██║██║     ██╔══╝      ╚════██║
                    ██║     ╚██████╔╝██║███████║███████║██║  ██║██║ ╚████║╚██████╗███████╗         ██║
                    ╚═╝      ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝         ╚═╝                                                                  
                """)

def aidemenu():
        #Cette procédure permet l'affichage du menu pour l'aide permettant d'en savoir plus sur les différents jeux ...
        print("""
                 █████╗ ██╗██████╗ ███████╗
                ██╔══██╗██║██╔══██╗██╔════╝
                ███████║██║██║  ██║█████╗  
                ██╔══██║██║██║  ██║██╔══╝  
                ██║  ██║██║██████╔╝███████╗
                ╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝
                    1- Jeu des devinettes
                    2- Jeu des allumettes
                    3- Jeu du morpion
                    4- Jeu du puissance 4
                    5- Quitter l'aide
                    """)
        
def byemenu():
        #Cette procédure permet de quitter le menu de l'aide ou le menu principal
        print("""
         █████╗ ██╗   ██╗    ██████╗ ███████╗██╗   ██╗ ██████╗ ██╗██████╗     ██╗██╗██╗
        ██╔══██╗██║   ██║    ██╔══██╗██╔════╝██║   ██║██╔═══██╗██║██╔══██╗    ██║██║██║
        ███████║██║   ██║    ██████╔╝█████╗  ██║   ██║██║   ██║██║██████╔╝    ██║██║██║
        ██╔══██║██║   ██║    ██╔══██╗██╔══╝  ╚██╗ ██╔╝██║   ██║██║██╔══██╗    ╚═╝╚═╝╚═╝
        ██║  ██║╚██████╔╝    ██║  ██║███████╗ ╚████╔╝ ╚██████╔╝██║██║  ██║    ██╗██╗██╗
        ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝  ╚═══╝   ╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═╝╚═╝╚═╝
              """)
        
def scoremenu():
        #Cette procédure permet l'affichage de présentation des scores des joueurs
        print("""
            ███████╗ ██████╗ ██████╗ ██████╗ ███████╗███████╗
            ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
            ███████╗██║     ██║   ██║██████╔╝█████╗  ███████╗
            ╚════██║██║     ██║   ██║██╔══██╗██╔══╝  ╚════██║
            ███████║╚██████╗╚██████╔╝██║  ██║███████╗███████║
            ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝                                                           
                  """)
        
def joueur1():
        #Cette procédure permet d'afficher en gros "JOUEUR 1" afin de déterminer ce dernier
        print("""
        ██╗ ██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗      ██╗
        ██║██╔═══██╗██║   ██║██╔════╝██║   ██║██╔══██╗    ███║
        ██║██║   ██║██║   ██║█████╗  ██║   ██║██████╔╝    ╚██║
    ██  ██║██║   ██║██║   ██║██╔══╝  ██║   ██║██╔══██╗     ██║
   ╚█████╔╝╚██████╔╝╚██████╔╝███████╗╚██████╔╝██║  ██║     ██║
    ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═╝ """)
        
def joueur2():
        #Cette procédure permet d'afficher en gros "JOUEUR 2" afin de déterminer ce dernier
        print("""
        ██╗ ██████╗ ██╗   ██╗███████╗██╗   ██╗██████╗     ██████╗ 
        ██║██╔═══██╗██║   ██║██╔════╝██║   ██║██╔══██╗    ╚════██╗
        ██║██║   ██║██║   ██║█████╗  ██║   ██║██████╔╝     █████╔╝
    ██  ██║██║   ██║██║   ██║██╔══╝  ██║   ██║██╔══██╗    ██╔═══╝ 
   ╚█████╔╝╚██████╔╝╚██████╔╝███████╗╚██████╔╝██║  ██║    ███████╗
    ╚════╝  ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ """)
        
def puissanceregle():
                            #Cette procédure permet d'afficher les règles du jeu du puissance 4
                            print("Le jeu du puissance 4 consiste à aligner horizontalement ou verticalement ou en diagonale des jetons pour déterminer un gagnant. Il faut donc faire preuve de stratégie afin de bloquer l'autre joueur pour l'empêcher de gagner\n")

def morpionregle():
                            #Cette procédure permet d'afficher les règles du jeu du morpion
                            print("Le jeu du morpion esr un jeu où deux joueurs s'affrontent. Ce jeu se réalise sur une grille de 9 cases. Chaque joueur se voit attribuer un symbole : O ou X et doit remplir chacun son tour, une des neuf cases présentes sur le tableau de jeu.\n"
                    "La partie s'arrête s'il y a match nul ou si un joueur a réussi à compter une ligne de 3 symboles alignés de manière diagonale, horizontale ou verticale !")
                            print("REGLES : Il n'est pas possible de poser un signe sur une case déjà occupée, dans le ce cas, le joueur rejoue jusqu'à ce que la case sélectionnée soit libre\n")
        

def allumettesregle():
                    #Cette procédure permet d'afficher les règles du jeu des allumettes
                            
                    print("Le jeu des allumettes est un jeu où deux joueurs s'affrontent. Ce jeu consiste à partir d'une pile de 20 allumettes et d'en retirer au choix une, deux ou trois ! \n" "La partie s'arrête lorsque le nombre d'allumettes tombe à 0 et le joueur perdant est celui qui fait arriver la pile à ce nombre quand il retire des allumettes.")
                    print("REGLES : Il est impossible de retirer plus de trois allumettes\n")

def devinnetteregle():
                    #Cette procédure permet d'afficher les règles du jeu des devinettes
                    print("PRINCIPE : Le jeu des devinettes est un jeu où deux joueurs s'affrontent. Ce jeu consiste à faire devinner un nombre à un autre joueur. A chaque nouvelle réponse, le joueur ayant donné le nombre doit indiquer si le nombre choisit par l'autre joueur est plus petit, plus grand ou égal au nombre initial ! Attention à ne pas mentir ... \n",
                    "La partie s'arrête lorsque le nombre a été devinné ! Le joueur ayant devinné gagne alors un point !")
                    print("REGLES : Il est interdit pour celui qui fait deviner le nombre de mentir, les joueurs doivent répondre honnêtement et jouer sérieusement ! Le joueur qui devine a autant de chances pour deviner le nombre mystère\n")

def Choix_mode_JEUX():
        #Cette procédure permet l'affichage du menu du choix des modes de jeux
        print("""
                     ________________________________________________________________________________
                    |                                                                                |
                    |    ██████╗██╗  ██╗ ██████╗ ██╗██╗  ██╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗ |
                    |   ██╔════╝██║  ██║██╔═══██╗██║╚██╗██╔╝    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝ |
                    |   ██║     ███████║██║   ██║██║ ╚███╔╝     ██╔████╔██║██║   ██║██║  ██║█████╗   |
                    |   ██║     ██╔══██║██║   ██║██║ ██╔██╗     ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝   |
                    |   ╚██████╗██║  ██║╚██████╔╝██║██╔╝ ██╗    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗ |
                    |    ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ |
                    |                                                                                |
                    |                   Quel mode de jeu voulez-vous choisir ?                       |
                    |                                                                                |
                    |                        1 - Joueur Contre Joueur (JCJ)                          |
                    |                        2 - Joueur Contre Ordinateur (JCO)                      |
                    |                        3 - Ordinateur Contre Ordinateur (OCO)                  |
                    |                        4 - Quitter                                             |  
                    |________________________________________________________________________________| 
              """)
        
def Choix_mode_BOTS():
        #Cette procédure permet l'affichage du menu du choix des différents BOTS
        print("""
                     ________________________________________________________________________________
                    |                                                                                |
                    |    ██████╗██╗  ██╗ ██████╗ ██╗██╗  ██╗    ██████╗  ██████╗ ████████╗███████╗   |
                    |   ██╔════╝██║  ██║██╔═══██╗██║╚██╗██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝   |
                    |   ██║     ███████║██║   ██║██║ ╚███╔╝     ██████╔╝██║   ██║   ██║   ███████╗   |
                    |   ██║     ██╔══██║██║   ██║██║ ██╔██╗     ██╔══██╗██║   ██║   ██║   ╚════██║   |
                    |   ╚██████╗██║  ██║╚██████╔╝██║██╔╝ ██╗    ██████╔╝╚██████╔╝   ██║   ███████║   |
                    |    ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝   |
                    |                                                                                |
                    |                         Quel BOT voulez-vous choisir ?                         |
                    |                                                                                |
                    |                        1 - WALL-E (débutant)                                   |
                    |                        2 - R2D2 (intermédiaire)                                |
                    |                        3 - TERMINATOR (diabolique)                             |
                    |                                                                                |  
                    |________________________________________________________________________________| 
              """)