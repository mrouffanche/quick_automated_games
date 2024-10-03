def pseudo_valide(pseudo: str) -> bool:
    #Cette fonction permet de vérifier si le pseudo de l'utilisateur est valide ou non.
    #Elle prend en entrée le pseudo choisit étant une chaîne de caractères.
    #Elle renvoie un booléen permettant de signifier si le pseudo est valide ou non

    for caractere in pseudo:
        if not caractere.isalnum():
            return False
        if pseudo=='TERMINATOR' or pseudo=='R2D2' or pseudo=='WALL-E':
            return False
    return True

def pseudo(num_joueur: int,) -> str:
    #Cette fonction permet de choisir le pseudo d'un joueur.
    #Elle prend en entrée le numéro du joueur (1 ou 2) étant un entier.
    #Elle prend en sortie une chaîne de caractères étant le pseudo choisit.
    
    num = str(num_joueur)
    
    while True:
        pseudo = input("Saisir nom joueur " + num + " : ")

        return pseudo

