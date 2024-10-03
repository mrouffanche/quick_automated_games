import random


def ajouter_points(nom_utilisateur:str, points:int):
    scores : list[tuple[str, int]]
    scores = []

    # Lire le fichier et obtenir une liste des noms d'utilisateurs et des scores
    with open("score.txt", "rb") as f:
        for ligne in f:
            nom, score = ligne.decode('utf-8').strip().split(":")
            scores.append((nom, int(score)))

    # Rechercher le joueur et ajouter les points
    joueur_trouve = False
    for i, (nom, score) in enumerate(scores):
        if nom == nom_utilisateur:
            scores[i] = (nom, score + points)
            joueur_trouve = True

    # Si le joueur n'a pas été trouvé, ajouter une nouvelle entrée
    if not joueur_trouve:
        scores.append((nom_utilisateur, points))

    # Écrire les scores mis à jour dans le fichier
    with open("score.txt", "wb") as f:
        for nom, score in scores:
            ligne = f"{nom}:{score}\n"
            f.write(ligne.encode('utf-8'))


# Fonction pour afficher la grille de jeu
def afficher_grille(grille:list[list[str]]):
    # Afficher les indices de colonnes
    print("  1   2   3   4   5   6   7 ")
    print("+   +   +   +   +   +   +   +")
    for ligne in grille:
        print("| " + " | ".join(ligne) + " |")
        print("+---+---+---+---+---+---+---+")


# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(grille:list[list[str]], joueur:str):
    # Vérifier les lignes
    for ligne in grille:
        for i in range(len(ligne) - 3):
            if ligne[i:i+4] == [joueur] * 4:
                return True

    # Vérifier les colonnes
    for colonne in range(len(grille[0])):
        for ligne in range(len(grille) - 3):
            if grille[ligne][colonne] == joueur and grille[ligne+1][colonne] == joueur and grille[ligne+2][colonne] == joueur and grille[ligne+3][colonne] == joueur:
                return True

    # Vérifier les diagonales ascendantes
    for colonne in range(len(grille[0]) - 3):
        for ligne in range(len(grille) - 3):
            if grille[ligne][colonne] == joueur and grille[ligne+1][colonne+1] == joueur and grille[ligne+2][colonne+2] == joueur and grille[ligne+3][colonne+3] == joueur:
                return True

    # Vérifier les diagonales descendantes
    for colonne in range(len(grille[0]) - 3):
        for ligne in range(3, len(grille)):
            if grille[ligne][colonne] == joueur and grille[ligne-1][colonne+1] == joueur and grille[ligne-2][colonne+2] == joueur and grille[ligne-3][colonne+3] == joueur:
                return True

    return False



# Fonction pour déterminer si le joueur est 'O' ou 'X'
def rond_ou_croix(joueur_actuel: str, pseudo1: str) -> str :
    if joueur_actuel == pseudo1:
        return 'O'
    else:
        return 'X'


# Fonction principale du jeu
# ...

def jouer_puissance4(pseudo1:str, pseudo2:str):
    grille = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    joueur_actuel = random.choice([pseudo1, pseudo2])
    tour = 1
    fin_partie = False

    while not fin_partie:
        # Afficher la grille
        afficher_grille(grille)
        # Demander au joueur de choisir une colonne
        print("Tour", tour)
        colonne = int(input(joueur_actuel + ", choisissez une colonne (1-7) : "))
        # Vérifier si la colonne est valide
        while colonne < 1 or colonne > 7 or grille[0][colonne - 1] != ' ':
            print("Colonne invalide ou pleine. Réessayez.")
            colonne = int(input(joueur_actuel + ", choisissez une colonne (1-7) : "))

        # Ajouter le pion du joueur dans la colonne
        for ligne in range(len(grille) - 1, -1, -1):
            if grille[ligne][colonne - 1] == ' ':
                grille[ligne][colonne - 1] = rond_ou_croix(joueur_actuel, pseudo1)
                break

        # Vérifier si le joueur a gagné
        if verifier_victoire(grille, rond_ou_croix(joueur_actuel, pseudo1)):
            print(joueur_actuel, "a gagné !")
            ajouter_points(joueur_actuel, 10)
            fin_partie = True
        # Vérifier s'il y a match nul
        elif tour == 42:
            print("Match nul !")
            fin_partie = True
        else:
            # Passer au joueur suivant
            joueur_actuel = pseudo1 if joueur_actuel == pseudo2 else pseudo2
            tour += 1

    # Afficher la dernière grille
    afficher_grille(grille)
