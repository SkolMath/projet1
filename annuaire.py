# -*- coding: utf-8 -*-
"""
Projet "Création d'un répertoire téléphonique"

Created on Mon Aug  5 17:20:55 2019

@author: d.planchet

"""


# la fonction menu permet à l'utilisateur de :
# 0 - quitter le programme
# 1 - écrire dans le répertoire
# 2 - rechercher dans le répertoire

def menu(choix):

    if choix==0:
        choix_menu=0
        return choix_menu
    elif choix==1:
        ecriture()
    elif choix==2:
        recherche=input("Entrer un nom : ")
        lecture(recherche)

# la fonction lecture permet à l'utilisateur de rechercher
# le numéro d'une personne inscrite dans l'annuaire

def lecture(recherche):
    annuaire=[]   # Création d'une liste vide

    # Ajout d'éléments correspondant aux lignes du fichiers
    with open('annuaire.txt','r') as f :
        for ligne in f:
            ligne=ligne.replace("\n","")
            annuaire.append(ligne)

    # Recherche dans la liste le nom recherché à l'aide d'une boucle
    for i in range(len(annuaire)):
        if recherche==annuaire[i]:
            return print(f"Le numéro recherché est : {annuaire[i+1]}")
    # Affiche Inconnu si le nom n'existe pas dans la liste
    return print("Inconnu")

# la fonction écriture permet à l'utilisateur de saisir
# le nom de la personne et son numéro dans l'annuaire

def ecriture():
    nom=1
    # Tant que l'utilisateur ne saisit pas 0 dans nom
    # Il peut continuer à saisir dans son annuaire
    while nom!='0':
        nom=input("Nom (0 pour terminer) : ")
        if nom!='0':
            tel=input("Téléphone : ")
            # Ajout des informations saisies par l'utilisateur
            with open('annuaire.txt','a') as f :
                f.write(nom+'\n')
                f.write(tel+'\n')

# DEBUT DU PROGRAMME
# le programme boucle tant que l'utilisateur ne quitte pas celui-ci

choix_menu = 3

print("\nBienvenue dans votre annuaire\n----------------------------------\n")

while choix_menu !=0:
    print("\n0-quitter \n1-écrire dans le répertoire \n2-rechercher dans le répertoire")
    choix_menu=int(input("Votre choix ? "))
    menu(choix_menu)

print("\n----------------------\nfin du programme")