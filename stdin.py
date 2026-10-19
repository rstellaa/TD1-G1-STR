#! /usr/bin/env python3
"""Ce programme permet de compter le nombre de caractères saisi par l'utilisateur dans son entrée standard et de l'afficher. 
- Ce programme demandera à l'utilisateur de saisir une chaine uniquement s'il est invoqué en mode interactif.  
- Ce programme ne devra afficher sur la sortie standard *que* le nombre de caractères saisi. 
- Une fois le programme ci-dessous mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

import sys

# stdin.py
import sys

def comptage():
    if sys.stdin.isatty():
        texte = input("Saisissez une chaine : ")
    else:
        texte = sys.stdin.read()
    
    compteur = 0
    for caractere in texte:
        compteur += 1
        
    return compteur

if __name__ == "__main__":
    print(comptage())
