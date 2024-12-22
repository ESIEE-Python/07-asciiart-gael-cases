#### Imports et définition des variables globales
"""
importer sys pour permettre de dépasser la limite de récursivité
"""
import sys

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères
      passée en argument selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    current = [s[0]]
    occurence = [1]
    for k in range(1,len(s)) :
        if s[k] == s[k-1] :
            occurence[-1] += 1
        else :
            occurence.append(1)
            current.append(s[k])
    lt = list(zip(current,occurence))
    return lt

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    sys.setrecursionlimit(10000)  # Augmente la limite de récursion

    if not s:  # Base de la récursion : si la chaîne est vide
        return []

    # Identifie le premier caractère et compte ses occurrences consécutives
    current = s[0]
    occurence = 1
    while occurence < len(s) and s[occurence] == current:
        occurence += 1

    # Appel récursif pour le reste de la chaîne
    return [(current, occurence)] + artcode_r(s[occurence:])



#### Fonction principale


def main():
    """
    permet d'executer artcode en itératif et récursif
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
