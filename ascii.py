#! /usr/bin/env python3

"""Programme permettant de lire un fichier et d'afficher ses caractéristiques détaillées. 
- ***Cet exercice s'inspire largement d'un TP construit par Christian Vercauter, enseignant d'informatique à l'Ecole Centrale de Lille, aujoud'hui retraité.***
- Le programme doit afficher en plus des informations précédentes du programme comptage : 
    - Le nombre total de caractères alphabétiques rencontrés. 
    - Un tableau présentant le nombre d'occurrences de chaque caractère alphabétique, ainsi que sa fréquence (rapport entre le nombre d'occurrences d'un caractère alphabétique sur le nombre total de caractères alphabétiques).
- **Indications** : Créer et initialiser à zéro, une liste de 29 composantes entières, qui contiendra les occurrences des caractères alphabétiques mais également le nombre total de mots, lignes, caractères et caractères alphabétiques rencontrés. 
- Considérer les caractères accentués de manière spéficique à l'aide d'un `match/case`; 
- Tester votre programme sur les deux extraits du roman de Georges Perec (1936-1982) intitulé "La Disparition" paru en 1969. Que remarquez-vous en examinant les résultats ?
- Tester votre programme sur l'extrait d'un autre roman de Georges Perec, intitulé "Les Revenentes" paru en 1972. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **lipogramme** ?
- Tester votre programme sur le texte suivant : *"Portez ce vieux whisky au juge blond qui fume"*. Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **pangramme** ? A quoi servent les pangrammes en informatique ?
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 
"""

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
                
                indice_lettre = ord(c) - ord('a')
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