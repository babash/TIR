#-*- coding: utf-8 -*-
import Vandal
import os
import sys
import pickle

PATH_DICO = "dictionnaire/dico_seconde_version.ket"
PATH_FILE_OUT = "dictionnaire/file_out.ket"

#ouverture ou creation du fichier dictionnaire
dico = dict()
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dico=pickle.load(fichier)

file_out = open(PATH_FILE_OUT, "w")

liste_classe = []
for i,classe in enumerate(dico.keys()) :
	print i, ":", classe
	liste_classe += [classe]

r = input("Saisissez les classes à mettre dans le fichier : ")
q = input("Sous quelle consigne ? : ")
r = r.split()
for numero_classe in r :
	file_out.write(dico[liste_classe[int(numero_classe)]].to_string(q))
file_out.close()