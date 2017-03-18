#-*- coding: utf-8 -*-
import sys
import pickle
import os
import Dico
import Word
import Classe

if len(sys.argv) != 2 :
	print "Usage : <nom_fichier_dictionnaire>"
	exit(1)

PATH_DICO = sys.argv[1]
# if os.path.isfile(PATH_DICO):
#     with open(PATH_DICO, 'rb') as fichier:
#         dico = pickle.load(fichier)
# else :
dico = Dico.Dico()

r = int(raw_input("Que voulez vous faire:\n 1: Ajouter une classe depuis un fichier.\n 2: Ajouter une classe manuellement.\n 3: Modifier une classe\n 4: Ajouter une interprétation\n 5: Créer un fichier test \n"))


if r == 1 :
	name_file = raw_input("Saisissez le chemin du fichier :")
	dico.add_class_from_file(name_file)
	print name_file
	pass
elif r == 2 :
	key = raw_input("Saisissez le nom de la classe :")
	s=raw_input("Saisissez un couples de mots par ligne, Saisissez la ligne STOP pour valider:\n:")
	couples=[]
	while s!="STOP":
		couples.append([Word.Word(s.split()[0]),Word.Word(s.split()[1])])
		s=raw_input(":")
	dico.add_class(key,Classe.Classe(key, couples))
	pass
elif r == 3 :
	dico.modif_class()
	pass
elif r == 4 :
	pass
elif r == 5 :
	pass
else :
	print "Error nombre entré"
	exit(1)

with open(PATH_DICO, 'wb') as fichier:
    pickle.dump(dico,fichier)
