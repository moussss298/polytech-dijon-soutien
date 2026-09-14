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
for lettre, nom in COULEURS.items():
    print(f"{lettre} = {nom}")

# Créer le code secret
code_secret = []

for i in range(NOMBRE_ELEMENTS_CODE):
    couleur = random.choice(list(COULEURS.keys()))
    code_secret.append(couleur)
