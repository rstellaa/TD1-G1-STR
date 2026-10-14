# APP 2026-2027 -- TP1

## Support de cours

[Support de cours au format Google docs](https://docs.google.com/presentation/d/1d3m4XQp80dvKl4Onl_fOCI69J0H3nr9LxeuCM5V4-5Q/edit?usp=sharing)

## Consigne générale 

On rappelle les principes qui vous permettront de monter en compétences : 
- Interpellez l'enseignant pour toute question. 
- N'utiliser pas les IA en phase d'apprentissage pour comprendre/apprendre. Au contraire, cherchez à lire, comprendre et exploiter la [documentation officielle du language](https://docs.python.org/fr/3/contents.html).
- Si votre environnement est configuré pour afficher des suggestions lors de la frappe, désactivez-les !
- Pour désactiver les suggestions dans VSCode, un fichier de configuration est déjà intégré dans ce projet : `.vscode/settings.json`.
- Ponctuellement, vous pouvez utiliser Ctrl+Espace pour demander la complétion des noms de variables/fonctions/méthodes... 
- Ne pas fuir la difficulté : sans effort, pas d'ancrage !
- Tout le travail de développement réalisé en séance est susceptible de donner lieu à des questions lors du QCM de la séance suivante. Plus particulièrement, les termes précédés du symbole 📌 représentent des concepts que vous devez être capables de *définir* et de *développer*, sans aide.
- Le travail réalisé **en séance** est également évalué, sur la base des interactions que vous aurez eu avec l'enseignant pour faire valider vos développements. 
- Si le travail demandé dans le sujet n'a pas été terminé à l'issue de la séance, il doit être poursuivi en TEA. Le QCM de la séance suivante permet également de le vérifier. 

## Objectifs

À l'issue de ce TD, vous devez savoir :

- Utiliser le vocabulaire associé à l'exécution des programmes et à leurs entrées-sorties.
- Mettre en place les bonnes pratiques associées. 
- Saisir des caractères en entrée d'un programme en *mode interactif* depuis le shell.
- Utiliser le shell pour mettre en place des redirections. 
- Lire l'entrée standard d'un programme.
- Récupérer les arguments fournis en ligne de commande à un programme.
- Ouvrir un fichier pour le lire ou l'écrire.
- Utiliser la structure de contrôle match/case. 
- Exploiter les codes ASCII des caractères.
- Exécuter une commande shell depuis un programme python.
- Utiliser les types `list` et `dict` du langage python.
- Utiliser les *tuples* du langage python et le *sequence unpacking*.
- Produire du code robuste et modulaire.


---

## Exercice 1 — Redirections d'entrée, de sortie, de commandes, d'erreur

Sur le shell, chaque programme en cours d'exécution (dénommé 📌 **processus**) est associé à trois descripteurs d'entrée-sortie : 
- stdin (0), son 📌 **entrée standard**, d'où il peut récupérer un flux de caractère à exploiter.
- stdout (1), sa 📌 **sortie standard**, sur laquelle il affiche ses résulats.
- stderr (2), sa 📌 **sortie d'erreur**, sur laquelle il **doit** (c'est une bonne pratique à respecter) afficher ses messages d'erreur. 

### Entrée standard
Sur le shell, on peut fournir des caractères sur *l'entrée standard* d'un programme de plusieurs façons : 

- En saisissant directement les caractères au clavier, en mode interactif. Dans ce cas, pour  terminer la saisie, on doit envoyer le 📌 **caractère de contrôle `EOF`** représentant la fin d'un fichier (*End Of File*). On peut le générer sur le terminal à l'aide du raccourci clavier `Ctrl+D`, sur une ligne vide. 
    - 📌 **Terminal** : interface permettant à l'utilisateur d'interagir avec un système en saisissant des commandes et en affichant leurs résultats.

```bash
wc
```

- En envoyant le contenu d'un fichier dans l'entrée standard du programme à l'aide du caractère `<` : *redirection d'entrée* ou *des données*. 
    - 📌 **Redirection** : mécanisme permettant de faire passer l’entrée ou la sortie d’un programme par une autre source ou destination que le terminal.

```bash
wc < README.md
```

- En envoyant le résultat d'une commande dans l'entrée standard du programme à l'aide du caractère `|` (*pipe*, signifiant *tube* en anglais -- représentant un canal de communication entre deux processus) : *redirection de commandes*.

```bash
ls | wc
```

1. Tester chacune des commandes proposées en faisant varier les flux de caractères envoyés à la commande `wc`. 

### Sortie standard

On peut rediriger la *sortie* d'un programme pour la stocker dans un fichier à l'aide du caractère  `>` (écrasement du fichier) ou '>>' (concaténation à la fin du fichier) : *redirection de sortie* ou *des résultats*.

```bash
wc < README.md > statistiques
cat statistiques
```

2. Tester une redirection de sortie pour sauvegarder le résultat d'un programme dans un fichier. 

### Sortie d'erreur 

Si un programme génère des messages d'erreur, elles **doivent** être générées sur sa sortie d'erreur. Il est possible de rediriger les erreurs pour les sauvegarder dans un fichier à l'aide des symboles `2>`ou `2>>`. C'est souvent une bonne pratique d'afficher les messages de débogage sur la sortie d'erreur. 

```bash
cat fichier_inexistant
cat fichier_inexistant 2> erreur 
cat erreur
chown user_inexistant erreur 
chown user_inexistant erreur 2>> erreur
cat erreur
```

Si vous ne souhaitez ni afficher, ni sauvegarder les messages d'erreur, il est possible de les rediriger vers le périphérique `/dev/null`, qui les fera disparaître du système. 

```bash
cat fichier_inexistant 2> /dev/null
```

---

## Exercice 2 — Gestion des entrées-sorties en python

On souhaite lire le flux de caractères envoyé à un programme sur son entrée standard. Deux solutions sont proposées en python : 

- La fonction `input()`, conçue pour lire une ligne. Cette fonction lit une ligne jusqu'au caractère de saut de ligne `\n` final, le supprime et retourne une chaîne de caractères. Elle peut prendre une chaîne de caractères en argument afin d'expliquer à l'utilisateur ce qu'il doit saisir. 
- La fonction `sys.stdin.read()` lit le flux d'entrée standard jusqu'à la fin de fichier (`EOF`) et renvoie une chaîne de caractères contenant l'ensemble des données lues.   

```python
import sys
for caractere in sys.stdin.read():
    print(caractere)
```

Pour déterminer si le programme python est lancé en mode interactif ou si l'entrée standard est redirigée, on peut utiliser la fonction `sys.stdin.isatty()` qui renvoie `true` si l'entrée standard correspond au clavier. 

Pour afficher un message sur la sortie d'erreur, deux solutions sont possibles : 
-  Utiliser 📌 **l'argument nommé** `file=sys.stderr` de la fonction `print`, qui induira un passage à la ligne (sauf mention contraire avec l'argument nommé `end=""`). 

```python
import sys
print("Une erreur est survenue", file=sys.stderr)
```

- Ecrire directement dans le flux de sortie d'erreur avec `sys.stderr.write()` : 

```python
import sys
sys.stderr.write("Une erreur est survenue\n")
```


3. Une fois les programmes ci-dessous mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 

- Produire un programme `input.py` permettant de récupérer le pseudo de l'utilisateur saisi au clavier et de le saluer : ***Bonjour [pseudo] !***
- Produire un programme `stdin.py` permettant de compter le nombre de caractères saisi par l'utilisateur dans son entrée standard et de l'afficher. 
  - Ce programme demandera à l'utilisateur de saisir une chaine uniquement s'il est invoqué en mode interactif.  
  - Ce programme ne devra afficher sur la sortie standard *que* le nombre de caractères saisi.  

> **Consigne pour les enseignants :**
> - Vérifier que le code de l'étudiant est bien présent dans son dépôt Github
> - Demander à l'étudiant de tester son programme sur le fichier `extraits/test_comptage` et de comparer sa sortie avec celle de la commande `wc`. 

---

## Exercice 3 — Codes de retour, arguments en ligne de commande, variables d'environnement

Un programme bien construit doit envoyer un *code de retour* lorsqu'il se termine. 
- 📌 **Code de retour** : valeur entière indiquant si un programme s'est terminé correctement ou avec une erreur.
- La valeur 0 représente un succès, tandis qu'une valeur numérique différente de 0 représente un code d'erreur. 
- Sur le shell, le symbole `$?` représente le code de retour du dernier programme qui s'est exécuté. 


```bash
ls 
echo $?
commande_inexistante
echo $?
```

En python, on peut quitter un programme en renvoyant un code de retour à l'aide de la fonction `sys.exit(codeDeRetour)`. 

Les *arguments* fournis *en ligne de commande* à un programme python sont stockés dans la liste `sys.argv`. 
- 📌 **Argument en ligne de commande** : valeur saisie après le nom du programme lors de son lancement, afin de lui transmettre une information ou de modifier son comportement.
- Il s'agit d'une liste de chaînes de caractères dont le premier élément contient le nom du programme invoqué lui-même. 

- 📌 Une **Variable d'environnement** du shell : variable associée au shell, dont la valeur est accessible par les programmes lancés depuis ce shell.  

```bash
export PSEUDO=Tom # Surtout pas d'espaces autour du signe égal pour définir une variable d'environnement !
echo $NOTE # Affichage de la variable NOTE
env # Affichage de toutes les variables d'environnement
unset NOTE  # supprime la variable 
```

En python, les *variables d'environnement* du shell sont accessibles avec le module `os` dans la structure `os.environ`. 
- Cette structure se comporte comme un dictionnaire (type `dict`) : une collection de paires clé-valeur. 

```python
import os
if "USER" in os.environ:
    print(os.environ["USER"])
```


4. Ecrire un programme `arguments.py` affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell. 
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 

> **Consigne pour les enseignants :**
> - Questionnez la manière la plus idiomatique de réaliser le parcours de la liste d'arguments et leur affichage. 
> - Vérifier le comportement du programme en fonction de la présence et de la nature (exportée ou non) de la variable `DEBUG`

---

## Exercice 4 — Lecture et écriture de fichiers

Plutôt que de lire son entrée standard, un programme python peut ouvrir lui-même un fichier pour le lire ou l'écrire.

- L'ouverture d'un fichier est mise en oeuvre à l'aide de la fonction `flux = open(chemin,mode)`. Les modes principaux sont :
  - "r"  pour ouvrir le fichier en lecture.
  - "w"  pour oucrir le fichier en écriture, en écrasant le fichier.
  - "a"  pour ouvrir le fichier en écriture, en ajoutant à la fin.

- Cette fonction peut provoquer des erreurs, par exemple si le fichier à ouvrir n'existe pas ou n'est pas lisible. 
- Dans ce genre de situations où il est normal de rencontrer des erreurs, la structure python `try/except` peut être utilisée : 

```python
try:
    # code pouvant déclencher une erreur  
except:
    # réaction 
```

- Une fois le fichier ouvert, la fonction open renvoie un objet **flux de texte**, de la même nature que `sys.stdin` pour décrire l'entrée standard. 
- Son contenu peut-être lu à l'aide de la fonction `chaine = flux.read()`, qui récupère dans une chaine de caractères le contenu du fichier. 
- Le fichier peut être écrit à l'aide de la fonction `flux.write(chaine)`
- Pour fermer le fichier, on utilise la fonction `flux.close()`. 

5. Ecrire un programme `comptage.py` permettant de lire un fichier et d'afficher ses caractéristiques principales. Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 

- Le chemin du fichier à lire devra être fourni comme argument en ligne de commandes. 
- En absence d'argument, le programme lira les caractères fournis sur l'entrée standard. 
- Le programme doit afficher le nombre de caractères, de lignes et de mots du texte lu. Pour cela, vous devez utiliser la structure de contrôle match/case afin de discrimer la nature des caractères au fur et à mesure de leur lecture. 
- De façon à ne pas trop compliquer les traitements, on considérera qu'un mot est une séquence de caractères encadrée de séparateurs et dans un premier temps, seuls trois séparateurs seront pris en compte : le saut de ligne, l'espace et le caractère de tabulation ('\t')
- Votre programme devra proposer un mode de débogage affichant les numéros des mots détectés. 


> **Consigne pour les enseignants :** 
> - Vérifier la **robustesse** du programme : séparateurs multiples, fichier vide, se terminant sans ou avec un saut de ligne...
   - 📌 **Robustesse d'un programme** : capacité d'un programme à fonctionner correctement, y compris lorsque les entrées sont inattendues ou invalides.
> - Vérifier la **modularité** du programme
   - 📌 **modularité** : organisation d'un programme en parties indépendantes, appelées fonctions, regroupées en modules.
> - Expliquer les différences de comptage observées avec celles de la commande `wc`

---

## Exercice 5 — Codes ASCII - Affichage de statistiques détaillées d'un fichier

Nous souhaitons étudier la fréquence d'apparition des caractères alphabétiques d'un fichier, sans distinction de casse des caractères. 
- 📌 **Casse des caractères** : distinction entre les lettres majuscules et minuscules.
- En informatique, les caractères alphabétiques non accentués sont représentés par une valeur numérique sur 7 bits, leur 📌 **code ASCII** (American Standard Code for Information Interchange). 
- La table des codes ASCII stocke les caractères alphabétiques minuscules et majuscules de manière contigüe (cf. `man ascii`). Ainsi, le code de caractère "b" est égal au code du caractère "a" + 1. Le code du caractère "C" est égal au code du caractère "A" + 2, etc.  
- En python, la gestion des codes ascii des caractères se fait principalement avec deux fonctions : 
  - `ord(car)` renvoie le code numérique associé à un caractère. 
  - `chr(code)` renvoie le caractère associé à un code 



6. Ecrire un programme `ascii.py` permettant de lire un fichier et d'afficher ses caractéristiques détaillées. 
- ***Cet exercice s'inspire largement d'un TP construit par Christian Vercauter, enseignant d'informatique à l'Ecole Centrale de Lille, aujoud'hui retraité.***
- Le programme doit afficher en plus des informations précédentes : 
    - Le nombre total de caractères alphabétiques rencontrés. 
    - Un tableau présentant le nombre d'occurrences de chaque caractère alphabétique, ainsi que sa fréquence (rapport entre le nombre d'occurrences d'un caractère alphabétique sur le nombre total de caractères alphabétiques).
- **Indications** : Créer et initialiser à zéro, une liste de 29 composantes entières, qui contiendra les occurrences des caractères alphabétiques mais également le nombre total de mots, lignes, caractères et caractères alphabétiques rencontrés.
- Considérer les caractères accentués de manière spéficique à l'aide d'un `match/case`; 
- Tester votre programme sur les deux extraits du roman de Georges Perec (1936-1982) intitulé "La Disparition" paru en 1969. Que remarquez-vous en examinant les résultats ?
- Tester votre programme sur l'extrait d'un autre roman de Georges Perec, intitulé "Les Revenentes" paru en 1972. 
    - Que constatez-vous en examinant les résultats ? Qu'est-ce-qu'un 📌 **lipogramme** ?
- Tester votre programme sur le texte suivant : *"Portez ce vieux whisky au juge blond qui fume"*. 
    - Que constatez-vous en examinant les résultats ? 
    - Qu'est-ce-qu'un 📌 **pangramme** ? A quoi servent les pangrammes en informatique ?
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 

---

## Exercice 6 — Chiffre de César - Chiffrement par décalage 

Dans cet exercice, nous souhaitons développer un programme permettant chiffrer et déchiffrer un texte à l'aide d'un *chiffrement par décalage*. 
- En cryptographie, le 📌 **chiffrement par décalage**, aussi connu comme le chiffre de César, est une méthode de chiffrement très simple utilisée par Jules César dans ses correspondances secrètes. Le procédé qu'il utilisait se fonde sur un décalage de 3 lettres vers la droite : le caractère **A** est remplacé par **D** (A+3), **B** par **E**, **C** par **F** et ainsi de suite. 
- Il s'agit d'un cas particulier de *chiffrement par substitution monoalphabétique*, mettant en place une permutation circulaire de l'alphabet : le texte chiffré s'obtient en remplaçant chaque lettre du texte clair original par une lettre à distance fixe, toujours du même côté, dans l'ordre de l'alphabet. Pour les dernières lettres (dans le cas d'un décalage à droite), on reprend au début. 
- Dans le cas de l'alphabet latin, le chiffre de César n'a que 26 clés possibles (y compris la clé nulle, qui ne modifie pas le texte). 
- Cf. [Lien Wikipédia sur le chiffrement par décalage](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage).

### Commande shell `tr`

La commande shell `tr` permet de mettre en place rapidement une commande de chiffrement-déchiffrement utilisant ce principe : il suffit de lui fournir en arguments les deux ensembles de caractères à substituer, et le texte à chiffrer/déchiffrer sur son entrée standard. Dans l'exemple ci-dessous, les ensembles à substituer sont construits à partir de deux types d'expressions : 
- Par 📌 **intention** (ou **compréhension**) : on exprime juste les *bornes* de l'ensemble des caractères à utiliser. Tous les caractères dont le code ASCII est compris entre les codes ASCII du premier et du dernier sont capturés dans l'ensemble à construire.  
- par 📌 **extension** (ou **énumération**) :  on *énumère* tous les caractères qui doivent faire partie de l'ensemble. 

```bash
echo "Voici un message à chiffrer" | tr 'a-z' 'D-ZABC' | tee texte_chiffre
cat texte_chiffre | tr 'D-ZABC' 'a-z'
```

7. Tester les commandes précédentes. Constatez l'erreur qu'elles provoquent et corrigez-là, de manière à traiter tous les caractères alphabétiques non accentués en inversant leur casse lors des opérations de chiffrement-déchiffrement.   

Pour développer un programme python réalisant un chiffrement par décalage, nous pouvons mettre en place deux démarches différentes : 
- Utiliser la commande shell `tr` comme un processus externe au sein d'un programme python, ce qui nécessite d'évoluer dans un environnement muni de cette commande.
- Développer intégralement les fonctionnalités nécessaires en python. 

### Exécution d'un processus externe : module `subprocess`

Pour demander en python à exécuter une commande shell dans un processus externe (on parle de *processus fils*) et récupérer son résultat, l'approche préconisée est de séparer *explicitement* la commande à utiliser de ses arguments, afin d'éviter tout risque *d'injection de commandes*. Le module `subprocess` permet de réaliser cela avec la fonction `run`. 
📌 **Injection de commandes** : technique consistant à faire exécuter par un programme des commandes supplémentaires fournies par un utilisateur, en exploitant une entrée insuffisamment contrôlée.

```python
import subprocess

resultat = subprocess.run(
    ["wc", "-c", "-w"],
    input="une chaine de 8 mots et 38 caractères",
    capture_output=True,
    text=True
)

print(resultat.stdout)
print(resultat.stderr)
print(resultat.returncode)
```

Le premier élément de la liste correspond à la commande à exécuter (`wc`) et les éléments suivants à ses arguments (`-c`,`-w`). Le paramètre `capture_output=True` permet de récupérer les sorties standard et d'erreur du processus fils, tandis que `text=True` demande à Python de les représenter sous forme de chaînes de caractères et non pas d'octets. Le paramètre `input` permet de fournir une chaîne de caractères dans l'entrée standard du processus. 

8. [BONUS] Développer un programme python `cesar.py` exploitant cette solution pour réaliser successivement les opérations de chiffrement puis déchiffrement du texte fourni sur son entrée standard, en utilisant le chiffrement de César. 


###  Développement d'une solution générique en python

Nous souhaitons implémenter un programme de chiffrement-déchiffrement par décalage en python, dont voici le cahier des charges : 


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

Pour cela, vous pourrez exploiter deux *listes python* déclarées de la manière suivante (les noms en majuscules sont une convention Python pour indiquer que ces valeurs sont considérées comme des constantes). 

```python
ACCENTS_MINUSCULES = ["à", "â", "ä","é", "è", "ê", "ë","î", "ï","ô", "ö","ù", "û", "ü","ÿ","ç"]
ACCENTS_MAJUSCULES = ["À", "Â", "Ä","É", "È", "Ê", "Ë","Î", "Ï","Ô", "Ö","Ù", "Û", "Ü","Ÿ","Ç"]
indice = ACCENTS_MINUSCULES.index("é")
print(ACCENTS_MAJUSCULES[indice])
```
- Alternativement, vous pouvez utiliser deux chaînes de caractères déclarées dans un *tuple* pour traiter les accents. Il s'agit d'un type immuable représentant un ensemble de valaurs dont la structure ne doit pas être modifiée. 

```python
ACCENTS = ("àâäéèêëîïôöùûüÿç","ÀÂÄÉÈÊËÎÏÔÖÙÛÜŸÇ")
ACCENTS_MINUSCULES, ACCENTS_MAJUSCULES = ACCENTS # unpacking 
indice = ACCENTS_MINUSCULES.index("é")
print(ACCENTS_MAJUSCULES[indice])
```
- Dans le code précédent, l'opération `a,b = tuple` est appelée 📌 **sequence unpacking** ou encore **unpacking assignment** (**affectation par déballage** en français). Elle peut également être mise en oeuvre sur des listes : `a,b = liste` ou sur des chaînes : `a,b = chaine`. Si le nombre d'éléments à affecter ne correspond pas au nombre de variables que l'on souhaite utiliser, on peut utiliser le symbole `*` : `a,*reste = valeurs`. 

- L'utilisation d'un *dictionnaire* est également possible. En Python, cette structure de données est implémentée à l'aide d'une *table de hachage* (*hash table*). L'exemple ci-dessous permet d'associer directement chaque lettre minuscule accentuée à son équivalent majuscule. 
    - 📌  Une **table de hachage** est une structure de données permettant d'associer des clés à des valeurs et d'accéder efficacement (en temps moyen constant, O(1)) à une valeur à partir de sa clé, en utilisant une fonction de hachage.


```python
ACCENTS = {
    "à": "À",
    "â": "Â",
    "ä": "Ä",
    "é": "É",
    "è": "È",
    "ê": "Ê",
    "ë": "Ë",
    "î": "Î",
    "ï": "Ï",
    "ô": "Ô",
    "ö": "Ö",
    "ù": "Ù",
    "û": "Û",
    "ü": "Ü",
    "ÿ": "Ÿ",
    "ç": "Ç"
}
if "é" in ACCENTS: 
        print(ACCENTS["é"])
```


9. Ecrire un programme `chiffrement_decalage.py` réalisant ces opérations et testez-le à l'aide du shell à l'aide de la commande `diff`. 
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant. 

> **Consigne pour les enseignants :** 
> - Vérifier que l'étudiant a produit un programme **robuste** capable de traiter le cas d'un décalage mal formé 
>   - 📌 **Robustesse d'un programme** : capacité d'un programme à fonctionner correctement, y compris lorsque les entrées sont inattendues ou invalides.
> - Vérifier que l'étudiant s'est assuré de la **couverture de ses tests**
>   - 📌 **Couverture des tests** : mesure de la part des exigences du cahier des charges vérifiées par les tests.
> - Demander à l'étudiant comment compléter le dictionnaire pour le rendre bidirectionnel  
> - Demander à l'étudiant quelle forme de représentation des accents est la meilleure
> - Le cas échéant, demander à l'étudiant s'il juge qu'utiliser `if ... in` ET `.index` est pertinent 
> - Vérifier que le programme ne produit pas de message sur stdin, en plus du texte chiffré. Vérifier que l'étudiant peut produire une commande réalisant déchiffrement(chiffrement) et que cela donne bien exactement le texte initial 


