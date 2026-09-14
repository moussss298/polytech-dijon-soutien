import random

# PARAMÈTRES DU JEU
NOMBRE_ELEMENTS_CODE = 4
MAX_TENTATIVES = 12

COULEURS = {
    "R": "Rouge",
    "V": "Vert",
    "B": "Bleu",
    "J": "Jaune",
    "M": "Mauve",
    "N": "Noir",
}

# Afficher les couleurs disponibles
print("Couleurs disponibles :")
for lettre, nom in COULEURS.items():
    print(f"{lettre} = {nom}")

# Créer le code secret
code_secret = []

for i in range(NOMBRE_ELEMENTS_CODE):
    couleur = random.choice(list(COULEURS.keys()))
    code_secret.append(couleur)

# Nombre de tentatives
tentatives = 0

# Boucle principale du jeu
while tentatives < MAX_TENTATIVES:

    print()
    proposition = input("Entrez votre code : ").upper()

    # Vérifier que le joueur entre le bon nombre de couleurs
    if len(proposition) != NOMBRE_ELEMENTS_CODE:
        print("Erreur : vous devez entrer 4 couleurs.")
        continue

    # Vérifier que les lettres existent
    code_valide = True

    for couleur in proposition:
        if couleur not in COULEURS:
            code_valide = False

    if not code_valide:
        print("Erreur : une couleur n'existe pas.")
        continue

    tentatives += 1

    # Calcul des couleurs correctes
    correct = 0

    for i in range(NOMBRE_ELEMENTS_CODE):
        if proposition[i] == code_secret[i]:
            correct += 1

    # Calcul des couleurs présentes mais mal placées
    partiel = 0

    for couleur in COULEURS:
        nombre_secret = code_secret.count(couleur)
        nombre_proposition = proposition.count(couleur)

        partiel += min(nombre_secret, nombre_proposition)

    # On enlève les couleurs déjà trouvées à la bonne position
    partiel -= correct

    print(f"Correct : {correct} | Partiel : {partiel}")

    # Le joueur a gagné
    if correct == NOMBRE_ELEMENTS_CODE:
        print("Bravo ! Vous avez trouvé le code !")
        print(f"Nombre de tentatives : {tentatives}")
        print(f"Score : {MAX_TENTATIVES - tentatives}")
        break

# Le joueur a perdu
if tentatives == MAX_TENTATIVES and correct != NOMBRE_ELEMENTS_CODE:
    print()
    print("Vous avez perdu !")
    print("Le code était :", "".join(code_secret))
    print(f"Score : {MAX_TENTATIVES - tentatives}")