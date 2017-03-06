#-*- coding: utf-8 -*-
import Dico
import os
import sys
import pickle

PATH_DICO = "dictionnaire/dico_seconde_version.ket"
PATH_FILE_OUT = sys.argv[1]

#ouverture ou creation du fichier dictionnaire
dico = dict()
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dico=pickle.load(fichier)

liste_classe = []
for i,classe in enumerate(dico.keys()) :
	print i, ":", classe
	liste_classe += [classe]

r = input("Saisissez les classes à mettre dans le fichier : ")
q = input("Sous quelle consigne ? : ")
r = r.split()

with open(PATH_FILE_OUT, 'w') as file_out:
    for numero_classe in r :
	       file_out.write(dico[liste_classe[int(numero_classe)]].to_string(q))
