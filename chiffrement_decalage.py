#! /usr/bin/env python3

"""Programme permettant de réaliser des opérations de chiffrement-déchiffrement par décalage
- Le texte à chiffrer ou déchiffrer sera fourni sur son l'entrée standard du programme.
- Lors de l'invocation du programme, l'utilisateur devra saisir lui-même le décalage à opérer, sous la forme d'un argument en ligne de commande. 
    - La classe `str` (dont héritent les chaînes de caractères dans un programme python) implémente la méthode `s.isnumeric` pour tester si une chaîne `s` est constituée exclusivement de caractères numériques. Malheureusement, cette méthode renvoie `False` lorsqu'elle est exécutée depuis la chaîne "-3"
    - Pour convertir une chaine de caractères numérique `s` en entier (on parle de *type casting*), on utilise la fonction `int(s)`. Cette fonction lève une exception si la conversion est impossible. 
    - 📌  Le **type casting** est l'opération qui consiste à convertir une valeur d'un type vers un autre type compatible, généralement en utilisant une opération ou une fonction de conversion.
- Si le programme est invoqué sans argument, il devra réaliser un chiffrement de César.
- Votre programme devra s'appuyer sur une fonction nommée `chiffrer` prenant deux arguments en paramètre : 
  - la chaîne à chiffrer. 
  - Le décalage (positif ou négatif) à opérer sur chacun des caractères alphabétiques de la chaine. 
- Les opérations de chiffrement-déchiffrement devront inverser la casse des caractères. Vous pourrez utiliser pour cela les *méthodes* `s.islower` et `s.isupper` de la classe `str`.  
- Votre programme devra traiter les caractères alphabétiques non accentués de manière générique en utilisant leurs codes ASCII.
- Votre programme devra traiter de manière spécifique les caractères accentués : il se contentera d'en changer la casse, sans réaliser de décalage.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""


import sys


def traiterArguments():
  if len(sys.argv) < 2:
    return 3

  arg = sys.argv[1]

  try:
    if arg.startswith("-"):
      if arg[1:].isnumeric():
        return int(arg)
    else:
      if arg.isnumeric():
        return int(arg)
  except ValueError:
    pass

   raise ValueError("Le décalage doit être un nombre entier.")


def lireStdin():
  return sys.stdin.read()


def chiffrer(texte, dec):
  resultat = []

  for c in texte:
    if c in "àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ":
      if c.islower():
        resultat.append(c.isupper())  # ou swapcase()
        resultat.append(c.upper())
      else:
        resultat.append(c.lower())
      continue

    if "a" <= c <= "z" or "A" <= c <= "Z":
      base = ord("a") if c.islower() else ord("A")
     code = (ord(c) - base + dec) % 26 # Appliquer le décalage modulo 26
      nouveau_caractere = chr(base + code)
    else:
      nouveau_caractere = c

    if nouveau_caractere.islower():
      resultat.append(nouveau_caractere.upper())
    elif nouveau_caractere.isupper():
      resultat.append(nouveau_caractere.lower())
    else:
      resultat.append(nouveau_caractere)

  return "".join(resultat)


if __name__ == "__main__":
  dec = traiterArguments()
  s1 = lireStdin()
  print(chiffrer(s1, dec), end="")