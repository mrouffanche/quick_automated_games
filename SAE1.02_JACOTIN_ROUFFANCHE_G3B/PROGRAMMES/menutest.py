from devinette2 import *
from allumettes import *
from morpion import *
from pseudo import *
from score import *
from interface import *
import time

if __name__ == "__main__":
    choix_jeux : int
    choix_jeux = 0
    choix_mode : int
    choix_mode = 0
    choix_bot : int
    choix_bot=0
    score_bot:int
    score_bot=0

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
                print('Le pseudo ne peut contenir que des chiffres et des lettres')
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
        menu()
        choix_jeux = int(input("Que voulez-vous faire ? : "))

        if choix_jeux == 1:
            victoire1 = 0
            victoire2 = 0
            temps_total = 0
            nb_essais = 1000
            cpt = 0
            for _ in range(nb_essais):
                start_time = time.time()
                if devinette(pseudo1,pseudo2,mode,choix_bot):
                    cpt += devinette(pseudo1,pseudo2,mode,choix_bot)
                end_time = time.time() - start_time
                temps_total += end_time
            print("nombre d'essais",pseudo1,":",cpt)
            print("la moyenne de temps requis pour",nb_essais,"parties : ",temps_total/nb_essais)

        elif choix_jeux == 2:
            "a"

        elif choix_jeux == 3:
            "a"

        elif choix_jeux == 4:
            print(jouer_puissance4(pseudo1,pseudo2,mode,choix_bot))
        elif choix_jeux == 5:
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

        elif choix_jeux == 6:
            afficher_scores_joueur(pseudo1)
            if mode == "jcj":
                afficher_scores_joueur(pseudo2)
            else :
                print("le score de ",pseudo2," est : ",score_bot)
        elif choix_jeux == 7:
            print("Au revoir !")
        else:
            print("Choix impossible, choisissez 1, 2, 3 ou 4 selon le menu")



#traiter cas ou pseudo1 = pseudo2