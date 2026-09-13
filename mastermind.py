import random

COLORS = {
    "R": "Rouge",
    "V": "Vert",
    "B": "Bleu",
    "J": "Jaune",
}

def afficher_couleurs():
    for lettre, nom in COLORS.items():
        print(f"{lettre} = {nom}")
        