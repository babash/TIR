#-*- coding: utf-8 -*-
import sys
import pickle
import os
import Dico
import Word
import Classe
import utils

nb_arg = len(sys.argv)
if nb_arg != 2 and nb_arg != 3 :
	print "Usage : <nom_fichier_dictionnaire> <optionnel : nom_file_out>"
	exit(1)

PATH_DICO = sys.argv[1]
if nb_arg == 3 :
	NOM_FILE_OUT = sys.argv[2]
else :
	NOM_FILE_OUT = None
if os.path.isfile(PATH_DICO):
    with open(PATH_DICO, 'rb') as fichier:
        dico = pickle.load(fichier)
else :
	dico = Dico.Dico()

r = int(raw_input("Que voulez vous faire:\n 1: Ajouter une classe depuis un fichier.\n 2: Ajouter une classe manuellement.\n 3: Modifier une classe\n 4: Ajouter une interprétation\n 5: Créer un fichier test \n"))


if r == 1 :
	#Ajoute une classe depuis un fichier
	name_file = raw_input("Saisissez le chemin du fichier :")
	dico.add_class_from_file(name_file)
elif r == 2 :
	#Ajoute une classe manuellement
	key = raw_input("Saisissez le nom de la classe :")
	s=raw_input("Saisissez un couples de mots par ligne, Saisissez la ligne STOP pour valider:\n:")
	couples=[]
	while s!="STOP":
		couples.append([Word.Word(s.split()[0]),Word.Word(s.split()[1])])
		s=raw_input(":")
	dico.add_class(key,Classe.Classe(key, couples))
elif r == 3 :
	dico.modif_class()
	pass
elif r == 4 :
	pass
elif r == 5 :
	#Créer un fichier test
	if NOM_FILE_OUT == None :
		print "Pas de nom de fichier de sortie."
		exit(1)
	tab = dico.get_classes_in_tab()
	for elem in tab :
		print str(elem[0]) + " : "  + str(elem[1]) 
	ret_classes = raw_input("Saisissez les numéros des classes que vous souhaitez avoir dans votre fichier :\n")
	ret_classes = ret_classes.split(" ")


	ret_unicode = None
	while(ret_unicode != "y" and ret_unicode != "n") :
		ret_unicode = raw_input("Voulez vous les accents ? (y/n)\n")

	ret_tiret = None
	while(ret_tiret != "y" and ret_tiret != "n") :
		ret_tiret = raw_input("Voulez vous compléter les espaces par des tirets ? (y/n)\n")

	string = ""
	for c in ret_classes :
		classe = dico.get_classe(tab[int(c)][1])
		if classe != None :
			string += classe.to_string("default")

	if ret_unicode == "y" :
		string = utils.to_ascii(string)

	if ret_tiret == "y" :
		string = utils.with_underscore(string)
	
	fichier = open(NOM_FILE_OUT, 'w')
	fichier.write(string)
	fichier.close()

else :
	print "Error nombre entré"
	exit(1)

with open(PATH_DICO, 'wb') as fichier:
    pickle.dump(dico,fichier)
