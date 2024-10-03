from devinette2 import devinette
from allumettes import allumettes
from morpion import morpion
from pseudo import *
from score import *
from interface import *
import puissance4

if __name__ == "__main__":
    choix_jeux : int
    choix_jeux = 0
    choix_mode : int
    choix_mode = 0
    choix_bot : int
    choix_bot=0
    score_bot:int
    score_bot=0
    score_bot1:int
    score_bot1=0
    score_bot2=0
    score_bot2:int=0
    ajouter_points2:int
    ajouter_points1:int
    ajouter_points:int

    num_joueur = 1
    mode : str
    mode = ""
    difficulte:int
    difficulte=0
    pseudo1:str
    pseudo2:str
    pseudo1='/'
    pseudo2='/'
    aide : int
    aide = 0

    while choix_mode != 4 and choix_mode != 3 and choix_mode != 2 and choix_mode != 1  :
        Choix_mode_JEUX()
        choix_mode = int(input("Que voulez-vous faire ? : "))
    


    if choix_mode == 1:
        mode="jcj"
        while not pseudo_valide(pseudo1):
            pseudo1 = pseudo(num_joueur)
            if not pseudo_valide(pseudo1):
                print("Le pseudo ne peut contenir que des chiffres et des lettres et ne doit pas correspondre au nom d'un bot")
        num_joueur = 2

        while not pseudo_valide(pseudo2):
            pseudo2=pseudo1
            while pseudo2 == pseudo1:
                    pseudo2 = pseudo(num_joueur)
                    if pseudo2==pseudo1:
                        print('Le pseudo ne peut pas être le même que celui du joueur 1. Veuillez en choisir un autre.')
            if not pseudo_valide(pseudo2):
                print('Le pseudo ne peut contenir que des chiffres et des lettres')

        print(pseudo1)
        print(pseudo2)

        verifier_fichier_score()
        verifier_utilisateur(pseudo1)
        verifier_utilisateur(pseudo2)

    elif choix_mode == 2:
            mode="jco"
            while not pseudo_valide(pseudo1):
                pseudo1 = pseudo(num_joueur)
                if not pseudo_valide(pseudo1):
                    print('Le pseudo ne peut contenir que des chiffres et des lettres')
            while choix_bot != 1 and choix_bot !=2 and choix_bot !=3 :
                Choix_mode_BOTS()
                choix_bot=int(input("Contre qui voulez vous jouer ?"))
        
            if choix_bot== 1 :
                pseudo2="WALL-E"
            elif choix_bot==2:
                pseudo2="R2D2"
            else :
                pseudo2="TERMINATOR"


    elif choix_mode == 3:
            mode="oco"
            while choix_bot != 1 and choix_bot !=2 and choix_bot !=3:
                Choix_mode_BOTS()
                choix_bot=int(input("Quel robot voulez-vous sélectionner ? : "))

            if choix_bot== 1 :
                pseudo1="WALL-E-1"
            elif choix_bot==2:
                pseudo1="R2D2-1"
            else :
                pseudo1="TERMINATOR-1"

            choix_bot = 0

            while choix_bot != 1 and choix_bot != 2 and choix_bot != 3:
                Choix_mode_BOTS()
                print("Contre qui voulez-vous que",pseudo1,"joue ?")
                choix_bot = int(input("Saisissez votre choix : "))

                if choix_bot == 1:
                    pseudo2 = "WALL-E-2"
                elif choix_bot == 2:
                    pseudo2 = "R2D2-2"
                else:
                    pseudo2 = "TERMINATOR-2"

            


    verifier_fichier_score()
    verifier_utilisateur(pseudo1)

            


    while choix_jeux != 7:
        if mode == 'jcj':
            menu()
        else:
            menu_sans_p4()
        choix_jeux = int(input("Que voulez-vous faire ? : "))
        if choix_jeux == 1:
            if mode == "jco" or mode == "jcj":
                ajouter_points=devinette(pseudo1,pseudo2,mode,choix_bot)
                score_bot += ajouter_points
            elif mode == "oco":
                ajouter_points1 = devinette(pseudo1,pseudo2,mode,choix_bot)
                ajouter_points2 = 10-ajouter_points1
                score_bot1 += ajouter_points1
                score_bot2 += ajouter_points2
        elif choix_jeux == 2:
            if mode == "jco" or mode == "jcj":
                ajouter_points=(allumettes(pseudo1, pseudo2,mode,choix_bot))
                score_bot += ajouter_points
            elif mode == "oco":
                ajouter_points1 = allumettes(pseudo1, pseudo2,mode,choix_bot)
                ajouter_points2 = 10-ajouter_points1
                score_bot1 += ajouter_points1
                score_bot2 += ajouter_points2
        elif choix_jeux == 3:
            if mode == "jco" or mode == "jcj":
                ajouter_points = morpion(pseudo1, pseudo2, mode, choix_bot)
                score_bot += ajouter_points
            elif mode == "oco":
                ajouter_points1 = morpion(pseudo1, pseudo2, mode, choix_bot)
                if ajouter_points1 >=0 :
                    ajouter_points2 = 10-ajouter_points1
                    score_bot1 += ajouter_points1
                    score_bot2 += ajouter_points2
        elif choix_jeux == 4 :
            if mode == 'jcj':
                print(puissance4.jouer_puissance4(pseudo1, pseudo2))
            else:
                while aide != 5:
                    aidemenu()
                    aide = int(input("Quelle aide voulez-vous consulter ?"))
                    if aide == 1:
                        devinettemenu()
                        devinnetteregle()
                    elif aide == 2:
                        allumettesmenu()
                        allumettesregle()
                    elif aide == 3:
                        morpionmenu()
                        morpionregle()
                    elif aide == 4:
                        puissancemenu()
                        puissanceregle()
                    elif aide == 5:
                        byemenu()

        elif choix_jeux == 5 :
            if mode == 'jcj':
                while aide != 5:
                    aidemenu()
                    aide = int(input("Quelle aide voulez-vous consulter ?"))
                    if aide == 1:
                        devinettemenu()
                        devinnetteregle()
                    elif aide == 2:
                        allumettesmenu()
                        allumettesregle()
                    elif aide == 3:
                        morpionmenu()
                        morpionregle()
                    elif aide == 4:
                        puissancemenu()
                        puissanceregle()
                    elif aide == 5:
                        byemenu()
            else:
                if mode == 'jco' :
                    afficher_scores_joueur(pseudo1)
                    print("le score de ",pseudo2," est : ",score_bot)
                else:
                    print("le score de ",pseudo1," est : ",score_bot1)
                    print("le score de ",pseudo2," est : ",score_bot2)
        elif choix_jeux == 6:
                if mode == "jcj":

                    afficher_scores_joueur(pseudo1)
                    afficher_scores_joueur(pseudo2)
                else:
                                print("Au revoir !")
                                break

        elif choix_jeux == 7 and mode == 'jcj' :
            print("Au revoir !")
        else:
                print("Choix impossible")



#traiter cas ou pseudo1 = pseudo2