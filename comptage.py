#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques principales.
- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes. 
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard. 
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture. 
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""

import os
import sys

def lire():
    args_fournis = sys.argv[1:]
    debug_mode = os.environ.get("DEBUG") is not None
    contenu = ""
    
    if len(args_fournis) >= 1:
        chemin_fichier = args_fournis[0]
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{chemin_fichier}' est introuvable.", file=sys.stderr)
            sys.exit(1)
    else:
        contenu = sys.stdin.read()

    stats = [0] * 29

    if contenu:
        stats[27] = 1 # On commence à 1 ligne si le texte n'est pas vide

    dans_un_mot = False
    mot_courant = ""

    for caractere in contenu:
        stats[28] += 1 # Incrémentation des caractères totaux
        
        char_lower = caractere.lower()
        
        match char_lower:
            case ' ' | '\t':
                if dans_un_mot:
                    dans_un_mot = False
                    if debug_mode: print(f"[DEBUG] Mot {stats[26]} : '{mot_courant}'")
                    mot_courant = ""
                    
            case '\n':
                stats[27] += 1 # Une ligne de plus
                if dans_un_mot:
                    dans_un_mot = False
                    if debug_mode: print(f"[DEBUG] Mot {stats[26]} : '{mot_courant}'")
                    mot_courant = ""
                    
            case 'é' | 'è' | 'ê' | 'ë' | 'à' | 'â' | 'ä' | 'ù' | 'û' | 'ü' | 'î' | 'ï' | 'ô' | 'ö' | 'ç':
                if not dans_un_mot:
                    dans_un_mot = True
                    stats[26] += 1 # Un mot de plus
                if debug_mode: mot_courant += caractere
                
                match char_lower:
                    case 'é' | 'è' | 'ê' | 'ë': stats[ord('e') - ord('a')] += 1
                    case 'à' | 'â' | 'ä': stats[ord('a') - ord('a')] += 1
                    case 'ù' | 'û' | 'ü': stats[ord('u') - ord('a')] += 1
                    case 'î' | 'ï': stats[ord('i') - ord('a')] += 1
                    case 'ô' | 'ö': stats[ord('o') - ord('a')] += 1
                    case 'ç': stats[ord('c') - ord('a')] += 1

            case c if 'a' <= c <= 'z':
                if not dans_un_mot:
                    dans_un_mot = True
                    stats[26] += 1
                if debug_mode: mot_courant += caractere
                
                stats[indice_lettre] += 1
                
            case _:
                if debug_mode and dans_un_mot: mot_courant += caractere

    if dans_un_mot and debug_mode:
        print(f"[DEBUG] Mot {stats[26]} : '{mot_courant}'")

    if stats[28] == 0:
        stats[27] = 0

    total_alphabetiques = sum(stats[0:26])

    print(f"Caractères totaux       : {stats[28]}")
    print(f"Caractères alphabétiques : {total_alphabetiques}")
    print(f"Mots                     : {stats[26]}")
    print(f"Lignes                   : {stats[27]}")
    print("\n--- Tableau des occurrences et fréquences ---")
    print(f"{'Lettre':<8}{'Occurrences':<15}{'Fréquence':<10}")
    print("-" * 33)
    
    for i in range(26):
        lettre = chr(ord('a') + i)
        occurrences = stats[i]
        frequence = (occurrences / total_alphabetiques) if total_alphabetiques > 0 else 0.0
        print(f"{lettre:<8}{occurrences:<15}{frequence:.4f}")

if __name__ == "__main__":
    lire()

