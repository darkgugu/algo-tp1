def recherche_dichotomique(liste, element):
    debut = 0
    fin = len(liste) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste[milieu] == element:
            return milieu
        elif liste[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1

    return -1
