#! /usr/bin/env python3

"""Programme permettant de réaliser successivement les opérations de chiffrement puis déchiffrement du texte fourni sur son entrée standard, en utilisant le chiffrement de César, à l'aide de la commande shell tr et de la commande python subprocess."""


def lire_stdin(): 
    return ""

def coder(s): 
    return ""

def decoder(s): 
    return ""

if __name__ == "__main__":
    s1 = lire_stdin()
    print("Chaine à traiter : " + s1)
    s2 = coder(s1)
    print("Chiffrement : " + s2)
    s3 = decoder(s2)
    print("Déchiffrement : " + s3)