#! /usr/bin/env python3

"""Programme affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell. 
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

import os
import sys

def arguments():
    """Fonction qui affiche les arguments de la ligne de commande."""
    args_fournis = sys.argv[1:]
    
    if not args_fournis:
        print("Erreur : Aucun argument n'a été fourni.", file=sys.stderr)
        return 1
        
    debug_mode = os.environ.get("DEBUG")
    
    if debug_mode is not None:
        for indice, argument in enumerate(args_fournis, start=1):
            print(f"Argument {indice} : {argument}")
    else:

        for argument in args_fournis:
            print(argument)

if __name__ == "__main__":
    code_retour = arguments()
    sys.exit(code_retour)      
