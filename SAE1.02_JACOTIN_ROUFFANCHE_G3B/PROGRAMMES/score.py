def afficher_scores_joueur(pseudo:str):
    #Cette procédure permet d'afficher les scores des différents joueurs.
    #Elle prend en entrée le pseudo du joueur étant une chaîne de caractères.
    with open("score.txt", "rb") as f:
        for ligne in f:
            nom_utilisateur, score = ligne.decode('utf-8').strip().split(":")
            if nom_utilisateur == pseudo:
                print(f"Le score de {pseudo} est : {score}")
                

def verifier_fichier_score() -> str:
    #Cette fonction permet de vérifier le fichier des scores.
    #Elle prend en sortie une chaîne de caractères permettant de renvoyer 1 si le ficiher et trouvé ainsi que 2 s'il n'est pas trouvé.
    try:
        with open("score.txt", "rb"):
            # Ne rien faire
            return '1'
    except FileNotFoundError:
        with open("score.txt", "wb"):
            # Ne rien faire
            return '2'
        
def verifier_utilisateur(nom_utilisateur:str):
    #Cette procédure permet de vérifier le score d'un utilisateur en particulier.
    #Elle prend en entrée le nom de l'utilisateur étant une chaîne de caractères.
    scores: list[tuple[str, int]] = []

    # Lire le fichier et obtenir une liste des noms d'utilisateurs et des scores
    with open("score.txt", "rb") as f:
        for ligne in f:
            nom, score = ligne.decode('utf-8').strip().split(":")
            scores.append((nom, int(score)))

    # Vérifier si le nom d'utilisateur existe déjà
    for nom, score in scores:
        if nom == nom_utilisateur:
            return

    # Ajouter l'utilisateur avec un score initial de 0
    scores.append((nom_utilisateur, 0))

    # Écrire les scores mis à jour dans le fichier
    with open("score.txt", "wb") as f:
        for nom, score in scores:
            ligne = f"{nom}:{score}\n"
            f.write(ligne.encode('utf-8'))