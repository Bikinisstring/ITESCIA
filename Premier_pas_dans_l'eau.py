# coding: utf-8

def verif_saisie(jour, mois, annee):
    global etat
    mois30 = ["avril", "juin", "septembre","novembre"]
    mois31 = ["janvier","mars","mais","juillet","aout","octobre", "decembre"]
    lmoisincompatibles = ["janvier", "fevrier", "mars", "avril", "mais", "juin", "juillet", "aout", "septembre", "octobre"]
    lmois = ["janvier", "fevrier", "mars", "avril", "mais", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]

    if annee == 1582 and mois in lmoisincompatibles:
        return False

    if etat == True and mois == 'février':
        if(jour < 0 or jour > 29):
            return False

    if etat == False and mois == 'février':
        if(jour < 0 or jour > 28):
            return False

    if mois in mois31:
        if (jour < 0 or jour > 31):
            return False

    if mois in mois30:
        if (jour < 0 or jour > 30):
            return False

    if not(jour < 0 or jour <= 31):
        if not (mois in lmois):
            if annee < 1582:
                return False
    else:
        return True


def verif_bissextile(mois, annee):
    global etat
    if annee % 4 == 0 and not(annee % 100 == 0):
        etat = True
        if mois == "janvier" or mois == " fevrier":
            return 1

    elif annee % 100 == 0 and annee % 400 == 0:
        etat = True
        if mois == "janvier" or mois == " fevrier":
            return 1

    else:
        etat = False
        return 0

def verif_dictionnaire_mois(mois):
    dicomois = {'janvier': 0, 'février': 3, 'mars': 3, 'Avril': 6, 'mai': 1, 'juin': 4, 'juillet': 6,
                'aout': 2, 'septembre': 5, 'octobre': 0, 'novembre': 3, 'decembre': 5}


    if(mois in dicomois):
        return dicomois.get(mois)
    else:
        print("Le mois n'est pas valide")


def verif_dictionnaire_annee(annee):

    dicoannees = {16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4}
    annee_transforme = transforme_date_debut(annee)
    if (annee_transforme in dicoannees):
        return dicoannees.get(annee_transforme)
    else:
        print("L'année n'est pas valide")

def transforme_date_fin(y):
    string = str(y)
    mem = string[-2:]
    datefin = int(mem)
    return datefin

def transforme_date_debut(y):
    string = str(y)
    mem = string[:-2]
    datedeb = int(mem)
    return datedeb


def calcul_jour(jour, mois, annee):
    jours_semaine = {0 :'Dimanche', 1:'Lundi' ,2:'Mardi', 3:'Mercredi', 4:'Jeudi', 5:'Vendredi', 6:'Samedi'}
#---- Etape 1 ---------
    newannee = transforme_date_fin(annee)
    res = int(newannee / 4)
    res =  int(newannee + res)
    print("Etape 1 resultat = ",res)


#---- Etape 2 ---------
    res = int(jour + res)
    print("Etape 2 resultat = ",res)

#---- Etape 3 ---------

    res = int(res + verif_dictionnaire_mois(mois))
    print("Etape 3 resultat = ",res)

#---- Etape 4---------
    res = int(res - verif_bissextile(mois, annee))
    print("Etape 4 resultat = ",res)
    print(verif_bissextile(mois, annee))

#---- Etape 5 ---------
    res = int(res + verif_dictionnaire_annee(annee))
    print("Etape 5 resultat = ",res)

#---- Etape 6 ---------
    res = int(res % 7)
    print("Etape 6 resultat = ", res)
    if (res in jours_semaine):
        print("Cette date correspond au jours de la semaine", jours_semaine.get(res))
    else:
        print("le jours n'est pas trouvé")
#-------------- Programme affichage -------------------------
etat = False
check = False
while check == False:
    print("Entrez une date en commençant par:")
    jour = int(input("Le jour: "))
    mois = input("Le mois: ")
    annee = int(input("L'année: "))

    if verif_saisie(jour, mois, annee)== True:
        check = True
    else:
        check = False
        print("Saisie incorrecte")

calcul_jour(jour, mois, annee)
'''

jour = int(1)
mois = 'aout'
annee = int(1947)

verif_saisie(jour, mois, annee)
print(transforme_date_debut(annee))
calcul_jour(jour, mois, annee)


print(jour, mois, annee)

for donnees in date:
    print(donnees)

annee = int(input("Entrer une année"))
verif_bissextile(annee)'''